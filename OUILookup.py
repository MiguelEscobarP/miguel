#Script que muestra la ip,mac y vendedor de una tarjeta de red
#USO:
#EL ARCHIVO 'datos.txt' DEBE ESTAR EN LA MISMA CARPETA QUE EL CODIGO, FUNCIONA DE MANERA LOCAL
#python3 OUILookup.py --ip<ip> --mac<mac> [--help]
#parametros:
#ip: si es ingresada busca por el numero ingresado.
#mac: si es ingresado busca por la direccion ingresada.
#help: muestra pantalla de uso y termina.


import sys
import socket #para ver cual es la ip desde donde se esta ejecutando 
import getopt

#verificacion de la misma red (si se encuentra en la misma retorna 1 y si no 0):
def mismared(ipx):
	redlocal = socket.gethostbyname(socket.gethostname()) #muestra la ip del equipo usando el nombre
	#SI SON DE LA MISMA RED LAS PRIMERAS TRES SECCIONES DEBEN SER IGUALES, LA CUARTA PUEDE VARIAR
	iplocal = redlocal.split('.') #separamos el ip local en 4 secciones
	ipbusca = ipx.split('.') #separamos el ip a buscar en 4 secciones
	for i in range (3) :
		if (iplocal[i] != ipbusca[i]):#comparamos las tres primeras secciones
			return 0
	return 1
#buscar mac en la lista (si existe devuelve su indice, si no existe retorna -1)
def buscarmac(lista,mac):
	for i in lista:
		if mac in i:
			return lista.index(i)
	return -1
#toma los datos del archivo, los guarda y retorna en una lista.	
def generarbase():
	lista = []
	archivo = open("datos.txt","r")
	while True:
		linea = archivo.readline()
		dato = linea.split('	')
		lista.append(dato)
		if not linea: break
	archivo.close()
	return lista
	    
#CUERPO PRINCIPAL:
def main():
    datos = generarbase() #creacion de base de datos
    #variables
    mac = None
    ip = None
    Vendedor = None
    
    argv = sys.argv[1:]#toma argumentos desde el primero en adelante
    
    try:
    	options, args = getopt.getopt(argv,"i,m",['ip=','mac=','help'])
    except:
    	print("Error: parametros mal ingresados.")
    	usar()
    	
    for opt, arg in options:
    	if opt in ('--help'):
    		usar()
    	if opt in ('--ip'):
    		ip = str(arg)
    	elif opt in ('--mac'):
    		mac = str(arg)
    		
    #para ver cual dato fue ingresado. 
    if (ip != None):
    	if (mismared(ip)):
    		print("F")
    	else:
    		print("Error: ip fuera de la red.")
    elif (mac != None):
     	indice = buscarmac(datos,mac)
     	if(indice !=-1):
     		print("MAC address : " + (datos[indice])[0])
     		print("Vendedor    : " + (datos[indice])[1])
     	else:
     		print("MAC address : " + mac)
     		print("Vendedor    : No Encontrado")
    else:
    	usar()

# Funcion para dar instrucciones:
def usar():
    print("Uso: Python3 " + sys.argv[0] + " --ip <IP> | --mac <IP> [--help] ")
    print("\nParametros:")
    print("     --ip: especificar la IP del host.")
    print("     --maxtime: especificar la direccion MAC")
    print("     --help: muestra esta pantalla y termina.")
    exit(1)    	
    	
##para ultizar script  en otros lados  
if __name__ == '__main__':
	main()

