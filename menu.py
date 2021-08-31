from opciones import Opciones
class Menu:
    def menu():#Funcion menu
        print("-----------MENU-------------")
        print("Practica1 IPC2")
        print("1.Insertar orden")
        print("2.Entregar orden")
        print("3.Mostrar ordenes")
        print("4.Mostrar datos del estudiante")
        print("5.Salir")
        print("----------------------------")

    while True:
        menu()
        print("")
        opcionMenu = input("Escoja una opción:")
        if opcionMenu=="1":
            Opciones.Opcion1()
            print("")
        elif opcionMenu=="2":
            Opciones.Opcion2()
            print("")
        elif opcionMenu=="3":
            Opciones.Opcion3()
            print("")
        elif opcionMenu=="4":
            print("->Sharon Estenfany Tagual Godoy")
            print("->201906173")
            print("->Introducción a la programación y computación 2 sección D")
            print("->Ingeniería en Ciencias y Sistemas")
            print("->4to Semestre")
            print ("")
        elif opcionMenu=="5":
            print("Gracias!")
            break
        else:
            print ("")
    