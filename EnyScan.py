# -*- coding: utf-8 -*-
# Python 3
#                                                                  
#                                                                  
#     ███████╗███╗   ██╗██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
#     ██╔════╝████╗  ██║╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
#     █████╗  ██╔██╗ ██║ ╚████╔╝ ███████╗██║     ███████║██╔██╗ ██║
#     ██╔══╝  ██║╚██╗██║  ╚██╔╝  ╚════██║██║     ██╔══██║██║╚██╗██║
#     ███████╗██║ ╚████║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║
#     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
#                                                                  
#                                                         By: LawlietJH
#                                                               v1.1.0

import keyboard
import socket
import time
import os



Autor = "LawlietJH"
Version = "v1.1.0"



def Salir(Num=0):
	try:
		time.sleep(1)
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
		Salir(0)
		
	
	

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
		print("\n\n\t\t Cancelando...\n\n")
		Salir(0)
	
	
	print ("\n\n [*] Escaneados " + str(Tam) + " Puertos.\n\n")
	


def Get_Puertos_Abiertos():
	
	if ListP == []:
		
		print("\n\t No Hay Puertos.")
		
	else:
		
		for P in ListP:
			
			print("\n\t [+] Puerto " + P)



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

Ip = ""
ListP = []
	
def main():
	
	Escaner()
	Ver_Puertos_Abiertos()
	

main()
