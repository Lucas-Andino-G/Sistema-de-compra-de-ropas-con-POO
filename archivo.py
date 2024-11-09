class Producto:
    def __init__(self, nombre, precio, cantidad):
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    def mostrar_info(self):
        return f"{self._nombre} - Precio: ${self._precio:.2f} - Cantidad disponible: {self._cantidad}"

    def obtener_precio(self):
        return self._precio

    def reducir_cantidad(self, cantidad):
        if self._cantidad >= cantidad:
            self._cantidad -= cantidad
            return True
        return False


class Ropa(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Talla: {self._talla}"


class Camisa(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Pantalon(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Chaqueta(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class RopaMujer(Ropa):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Falda(RopaMujer):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Blusa(RopaMujer):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Vestido(RopaMujer):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad, talla)


class Zapato(Producto):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Talla: {self._talla}"


class Tienda:
    def __init__(self):
        self._inventario = []

    def agregar_prenda(self, prenda):
        self._inventario.append(prenda)

    def mostrar_inventario(self):
        for i, prenda in enumerate(self._inventario):
            print(f"{i + 1}. {prenda.mostrar_info()}")

    def buscar_prenda(self, index):
        if 0 <= index < len(self._inventario):
            return self._inventario[index]
        return None


class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto, cantidad):
        if producto.reducir_cantidad(cantidad):
            self._productos.append((producto, cantidad))
            print(f"Agregado {cantidad} de {producto._nombre} al carrito.")
        else:
            print(f"No hay suficiente cantidad de {producto._nombre}.")

    def calcular_total(self):
        total = sum(producto.obtener_precio() * cantidad for producto, cantidad in self._productos)
        return total

    def mostrar_resumen(self):
        print("\nResumen de compra:")
        for producto, cantidad in self._productos:
            print(f"{producto._nombre} - Cantidad: {cantidad} - Precio total: ${producto.obtener_precio() * cantidad:.2f}")
        print(f"Total a pagar: ${self.calcular_total():.2f}")


# Inicialización de la tienda y el inventario
tienda = Tienda()
tienda.agregar_prenda(Camisa("Camisa de Hombre", 25.00, 50, "M"))
tienda.agregar_prenda(Pantalon("Pantalón de Hombre", 30.00, 30, "L"))
tienda.agregar_prenda(Chaqueta("Chaqueta de Hombre", 55.00, 20, "XL"))
tienda.agregar_prenda(Falda("Falda de Mujer", 28.00, 15, "S"))
tienda.agregar_prenda(Blusa("Blusa de Mujer", 22.00, 40, "M"))
tienda.agregar_prenda(Vestido("Vestido de Mujer", 45.00, 10, "L"))
tienda.agregar_prenda(Zapato("Zapatos de Hombre", 60.00, 25, "42"))
tienda.agregar_prenda(Zapato("Zapatos de Mujer", 50.00, 20, "38"))

# Interacción con el usuario
def main():
    carrito = Carrito()
    
    while True:
        print("\nBienvenido a la tienda de ropa")
        print("Seleccione una opción:")
        print("1. Mostrar inventario")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Finalizar compra")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            tienda.mostrar_inventario()
        
        elif opcion == '2':
            tienda.mostrar_inventario()
            try:
                index = int(input("Ingrese el número del producto que desea agregar al carrito: ")) - 1
                cantidad = int(input("Ingrese la cantidad que desea agregar: "))
                producto = tienda.buscar_prenda(index)
                if producto:
                    carrito.agregar_producto(producto, cantidad)
                else:
                    print("Producto no encontrado.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")

        elif opcion == '3':
            carrito.mostrar_resumen()
        
        elif opcion == '4':
            carrito.mostrar_resumen()
            print("Gracias por su compra!")
            break
        
        elif opcion == '5':
            print("Saliendo de la tienda. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()