class Inventario:
    def __init__(self, productoID, nombreProducto, cantidadDisponible, categoria, proveedor):
        self._productoID = productoID
        self._nombreProducto = nombreProducto
        self._cantidadDisponible = cantidadDisponible
        self._categoria = categoria
        self._proveedor = proveedor
        self.listaProductos = [
            {"productoID": 1, "nombreProducto": "Toalla", "cantidadDisponible": 100, "categoria": "Baño", "proveedor": "TextilesHotel"},
            {"productoID": 2, "nombreProducto": "Almohada", "cantidadDisponible": 50, "categoria": "Habitación", "proveedor": "SueñosFelices"},
            {"productoID": 3, "nombreProducto": "Jabón", "cantidadDisponible": 200, "categoria": "Amenidades", "proveedor": "LimpiezaTotal"},
            {"productoID": 4, "nombreProducto": "Secador de pelo", "cantidadDisponible": 30, "categoria": "Electrónica", "proveedor": "ElectroHotel"},
            {"productoID": 5, "nombreProducto": "Minibar", "cantidadDisponible": 20, "categoria": "Alimentación", "proveedor": "BebidasFrescas"}
        ]

    def agregarProducto(self, productoID, nombreProducto, cantidadDisponible, categoria, proveedor):

        print(f"El producto agregado es {productoID}:{nombreProducto}, la cantidad es {cantidadDisponible}")
        self.listaProductos.append({
            "productoID": productoID,
            "nombreProducto": nombreProducto,
            "cantidadDisponible": cantidadDisponible,
            "categoria": categoria,
            "proveedor": proveedor
        })

    # Otros métodos quedan igual


    def actualizarStock(self, numero):
        print(f"El producto {self.productoID}:{self.nombreProducto} ha sido actualizado con la cantidad de {numero}")
        for producto in self.listaProductos:
            if producto["productoID"] == self.productoID:
                producto["cantidadDisponible"] = numero
                break

    def eliminarProducto(self, nombre, cantidad):
        """
        Elimina o reduce la cantidad de un producto del inventario
        Args:
            nombre: nombre del producto a eliminar/reducir
            cantidad: cantidad a reducir (int)
        """
        try:
            # Aseguramos que cantidad sea un entero
            cantidad = int(cantidad)
            
            for producto in self.listaProductos:
                if producto["nombreProducto"].lower() == nombre.lower():
                    if producto["cantidadDisponible"] >= cantidad:
                        producto["cantidadDisponible"] -= cantidad
                        print(f"Se han removido {cantidad} unidades de {nombre}")
                        
                        # Si la cantidad llega a 0, eliminamos el producto
                        if producto["cantidadDisponible"] == 0:
                            self.listaProductos.remove(producto)
                            print(f"El producto {nombre} ha sido eliminado del inventario")
                        return True
                    else:
                        print(f"Error: Solo hay {producto['cantidadDisponible']} unidades de {nombre} disponibles")
                        return False
            
            print(f"Error: El producto {nombre} no se encuentra en el inventario")
            return False
        except ValueError:
            print("Error: La cantidad debe ser un número entero válido")
            return False
    def mostrar_inventario(self):
        if not self.listaProductos:
            print("El inventario está vacío.")
        else:
            print("\nInventario actual:")
            for producto in self.listaProductos:
                print(f"ID: {producto['productoID']}, Producto: {producto['nombreProducto']}, Cantidad: {producto['cantidadDisponible']}, Categoría: {producto['categoria']}, Proveedor: {producto['proveedor']}")
