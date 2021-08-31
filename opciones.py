from lista import Lista 

Enviar = Lista() #global para poder usarlo en todos los métodos 
class Opciones:
    
    def Opcion1():
        print("🍕 Pizzas a domicilio 🍕")
        ingrediente = input(">Ingrese el ingrediente que le desea agregar a su pizza: ")
        Enviar.insertar(ingrediente)
        #Enviar.mostrar()
    
    def Opcion2():
        Enviar.eliminar()
    
    def Opcion3():
        print("Ordenes registradas")
        Enviar.mostrar()