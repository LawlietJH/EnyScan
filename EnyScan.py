# Python 3
# By: LawlietJH
# 		v1.0.4
import socket

def Escaner():
	
	Puntos=0
	
	print ("\n\n\t Escaner de Puertos.")
			
	Ip = input("\n\n\t IP: ")
	
	print("\n\n\n\n")

	# Puertos Bien Conocidos.
	Puerto = [1, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 25, 37,\
			39, 42, 43, 49, 50, 53, 63, 67, 68, 69, 70, 79, 80, 88, 95,\
			101, 107, 109, 110, 111, 113, 115, 117, 119, 123, 135, 137,\
			138, 139, 143, 161, 162, 174, 177, 178, 179, 194, 199, 201,\
			202, 204, 206, 209, 210, 213, 220, 245, 347, 363, 369, 370,\
			372, 389, 427, 434, 435, 443, 444, 445, 465, 500, 512, 513,\
			514, 515, 520, 587, 591, 631, 666, 690, 993, 995, 1080, 1337]
			
	Tam = len(Puerto)
	
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
				print("\t [X] El Puerto " + str(Puerto[x]) + "/tcp Está cerrado.")

		else:
			if Puerto[x] == 53 or Puerto[x] == 67 or Puerto[x] == 68 or Puerto[x] == 69 or Puerto[x] == 123\
			or Puerto[x] == 161 or Puerto[x] == 500 or Puerto[x] == 514 or Puerto[x] == 520:
				
				print("\n [+] El Puerto " + str(Puerto[x]) + "/udp Está Abierto.\n")
			
			elif(Puerto[x] == 43):
				print("\n [+] El Puerto " + str(Puerto[x]) + "/betocp Está Abierto.\n")
			
			else:
				print("\n [+] El Puerto " + str(Puerto[x]) + "/tcp Está Abierto.\n")
				
	print ("\n\n [*] Escaneados " + str(Tam) + " Puertos.")


Escaner()
