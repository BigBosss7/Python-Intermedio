


def my_agenda():
    
    agenda={}
    
    def insert_contact():
        new_phone = input("Ingrese el nuevo teléfono del contacto: ")
        if new_phone.isdigit() and len(new_phone) > 0 and len(new_phone) <= 11:
            agenda[name] = new_phone
        else:
            print("Número de teléfono inválido. Debe contener solo dígitos y tener entre 1 y 11 caracteres.")

    while True:
        
        print("\n--- AGENDA DE CONTACTOS ---")
        
        print("1. Buscar contacto")
        print("2. Agregar contacto")
        print("3. Actualizar contacto") 
        print("4. eliminar contactos") 
        print("5. Salir")
    
        option = input("\nSeleccione una opción: ")
    
        match option:
            case "1":
                name = input("Ingrese el nombre del contacto a buscar: ")
                if name in agenda:
                    print(f"El teléfono de {name} es: {agenda[name]}")
                else:
                    print(f"El contacto {name} no se encuentra en la agenda.")
            case "2":
                name = input("Ingrese el nombre del contacto: ")  
                insert_contact()
            case "3":
                name = input("Ingrese el nombre del contacto a actualizar: ")
                if name in agenda:
                    
                    insert_contact()
                else:
                    print(f"El contacto {name} no se encuentra en la agenda.")
            case "4":
                name = input("Ingrese el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                    print(f"El contacto {name} ha sido eliminado.")
                else:
                    print(f"El contacto {name} no se encuentra en la agenda.")
            case "5":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida. Elija una opción del 1 al 5.")
    
    
    
my_agenda()