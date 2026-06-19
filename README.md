#Proyecto: Gestión de  Restaurante 
Nombre: Nathaly Lisbeth Tnizaray Abad

#Descripción del sistema

Este proyecto es una aplicación básica desarrollada en *Python, bajo el paradigma de **Programación Orientada a Objetos*. Su objetivo es administrar los datos principales de un restaurante: registrar productos con su precio y clientes con sus datos de contacto, además de permitir mostrar toda la información guardada. Es funcional, sencilla y está organizada para facilitar su lectura, mantenimiento y ampliación futura

#Estructtura del Proyecto

Repositorio GitHub
├── restaurante_app/
│   ├── modelos/
│   │   ├── producto.py       # Define la clase Producto
│   │   └── cliente.py        # Define la clase Cliente
│   ├── servicios/
│   │   └── restaurante.py     # Gestiona la lógica del restaurante (clientes y productos)
│   └── main.py                # Punto de entrada de la aplicación
└── README.md                  # Documentación del proyecto

#Componentes Principales
  1.Modelos 
 ⁠Cliente⁠: Registra los datos básicos del cliente como su nombre y número de teléfono.
 ⁠Producto⁠: Registra el menú disponible con el nombre del producto y su respectivo precio.

   2.Servicios 
 ⁠Restaurante⁠: Funciona como el núcleo del sistema. Se encarga de almacenar las listas de productos y clientes mediante métodos dedicados para agregar y mostrar la información en consola

 #Reflexión 
La modularización del software es fundamental porque permite "separar responsabilidades", mejorar la organización y facilitar el mantenimiento. Al dividir el sistema en módulos, cada parte cumple un rol específico, lo que hace que el código sea más claro, escalable y fácil de reutilizar. Esta práctica fomenta la colaboración y asegura que los proyectos puedan crecer sin perder orden ni calidad.