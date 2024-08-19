import pyautogui,keyboard



   
print(r'''

      _   _____  _____  _________    ___              ______  _____     _____   ______  ___  ____   
     / \ |_   _||_   _||  _   _  | .'   `.          .' ___  ||_   _|   |_   _|.' ___  ||_  ||_  _|  
    / _ \  | |    | |  |_/ | | \_|/  .-.  \ ______ / .'   \_|  | |       | | / .'   \_|  | |_/ /    
   / ___ \ | '    ' |      | |    | |   | ||______|| |         | |   _   | | | |         |  __'.    
 _/ /   \ \_\ \__/ /      _| |_   \  `-'  /        \ `.___.'\ _| |__/ | _| |_\ `.___.'\ _| |  \ \_  
|____| |____|`.__.'      |_____|   `.___.'          `.____ .'|________||_____|`.____ .'|____||____| ''')
                                                                                                    
print(r'''
MMMMMMMO:oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMk. 'oXMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMk.   'dXMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMk.     'dXMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMk.       'dXMMMMMMMMMMMMMMMMMMMMM
MMMMMMMk.         'x0XMMMMMMMMMMMMMMMMMM
MMMMMMMk.           .,xXMMMMMMMMMMMMMMMM
MMMMMMMk.              ,xNMMMMMMMMMMMMMM
MMMMMMMk.                ,xNMMMMMMMMMMMM
MMMMMMMk.                  ,kNMMMMMMMMMM
MMMMMMMk.                    ;kNMMMMMMMM
MMMMMMMk.              .'',,;;l0WMMMMMMM
MMMMMMMk.              ;0NWWWWMMMMMMMMMM
MMMMMMMk.    .,.        lNMMMMMMMMMMMMMM
MMMMMMMk.  ,dXNl        .dWMMMMMMMMMMMMM
MMMMMMMO,:kNMMMX:        .kWMMMMMMMMMMMM
MMMMMMMNXWMMMMMM0,        'OMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWO'        ;KMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWx.    .,cxXMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMXc..,oONMMMMMMMMMMMMMM
''')
print('por Urb@n')

tecla_pausa= '-'
tecla_avanzar = '1'
tecla_ejecucion= '|'

print(f'''
ejecutar script:{tecla_ejecucion}
pausar script:{tecla_pausa}
ejecutar tecla para avanzar (primero ejecutar script):{tecla_avanzar} 
''')

def ejecucion():
        try:
            while not keyboard.is_pressed('-'):
                pyautogui.mouseDown()
                if keyboard.is_pressed('1'):
                    keyboard.press('w')
        except:
            escuchando()

def escuchando():
    keyboard.add_hotkey('|',ejecucion)
    keyboard.wait()
    
escuchando()

