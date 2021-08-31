from nodo import Nodo

class Lista():

    def __init__(self):#métoedo constructor 
        #dos referencias
        self.primero = None #un nodo primero que inserte el usuario
        self.ultimo = None #un nodo que apunta al ultimo nodo

    #Creando el primer nodo self, id, nombre, m, n, primero, fin
    def insertar(self, ingrediente):
        pizza="Pizza de "+ingrediente
        nuevo = Nodo(pizza) 
        if self.primero is None: #si el primero está vacío
            self.primero = nuevo #entonces el primero será igual al objeto que mandó el usuario 
        else: #si el primero no está vacío 
            tem = self.primero #temporal, para una referencia 
            while tem.siguiente is not None:#se ejecutará mientras el siguiente sea no sea nulo, cuando encuentre 
                tem = tem.siguiente         #el siguiente que sea nulo 
            tem.siguiente=nuevo#ahora el siguiente del último nodo ya no será nulo, sino será el nuevo nodo
    
    def eliminar(self):
        try:
            retorno = self.primero.ingrediente
            if self.primero is not None:
                if self.primero.siguiente is not None:
                    self.primero = self.primero.siguiente
                else:
                    self.primero = None
            print("Se ha entregado la pizza", retorno)
        except:
            print("Cola vacía, totalidad de ordenes entregadas")
    
    def mostrar(self):
        tem = self.primero#empezando por el principio 
        i=1
        while tem is not None:
            print(" |"+str(i)+")",tem.ingrediente+"| ", end=" ")
            i+=1
            #Listasube.mostrar()
            tem = tem.siguiente



