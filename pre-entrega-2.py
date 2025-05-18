# Lista vacía para Agregar, Mostrar, Buscar y Eliminar productos.
productos = []

while True:
    # Menú de opciones
    print("\n--- Menú de Productos ---")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    opcion = input("Seleccione una opción (1/2/3/4/5): ").strip()

    # Agregar producto
    if opcion == "1":
        print("\n--- Agregar Producto ---")
        nombre = input("Nombre del producto: ").strip()
        if not nombre:
            print("Nombre vacío. Cancelando registro.")
            continue
        categoria = input("Categoría del producto: ").strip()
        while True:
            precio_str = input("Precio (sin centavos): ").strip()
            if precio_str.isdigit():
                precio = int(precio_str)
                break
            else:
                print("Error: ingrese un precio válido (solo números enteros).")
        productos.append([nombre, categoria, precio])
        print(f"Producto '{nombre}' agregado.")

    # Mostrar productos
    elif opcion == "2":
        print("\n--- Lista de Productos ---")
        if len(productos) > 0:
            for i in range(len(productos)):
                prod = productos[i]
                print(f"{i+1}. Nombre: {prod[0].title()}, Categoría: {prod[1].upper()}, Precio: {prod[2]}")
        else:
            print("No hay productos registrados.")

    # Buscar producto por nombre
    elif opcion == "3":
        print("\n--- Buscar Producto ---")
        if len(productos) == 0:
            print("No hay productos registrados para buscar.")
        else:
            termino = input("Ingrese nombre o parte del nombre a buscar: ").strip()
            resultados = []
            for prod in productos:
                if prod[0].upper().find(termino.upper()) != -1:
                    resultados.append(prod)
            if len(resultados) > 0:
                print(f"Se encontraron {len(resultados)} producto(s):")
                for i in range(len(resultados)):
                    r = resultados[i]
                    print(f"{i+1}. Nombre: {r[0].title()}, Categoría: {r[1].upper()}, Precio: {r[2]}")
            else:
                print("No se encontraron productos con ese término.")

    # Eliminar producto por posición
    elif opcion == "4":
        print("\n--- Eliminar Producto ---")
        if len(productos) == 0:
            print("No hay productos registrados para eliminar.")
        else:
            # Mostrar lista breve
            for i in range(len(productos)):
                prod = productos[i]
                print(f"{i+1}. {prod[0].title()} - {prod[1].upper()} - {prod[2]}")
            while True:
                idx_str = input("Ingrese el número del producto a eliminar: ").strip()
                if idx_str.isdigit():
                    idx = int(idx_str) - 1
                    if 0 <= idx < len(productos):
                        eliminado = productos.pop(idx)
                        print(f"Producto '{eliminado[0]}' eliminado.")
                        break
                    else:
                        print("Número fuera de rango. Intente de nuevo.")
                else:
                    print("Entrada inválida. Ingrese un número válido.")

    # Salir del programa
    elif opcion == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor ingrese 1, 2, 3, 4 o 5.")

# Fin del programa