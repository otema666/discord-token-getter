from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, init, Style
import win32clipboard
import ctypes
import requests

import os
import time

ctypes.windll.kernel32.SetConsoleTitleW("Discord Token getter")
# Inicio tol colorama
init()

#Defino los colores
BLUE = Fore.BLUE
RED = Fore.RED 
GREEN= Fore.GREEN
YELLOW = Fore.YELLOW
PURPLE= Fore.MAGENTA
CIAN = Fore.CYAN
RESET = Fore.RESET

def animate_text(text, color, sec):
    for char in text:
        # Cambia el color de la letra
        print(color + char, end='', flush=True)
        time.sleep(sec)

    # Resetea el color de la letra
    print(Style.RESET_ALL)

def espacio():
    for a in range(24):
        print(Fore.GREEN + "-" + Style.RESET_ALL, end="", flush=True)
        print(Fore.RED + "-" + Style.RESET_ALL, end="", flush=True)  
        print(Fore.BLUE + "-" + Style.RESET_ALL, end="", flush=True)
        print(Fore.YELLOW + "-" + Style.RESET_ALL, end="", flush=True)
        print(Fore.MAGENTA + "-" + Style.RESET_ALL, end="", flush=True)

def loading(pts):
    for i in range(pts):
        time.sleep(0.25)
        print(".", end="", flush=True)

def execute_browser():
    nav = int(input())
    if nav == 1:
        print()
        print(f'{GREEN}Navegador ejecutado:     ',  end="")
        animate_text("G O O G L E  C H R O M E", BLUE, 0.05)
        print()
        
        # Configuramos el navegador GOOGLE CHROME
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-extensions')
        options.add_argument('--profile-directory=Default')
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
    
    elif nav == 2:
        print()
        print(f'{GREEN}Navegador ejecutado:     ',  end="")
        animate_text("B R A V E  B R O W S E R", BLUE, 0.05)
        print()
        
        # Configuramos el navegador Brave Browser
        options = webdriver.ChromeOptions()
        options.binary_location = 'C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'
        options.add_argument('--disable-extensions')
        options.add_argument('--profile-directory=Default')
        options.add_argument("--disable-plugins-discovery")
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
    
    elif nav == 3:
        print()
        print("Navegador ejecutado:     ", end="")
        animate_text("F I R E F O X", BLUE, 0.05)
        print()
        
        # Configuramos el navegador Firefox
        options = webdriver.FirefoxOptions()
        options.add_argument('--start-maximized')
        options.add_argument("--start-maximized")
        options.add_argument('--private-window')
        driver = webdriver.Firefox(options=options)
        
    else:
        animate_text("Respuesta no válida!!", RED, 0)
        print()
        return False
    
    driver.get("https://discord.com/login")
    os.system("cls")
    # Esperar hasta que se cargue la página después de iniciar sesión
    print(f"{BLUE}Esperando a que se inicie sesión...{RESET}")
    WebDriverWait(driver, 300).until(
        EC.url_contains("https://discord.com/channels/")
    )
    print(f"[{GREEN}√{RESET}] Sesión iniciada correctamente")
    espacio()
    print()
    

    tokenGetter = open("getToken.js").read()

    
    driver.execute_script(tokenGetter)
    print("Ejecutando script", end="")
    loading(6)
    os.system("cls")
    espacio()
    win32clipboard.OpenClipboard()
    token = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    res = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
    
    res_json = res.json()
    user_name = f'{res_json["username"]}#{res_json["discriminator"]}'
    print(f'{Fore.LIGHTWHITE_EX}Nombre de la cuenta: {Fore.GREEN}{user_name}')
    print()


    
    print(f'{Fore.LIGHTWHITE_EX}Token: {Fore.GREEN}{token}{Fore.RESET}')
    print()
    print(f'{Fore.MAGENTA}El token ha sido copiado al portapapeles correctamente.{Fore.RESET}')
    espacio()
    print(" ")

    print(f'{RED}Presiona ENTER para salir', end="")
    input()
    driver.quit()
    print(f"{Fore.RED}Saliendo...{Fore.RESET}")



os.system("cls")
animate_text("Qué navegador desea usar?", GREEN, 0.002)
print()
animate_text("1. Google Chrome", PURPLE, 0.0005)
animate_text("2. Brave Browser", YELLOW, 0.0005)
animate_text("3. Firefox", RED, 0.001)
espacio()


while True:
    if execute_browser() != False:
        break
    else:
        continue
