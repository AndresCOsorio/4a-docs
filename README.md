# 4a-docs
creación Jira ciclas_Ecommerce

PROYECTO e-Comerce Bicicletas CICLAX2000

Especificación del cliente (CICLAX2000):
“Deseamos que el sistema permita que nuestros usuarios accedan a tres servicios principales: 

1.Catalogo de productos, donde pueda consultar de manera sencilla todos los productos que hay    disponibles, sus especificaciones, imágenes, precio y disponibilidad.

2.Carrito de compras, donde el usuario pueda realizar sus compras, pagar con diferentes medios de pagos, ver lo pedido, y ver cual es el estado de su pedido.

3.Creacion de usuarios, donde el usuario pueda crear su perfil y luego pueda modificar sus datos.”

User Story 1.1:
 “Yo como cliente de CICLAX2000, quiero consultar de manera sencilla todos los productos que hay disponibles, sus especificaciones, imágenes, precio y disponibilidad.”
 
 User Story 2.1: 
“Yo como cliente de CICLAX2000, quiero realizar una o varias compras, pagar con diferentes medios de pagos, ver lo pedido, y ver cual es el estado del pedido.”

User Story 3.1: 
“Yo como cliente de CICLAX2000, quiero crear mi usuario donde pueda ingresar mis datos y preferencias, y que después pueda administrar mi perfil y modificar mis datos.”



Task 0.0.1: Diseñar el diagrama de despliegue y el diagrama de componentes. [team]
Task 0.0.2: Diseñar el modelo de la base de datos. [backend]
Task 0.0.3: Construir base de datos en PostgreSQL. [backend]
Task 0.0.4: Desplegar la base de datos en Heroku. [leader]


EPICs
Epic 1: Gestionar modulo de catalogo de productos.

User Story 1.1:
 “Yo como cliente de CICLAX2000, quiero consultar de manera sencilla todos los productos que hay disponibles, sus especificaciones, imágenes, precio y disponibilidad.”

Task 1.1.1: Construir un servicio web para consultar el catalogo de productos disponibles. [backend]

Task 1.1.2: Construir un servicio web para consultar las especificaciones, imágenes, precio y disponibilidad de cada producto. [backend]

Task 1.1.3: Diseñar los mockups correspondientes a las UIs de: catalogo de productos actual, y de las características individuales de cada producto(especificaciones, imágenes, precio y disponibilidad). [frontend]

Task 1.1.4: Construir una UI para mostrar el catalogo de productos actual. [frontend]

Task 1.1.5: Construir una UI para mostrar las características individuales de cada producto(especificaciones, imágenes, precio y disponibilidad). [frontend]

Task 1.1.6: Diseñar casos de prueba tanto para los servicios web de consulta de catalogo de productos disponibles; como para las especificaciones, imágenes, precio y disponibilidad de cada producto. [QA]

Task 1.1.7: Llevar a cabo los casos de prueba para los servicios web de consulta de catalogo de productos disponibles; como para las especificaciones, imágenes, precio y disponibilidad de cada producto. [QA]

Task 1.1.8: Diseñar casos de prueba tanto para la utilización de las UI relacionadas con consulta de el catalogo de productos actual; como para mostrar las características individuales de cada producto(especificaciones, imágenes, precio y disponibilidad). [QA]

Task 1.1.9: Llevar a cabo casos de prueba para las UI relacionadas con consulta de el catalogo de productos actual; como para mostrar las características individuales de cada producto(especificaciones, imágenes, precio y disponibilidad). [QA]

Task 1.1.10: Desplegar los servicios web de consulta de el catalogo de productos disponibles y  las especificaciones, imágenes, precio y disponibilidad de cada producto, en el backend de producción usando Heroku. [leader]

Task 1.1.11: Desplegar las UI relacionadas con consulta de el catalogo de productos disponibles y  las especificaciones, imágenes, precio y disponibilidad de cada producto, en el frontend de producción usando Heroku. [leader]


Epic 2: Construir el módulo de carrito de compras.

User Story 2.1: 
“Yo como cliente de CICLAX2000, quiero realizar una o varias compras, pagar con diferentes medios de pagos, ver lo pedido, y ver cual es el estado del pedido.”

Task 2.1.1: Construir un servicio web para traer la lista de productos que selecciono el cliente para comprar. [backend]

Task 2.1.2: Construir un servicio web para que el cliente seleccione el medio de pago y que haga la transacción. [backend]

Task 2.1.3: Construir un servicio web para que el cliente vea su pedido y el estado de este. [backend]

Task 2.1.4: Diseñar los mockups correspondientes a las UIs de: productos seleccionados por el cliente para su compra, formulario donde el cliente escoja y realice el pago correspondiente  Y vista del pedido y el estado en que se encuentra. [frontend]

Task 2.1.5: Construir una UI que muestre una descripción general de los productos que va a comprar el cliente. [frontend]

Task 2.1.6: Construir una UI donde muestre un formulario donde el cliente escoja su medio de pago y haga la compra. [frontend]

Task 2.1.7: Construir una UI que indique cual es su pedido y el estado que se encuentra. [frontend]

Task 2.1.8: Diseñar casos de prueba tanto para los servicios web de lista de clientes y registro de transferencia electrónica. [QA]

Task 2.1.9: Diseñar casos de prueba tanto para los servicios web de: la lista de productos que selecciono el cliente para comprar, los medios de pagos disponibles para realizar la transferencia, el pedido y su estado . [QA]

Task 2.1.10: Llevar a cabo los casos de prueba para los servicios web de: la lista de productos que selecciono el cliente para comprar, los medios de pagos disponibles para realizar la transferencia, el pedido y su estado . [QA]

Task 2.1.11: Desplegar los servicios web de lista de productos que selecciono el cliente, el medio de pago y  la transacción, el pedido y el estado de este, en el backend de producción usando Heroku. [leader]

Task 2.1.12: Desplegar la UI relacionada con los productos seleccionados por el cliente para su compra,  formulario donde el cliente escoja y realice el pago correspondiente, y vista del pedido y el estado en que se encuentra, en el frontend de producción usando Heroku. [leader]


Epic 3: Gestionar el módulo de Usuario.

User Story 3.1: 
“Yo como cliente de CICLAX2000, quiero crear mi usuario donde pueda ingresar mis datos y preferencias, y que después pueda administrar mi perfil y modificar mis datos.”

Task 3.1.1: Construir un servicio web para crear un nuevo usuario. [backend]

Task 3.1.2: Construir un servicio web para que el cliente consulte su perfil y modifique alguno de sus datos. [backend]

Task 3.1.3: Diseñar los mockups correspondientes a las UIs de creación de un nuevo usuario y  modificación de un perfil actual. [frontend]

Task 3.1.4: Construir una UI con un formulario para crear un nuevo usuario. [frontend]

Task 3.1.5: Construir una UI con un formulario donde pueda editar los datos de un usuario activo. [frontend]

Task 3.1.6: Diseñar casos de prueba tanto para los servicios web de crear un nuevo usuario y para que el cliente consulte su perfil y modifique alguno de sus dato. [QA]

Task 3.1.7: Llevar a cabo los casos de prueba para los servicios web de crear un nuevo usuario y para que el cliente consulte su perfil y modifique alguno de sus datos. [QA]

Task 3.1.8: Diseñar casos de prueba tanto para la utilización de las UI relacionadas con la creación de un nuevo usuario y  modificación de un perfil actual. [QA]

Task 3.1.9: Llevar a cabo casos de prueba para las UI relacionadas con la creación de un nuevo usuario y  modificación de un perfil actual. [QA]

Task 3.1.10: Desplegar los servicios web de crear un nuevo usuario y para que el cliente consulte su perfil y modifique alguno de sus dato, en el backend de producción usando Heroku. [leader]

Task 3.1.11: Desplegar las UI relacionadas con la creación de un nuevo usuario y  modificación de un perfil actual, en el frontend de producción usando Heroku. [leader]
