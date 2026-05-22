# DuoStreak-Keeper 🦉🚀

A lightweight, API-based，free automation tool to help you maintain your Duolingo streak with human-like, randomized activity intervals.

**⚠️ Disclaimer:** This tool is for educational purposes only. Automated activities may violate Duolingo's Terms of Service. Please maintain a reasonable usage frequency (e.g., 10-30 lessons daily) to mimic natural behavior and minimize account risk. Use at your own discretion.

## ✨ Features
* **Human-like Pacing:** Randomized delays (30-50s) to simulate real study sessions.
* **Smart XP Management:** Designed for maintaining streaks rather than aggressive leaderboard grinding.
* **Direct API Integration:** No heavy browser automation required; low resource consumption.

## 🛠️ Prerequisites
* **Python 3.x**
* **requests library:**
  ```bash
  pip install requests
<img width="2240" height="1260" alt="image" src="https://github.com/user-attachments/assets/103f4879-a3f7-4dc0-9b88-290a03274fa6" />

## ⭐ Support & Feedback
If you find **DuoFarmer** useful and it helped you keep your streak alive without the grind, please consider giving this repository a **Star (⭐)**! 

It really motivates me to keep this project updated and secure. If you have any suggestions or encounter any issues, feel free to open an **Issue**—I'm always happy to hear your feedback!

# DuoFarmer step-by-step Guide

A simple and effective Python script to automate Duolingo lessons and earn XP quickly. The entire setup boils down to one simple action: Extract your JWT Token. Once you have it, the script is ready to run!

## 🔑 JWT Extraction Guide

This method works on all major browsers (Chrome, Edge, Safari, Firefox) on both **Windows** and **macOS**.

1. Log in to [Duolingo](https://www.duolingo.com/) in your browser.
2. Open the Developer Tools:
   * **Windows/Chrome/Edge:** Press **F12** or **Ctrl + Shift + J**.
   * **macOS/Chrome:** Press **Cmd + Option + J**.
   * **macOS/Safari:** Press **Cmd + Option + C** (Ensure "Develop" menu is enabled).
3. Switch to the **Console** tab.
4. Paste the following command and press **Enter**:
   ```javascript
   document.cookie.split('; ').find(row => row.startsWith('jwt_token=')).split('=')[1]

## 🚀 Let's Farm!

1. Open `duofarmer.py` with your favorite text editor.
2. Paste your `jwt_token` into the `JWT_TOKEN` variable.
3. Configure `TOTAL_LESSONS` (suggested: 10-30).
4. Run the script in your terminal:

```bash
python duofarmer.py

