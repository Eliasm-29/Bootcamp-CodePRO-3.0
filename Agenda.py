agenda = {}

opcion = ''

while opcion != '4':

    print("\n--- Menú de la Agenda ---")
    print("1. Mostrar Contactos")
    print("2. Crear Contacto")
    print("3. Modificar Contacto")
    print("4. Salir")

    opcion = input("Indique la acción que desea realizar (1-4): ")

    if opcion == '1':

        if not agenda:
            print("La agenda está vacía.")

        else:
            print("\nContactos guardados:")

            for nombre, datos in agenda.items():
                print(f"Nombre: {nombre}")
                print(f"  Teléfono: {datos['telefono']}")
                print(f"  Email: {datos['email']}")
                print("-" * 20)

    elif opcion == '2':
        nombre_contacto = input('Ingrese el nombre del contacto: ')
        telefono_contacto = input('Ingrese el número de teléfono del contacto: ')
        email_contacto = input('Ingrese el email del contacto: ')

        contador = 0
        nombre_final = nombre_contacto

        while nombre_final in agenda:
            contador += 1
            nombre_final = f"{nombre_contacto}{contador}"

        agenda[nombre_final] = {
            'telefono': telefono_contacto,
            'email': email_contacto
        }
        print(f"Contacto '{nombre_final}' creado con éxito.")

    elif opcion == '3':
        nombre_actual = input("Ingrese el nombre del contacto que desea modificar: ")

        if nombre_actual in agenda:
            datos = agenda[nombre_actual]

            print(f"\nContacto encontrado: {nombre_actual}")
            print(f"Teléfono: {datos['telefono']}")
            print(f"Email: {datos['email']}")
            
            print("\n¿Qué desea modificar?")
            print("1. Nombre")
            print("2. Teléfono")
            print("3. Email")
            print("4. Todos")

            sub_opcion = input("Elija una opción (1-4): ")

            if sub_opcion == '1':
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                agenda[nuevo_nombre] = datos
                del agenda[nombre_actual]

                print("Nombre actualizado con éxito.")

            elif sub_opcion == '2':
                nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
                datos["telefono"] = nuevo_telefono

                print("Teléfono actualizado con éxito.")

            elif sub_opcion == '3':
                nuevo_email = input("Ingrese el nuevo email: ")
                datos["email"] = nuevo_email
                
                print("Email actualizado con éxito.")

            elif sub_opcion == '4':
                nuevo_nombre = input("Ingrese el nuevo nombre: ")
                nuevo_telefono = input("Ingrese el nuevo teléfono: ")
                nuevo_email = input("Ingrese el nuevo email: ")

                datos["telefono"] = nuevo_telefono
                datos["email"] = nuevo_email

                agenda[nuevo_nombre] = datos

                if nuevo_nombre != nombre_actual:
                    del agenda[nombre_actual]
                print("Contacto actualizado con éxito.")

            else:
                print("Opción no válida.")

        else:
            print("El contacto no existe.")

    elif opcion == '4':
        print("Saliendo del programa...")

    else:
        print("Ingrese una opción válida.")
