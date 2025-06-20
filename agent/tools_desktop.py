import pyautogui
import time
import subprocess
import platform

def write_to_notepad(text):
    # Windows Notepad
    if platform.system() == "Windows":
        subprocess.Popen(['notepad.exe'])
    else:
        # For Mac, use TextEdit
        subprocess.Popen(['open', '-a', 'TextEdit'])
    time.sleep(2)  # Wait for app to open

    pyautogui.typewrite(text, interval=0.01)
    # Optionally, save the file with a hotkey
    # pyautogui.hotkey('ctrl', 's')
    # pyautogui.typewrite("AI_Research_Summary.txt")
    # pyautogui.hotkey('enter')
