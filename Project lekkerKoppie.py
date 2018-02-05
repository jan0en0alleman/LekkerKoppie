from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def lekkerKonkie():
    F1 = True

    print("Welkom bij Operatie lekkerKoppie.")

    acti = input("Wil je de Spam beginnen? (voer in: Ja of Nee)")

    if acti == 'Ja' or acti == "ja":
        print("Operatie begint over 5 seconden klik op je text veld.")
        time.sleep(5)
    else:
        print('Tot de volgende keer lekkerDag')
        return

    while F1 == True:
        for char in ("lekkerKoppie "*30):
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.005)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        for char in ("lekkerKoppie "*29):
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.005)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

lekkerKonkie()