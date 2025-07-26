Keylogger – Ethical Key Capture Tool in Python
SkillCraft Cybersecurity Internship – Task 4
Author: B S Namith Kumar
Domain: Cybersecurity

Project Overview
This is a Python-based keylogger tool developed for Task 4 of my internship at SkillCraft Technology. It captures keystrokes in real time and logs them to a file for educational demonstration of keyboard input monitoring.

Features
Captures all keyboard input, including alphanumeric and special keys

Records keystrokes continuously to a text file (key_log.txt)

Runs in the background using a listener setup

Modular CLI/script structure for clean execution

Learning Outcomes
Learned how to use the pynput library to listen for keyboard events

Built logic for continuous monitoring and file output

Explored ethical considerations and importance of consent in cyber tools

Implemented a basic background process using Python

Practiced secure logging and simple file handling

Sample Usage
bash
Copy
Edit
python keylogger.py
Output:

A file named key_log.txt in the working directory

Every key pressed (letters, enter, space, shift, etc.) logged with timestamps

Notes
Requires pynput library (pip install pynput)

Intended for ethical and educational use only — do not deploy on devices without explicit permission

Compatible with Python 3.x on Windows, macOS, or Linux

Outputs a simple plaintext log; additional formatting or encryption can be added

How to Run
Install Python 3

Install dependency:

bash
Copy
Edit
pip install pynput
Run the script:

bash
Copy
Edit
python keylogger.py
Ethical Usage
This tool is designed strictly for learning and demonstration. Misuse of keylogging software can lead to serious legal consequences. Always obtain consent and respect privacy regulations.
