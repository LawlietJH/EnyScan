# -*- coding: utf-8 -*-
# Python 3
#                                                                  
#     ███████╗███╗   ██╗██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
#     ██╔════╝████╗  ██║╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
#     █████╗  ██╔██╗ ██║ ╚████╔╝ ███████╗██║     ███████║██╔██╗ ██║
#     ██╔══╝  ██║╚██╗██║  ╚██╔╝  ╚════██║██║     ██╔══██║██║╚██╗██║
#     ███████╗██║ ╚████║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║
#     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
#                                                         By: LawlietJH
#                                                               v1.2.0

import threading
import socket
import time
import sys
import re
import os

#~ https://www.ciberbyte.com/ciberseguridad/buscar-hosts-vivos-python/

Autor = "LawlietJH"
Version = "v1.2.0"



def Chk_Dep():
	
	try:
		import keyboard
		
	except ModuleNotFoundError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		os.system("Title Instalando Keyboard && py -m pip install keyboard > Nul && cls && Title EnyScan.py            By: LawlietJH")
		
	except ImportError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		os.system("Title Instalando Keyboard && py -m pip install keyboard > Nul && cls && Title EnyScan.py            By: LawlietJH")
		
	except Exception as ex:
		print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.



Chk_Dep()				#~ Se instala el módulo keyboard si este no esta instalado.
try:
	import keyboard 	# Se Importa El Módulo.
except:					# Si Hay Algún Error Significa Que No Se Instaló Correctamente.
	print("\n\n   No se pudo instalar correctamente el Módulo 'keyboard'.")
	print("\n   Revise Su Conexión o Instale El Módulo Manualmente Desde Consola Con:")
	print("\n\t 'py -m pip install keyboard'   o   'pip install keyboard'")
	
	try:
		os.system("Pause > Nul")
	except KeyboardInterrupt: pass
	
	Dat()
	Salir(0)



def Salir(Num=0):
	
	try:
		sys.exit(Num)
		
	except KeyboardInterrupt:
		Salir(Num)



def Modo_De_Uso():
	
	os.system("Cls")
	
	print("\n\n [+] Modo de Uso:")
	print("\n\n  abs == 192.168.1.0/24 \t(All Bytes + SubRed)")
	print("\n  ab  == 192.168.1.0 \t\t(All Bytes)")
	print("\n  bs  == 192.168 \t\t(Bytes 1 y 2)")
	print("\n\n [+] Ejemplos:")
	print("\n\n  192.168.1.0/24 o abs (Escanea Toda la subred)")
	print("\n  -r 0/99 192.168.1.0 (Escanea entre la subred 192.168.1.0 y 192.168.1.99)")
	print("\n  -r 60/70 ab (Escanea entre la subred 192.168.1.60 y 192.168.1.70)")
	
	os.system("Pause > Nul")
	



def Set_IP(Eny = "P", CadenaIP = "\n\n\t > "):
	
	global Ip
	xD = False
	xD2 = False
	Imp = ""
	
	try:
		# Validar IP.
		while(xD == False):
			
			xD = True
			
			if Eny == "S": print("\n\n\t\t Ejemplo: 192.168.1.0/24 | -r 60/70 192.168.1.0\n\n\t\t\t  [ -h | help | ? | /? ]")
			elif Eny == "P": print ("\n\n\t Escaner de Puertos.")
			
			Ip = input(CadenaIP)
			
			if Ip == "-h" or Ip == "help" or Ip == "?" or Ip == "/?":
				
				Modo_De_Uso()
				os.system("Cls")
				xD2 = True
			
			Ip = Ip.replace("abs", "192.168.1.0/24")
			Ip = Ip.replace("ab", "192.168.1.0")
			Ip = Ip.replace("bs", "192.168")
			
			if Eny == "S": Imp = Ip.split(" ")[-1].replace("/24", "").strip()
			elif Eny == "P": Imp = Ip
			
			Patron = "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
				
			if re.search(Patron, Imp):
				
				Byte = Imp.split(".")
				
				for x in range(4):
					
					if (int(Byte[x]) < 0 or (int(Byte[x])) > 255): xD = False
				
			else: xD = False
			
			if xD: break
			else: 
				if xD2: pass
				else:
					xD2 = False
					print("\n\n\n\t Ip No Válida."), time.sleep(1)
	
	except KeyboardInterrupt:
		print("\n\n\t [!] Cancelando!...\n\n")
		time.sleep(2)
		Salir(0)
		
	except EOFError:
		print("\n\n\t [!] Cancelando!...\n\n")
		time.sleep(2)
		Salir(0)



def EscanerThread(x):
	
	global ListP
	
	Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	if Sock.connect_ex((Ip, x)):
		
		if x == 53 or x == 67 or x == 68 or x == 69\
		 or x == 123 or x == 161 or x == 162 or x == 500\
		 or x == 514 or x == 520: pass
			
			#~ print("\t [X] El Puerto " + str(x) + "/udp Está Cerrado.")
		
		elif(x == 43): pass
			#~ print("\t [X] El Puerto " + str(x) + "/betocp Está Cerrado.")
		
		else: pass
			#~ print("\t [X] El Puerto " + str(x) + "/tcp Está Cerrado.")

	else:
		if x == 53 or x == 67 or x == 68 or x == 69 or x == 123\
		 or x == 137 or x == 138 or x == 161 or x == 192 or x == 500\
		 or x == 514 or x == 520 or x == 623 or x == 1701 or x == 1900\
		 or ( x >= 3478 and x <= 3497 ) or x == 4398 or x == 4500\
		 or x == 5350 or x == 5351 or x == 5353 or x == 5597\
		 or x == 5898 or x == 6970 or x == 9999 or x == 7070:
			
			print(" [+] El Puerto " + str(x) + "/udp Está Abierto.")
			ListP.append(str(x)+"/udp")
			
		elif(x == 43):
			print(" [+] El Puerto " + str(x) + "/betocp Está Abierto.")
			ListP.append(str(x)+"/betocp")
			
		else:
			print(" [+] El Puerto " + str(x) + "/tcp Está Abierto.")
			ListP.append(str(x)+"/tcp")



def Escaner():
	
	global ListP
	
	Set_IP("P")
	
	print("\n\t IP: " + Ip)
	
	print("\n\n\n\n")

	# Puertos Para Escanear.
	Puerto = [ x for x in range(65536)]
			
	#~ Para pruebas
	#~ Puerto =[1,7,9,135,139]
			
	Tam = len(Puerto)
	try:
		for x in range(0, Tam):
			
			t = threading.Thread(target=EscanerThread, args=(Puerto[x], ))  
			t.start()
				
	except KeyboardInterrupt:
		os.system("Title Cancelando...")
		print("\n\n\t [!] Cancelando!...\n\n")
		time.sleep(2)
		Salir(0)
	
	
	print ("\n\n [*] Escaneados " + str(Tam) + " Puertos.\n\n")



def Get_Puertos_Abiertos():
	
	if ListP == []:
		
		print("\n\t No Hay Puertos.")
		
	else:
		
		for P in ListP:
			
			print("\n\t [+] Puerto " + P)



def Get_Servidores_Activos():
	
	if ListR == []:
		
		print("\n\t No Hosts Activos.")
		
		os.system("Pause > Nul")
		
	else:
		
		for R in ListR:
			
			print("\n\t [+] Host " + R)
		
		os.system("Pause > Nul")


def Ver_Puertos_Abiertos():

	print("\n\n\n Presiona Un Comando:\n")
	print("\t 'L' \t - Ver Lista de Puertos Abiertos.")
	print("\t 'Esc' \t\t - Salir.")
	
	
	while True:
		
		try:
			
			if keyboard.is_pressed('L'):
			
				os.system("cls && Title Puertos Abiertos en la IP: "+Ip)
				
				print("\n\n [*] Puertos Abiertos: \n\n")
				
				Get_Puertos_Abiertos()
				
				break
				
			elif keyboard.is_pressed('Esc'):
				
				break
			
			else:
				pass
		
		except:
			pass



def Ver_Servidores_Activos():

	print("\n\n\n Presiona Un Comando:\n")
	print("\t 'L' \t - Ver Lista de Servidores Activos.")
	print("\t 'Esc' \t\t - Salir.")
	
	
	try:
		
		while True:
					
			if keyboard.is_pressed('L'):
			
				os.system("cls && Title Puertos Abiertos en la Red: ")
				
				print("\n\n [*] Servidores Activos: \n\n")
				
				Get_Servidores_Activos()
				
				break
				
			elif keyboard.is_pressed('Esc'):
				break
			
			else:
				pass
		
	except KeyboardInterrupt:
		pass
		
	except:
		pass




def Ecanear_Subred():
	
	global ListR
	global Ip
	ListR = []
	Ip_Ran = ""
	Ip_Rango = ""
	Red = ""
	Inicio = 0
	Fin = 0
	
	os.system("cls && Title Analizar Subred...")
	
	try:
		
		while True:
			
			os.system("cls")
			
			Set_IP("S")
			
			if "/24" in Ip:
				ALL = True
				
				Ip = Ip.replace("/24","")
				Ip_Separada = Ip.split(".")
				Red = Ip_Separada[0] + "." + Ip_Separada[1] + "." + Ip_Separada[2] + "."
				
				Inicio = 0
				Fin = 255
			
			elif "-r" in Ip:
				
				if (" / " in Ip or " /" in Ip or "/ " in Ip):
						
						print("\n\n\t\t [!] Comando No Valido!")
						time.sleep(2)
				else:
				
					Ip_R = Ip.split(" ")
					
					if Ip_R[0] == "-r":
						
						Ip_Ran = Ip_R[1]
						Ip = Ip_R[2]
						
						Ip_Rango = Ip_Ran.split("/")
						
						Inicio = int(Ip_Rango[0])
						Fin = int(Ip_Rango[1])
						
						Ip_Separada = Ip.split(".")
						Red = Ip_Separada[0] + "." + Ip_Separada[1] + "." + Ip_Separada[2] + "."
						
						if Inicio > Fin:
							
							Aux = Inicio
							Inicio = Fin
							Fin = Aux
			
			else: pass	
			break
		
		# Buscando Hosts Activos

		ping = "ping -n 1 "

		print("\n\n\t [*] Scaneando Servidores Desde " + Red +
			str(Inicio) + " a " + Red + str(Fin) + "\n\n")

		for Subred in range(Inicio, Fin + 1):
			
			Activo = False
			Direccion = Red + str(Subred)
			Respuesta = os.popen(ping + Direccion)
			
			for Linea in Respuesta.readlines():
				
				if "ttl" in Linea.lower():
					
					print("\n    [+]", Direccion, "Activo.\n")
					ListR.append(Direccion)
					Activo = True
					break
			
			if not Activo:
				
				print("\t [-]", Direccion, "No Esta Activo.")
	
		Ver_Servidores_Activos()
		
	except KeyboardInterrupt:
		os.system("Title Cancelando...")
		print("\n\n\t [!] Cancelando!...\n\n")
		time.sleep(2)
		
	
	except:
		print("\n\n\t [!] Ip No Valida.")
		os.system("Title Ip No Valida!")
		time.sleep(2)






def Menu_Opciones():

	try:
		
		while True:
				
			os.system("cls && Title EnyScan.py           By: LawlietJH")
			print("\n\n\n Elige Una Opción.\n")
			print("\t 1 - Escanear Puertos.")
			print("\t 2 - Escanear Subred.")
			print("\t 0 - Salir.")
		
			xD = int(input("\n\t Elige Una Opción: "))
				
			if xD == 1:
				
				os.system("cls && Title Analizar Puertos de Un Host")
				
				Escaner()
				#~ Ver_Puertos_Abiertos()
				os.system("Pause > Nul")
				
			if xD == 2:
			
				os.system("cls && Title Analizar Subred")
				
				Ecanear_Subred()
				
			elif xD == 0:
				break
			
			else: pass
		
	except KeyboardInterrupt:
		os.system("Title Bye Bye...")
		print("\n\n\t\t\t  [*] Bye Bye...\n\n")
		time.sleep(2)
		Salir(0)
		
	except: pass




Ip = ""
ListP = []
ListR = []


	
def main():
	
	Menu_Opciones()
	

main()
