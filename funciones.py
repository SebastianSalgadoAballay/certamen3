from os import system
system("cls")
from random import randint
id=randint(99999,999999)
nombre=""
comunas=[concepcion,chiguayante,talcahuano,hualpen,san pedro]
while not nombre:
    try:
         nombre = input("ingrese su nombre: ")
         nombre = nombre.replace(" ","") 
         if nombre.isalpha()==False:
              nombre=""
         raise ValueError()
    except ValueError:
         print("nombre correcto")
         pass 

apellido=""
while not apellido:
    try:
         apellido = input("ingrese su apellido: ")
         apellido = apellido.replace(" ","") 
         if apellido.isalpha()==False:
              apellido=""
         raise ValueError()
    except ValueError:
         print("apellido correcto") 
         pass
       
direccion=""
while not direccion:
    try:
         direccion = input("ingrese su apellido: ")
         direccion = direccion.replace(" ","") 
         if direccion=="":
              direccion=""
         raise ValueError()
    except ValueError:
         print("apellido correcto") 
         pass


comuna = input("ingrese su comuna: ")


print("de cuantos litros desea su dispensador 6 , 10 o 20")
while True:
        print("""
        1. 6 litros
        2. 10 litros
        3. 20 litro
        4. salir
        """)
        dispensador6=0
        dispensador10=0
        dispensador20=0
        totaldispensadores=0
        li= input("elija que dispensador quiere: ")
        match li:
            case "1":
                dispensador6=dispensador6+1
                totaldispensadores=totaldispensadores+1
            case "2":
                dispensador10=dispensador10+1
                totaldispensadores=totaldispensadores+1
            case "3":
                dispensador20=dispensador20+1
                totaldispensadores=totaldispensadores+1
            case "4":
                break
            case "0":
                  print("opcion invalida")
print(f"ID: {id} Nombre: {nombre} apellido: {apellido} direccion: {direccion} comuna: {comuna}        disp. de 6 litros: {dispensador6} disp. de 10 litros: {dispensador10} disp. de 20 litros: {dispensador20}  ")                  

                

