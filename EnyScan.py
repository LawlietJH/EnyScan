# Python 3
# By: LawlietJH
# 		v1.0.7
import keyboard
import socket
import time
import os

def Escaner():
	
	Puntos=0
	ListP = []
	
	print ("\n\n\t Escaner de Puertos.")
	
	Ip = input("\n\n\t IP: ")
	
	print("\n\n\n\n")

	# Puertos Para Escanear.
	Puerto = [1, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 25, 37,\
			39, 42, 43, 49, 50, 53, 63, 67, 68, 69, 70, 79, 80, 88, 95,\
			101, 107, 109, 110, 111, 113, 115, 117, 119, 123, 135, 137,\
			138, 139, 143, 161, 162, 174, 177, 178, 179, 194, 199, 201,\
			202, 204, 206, 209, 210, 213, 220, 245, 347, 363, 369, 370,\
			372, 389, 427, 434, 435, 443, 444, 445, 465, 500, 512, 513,\
			514, 515, 520, 587, 591, 631, 666, 690, 993, 995, 1080, 1337]
			
			
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
		time.sleep(3)
		exit(0)
	
	
	print ("\n\n [*] Escaneados " + str(Tam) + " Puertos.\n\n")
	
	
	print("\n\n\n Presiona Un Comando:\n")
	print("\t 'Ctrl + Z' \t - Ver Lista de Puertos Abiertos.")
	print("\t 'Esc' \t\t - Salir.")
	
	
	Entry = True
	Ctrl_Z = True
	
	while Entry and Ctrl_Z:
		
		try:
			if keyboard.is_pressed('Ctrl+Z'):
			
				os.system("cls && Title Puertos Abiertos en la IP: "+Ip)
				
				print("\n\n [*] Puertos Abiertos: \n\n")
				
				for P in ListP:
				
					print("\n\t [+] Puerto " + P)
				
				Ctrl_Z = False
				
			elif keyboard.is_pressed('Esc'):
				
				Entry = False
			
			else:
				pass
		
		except:
			pass
	

Escaner()
