def menu():
    print("--------------MENU--------------")
    print("n°1:agregar notas")
    print("n°2:visualizar nota")
    print("n°3:buscar nota")
def agregarnota():
    print("ingrese:")
    print("nombre de la nota")
    print("fecha")
    print("descripcion")
    
while(True):
    lista = []
    lista2 = []
    menu()
    print("ingrese una opcion")
    opcion = int(input())
    if (opcion == 1):
        agregarnota()
        for i in range(0,3):
            a = input()
            lista2.append(a)
        lista.extend(lista2)
    elif (opcion == 2):
        print(lista)
        print(lista2)
    elif (opcion == 3):
        print("seleccione numero de nota")
        n.nota = int(input())
        for i in lista:
            if (i == n.nota):
                print("selecione entre:nombre de la nota(1),fecha(2),descripcion(3)")
                opcion2 = int(input())
                i[opcion2]
