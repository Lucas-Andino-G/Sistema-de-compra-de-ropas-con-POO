# Sistema-de-compra-de-ropas-con-POO

Clase Producto:
En la clase producto tengo los atributos basicos de nombre, precio y cantidad disponible
-Atributos:
  _nombre
  _precio
  _cantidad

-Metodos:
  mostrar_info() "Muestra una lista con la informacion del producto"
  obtener_presio() "Retorno el presio del producto"
  reducir_cantidad(cantidad) "Se reduce la cantidad del producto si es que hay suficiente"

Clase Ropa:
Aqui heredo de "Producto" para representar un tipo especifico de producto, osea ropa y agrego el atributo talla
-Atributo:
  _talla

_Metodo:
  mostrar_info() "Aqui sobrescribo el metodo de la clase para agregar la talla en la informacion que se muestra"

Clases derivadas de Ropa:
- Camisa, Pantalon y Chaqueta se heredan de Ropa y son solo prendas para hombres
- Falda, Blusa y Vestido tambien se heredan de Ropa y son solo prendas de mujeres

Clase Zapato:
Este es producto especifico (zapatos) que se hereda de Producto
-Atributo:
  _talla

-Metodo:
  Mostrar_info() "Aqui sobrescribo el metodo de la clase para agregar la talla en la informacion que se muestra"

Clase Tienda:
En la clase tienda se maneja el inventario de productos que estan disponibles en la tienda
-Atributo:
  _inventario "Es la lista que contiene todos los producto que estan en la tienda"
-Metodos:
  agregar_prenda(prenda) "Aqui se agregan los productos al inventario"
  mostrar_inventario() "Aqui se muestran todos los productos que estan disponibles en el inventario"
  buscar_prenda(index) "Devuelvo un producto basandome en el indice del producto en la lista del inventario"

Clase Carrito:
En la clase carrito se almacenan todos los productos agregados por el usuario
-Atributo:
  _producto "Aqui se almacenan los productos añadidos junto con la cantidad de producto seleccionado"

-Metodos:
  agregar_producto(producto, cantidad) "Aqui se agrega un producto al carrito y se reduce la cantidad disponible"
  calcular_total() "Aqui se calcula el monto que va a pagar el usuario"
  mostrar_resumen() "Se muestra un resumen todos los articulos y el monto a pagar"


  Interaccion del usuario
  Con el main() el usuario tiene las siguientes opciones:
  - Ver inventario
  - Agregar productos al carrito de compras
  - Ver resumen del carrito
  - Finalizar la compra
