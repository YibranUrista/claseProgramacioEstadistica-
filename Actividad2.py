lista = []

while True:
  print("1. Ingresar dato a la lista")
  print("2. Borrar dato de la lista")
  print("3. Mostrar lista")
  print("4. Salir")
  opcion = int(input("Ingrese una opcion: "))

  if opcion == 1:
    dato = input("Ingrese un dato: ")
    lista.append(dato)
    print("Se a agregado el dato a la lista")

  elif opcion == 2:
    dato = input("Ingrese el dato a borrar:")
    lista.remove(dato)
    print("Se a borrado el dato de la lista")

  elif opcion == 3:
    print(lista)
  
  elif opcion == 4:
    print("Saliendo del programa")
    break 
  else:
    print("Opcion invalida")