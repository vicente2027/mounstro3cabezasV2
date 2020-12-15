class Node:
    def __init__(self, nombre=None, apellido_paterno=None, apellido_materno=None):
        # Atributos del nodo actual
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        #Apuntadores
        self.next_nombre = None
        self.next_apellido_paterno = None
        self.next_apellido_materno = None


class List:

    def __init__(self):
        self.head = Node() # Nodo cabeza
        self.recovery_node = Node()  # Ultimo nodo insertado

    def append_node(self, node): # Metodo para reinsertar nodo nombre
        new_node = node
        current_node = self.head
        while current_node.next_nombre is not None:
            current_node = current_node.next_nombre
        current_node.next_nombre = new_node

    def append_node_apellido_paterno(self, node): # Metodo para reinsertar nodo apellido paterno
        new_node = node
        current_node = self.head
        while current_node.next_apellido_paterno is not None:
            current_node = current_node.next_apellido_paterno
        current_node.next_apellido_paterno = new_node

    def append_node_apellido_materno(self, node): # Metodo para reinsertar nodo apellido materno
        new_node = node
        current_node = self.head
        while current_node.next_apellido_materno is not None:
            current_node = current_node.next_apellido_materno
        current_node.next_apellido_materno = new_node

    def is_empty(self): # Metodo si el siguiente nodo nombre esta vacio
        current_node = self.head
        if current_node.next_nombre is None:
            return True
        else:
            return False

    def is_empty2(self): # Metodo si el siguiente nodo apellido paterno esta vacio
        current_node = self.head
        if current_node.next_apellido_paterno is None:
            return True
        else:
            return False

    def is_empty3(self): # Metodo si el siguiente nodo apellido materno esta vacio
        current_node = self.head
        if current_node.next_apellido_materno is None:
            return True
        else:
            return False

    def display_by_nombre(self): # Metodo para desplegar nombres
        names = []
        current_node = self.head
        while current_node.next_nombre is not None:
            current_node = current_node.next_nombre
            names.append(current_node.nombre)
            names.append(current_node.apellido_paterno)
            names.append(current_node.apellido_materno)
            names.append("->")
        print(names)

    def display_by_apellido_paterno(self): # Metodo para desplegar apellidos paternos
        apellido = []
        current_node = self.head
        while current_node.next_apellido_paterno is not None:
            current_node = current_node.next_apellido_paterno
            apellido.append(current_node.apellido_paterno)
            apellido.append(current_node.apellido_materno)
            apellido.append(current_node.nombre)
            apellido.append("->")
        print(apellido)

    def display_by_apellido_materno(self): # Metodos para desplegar apellidos maternos
        apellido = []
        current_node = self.head
        while current_node.next_apellido_materno is not None:
            current_node = current_node.next_apellido_materno
            apellido.append(current_node.apellido_materno)
            apellido.append(current_node.apellido_paterno)
            apellido.append(current_node.nombre)
            apellido.append("->")
        print(apellido)

    def append_nombre(self, nombre, apellido_paterno, apellido_materno):  # Metodo para insertar nombre

        new_node = Node(nombre, apellido_paterno, apellido_materno)
        node_cabeza = self.head
        node_anterior = self.recovery_node

        if self.is_empty():  # Si la lista esta vacia
            # print("Vacia")
            node_cabeza.next_nombre = new_node  # Priximo nodo igual a nuevo nodo
            node_anterior.next_nombre = node_cabeza.next_nombre  # Nodo anterior igual primer nodo
            # self.display_by_nombre()
        else:
            # print("Nodo anterior "+str(node_anterior.next.pointer))
            # self.display_name()
            if new_node.nombre < node_anterior.next_nombre.nombre:
                # print("Node nuevo "+str(new_node.nombre) + " es menor a node anterior " + str(node_anterior.next_nombre.nombre))
                boolean = False
                # print("fuera del if")
                # print(node_cabeza.next.pointer)
                if new_node.nombre < node_cabeza.next_nombre.nombre:
                    # print("2,3,5")
                    node_anterior = node_cabeza.next_nombre
                    node_cabeza.next_nombre = new_node
                    self.append_node(node_anterior)
                else:
                    # print("3,4,5")
                    while node_cabeza.next_nombre.nombre < new_node.nombre:
                        node_cabeza = node_cabeza.next_nombre
                        # print("dentro while")
                    # print(node_cabeza.next.pointer)
                    while boolean is False and new_node.nombre < node_cabeza.next_nombre.nombre:  # (node_cabeza.next.data and node_nuevo.data) < node_anterior.next.data: # Mientras nuevo nodo sea menor a nodo anterior
                        # print("antes del if ")
                        if new_node.nombre < node_anterior.next_nombre.nombre:
                            # print("dentro del if")
                            node_cabeza.next_nombre = new_node
                            # print(node_anterior.next.pointer)
                            self.append_node(node_anterior.next_nombre)
                            # self.display_name()
                            return
                            boolean = True
                        else:
                            # print("dentro del else")
                            return
                            boolean = True
                # self.display_name()
                return
            else:
                # print("Node nuevo " + str(node_nuevo.pointer) + " es mayor a node anterior " + str(node_anterior.next.pointer))
                while node_cabeza.next_nombre != None:
                    node_cabeza = node_cabeza.next_nombre
                node_cabeza.next_nombre = new_node

            node_anterior.next_nombre = node_cabeza.next_nombre  # set el ultimo nodo
            # self.display_name()

    def append_apellido_paterno(self, nombre, apellido_paterno, apellido_materno):  # Metodo para insertar apellido paterno
        #print("inica ")
        new_node = Node(nombre, apellido_paterno, apellido_materno)
        node_cabeza = self.head
        node_anterior = self.recovery_node

        if self.is_empty2():  # Si la lista esta vacia
            #print("Vacia")
            node_cabeza.next_apellido_paterno = new_node  # Priximo nodo igual a nuevo nodo
            node_anterior.next_apellido_paterno = node_cabeza.next_apellido_paterno  # Nodo anterior igual primer nodo
            # self.display_by_nombre()
        else:
            # print("Nodo anterior "+str(node_anterior.next.pointer))
            # self.display_name()
            if new_node.apellido_paterno < node_anterior.next_apellido_paterno.apellido_paterno:
                # print("Node nuevo "+str(new_node.nombre) + " es menor a node anterior " + str(node_anterior.next_nombre.nombre))
                boolean = False
                # print("fuera del if")
                # print(node_cabeza.next.pointer)
                if new_node.apellido_paterno < node_cabeza.next_apellido_paterno.apellido_paterno:
                    # print("2,3,5")
                    node_anterior = node_cabeza.next_apellido_paterno
                    node_cabeza.next_apellido_paterno = new_node
                    self.append_node_apellido_paterno(node_anterior)
                else:
                    # print("3,4,5")
                    while node_cabeza.next_apellido_paterno.apellido_paterno < new_node.apellido_paterno:
                        node_cabeza = node_cabeza.next_apellido_paterno
                        # print("dentro while")
                    # print(node_cabeza.next.pointer)
                    while boolean is False and new_node.apellido_paterno < node_cabeza.next_apellido_paterno.apellido_paterno:  # (node_cabeza.next.data and node_nuevo.data) < node_anterior.next.data: # Mientras nuevo nodo sea menor a nodo anterior
                        # print("antes del if ")
                        if new_node.apellido_paterno < node_anterior.next_apellido_paterno.apellido_paterno:
                            # print("dentro del if")
                            node_cabeza.next_apellido_paterno = new_node
                            # print(node_anterior.next.pointer)
                            self.append_node_apellido_paterno(node_anterior.next_apellido_paterno)
                            # self.display_name()
                            return
                            boolean = True
                        else:
                            # print("dentro del else")
                            return
                            boolean = True
                # self.display_name()
                return
            else:
                # print("Node nuevo " + str(node_nuevo.pointer) + " es mayor a node anterior " + str(node_anterior.next.pointer))
                while node_cabeza.next_apellido_paterno != None:
                    node_cabeza = node_cabeza.next_apellido_paterno
                node_cabeza.next_apellido_paterno = new_node

            node_anterior.next_apellido_paterno = node_cabeza.next_apellido_paterno  # set el ultimo nodo
            # self.display_name()

    def append_apellido_materno(self, nombre, apellido_paterno, apellido_materno):  # Metodo para insertar apellido materno
        #print("inica ")
        new_node = Node(nombre, apellido_paterno, apellido_materno)
        node_cabeza = self.head
        node_anterior = self.recovery_node

        if self.is_empty3():  # Si la lista esta vacia
            #print("Vacia")
            node_cabeza.next_apellido_materno = new_node  # Priximo nodo igual a nuevo nodo
            node_anterior.next_apellido_materno = node_cabeza.next_apellido_materno  # Nodo anterior igual primer nodo
            # self.display_by_nombre()
        else:
            # print("Nodo anterior "+str(node_anterior.next.pointer))
            # self.display_name()
            if new_node.apellido_materno < node_anterior.next_apellido_materno.apellido_materno:
                # print("Node nuevo "+str(new_node.nombre) + " es menor a node anterior " + str(node_anterior.next_nombre.nombre))
                boolean = False
                # print("fuera del if")
                # print(node_cabeza.next.pointer)
                if new_node.apellido_materno < node_cabeza.next_apellido_materno.apellido_materno:
                    # print("2,3,5")
                    node_anterior = node_cabeza.next_apellido_materno
                    node_cabeza.next_apellido_materno = new_node
                    self.append_node_apellido_materno(node_anterior)
                else:
                    # print("3,4,5")
                    while node_cabeza.next_apellido_materno.apellido_materno < new_node.apellido_materno:
                        node_cabeza = node_cabeza.next_apellido_materno
                        # print("dentro while")
                    # print(node_cabeza.next.pointer)
                    while boolean is False and new_node.apellido_materno < node_cabeza.next_apellido_materno.apellido_materno:  # (node_cabeza.next.data and node_nuevo.data) < node_anterior.next.data: # Mientras nuevo nodo sea menor a nodo anterior
                        # print("antes del if ")
                        if new_node.apellido_materno < node_anterior.next_apellido_materno.apellido_materno:
                            # print("dentro del if")
                            node_cabeza.next_apellido_materno = new_node
                            # print(node_anterior.next.pointer)
                            self.append_node_apellido_materno(node_anterior.next_apellido_materno)
                            # self.display_name()
                            return
                            boolean = True
                        else:
                            # print("dentro del else")
                            return
                            boolean = True
                # self.display_name()
                return
            else:
                # print("Node nuevo " + str(node_nuevo.pointer) + " es mayor a node anterior " + str(node_anterior.next.pointer))
                while node_cabeza.next_apellido_materno != None:
                    node_cabeza = node_cabeza.next_apellido_materno
                node_cabeza.next_apellido_materno = new_node

            node_anterior.next_apellido_materno = node_cabeza.next_apellido_materno  # set el ultimo nodo
            # self.display_name()

list = List()

def main():

    print("Bienvenido\n1) Insertar Nombre\n2)Mostrar por nombre\n3)Mostrar por apellido paterno\n4)Mostrar por apellido materno\n5)Salir")

    option = input("Seleccione una opcion: ")

    if option == "1":
        nombre = input("Nombre(s): ")
        apelldio_paterno = input("Apellido Paterno: ")
        apellido_materno = input("Apellido Materno: ")
        list.append_nombre(nombre,apelldio_paterno,apellido_materno)
        list.append_apellido_paterno(nombre, apelldio_paterno, apellido_materno)
        list.append_apellido_materno(nombre, apelldio_paterno, apellido_materno)
        main()
    elif option == "2":
        list.display_by_nombre()
        main()
    elif option == "3":
        list.display_by_apellido_paterno()
        main()
    elif option == "4":
        list.display_by_apellido_materno()
        main()
    elif option == "5":
        exit()

main()
