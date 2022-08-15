import time
import pyautogui

#timeOut is in seconds.
timeOut = 60
looped = 0
minutes = 0
hours = 0

print("Work started!")
while (True):
  time.sleep(timeOut)
  looped += 1
  minutes = int((looped*(timeOut/60)) % 60)
  hours = int((looped*(timeOut/60))//60)
  if(hours == 0):
    print("Working for", minutes, "minutes")
  else:
    print("Working for", hours, "hours and", minutes, "minutes")
  pyautogui.move(0, 1)
  pyautogui.move(0, -1)
