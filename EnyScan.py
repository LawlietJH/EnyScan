# Python 3
# By: LawlietJH
# 		v1.0.1
import socket

def Escaner():
	
	Puntos=0
	
	print ("\n\n\t Escaner de Puertos.")
			
	Ip = input("\n\n\t IP: ")
	
	print("\n\n\n\n")

	# Puertos Bien Conocidos.
	Puerto = [1,7,9,13,17,19,20,21,22,23,\
			25,37,43,53,67,68,69,70,79,80,\
			88,110,111,113,119,123,135,137,138,139,\
			143,161,162,177,389,443,445,465,500,512,\
			513,514,515,520,587,591,631,666,690,993,\
			995,1080]
			
	Tam = len(Puerto)
	
	for x in range(0, Tam):
		
		Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		
		if Sock.connect_ex((Ip, Puerto[x])):

			if Puerto[x] == 53 or Puerto[x] == 67 or Puerto[x] == 68 or Puerto[x] == 69 or Puerto[x] == 123\
			or Puerto[x] == 161 or Puerto[x] == 500 or Puerto[x] == 514 or Puerto[x] == 520:
				
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
