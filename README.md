# S1
#Seminario 1  DDSI

La idea consiste en crear un pequeño sistema de información para gestionar pedidos ficticios.

Las tareas a realizar son:

la información se guardará en 3 tablas:
  -Stock(Cproducto, Cantidad)
  -Pedido(CPedido, Ccliente, Fecha-pedido)
  -Detalle-Pedido(Cpedido, Cproducto, Cantidad)
  
  La aplicación debe realizar:
  
  Conexión a BD mediante ODBC ó JDBC.
  
  Mostrar un interfaz muy sencillo con un menú principal que permita las siguientes opciones:
    
  1.-Borrado y nueva creación de las tablas e inserción de 10 tuplaspredefinidas en el código en la tabla Stock.
    
  2.-Dar de alta nuevo pedido:
    2.1.-El interfaz capturará los datos básicos del pedido, que se insertarán en la tabla Pedido con un INSERT.
    2.2.-A continuación ofrecerá como opciones “1. Añadir detalle de producto”, “2. Eliminar todos los detalles de producto”, “3. Cancelar pedido” y “4. Finalizar pedido”.
    2.3.-La opción 1 debe capturar los datos de un artículo y cantidad, y realizar la inserción correspondiente en la tabla Detalle-Pedido, si hay stock, así como actualizar el stock, quedando en este mismo menú.
    2.4.-La opción 2 debe eliminar todos los detalles de pedido que se han insertado en Detalle-Pedido para el pedido actual (pero no el pedido en la tabla Pedidos) y quedar en este mismo menú.
    2.5.-La opción 3 debe eliminar el pedido y todos sus detalles y volver al menú principal de la aplicación.
    2.6.-La opción 4 debe hacer los cambios permanentes y volver al menú principal de la aplicación.
    
  3.-Mostrar contenido de las tablas de la BD
    
  4.-Salir del programa y cerrar conexión a BD
    
Se exige que el programa use obligatoriamente control de transacciones, hemos hecho un análisis preliminar y hemos decido crear un SAVEPOINT <INICIAL> justo después de la opción 1, otro **SAVEPOINT PEDIDO** una vez que se da de alta un nuevo pedido 2.1, para la opción 2.4 **ROLLBACK TO PEDIDO** , para la opción 2.5 **ROLLBACK TO INICIAL**, para la opción 2.6 **COMMIT**
