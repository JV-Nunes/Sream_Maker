import pyautogui
import time
import random
 
def click():      
    pyautogui.click()

def move_to_replay(x,y):
    pyautogui.moveTo(x,y)

def main():
    x = int(input("Insira a quantidade desejada de streams: "))
    display_message()
    for i in range(x):
        time.sleep(random.randint(31,40))
        move_to_replay(638,656)
        click()

def display_message():
    print("Abra a janela do spotify.")
    time.sleep(1)
    print("Aguardando 10 segundos...")
    time.sleep(9)

main()