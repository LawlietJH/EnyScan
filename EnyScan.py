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
#                                                               v1.1.5

import socket
import time
import os

#~ https://www.ciberbyte.com/ciberseguridad/buscar-hosts-vivos-python/

Autor = "LawlietJH"
Version = "v1.1.5"



def Chk_Dep():
	
	try:
		import keyboard
		
	except ModuleNotFoundError:
		print("\n\n\t[!] Instalando Dependencias...\n\n\t\t")
		os.system("Title Instalando Keyboard && pip install keyboard > Nul && cls && Title EnyScan.py            By: LawlietJH")
		
	except Exception as ex:
		print( type(ex).__name__ )		#Ver cuando ocurre un error y poder añadirlo a las ecepciones, y no cierre el programa.

Chk_Dep()				#~ Se instala el módulo pytube si esta no esta instalada.
import keyboard 		#~ Se importa la módulo.



def Salir(Num=0):
	
	try:
		exit(Num)
		
	except KeyboardInterrupt:
		Salir(Num)



def Set_IP():
	
	global Ip
	Puntos = 0
	
	try:
		# Validar IP.
		while(Puntos != 3):
			
			Ip = input("\n\n\t IP: ")

			TamIp= len(Ip)

			for x in range (0, TamIp):
			
				if (Ip[x] == "."):
					
					Puntos = Puntos + 1
					
			if(Puntos == 3): break
			else: print("\n\n\n\t Ip No Válida.")
	
	except KeyboardInterrupt:
		print("\n\n\t [!] Cancelando!...\n\n")
		time.sleep(2)
		Salir(0)


def Set_IP_Base():
	
	global Ip
	Puntos = 0
	
	# Validar IP.
	while(Puntos != 3):
		
		os.system("cls")
		
		print("\n\n\t\t Ejemplo: 192.168.1.0/24 | -r 60/70 192.168.1.0\n")
		
		Ip = input("\n\n\t IP Base de Subred: ")
		
		TamIp= len(Ip)

		for x in range(0, TamIp):
		
			if (Ip[x] == "."):
				
				Puntos = Puntos + 1
				
		if(Puntos == 3): break
		else:
			print("\n\n\n\t Ip No Válida.")
			time.sleep(1)




def Escaner():
	
	global ListP
	
	print ("\n\n\t Escaner de Puertos.")
	
	Set_IP()
	
	print("\n\n\n\n")

	# Puertos Para Escanear.
	Puerto = [1, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 25, 37,\
			39, 42, 43, 49, 50, 53, 63, 67, 68, 69, 70, 79, 80, 88, 95,\
			101, 107, 109, 110, 111, 113, 115, 117, 119, 123, 135, 137,\
			138, 139, 143, 161, 162, 174, 177, 178, 179, 194, 199, 201,\
			202, 204, 206, 209, 210, 213, 220, 245, 347, 363, 369, 370,\
			372, 389, 427, 434, 435, 443, 444, 445, 465, 500, 512, 513,\
			514, 515, 520, 587, 591, 631, 666, 690, 993, 995, 1080, 1337]
			
	#~ Para pruebas
	#~ Puerto =[1,7,9,135,139]
			
	Tam = len(Puerto)
	try:
		for x in range(0, Tam):
			
			Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			
			if Sock.connect_ex((Ip, Puerto[x])):
				
				if Puerto[x] == 53 or Puerto[x] == 67 or Puerto[x] == 68 or Puerto[x] == 69\
				or Puerto[x] == 123 or Puerto[x] == 161 or Puerto[x] == 162 or Puerto[x] == 500\
				or Puerto[x] == 514 or Puerto[x] == 520:
					
					print("\t [X] El Puerto " + str(Puerto[x]) + "/udp Está Cerrado.")
				
				elif(Puerto[x] == 43):
					print("\t [X] El Puerto " + str(Puerto[x]) + "/betocp Está Cerrado.")
				
				else:
					print("\t [X] El Puerto " + str(Puerto[x]) + "/tcp Está Cerrado.")

			else:
				if Puerto[x] == 53 or Puerto[x] == 67 or Puerto[x] == 68 or Puerto[x] == 69 or Puerto[x] == 123\
				or Puerto[x] == 161 or Puerto[x] == 500 or Puerto[x] == 514 or Puerto[x] == 520:
					
					print("\n [+] El Puerto " + str(Puerto[x]) + "/udp Está Abierto.\n")
					ListP.append(str(Puerto[x])+"/udp")
					
				elif(Puerto[x] == 43):
					print("\n [+] El Puerto " + str(Puerto[x]) + "/betocp Está Abierto.\n")
					ListP.append(str(Puerto[x])+"/betocp")
					
				else:
					print("\n [+] El Puerto " + str(Puerto[x]) + "/tcp Está Abierto.\n")
					ListP.append(str(Puerto[x])+"/tcp")
				
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
		
	else:
		
		for R in ListR:
			
			print("\n\t [+] Host " + R)



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
	
	
	while True:
		
		try:
			
			if keyboard.is_pressed('L'):
			
				os.system("cls && Title Puertos Abiertos en la Red: ")
				
				print("\n\n [*] Servidores Activos: \n\n")
				
				Get_Servidores_Activos()
				
				break
				
			elif keyboard.is_pressed('Esc'):
				
				break
			
			else:
				pass
		
		except:
			pass




def Ecanear_Subred():
	
	global ListR
	global Ip
	Ip_Ran = ""
	Ip_Rango = ""
	Red = ""
	Inicio = 0
	Fin = 0
	
	
	os.system("cls && Title Analizar Subred...")
	
	try:
		
		while True:
			
			Set_IP_Base()
			
			if "/24" in Ip:
				ALL = True
				
				Ip = Ip.replace("/24","")
				Ip_Separada = Ip.split(".")
				Red = Ip_Separada[0] + "." + Ip_Separada[1] + "." + Ip_Separada[2] + "."
				Inicio = 2
				Fin = 254
			
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

		print("\n\n\t [*] Scaneando Servidores Desde", Red +
			str(Inicio), "a", Red + str(Fin), "\n\n")

		for Sub_Red in range(Inicio, Fin + 1):
			
			Activo = False
			Direccion = Red + str(Sub_Red)
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
			print("\t 2 - Escanear Red.")
			print("\t 0 - Salir.")
		
			xD = int(input("\n\t Elige Una Opción: "))
				
			if xD == 1:
				
				os.system("cls && Title Analizar Puertos de Un Host")
				
				Escaner()
				Ver_Puertos_Abiertos()
				
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
