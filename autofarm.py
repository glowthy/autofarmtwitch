import pyautogui
import time
import keyboard

attente = 10      
marge_vert = 100       

actif = False


def est_vert(r, g, b):
    return g > marge_vert and g > r * 1.3 and g > b * 1.3


def toggle():
    global actif
    actif = not actif
    print("ACTIVÉ" if actif else "DÉSACTIVÉ")


keyboard.add_hotkey("f8", toggle)

print("Programme lancé.")
print("Appuie sur F8 pour activer/désactiver.")
print("Appuie sur Échap pour quitter.")

while True:
    if keyboard.is_pressed("esc"):
        break

    if actif:
        x, y = pyautogui.position()
        r, g, b = pyautogui.pixel(x, y)
        if est_vert(r, g, b):
            pyautogui.click()
            time.sleep(0.2)
    time.sleep(attente)

print("Programme arrêté.")