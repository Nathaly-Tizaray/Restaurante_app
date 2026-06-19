class Restaurante:
    def __init__(self):
        self.producto = []
        self.cliente = []

    def agregar_producto(self, producto):
        self.producto.append(producto)

    def agregar_cliente(self, cliente):
        self.cliente.append(cliente)

    def mostrar_producto(self):
        print("\n--- PRODUCTO ---")
        for producto in self.producto:
            print(producto)

    def mostrar_cliente(self):
        print("\n--- CLIENTE ---")
        for cliente in self.cliente:
            print(cliente)