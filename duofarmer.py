import requests
import time
import base64
import json
import random
from datetime import datetime

# ================= CONFIGURATION AREA =================
# [Paste your JWT Token here]
# WARNING: NEVER share your real token or upload it to GitHub!
JWT_TOKEN = "PASTE_YOUR_TOKEN_HERE"

# [XP Farming Settings] Set how many lessons you want to complete consecutively
# Hint: Since each lesson includes a 30-50 second delay, 10 lessons take about 6-8 minutes.
TOTAL_LESSONS = random.randint(20, 30) 
# ======================================================

def farm_xp():
    headers = {
        "Authorization": f"Bearer {JWT_TOKEN}",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Content-Type": "application/json",
        "Cookie": f"jwt_token={JWT_TOKEN}" 
    }

    print("==========================================")
    print(f"🔥 Duolingo XP Farmer Started - Target: {TOTAL_LESSONS} lessons")
    print("==========================================\n")

    print("1. Parsing account token...")
    try:
        payload = JWT_TOKEN.split('.')[1]
        payload += '=' * (-len(payload) % 4)
        user_id = json.loads(base64.b64decode(payload).decode('utf-8'))['sub']
    except Exception as e:
        print("❌ Token parsing failed. Please check if your token is copied completely!")
        return

    print("2. Connecting to Duolingo servers to verify learning progress...")
    user_url = f"https://www.duolingo.com/2017-06-30/users/{user_id}?fields=fromLanguage,learningLanguage"
    try:
        resp = requests.get(user_url, headers=headers)
        if resp.status_code != 200:
            print(f"❌ Account connection failed! Status code: {resp.status_code}. Token might be expired.")
            return
            
        user_data = resp.json()
        from_lang = user_data.get("fromLanguage")
        learning_lang = user_data.get("learningLanguage")
        print(f"👉 Confirmed learning path: [{from_lang}] ➜ [{learning_lang}]")
    except Exception as e:
        print(f"❌ Network Error: {e}")
        return

    total_xp_gained = 0

    # ================= CORE FARMING LOOP =================
    for lesson_idx in range(TOTAL_LESSONS):
        current_num = lesson_idx + 1
        print(f"\n==========================================")
        print(f"🕒 Current Time: {datetime.now().strftime('%H:%M:%S')}")
        print(f"🎬 Starting lesson {current_num} / {TOTAL_LESSONS}...")

        session_url = "https://www.duolingo.com/2017-06-30/sessions"
        session_payload = {
            "challengeTypes": ["translate", "listen", "speak", "select", "match"],
            "fromLanguage": from_lang,
            "isFinalLevel": False,
            "isV2": True,
            "juicy": True,
            "learningLanguage": learning_lang,
            "type": "GLOBAL_PRACTICE" 
        }
        
        try:
            session_resp = requests.post(session_url, headers=headers, json=session_payload)
            if session_resp.status_code != 200:
                print(f"❌ Failed to request lesson session: {session_resp.status_code}")
                return
                
            session_data = session_resp.json()
            session_id = session_data.get("id")
        except Exception as e:
             print(f"❌ Network Error: {e}")
             return

        # 🔥 Core Anti-Ban Camouflage: Simulate human waiting time of 30-50 seconds
        simulated_time = random.randint(30, 50)
        print(f"🤫 Anti-ban camouflage activated: Idling for {simulated_time} seconds, pretending to think...")
        
        # Countdown progress bar
        for remaining in range(simulated_time, 0, -1):
            print(f"\r⏳ Time remaining to submit: {remaining} seconds...", end="", flush=True)
            time.sleep(1)
        print("\n📝 Lesson complete, preparing to submit a perfect score!")

        # Manipulate timestamps. Must subtract the idle time, otherwise server logic fails
        session_data["startTime"] = int(time.time()) - simulated_time - 5
        session_data["endTime"] = int(time.time())
        session_data["heartsLeft"] = 5
        session_data["failed"] = False
        session_data["quit"] = False
        
        if "challenges" in session_data:
            for idx in range(len(session_data["challenges"])):
                session_data["challenges"][idx]["status"] = "CORRECT"
            
        submit_url = f"https://www.duolingo.com/2017-06-30/sessions/{session_id}"
        try:
            submit_resp = requests.put(submit_url, headers=headers, json=session_data)
            if submit_resp.status_code == 200:
                xp_gained = submit_resp.json().get('xpGained', 10)
                total_xp_gained += xp_gained
                print(f"✅ Lesson {current_num} completed! Earned: +{xp_gained} XP (Total earned this session: {total_xp_gained} XP)")
            else:
                print(f"❌ Submission blocked by server: {submit_resp.status_code}")
                return
        except Exception as e:
            print(f"❌ Network request error: {e}")
            return

        # Add a tiny random break before the next lesson
        if current_num < TOTAL_LESSONS:
            cooldown = random.randint(3, 8)
            print(f"☕ Taking a quick break for {cooldown} seconds before the next lesson...")
            time.sleep(cooldown)

    print(f"\n🎉 Farming session complete!")
    print(f"📈 Summary: Successfully finished {TOTAL_LESSONS} lessons, contributed a total of {total_xp_gained} XP to your leaderboard.")
    print("🏆 Good luck with your league promotion this week!")

if __name__ == '__main__':
    farm_xp()