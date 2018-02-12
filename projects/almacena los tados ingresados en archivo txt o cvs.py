while 1 == 1:    
       import time
        hora = time.strftime("%H:%M:%S")
        fecha = time.strftime("%d/%m/%y")
        print("Introduce el numero de empleado1\n")
        Num = str(input())
        prueba = open("/home/pi/pitando/Lista_usuarios.csv","a")
        prueba.write(Num + "," + hora + "," + fecha + "\n")
        prueba.close()