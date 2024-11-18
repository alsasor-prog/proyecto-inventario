class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Precio: ${self.precio}"

class Inventario:
    def __init__(self):
        # Inicializamos una lista vacía para almacenar productos
        self.productos = []
    
    def agregar_producto(self, producto):
        # Método para agregar un producto a la lista
        self.productos.append(producto)
    
    def eliminar_producto(self, id_producto):
        # Método para eliminar un producto por su ID
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                print(f"Producto con ID {id_producto} eliminado.")
                return
        print(f"No se encontró el producto con ID {id_producto}.")
    
    def mostrar_inventario(self):
        # Método para mostrar todos los productos
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)

    def buscar_producto(self, id_producto):
        # Método para buscar un producto por su ID usando un ciclo for
        for producto in self.productos:
            if producto.id_producto == id_producto:
                print(producto)
                return
        print(f"No se encontró el producto con ID {id_producto}.")

# Uso de la clase
inventario = Inventario()

# Crear productos
producto1 = Producto(101, "cocacola 2lts", 1200)
producto2 = Producto(102, "yogurt", 800)
producto3 = Producto(103, "sopa", 100)

# Agregar productos al inventario
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)
inventario.agregar_producto(producto3)

# Mostrar inventario
print("Inventario:")
inventario.mostrar_inventario()

# Buscar un producto por ID
print("\nBuscar producto con ID 102:")
inventario.buscar_producto(102)

# Eliminar un producto por ID
print("\nEliminar producto con ID 102:")
inventario.eliminar_producto(102)

# Mostrar inventario después de eliminar
print("\nInventario después de eliminar:")
inventario.mostrar_inventario()

# Intentar eliminar un producto que no existe
print("\nIntentar eliminar producto con ID 999:")
inventario.eliminar_producto(999)
