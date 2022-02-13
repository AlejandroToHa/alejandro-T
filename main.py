#vamos a importar las listas de archivos
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#inicio de sesion
"""
Login
credenciales:

usuario:
    alejandroTh
contrase;a:
    1952131
"""

usuarioAccedio = False
intentos = 0

# Bienvenida!
mensaje_bienvenida = 'Bienvenido al sistema!\nAccede con tus credenciales'
print(mensaje_bienvenida)

# Recibo constantemente sus intentos
while not usuarioAccedio:
    # Primero ingresa Credenciales
    usuario = input('Usuario: ')
    contras = input('Contraseña: ')
    intentos += 1
    # Reviso si el par coincide
    if usuario == 'alejandroTh' and contras == '1952131':
        usuarioAccedio = True
        print('Hola de nuevo!')
    else:
        print('Tienes', 3 - intentos, 'intentos restantes')
        print(f'Tienes {3 - intentos} intentos restantes')
        if usuario == 'alejandroTh':
            print('Te equivocaste en la contrase;a')
        else:
            print(f'El usuario: "{usuario}" no esta registrado')
            
    if intentos == 3:
        exit()

print('bienvenido')






#ventas 
masvendidos= [] 
resagados=[]


masvendidos = [venta[1] for venta in lifestore_sales] 

for venta in lifestore_products :
   #empezamos a  crear la lista

    lista1=[]
    resagados.append(lista1)
    for j in range(1):
      #aqui guardamos el id el nombre y la categoria del producto
      lista1.append(venta[0])
      lista1.append(venta[1])
      lista1.append(masvendidos.count(venta[0])) 
      #aqui contamos los productos resagados
      lista1.append(venta[-2])
      


  #sort es la forma mas facil de ordenar una lista 
  
def sort(resagados):
    resagados.sort(key = lambda x : x[2])
    return resagados

resagados= sort(resagados)
#generamos un listado de los productos con mayores ventas
print("\n los mas vendidos")
for i in [-1,-2,-3,-4,-5]:
 print( F'ID: {resagados[i][0]}\t nombre: {resagados[i][1]}\t ventas: {resagados[i][2]}' )
#generamos un listado de los productos con menores ventas
print("\n los menos vendidos")

for i in range(0,5):
  print( f'ID: {resagados[i][0]}\t nombre: {resagados[i][1]}\t ventas: {resagados[i][2]}' ) 

 


   

  
#ventas por categoria
# analisis por categoria "menores ventas y categorias con menores busquedas"
categorias=[]                  #creamos las categorias en forma de lista para llenarlas con la lista lifestore_products
procesadores=[]
speakers=[]
gpus=[]
headphones=[]
discosduros=[]
unidades=[]
usb=[]
pantallas=[]

categorias= [i[-2] for i in lifestore_products]
categorias =list(dict.fromkeys(categorias))   #aqui ya lo estamos llenando a sus respectivas categorias

for i in resagados:
      if categorias [0] in i :
        procesadores.append(i[:3])
      elif categorias[1] in i:
        gpus.append(i[:3])
      elif categorias[2] in i:
        discosduros.append(i[:3])
      elif categorias [3] in i :
          unidades.append(i[:3])
      elif categorias[4] in i:
        usb.append(i[:3])
      elif categorias[5] in i:
        pantallas.append(i[:3])
      elif categorias [6] in i :
        speakers.append(i[:3])
      elif categorias[7] in i:
        headphones.append(i[:3])

print("\n procesadores menos buscados")       #imprimimos los mas buscados de cada categoria
for i in range (5): 
  print("ID :", procesadores [i] [0] )
  print("nombre :", procesadores [i] [1] )
  print(" numero de veces buscado:", procesadores [i] [2] )


print("\n  speakers menos buscados")
for i in range (5):
  print("ID :", speakers [i] [0] )
  print("nombre :", speakers [i] [1] )
  print(" numero de veces buscado:", speakers [i] [2] )

print("\n  gpus menos buscados")
for i in range (5):
  print("ID :", gpus [i] [0] )
  print("nombre :", gpus [i] [1] )
  print(" numero de veces buscado:", gpus [i] [2] )


print("\n  headphones  menos buscados")
for i in range (5):
  print("ID :", headphones [i] [0] )
  print("nombre :", headphones [i] [1] )
  print(" numero de veces buscado:", headphones [i] [2] )


print("\n  discosduros menos buscados")
for i in range (5):
  print("ID :", discosduros [i] [0] )
  print("nombre :", discosduros [i] [1] )
  print(" numero de veces buscado:", discosduros [i] [2] )

print("\n lunidades  menos buscadas")
for i in range (5):
  print("ID :", unidades [i] [0] )
  print("nombre :", unidades [i] [1] )
  print(" numero de veces buscado:", unidades [i] [2] )
  
print("\n usb menos buscadas")
for i in range (2):
  print("ID :", usb [i] [0] )
  print("nombre :", usb [i] [1] )
  print(" numero de veces buscado:", usb [i] [2] )

print("\n pantallas menos buscadas")
for i in range (5):
  print("ID :", pantallas [i] [0] )
  print("nombre :", pantallas  [i] [1] )
  print(" numero de veces buscado:", pantallas [i] [2] )

#busquedas

producto_buscado = []
tiempo_de_busqueda= []

producto_buscado = [search[1] for search in lifestore_searches]

for search in lifestore_products: 
    lista=[]
    tiempo_de_busqueda.append(lista)
    for k in range(1):
        lista.append(search[0]) 
        lista.append(search[1]) 
        lista.append(producto_buscado.count(search[0])) 
        lista.append(search[-2]) 
        
def Sort(tiempo_de_busqueda):
    tiempo_de_busqueda.sort(key = lambda x: x[2])
    return tiempo_de_busqueda

tiempo_de_busqueda = Sort(tiempo_de_busqueda)

print("\n los 5 productos mas buscados son")
for i in [-1,-2,-3,-4,-5]:
    print( F'ID: {tiempo_de_busqueda[i][0]}\t nombre: {tiempo_de_busqueda[i][1]}\t buscado: {tiempo_de_busqueda[i][2]}' )

print("\n los 10 productos menos buscados son")
for i in range(0,10):
    print( F'ID: {tiempo_de_busqueda[i][0]}\t nombre: {tiempo_de_busqueda[i][1]}\t busquedas: {tiempo_de_busqueda[i][-1]}' )

#comentarios de los productos
sumax=0
total = []
promedio = []

for i in range(0,len(lifestore_products)): 
    for k in range(0,len(lifestore_sales)):
        if lifestore_sales[k][1]==resagados[i][0]:
            sumax += lifestore_sales[k][2] #suma de las puntuaciones de comentarios
    
    total.append(sumax)
    sumax=0

for product in lifestore_products: 
    for review in lifestore_sales:
        if product[0]==review[1]:
            sumax += review[2] 
    
    total.append(sumax)
    sumax=0

 #resagados [id_product, nombre, veces vendido, categoria]

for review in lifestore_products: #Creamos una nueva lista
    lista2=[]
    if resagados[review[0]-1][2] > 0: #aqui hacemos una comparacion para confirmar que los productos se vendieron por lo menos una vez
        promedio.append(lista2)
        for k in range(1):
            lista2.append(review[0])
            lista2.append(review[1])
            lista2.append(resagados[review[0]-1][2]) # aqui vemos cuantos comentarios hay
            lista2.append(total[review[0]-1]/resagados[review[0]-1][2]) #obtenemos el promedio

for review in resagados: #Creamos una nueva lista
    lista3=[]
    if review[2] > 0: #obtenemos una lista de los productos vendidos por lo menos una vez
        promedio.append(lista3)
        for k in range(1):
            lista3.append(review[0])
            lista3.append(review[1])
            lista3.append(review[2]) 
            lista3.append(total[review[0]-1]/review[2]) #promedio

def Sort(promedio):
    promedio.sort(key = lambda x: x[-1])
    return promedio

promedio = Sort(promedio)

print("\n productos mejor valorados")
print(); print();
for i in range(-1,-11,-1):
    print( F'ID: {promedio[i][0]}\t nombre: {promedio[i][1]}\t puntuacion: {promedio[i][-1]}\t reseñas: {promedio[i][2]}' )

print("\n productos mal valorados")
for i in range(0,10):
    print( F'ID: {promedio[i][0]}\t nombre: {promedio[i][1]}\t puntuacion: {promedio[i][-1]}\t  reseñas: {promedio[i][2]}' )

# ventas por mes


from datetime import datetime; import calendar

date = [sale[3] for sale in lifestore_sales]
date.sort(key = lambda date: datetime.strptime(date, '%d/%m/%Y')) # formato de la fecha

mes =calendar.month_name[1:]

devolucion = []
totalrefunds = 0
promedio = []
totalsales = 0
ventaspormes = [0]*12
ganaciaxmes = [0]*12

soldproduct = [sale[1] for sale in lifestore_sales]

for i in range(0,len(lifestore_sales)):
    if int(lifestore_sales[i][-1]) == 0:                    #verificar que no fue una devolucion 
        totalsales+=lifestore_products[soldproduct[i]][2]   #añadir al total de ventas
        if "/01/" in date[i]:
            ganaciaxmes[0]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[0]+=1
        elif "/02/" in date[i]:
            ganaciaxmes[1]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[1]+=1
        elif "/03/" in date[i]:
            ganaciaxmes[2]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[2]+=1
        elif "/04/" in date[i]:
            ganaciaxmes[3]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[3]+=1
        elif "/05/" in date[i]:
            ganaciaxmes[4]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[4]+=1
        elif "/06/" in date[i]:
            ganaciaxmes[5]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[5]+=1
        elif "/07/" in date[i]:
            ganaciaxmes[6]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[6]+=1
        elif "/08/" in date[i]:
            ganaciaxmes[7]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[7]+=1
        elif "/09/" in date[i]:
            ganaciaxmes[8]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[8]+=1
        elif "/10/" in date[i]:
            ventaspormes[9]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[9]+=1
        elif "/11/" in date[i]:
            ganaciaxmes[10]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[10]+=1
        elif "/12/" in date[i]:
            ganaciaxmes[11]+=lifestore_products[soldproduct[i]][2]
            ventaspormes[11]+=1
    else:
        devolucion.append(soldproduct[i])                 #ID del producto devuelto
        totalrefunds+=lifestore_products[soldproduct[i]][2] #perdidas por devoluciones

for i in range(12): 
    if ventaspormes[i] > 0:
        promedio.append(ganaciaxmes[i]/ventaspormes[i]) #obteniendo el promedio
    else:
        promedio.append(0)

ventasxmes = [list(l) for l in zip(mes, ganaciaxmes, ventaspormes, promedio)]

def Sort(ventasxmes): #ordenamos por ganancia
    ventasxmes.sort(key = lambda x: x[1])
    return ventasxmes
ventasxmes = Sort(ventasxmes)

print("\n meses con mas ingresos")
for i in [-1,-2,-3,-4,-5]:
    print( F'mes: {ventasxmes[i][0]}\t ganancia: {"${:,.2f}".format(ventasxmes[i][1])}\t ventas: {ventasxmes[i][2]}\t promedio: {ventasxmes[i][-1]}' )

def Sort(ventasxmes): #ordenamos por ventas
    ventasxmes.sort(key = lambda x: x[2])
    return ventasxmes
ventasxmes = Sort(ventasxmes)

print("\n mejores ventas por mes")
for i in [-1,-2,-3,-4,-5]:
    print( F'mes: {ventasxmes[i][0]}\t ganancia: {"${:,.2f}".format(ventasxmes[i][1])}\t SALES: {ventasxmes[i][2]}\t promedio: {ventasxmes[i][-1]}' )

def Sort(ventasxmes): #ticket promeedio
    ventasxmes.sort(key = lambda x: x[-1])
    return ventasxmes
ventasxmes = Sort(ventasxmes)

print("\n tickets con las ventas mas altas")
for i in [-1,-2,-3,-4,-5]:
    print( F'mes: {ventasxmes[i][0]}\t ganancia: {"${:,.2f}".format(ventasxmes[i][1])}\t SALES: {ventasxmes[i][2]}\t promedio: {ventasxmes[i][-1]}' )