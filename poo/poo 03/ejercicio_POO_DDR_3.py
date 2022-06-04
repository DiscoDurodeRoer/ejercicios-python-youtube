class Producto:

    __codigo = 0
    __nombre = ""
    __precio = 0

    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, valor):
        self.__codigo = valor

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, valor):
        self.__nombre = valor

    def get_precio(self):
        return self.__precio

    def set_precio(self, valor):
        self.__precio = valor

    def calcular_total(self, unidades):
        return self.__precio * unidades

    def __str__(self):
        return 'Codigo: ' + str(self.__codigo) + ', nombre: ' + self.__nombre + ', precio: ' + str(self.__precio)

class Pedido:

    def __init__(self):
        self.__productos = []
        self.__cantidades = []

    def aniadir_producto(self, producto, cantidad):

        if not isinstance(producto, Producto):
            raise Exception('aniadir_producto: producto debe ser de la clase producto')

        if not isinstance(cantidad, int):
            raise Exception('aniadir_producto: cantidad debe ser un numero')

        if cantidad <= 0:
            raise Exception('aniadir_producto: cantidad debe ser positivo y mayor que 0')

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            self.__cantidades[indice] += cantidad
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)

    def eliminar_producto(self, producto):

        if not isinstance(producto, Producto):
            raise Exception('eliminar_producto: producto debe ser de la clase producto')

        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]
        else:
            raise Exception('eliminar_producto: el producto no existe')


    def total_pedido(self):
        total = 0

        for (p,c) in zip(self.__productos, self.__cantidades):
            total = total + p.calcular_total(c)

        return total

    def mostrar_productos(self):

        for (p,c) in zip(self.__productos, self.__cantidades):
            print('Producto: ' + p.get_nombre() + ', Cantidad: ' + str(c))



p1 = Producto(1, "producto 1", 5)
p2 = Producto(2, "producto 2", 15)
p3 = Producto(3, "producto 3", 25)

pedido = Pedido()

try:

    pedido.aniadir_producto(p1, 3)
    pedido.aniadir_producto(p2, 5)
    pedido.aniadir_producto(p1, 5)

    print('Total pedido: '+ str(pedido.total_pedido()))

    pedido.mostrar_productos()

    pedido.eliminar_producto(p3)


    print('Total pedido: '+ str(pedido.total_pedido()))

    pedido.mostrar_productos()

except Exception as e:
    print(e)




