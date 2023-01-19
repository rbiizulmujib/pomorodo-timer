import time
import os
import sys
import subprocess
from tqdm import tqdm
from plyer import notification


sleep = 1500
notification.notify(
    title = 'Pomorodo Timer',
    message = 'Happy Working!',
    app_icon = r"C:\Users\Mujib\Downloads\work-in-progress.ico",
    timeout = 5,
)

for i in tqdm(range(0, sleep), desc ="Waktu yang tersisa"):
    if i == 900:
        notify("Pomorodo Timer", "Hai, komputer akan sleep dalam 10 menit")
    if i == 1200:
        notify("Pomorodo Timer", "Hai, komputer akan sleep dalam 5 menit")
    if i == 1320:
        notify("Pomorodo Timer", "Hai, komputer akan sleep dalam 3 menit")
    if i == 1440:
        notify("Pomorodo Timer", "Hai, komputer akan sleep dalam 1 menit")
    if i == 1480:
        notify("Pomorodo Timer", "Hai, komputer akan sleep dalam 10 detik")
    time.sleep(1)

os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
