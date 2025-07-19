"""
--- Gestor de Tareas ---
1. Agregar tarea
2. Ver tareas
3. Marcar tarea como completada
4. Eliminar tarea
5. Salir
Elige una opción: 
"""
#lista tareas
tareas =[]

#agregar tareas
def agregar_tarea():
    tarea = input("Ingrese nueva tarea...")
    tarea_capitalized = tarea.capitalize()
    nueva_tarea ={
        'Tarea': tarea_capitalized,
        'Estado': "Pendiente"
    }

    tareas.append(nueva_tarea)
    print(f"Tarea {nueva_tarea["Tarea"]} ingresada correctamente. ")

#ver tarea
def ver_tarea():
    for tarea in tareas:
        task=[]
        for key, valor in tarea.items():
            task.append(f"{key} - {valor}")
        print (f" / ".join(task))
        



#mostrar tareas
def mostrar_tarea():
    for tarea in tareas:
        task=[]
        for key, valor in tarea.items():
            task.append(f"{key} - {valor}")
        print (f" / ".join(task))
    task_to_edit= input("Escriba el nombre de la tarea para seleccionarla...")
    task_to_edit_capitalized = task_to_edit.capitalize()        
    
    flag = True
    while flag:
        
        print("\n--- ¿Que deseas realizar? ---")
        print("1. Completar Tarea")
        print("2. Eliminar Tarea")
        print("3. Volver al menu")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            completar_tarea(task_to_edit_capitalized)
            break  
        elif opcion == "2":
            eliminar_tarea(task_to_edit_capitalized)
            break
        elif opcion == "3":
            flag = False
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.") 

    
            

#completar tarea
def completar_tarea(nombre_tarea):
    for tarea in tareas:
        if tarea['Tarea'] == nombre_tarea and tarea['Estado'] == "Pendiente":
            tarea['Estado'] = "Completado"
            print(f"Tarea '{nombre_tarea}' marcada como completada.")
            return
    print(f"No se encontró la tarea '{nombre_tarea}'.")


#eliminar tarea
def eliminar_tarea(nombre_tarea):
    for tarea in tareas:
        if tarea['Tarea'] == nombre_tarea:
            tareas.remove(tarea)
            print(f"Tarea '{nombre_tarea}' eliminada.")
            return
        else:
            print(f"No se encontró la tarea '{nombre_tarea}'.")




#funcion menu
def menu_principal():
    """Muestra el menú principal del gestor de tareas"""
    flag = True
    while flag:
        print("\n--- Gestor de Tareas ---")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Completar/Eliminar")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            if len(tareas) == 0:
                print("No hay tareas para mostar, por favor agregue tareas para mostrar")
            else:
                ver_tarea()
        elif opcion == "3":
            if len(tareas) == 0:
                print("No hay tareas para mostar, por favor agregue tareas para mostrar")
            else:
                mostrar_tarea()
        elif opcion == "4":
            print("Gracias por usar el gestor de Tareas. ¡Hasta pronto!")
            flag = False
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")

#ejecutar el menu
if __name__ == "__main__":
    menu_principal()