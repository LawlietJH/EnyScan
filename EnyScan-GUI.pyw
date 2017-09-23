# -*- Coding: UTF-8 -*-
# Python 3
#                                                                  
#     ███████╗███╗   ██╗██╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
#     ██╔════╝████╗  ██║╚██╗ ██╔╝██╔════╝██╔════╝██╔══██╗████╗  ██║
#     █████╗  ██╔██╗ ██║ ╚████╔╝ ███████╗██║     ███████║██╔██╗ ██║
#     ██╔══╝  ██║╚██╗██║  ╚██╔╝  ╚════██║██║     ██╔══██║██║╚██╗██║
#     ███████╗██║ ╚████║   ██║   ███████║╚██████╗██║  ██║██║ ╚████║
#     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
#                                                         By: LawlietJH
#                                                         GUI - v1.3.2
# http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=EnyScan

from tkinter import *
import threading
import datetime
import socket
import time
import sys
import os



Version = "v1.3.2"



#=======================================================================



IP = ""
Eny = True
Cont = 0
Comando = ""
Puerto = [ x for x in range(1,65536) ]
#~ Puerto = [ x for x in range(1,6553) ]
Host = [ x for x in range(0,255) ]
Tam = len(Puerto)
TamH = len(Host)
Inicio = 0
Final = 0


def EscanerThread(x, IP, win):
	
	global Cont
		
	Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	if not Sock.connect_ex((IP, x)):
		
		Cont += 1
		
		e3 = Label(win, text="El Puerto "+str(x)+" Está Abierto.",\
				font="timesnewroman 9 bold", justify="left",\
				bg="cadetblue", fg="darkblue", bd=0,\
				highlightbackground="#1E6FBA", highlightcolor="red",\
				highlightthickness=1)
		e3.pack(padx=5,pady=5,ipadx=5,ipady=0,fill=X)
		
		root.update_idletasks()
	
	if x == Tam-1:
		
		e3 = Label(win, text="Escaneo Finalizado.",\
				font="Calibri 10 bold", \
				bg="cadetblue", fg="white", anchor=W, justify=LEFT, bd=0,\
				highlightbackground="#1E6FBA", highlightcolor="red",\
				highlightthickness=1)
		e3.pack(padx=5,pady=10,ipadx=5,ipady=5,fill=X)



def Hosts(Subred, Fr, win, Activo, Red, ping):
	
	global Comando
	global Cont
	global IP
	global Final
	
	Activo = False
	Direccion = Red + str(Subred)
	Respuesta = os.popen(ping + Direccion)
	
	for Linea in Respuesta.readlines():
		
		if "ttl" in Linea.lower():
			
			Cont += 1
			
			e3 = Label(win, text="El Host "+str(Direccion)+" Está Activo.",\
					font="timesnewroman 9 bold", justify="left",\
					bg="cadetblue", fg="darkblue", bd=0,\
					highlightbackground="#1E6FBA", highlightcolor="red",\
					highlightthickness=1)
			e3.pack(padx=5,pady=5,ipadx=5,ipady=0,fill=X)
			
			root.update_idletasks()
			
			Activo = True
			break

	if Subred == Final:
		
		time.sleep(4)
		# Host Activos...
		
		Texto3.delete(0,100)
		Texto3.insert(0, str(Cont)+" Host Activos de "+str(TamH)+" Escaneados.")
	
		Texto2.delete(0,100)
		Texto2.insert(0, str(Comando))
		
		e3 = Label(win, text="Host Activos: "+str(Cont),\
					font="Calibri 10 bold", \
					bg="cadetblue", fg="white", anchor=W, justify=LEFT, bd=0,\
					highlightbackground="#1E6FBA", highlightcolor="red",\
					highlightthickness=1)
		e3.pack(padx=5,pady=0,ipadx=5,ipady=5,fill=X)
		
		e3 = Label(win, text="Escaneo Finalizado.",\
				font="Calibri 10 bold", \
				bg="cadetblue", fg="white", anchor=W, justify=LEFT, bd=0,\
				highlightbackground="#1E6FBA", highlightcolor="red",\
				highlightthickness=1)
		e3.pack(padx=5,pady=10,ipadx=5,ipady=5,fill=X)
		
		root.update_idletasks()
		
		Cont = 0



def Cerrar(ventana): ventana.exit()
def Mostrar(ventana): ventana.deiconify()
def Ocultar(ventana): ventana.withdraw()

def ejecutar(Funcion): root.after(200,Funcion)



def Puertos(Fr): # Función que obtiene los Puertos Abiertos de una IP.
	
	global TamH
	global Cont
	global Comando
	global Eny
	global Inicio
	global Final
	global IP
	
	Inicio = 0
	Final = 0
	TamH = len(Host)
	Cont = 0
	Eny = True
	Elaine = False
	
	IP = Texto1.get().strip()
	Comando = IP
	
	# Validar IP.
	try:
		
		IP = IP.replace("abs", "192.168.1.0/24")
		IP = IP.replace("ab", "192.168.1.0")
		IP = IP.replace("bs", "192.168")
		Comando = IP
		
		if IP == "":
			
			Texto2.delete(0,100)
			Texto2.insert(0,"Escribe Una IP.")
			
			Texto3.delete(0,100)
			Texto3.insert(0,"Escribe Una IP.")
			
			root.update_idletasks()
			return
		
		if IP.endswith("/24") and IP.startswith("-r") :
			
			Texto2.delete(0,100)
			Texto2.insert(0,"El Comando Es Invalido.")
			
			Texto3.delete(0,100)
			Texto3.insert(0,"Usa [ -r ] y [ /24 ] por separado .")
			
			root.update_idletasks()
			return
		#~ print(re.search(" */?2?4? *[0-9\.]+ */? *2?4?", IP))
		if IP.endswith("/24") or IP.startswith("-r") or "/24" in IP or "-r" in IP:
			
			if IP.startswith("-r") and len(IP.split(" ")) != 3:

					Texto2.delete(0,100)
					Texto2.insert(0,"El Comando Es Invalido.")
					
					Texto3.delete(0,100)
					Texto3.insert(0,"Usa [ -r 80/100 192.168.1.0 ] separando correctamente.")
					
					root.update_idletasks()
					return
					
			if IP.endswith("/24") and len(IP.split(" ")) != 1:

					Texto2.delete(0,100)
					Texto2.insert(0,"El Comando Es Invalido.")
					
					Texto3.delete(0,100)
					Texto3.insert(0,"Usa [ 192.168.1.0/24 ] todo junto.")
					
					root.update_idletasks()
					return
			
			Elaine = True
			Imp = IP.split(" ")[-1].replace("/24", "").strip()
			
		else: Imp = IP
		
		Patron = "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
			
		if re.search(Patron, Imp):
			
			Byte = Imp.split(".")
			
			for x in range(4):
				
				if (int(Byte[x]) < 0 or (int(Byte[x])) > 255): Eny = False
			
			if Eny == False:
				
				Texto2.delete(0,100)
				Texto2.insert(0,"IP No Valida... Fuera de Rango [ 0/255 ]")
				
				Texto3.delete(0,100)
				Texto3.insert(0,str(IP))
				
				root.update_idletasks()
				return
		else:
			
			Texto2.delete(0,100)
			Texto2.insert(0,"Comando No Valido...")
			
			Texto3.delete(0,100)
			Texto3.insert(0,str(IP))
			
			root.update_idletasks()
			return
		
	except IndexError:
		
		Texto2.delete(0,100)
		Texto2.insert(0,"ERROR!")
		
		Texto3.delete(0,100)
		Texto3.insert(0,"ERROR!")
		
		root.update_idletasks()
		return
	
	# Buscando Si Esta Activo el Host.
	Activo = False
	ping = "ping -n 1 "
	Red = ""
	
	if Elaine == True: #=======================================================================================
		
		Et4.config(text="Comando: ")
		Et5.config(text="Host: ")
		
		Aux = 0
			
		if IP.endswith("/24"):
			
			IP = IP.replace("/24","")
			Ip_Separada = IP.split(".")
			Red = Ip_Separada[0] + "." + Ip_Separada[1] + "." + Ip_Separada[2] + "."
			
			Inicio = 0
			Final = 255
			
		
		elif IP.startswith("-r"):
				
			if (" / " in IP or " /" in IP or "/ " in IP):
					
					Texto3.delete(0,100)
					Texto3.insert(0,"Comando No Valido...")
					
					Texto2.delete(0,100)
					Texto2.insert(0,str(IP))
					
					root.update_idletasks()
					return
			else:
				
				Ip_R = IP.split(" ")
				
				if Ip_R[0] == "-r":
					
					Ip_Ran = Ip_R[1]
					IP = Ip_R[2]
					
					Ip_Rango = Ip_Ran.split("/")
					
					Inicio = int(Ip_Rango[0])
					Final = int(Ip_Rango[1])
					
					Ip_Separada = IP.split(".")
					Red = Ip_Separada[0] + "." + Ip_Separada[1] + "." + Ip_Separada[2] + "."
					
					if Inicio > Final:
						
						Aux = Inicio
						Inicio = Final
						Final = Aux
					
					if (Inicio < 0 or Inicio > 255) or (Final < 0 or Final > 255):
						
						Texto3.delete(0,100)
						Texto3.insert(0,"Comando Incorrecto... Estas Fuera del Rango [ 0/255 ]")
						
						Texto2.delete(0,100)
						Texto2.insert(0,str(Comando))
						
						root.update_idletasks()
						return
					
					TamH = Final - Inicio
		else:
			
			Texto3.delete(0,100)
			Texto3.insert(0,"Comando No Valido...")
			
			Texto2.delete(0,100)
			Texto2.insert(0,str(IP))
			
			root.update_idletasks()
			return
		
		#Crea la Segunda Ventana.
		win=Toplevel()
		win.resizable(0,1)
		#~ win.geometry("280x600+850+50")
		winW = win.winfo_screenwidth() # - w
		winH = win.winfo_screenheight() # - h
		win.geometry("280x600%+d%+d" % (int((winW*1.5)/2),int(winH/13)))
		win.config(relief="sunken", bd=5, background="cadetblue")
		win.title("Host: " + str(Comando))
		win.iconbitmap("Imagenes\LawlietJH.ico")
			
		win.update_idletasks()
		
		#Crea el Boton CERRAR de Segunda Ventana.
		boton2=Button(win, bg="cadetblue", fg="darkBlue",\
			activebackground="lightblue", activeforeground="#1E6FBA",\
			width=10, height=1, text=" CERRAR ",\
			font="Calibri 10 bold", command=lambda: ejecutar(Ocultar(win)))
		boton2.pack(side=BOTTOM)
		
		
		# Cambia Información en Ventana Principal.
		Texto3.delete(0,100)
		Texto3.configure(background="dark turquoise", fg="darkBlue",)
		Texto3.insert(0,"Escaneando " + str(TamH) + " Host")
		
		Texto2.delete(0,100)
		Texto2.configure(background="dark turquoise", fg="darkBlue",)
		Texto2.insert(0,"Escaneando Host en el Rango: " + str(Comando))
		
		# Escribe Información en Ventana Secundaria.
		e3 = Label(win, text="Escaneando Subred...",\
					font="Timesnewroman 12 bold italic",\
					bg="cadetblue", fg="darkblue", bd=1,)
		e3.pack(padx=10,pady=10,ipadx=10,ipady=10,fill=X)
		
		root.update_idletasks()
		
		#~ FechaI = time.strftime("[!] Iniciado: %d/%m/%Y %H:%M:%S")
		
		# Mide El Tiempo Inicial.
		TiempoHI = int(datetime.datetime.now().strftime("%H"))
		TiempoMI = int(datetime.datetime.now().strftime("%M"))
		TiempoSI = int(datetime.datetime.now().strftime("%S"))
		
		#~ print(FechaI, " - Seg: ", TiempoSI, " - Min: ", TiempoMI, " - Hora: ", TiempoHI)
		
		# Crea Los Hilos Necesarios De Ejecuación.
		
		for x in range(Inicio, Final + 1):
			
			root.update_idletasks()
			threading.Thread(target=Hosts, args=(x, Fr, win, Activo, Red, ping)).start()
		
		root.update_idletasks()
		
		#~ time.sleep(5)
		
		#~ FechaF = time.strftime("[!] Finalizado: %d/%m/%Y %H:%M:%S")
		
		# Mide El Tiempo Final.
		TiempoHF = int(datetime.datetime.now().strftime("%H"))
		TiempoMF = int(datetime.datetime.now().strftime("%M"))
		TiempoSF = int(datetime.datetime.now().strftime("%S"))
		
		#~ print(FechaF, " - Seg: ", TiempoSF, " - Min: ", TiempoMF, " - Horas: ", TiempoHF)
		
		# Obtiene El Tiempo Trancurrido en Segundos.
		TiempoH = ((TiempoHF - TiempoHI) + 24) % 24
		TiempoM = TiempoMF - TiempoMI + (TiempoH * 60)
		TiempoS = (TiempoSF - TiempoSI) + (TiempoM * 60)
		
		# Imprime El Tiempo Transcurrido.
		e3 = Label(win, text="Duración: "+str(TiempoS+4)+" segundos",\
					font="Calibri 10 bold", \
					bg="cadetblue", fg="white", anchor=W, justify=LEFT, bd=0,\
					highlightbackground="#1E6FBA", highlightcolor="red",\
					highlightthickness=1)
		e3.pack(padx=5,pady=0,ipadx=5,ipady=0,fill=X)
		
		# Imprime El Número de Puertos Escaneados.
		e3 = Label(win, text="Host Escaneados: "+str(TamH)+" de 255",\
					font="Calibri 10 bold", \
					bg="cadetblue", fg="white", anchor=W, justify=LEFT, bd=0,\
					highlightbackground="#1E6FBA", highlightcolor="red",\
					highlightthickness=1)
		e3.pack(padx=5,pady=0,ipadx=5,ipady=5,fill=X)
		
		# Actualiza Toda La Interfaz Grafica.
		root.update_idletasks()
		
		
	else: #=======================================================================================
		
		Et4.config(text="Puertos: ")
		Et5.config(text="Comando: ")
		
		# Buscando Si Esta Activo el Host.

		Respuesta = os.popen(ping + IP)
		
		for Linea in Respuesta.readlines():
			
			if "ttl" in Linea.lower():
					
				Texto2.delete(0,100)
				Texto2.insert(0,"UP")
				
				Texto3.delete(0,100)
				Texto3.insert(0,IP)
				
				Activo = True
				root.update_idletasks()
				break
		
		if not Activo:
			
			Texto2.delete(0,100)
			Texto2.insert(0,"DOWN")
			
			Texto3.delete(0,100)
			Texto3.insert(0,IP)
		
			root.update_idletasks()
			
			return
		
		#Crea Seginda Ventana.
		win=Toplevel()
		win.resizable(0,1)
		win.geometry("280x600+50+50")
		win.config(relief="sunken", bd=5, background="cadetblue")
		win.title("Host: " + str(IP))
		win.iconbitmap("Imagenes\LawlietJH.ico")
			
		win.update_idletasks()
		
		#Crea el Boton CERRAR de Segunda Ventana.
		boton2=Button(win, bg="cadetblue", fg="darkBlue",\
			activebackground="lightblue", activeforeground="#1E6FBA",\
			width=10, height=1, text=" CERRAR ",\
			font="Calibri 10 bold", command=lambda: ejecutar(Ocultar(win)))
		boton2.pack(side=BOTTOM)
		
		# Cambia Información en Ventana Principal.
		Texto2.delete(0,100)
		Texto2.configure(background="dark turquoise", fg="darkBlue",)
		Texto2.insert(0,"Escaneando " + str(Tam) + " Puertos")
		
		Texto3.delete(0,100)
		Texto3.configure(background="dark turquoise", fg="darkBlue",)
		Texto3.insert(0,"Escaneando Puertos en el Host: " + str(IP))
		
		# Escribe Información en Ventana Secundaria.
		e3 = Label(win, text="Escaneando Puertos...",\
					font="Timesnewroman 12 bold italic",\
					bg="cadetblue", fg="darkblue", bd=1,)
		e3.pack(padx=10,pady=10,ipadx=10,ipady=10,fill=X)
		
		root.update_idletasks()
		
		#~ FechaI = time.strftime("[!] Iniciado: %d/%m/%Y %H:%M:%S")
		
		# Mide El Tiempo Inicial.
		TiempoHI = int(datetime.datetime.now().strftime("%H"))
		TiempoMI = int(datetime.datetime.now().strftime("%M"))
		TiempoSI = int(datetime.datetime.now().strftime("%S"))
		
		#~ print(FechaI, " - Seg: ", TiempoSI, " - Min: ", TiempoMI, " - Hora: ", TiempoHI)
		
		# Crea Los Hilos Necesarios De Ejecuación.
		for x in range(Tam):
			
			root.update_idletasks()
			threading.Thread(target=EscanerThread, args=(Puerto[x], IP, win,)).start()
		
		# Si No Hay Puertos Habiertos...
		if Cont == 0:
			
			Texto2.delete(0,100)
			Texto2.insert(0,"No Hay Puertos Abiertos...")
			
			Texto3.delete(0,100)
			Texto3.insert(0,str(IP))
			
			e3 = Label(win, text="No Hay Puertos Abiertos.",\
					font="Calibri 11 bold", \
					bg="cadetblue", fg="darkblue", bd=1,\
					highlightbackground="#1E6FBA", highlightcolor="red",\
					highlightthickness=1)
			e3.pack(padx=5,pady=5,ipadx=5,ipady=5,fill=X)
			
			e3 = Label(win, text="Escaneo Finalizado.",\
					font="Calibri 10 bold", \
					bg="cadetblue", fg="white", anchor=W, justify=LEFT, bd=0,\
					highlightbackground="#1E6FBA", highlightcolor="red",\
					highlightthickness=1)
			e3.pack(padx=5,pady=10,ipadx=5,ipady=5,fill=X)
			
			root.update_idletasks()
		
		# Si, Sí Hay Puertos Habiertos...
		else:
			Texto2.delete(0,100)
			Texto2.insert(0, str(Cont)+" Puertos Abiertos de "+str(Tam)+" Escaneados.")
		
			Texto3.delete(0,100)
			Texto3.insert(0, str(IP))
			
			e3 = Label(win, text="Puertos Abiertos: "+str(Cont),\
						font="Calibri 10 bold", \
						bg="cadetblue", fg="white", anchor=W, justify=LEFT, bd=0,\
						highlightbackground="#1E6FBA", highlightcolor="red",\
						highlightthickness=1)
			e3.pack(padx=5,pady=0,ipadx=5,ipady=5,fill=X)
			
			Cont = 0
			
			root.update_idletasks()
		
		#~ FechaF = time.strftime("[!] Finalizado: %d/%m/%Y %H:%M:%S")
		
		# Mide El Tiempo Final.
		TiempoHF = int(datetime.datetime.now().strftime("%H"))
		TiempoMF = int(datetime.datetime.now().strftime("%M"))
		TiempoSF = int(datetime.datetime.now().strftime("%S"))
		
		#~ print(FechaF, " - Seg: ", TiempoSF, " - Min: ", TiempoMF, " - Horas: ", TiempoHF)
		
		# Obtiene El Tiempo Trancurrido en Segundos.
		TiempoH = ((TiempoHF - TiempoHI) + 24) % 24
		TiempoM = TiempoMF - TiempoMI + (TiempoH * 60)
		TiempoS = (TiempoSF - TiempoSI) + (TiempoM * 60)
		
		# Imprime El Tiempo Transcurrido.
		e3 = Label(win, text="Duración: "+str(TiempoS)+" segundos",\
					font="Calibri 10 bold", \
					bg="cadetblue", fg="white", anchor=W, justify=LEFT, bd=0,\
					highlightbackground="#1E6FBA", highlightcolor="red",\
					highlightthickness=1)
		e3.pack(padx=5,pady=0,ipadx=5,ipady=0,fill=X)
		
		# Imprime El Número de Puertos Escaneados.
		e3 = Label(win, text="Puertos Escaneados: "+str(Tam)+" de 65535",\
					font="Calibri 10 bold", \
					bg="cadetblue", fg="white", anchor=W, justify=LEFT, bd=0,\
					highlightbackground="#1E6FBA", highlightcolor="red",\
					highlightthickness=1)
		e3.pack(padx=5,pady=0,ipadx=5,ipady=5,fill=X)
		
		# Actualiza Toda La Interfaz Grafica.
		root.update_idletasks()
		


#=======================================================================
#=======================================================================
#=======================================================================



if __name__ == "__main__":
	
	root = Tk()
	root.resizable(0,0)
	root.config( background="cadetblue" )
	
	# Centrar la Ventana
	#~ w = root.winfo_width()
	#~ h = root.winfo_height()
	extraW = root.winfo_screenwidth() # - w
	extraH = root.winfo_screenheight() # - h
	root.geometry("%+d%+d" % (int(extraW//3),int(extraH/3)))
	#~ print(w,h,extraW,extraH)
	#~ root.geometry("+360+180")
	
	root.title("EnyScan.py    By: LawlietJH    GUI_" + Version)
	root.iconbitmap("Imagenes\LawlietJH.ico")
	
	#===============================================================
	
	# Ventana Principal
	Fr = Frame()
	Fr.grid(column=0, row=0, padx=(5,5), pady=(7,7))
	Fr.columnconfigure(0, weight=1)
	Fr.rowconfigure(0, weight=1)
	Fr.config(relief="sunken", bd=3, background="cadetblue")
	
	#===============================================================
	
	# Etiqueta 1:
	Et1 = Label(Fr, fg="Purple", text="Ejemplo: ", font="Calibri 11 bold", background="cadetblue")
	Et1.grid(row=0, column=0, sticky=E, padx=(5,0), pady=(15,5))
	
	# Etiqueta 2:
	Et2 = Label(Fr, fg="darkblue", text="192.168.1.77    o    192.168.1.0/24    o    -r 60/80 ab")
	Et2.grid(row=0, column=1, sticky=(W,E), pady=(15,5))
	Et2.config(font="Calibri 11 bold italic", relief="sunken", background="cadetblue")#, justify="center")
	
	#===============================================================
	
	#~ # Etiqueta 6:
	#~ Et6 = Label(Fr, fg="Purple", text="Comando: ", font="Calibri 11 bold")
	#~ Et6.grid(row=1, column=0, sticky=E, padx=(0,0), pady=(0,0))
	
	#~ # Cuadro de Texto 4:
	#~ Texto4 = Entry(Fr, width=50, font="Calibri 11 italic bold",\
			 #~ justify="center", bg="White", fg="Green", bd=0,\
			 #~ highlightbackground="#1E6FBA", highlightcolor="red",\
			 #~ highlightthickness=1)
	#~ Texto4.grid(row=1, column=1, sticky=W)
	#~ Texto4.config(justify="center", state="normal")
	#~ Texto4.insert("0","/24")
	
	#~ #===============================================================
	
	# Etiqueta 3:
	Et3 = Label(Fr, fg="Purple", text="IP: ", font="Calibri 11 bold", background="cadetblue")
	Et3.grid(row=1, column=0, sticky=E)
	
	# Cuadro de Texto 1:
	Texto1 = Entry(Fr, width=50, font="Calibri 11 italic bold",\
			 justify="center", bg="White", fg="Green", bd=0,\
			 highlightbackground="#1E6FBA", highlightcolor="red",\
			 highlightthickness=1)
	Texto1.grid(row=1, column=1, sticky=W)
	Texto1.config(justify="center", state="normal")
	Texto1.insert(0,"192.168.1.0/24")
	Texto1.bind('<Return>', lambda e: ejecutar(Puertos(Fr)))
	
	# Boton 1:
	
	#~ entry.bind('<Return>', lambda: ejecutar(Puertos(Fr)))
		
	BgetIP = Button(Fr, bg="cadetblue", fg="darkBlue",\
		activebackground="lightblue", activeforeground="#1E6FBA",\
		width=10, height=1, cursor="exchange", text="ESCANEAR",\
		font="Calibri 10 bold", command=lambda: ejecutar(Puertos(Fr)))
	BgetIP.grid(row=1, column=2, sticky=W, padx=10)
	
	#===============================================================
	
	# Etiqueta 4:
	Et4 = Label(Fr, fg="Purple", text="Puertos: ", font="Calibri 11 bold", background="cadetblue")
	Et4.grid(row=2, column=0, sticky=E, pady=(25,0))
	
	# Cuadro de Texto 2:
	Cad ="Esperando Número de Puertos Activos..."
	
	Texto2 = Entry(Fr, width=50, font="Calibri 11 bold", justify="center",\
			 bg="dark turquoise", fg="Red", bd=0, exportselection=1,\
			 highlightbackground="#1E6FBA", highlightcolor="red",\
			 highlightthickness=1)
	Texto2.grid(row=2, column=1, sticky=W, pady=(25,0))
	Texto2.config(justify="center", state="normal")
	Texto2.insert(0, Cad)
	
	#===============================================================
		
	# Etiqueta 5:
	Et5 = Label(Fr, fg="Purple", text="Host: ", font="Calibri 11 bold", background="cadetblue")
	Et5.grid(row=3, column=0, sticky=E, pady=(5,15))
	
	# Cuadro de Texto 3:
	Cad ="Esperando Número de Hosts Activos..."
	
	Texto3 = Entry(Fr, width=50, font="Calibri 11 bold", justify="center",\
			 bg="dark turquoise", fg="Red", bd=0, exportselection=1,\
			 highlightbackground="#1E6FBA", highlightcolor="red",\
			 highlightthickness=1)
	Texto3.grid(row=3, column=1, sticky=W, pady=(5,15))
	Texto3.config(justify="center", state="normal")
	Texto3.insert(0, Cad)
	
	#===============================================================
	
	root.mainloop()



#=======================================================================


