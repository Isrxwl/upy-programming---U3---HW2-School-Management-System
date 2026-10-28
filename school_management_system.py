# INPUT
# Base de datos simulada
usuarios = {
    'jperez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Juan Pérez'},
    'amartin': {'password': '1234', 'rol': 'alumno', 'nombre': 'Ana Martín'},
    'cgonzalez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Carlos González'},
    'lhernandez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Laura Hernández'},
    'mrodriguez': {'password': '1234', 'rol': 'alumno', 'nombre': 'Miguel Rodríguez'},
    'sruiz': {'password': '1234', 'rol': 'alumno', 'nombre': 'Sofía Ruiz'},
    'mlopez': {'password': '1234', 'rol': 'maestro', 'nombre': 'María López'},
    'rgarcia': {'password': '1234', 'rol': 'coordinador', 'nombre': 'Rosa García'}
}

# Materias
materias = ('Matemáticas', 'Programación', 'Inglés')

# Calificaciones de los 6 alumnos
calificaciones = {
    'jperez': {'Matemáticas': 8.5, 'Programación': 9.0, 'Inglés': 7.5},
    'amartin': {'Matemáticas': 9.0, 'Programación': 8.0, 'Inglés': 8.5},
    'cgonzalez': {'Matemáticas': 7.0, 'Programación': 7.5, 'Inglés': 8.0},
    'lhernandez': {'Matemáticas': 10.0, 'Programación': 9.5, 'Inglés': 9.0},
    'mrodriguez': {'Matemáticas': 6.0, 'Programación': 7.0, 'Inglés': 6.5},
    'sruiz': {'Matemáticas': 8.0, 'Programación': 8.5, 'Inglés': 9.0}
}


# PROCESS y OUTPUT
login_exitoso = False
usuario_actual = ""

# 1. Login con ciclo while (intentos ilimitados)
while not login_exitoso:
    user = input("Usuario: ")
    pwd = input("Contraseña: ")
    
    if user in usuarios and usuarios[user]['password'] == pwd:
        login_exitoso = True
        usuario_actual = user
    else:
        print("Usuario o contraseña incorrectos. Intenta de nuevo.\n")

# Extraer datos del usuario
rol_actual = usuarios[usuario_actual]['rol']
nombre_actual = usuarios[usuario_actual]['nombre']

print(f"\nBienvenido, {nombre_actual} ({rol_actual})")


# 2. Separamos por roles usando if/elif/else
if rol_actual == 'alumno':
    print(f"\nBoleta de {nombre_actual}")
    
    aprobadas = set() # Set vacío para las materias aprobadas
    
    # Recorremos la tupla de materias
    for materia in materias:
        calif = calificaciones[usuario_actual][materia]
        print(f"{materia}: {calif}")
        
        # Validamos si se aprobó (mayor o igual a 8.0)
        if calif >= 8.0:
            aprobadas.add(materia)
            
    # Calculamos pendientes restando los sets
    pendientes = set(materias) - aprobadas
    
    print(f"Materias aprobadas: {aprobadas}")
    print(f"Materias pendientes: {pendientes}")


elif rol_actual == 'maestro':
    print("\nLista de alumnos:")
    # Filtramos usuarios por rol 'alumno'
    for u in usuarios:
        if usuarios[u]['rol'] == 'alumno':
            print(f"- {u} ({usuarios[u]['nombre']})")
            
    print("")
    alumno_a_calificar = input("Alumno a calificar (usuario): ")
    
    if alumno_a_calificar in calificaciones:
        materia_a_calificar = input("Materia: ")
        
        if materia_a_calificar in materias:
            nueva_calif = float(input("Nueva calificación: "))
            
            # Actualizamos las calificaciones en el diccionario
            calificaciones[alumno_a_calificar][materia_a_calificar] = nueva_calif
            print("Calificación actualizada.")
        else:
            print("Materia no válida.")
    else:
        print("Usuario de alumno no encontrado.")


elif rol_actual == 'coordinador':
    print("\n--- REPORTE DEL COORDINADOR ---")
    
    print("\nMaestros:")
    for u in usuarios:
        if usuarios[u]['rol'] == 'maestro':
            print(f"- {usuarios[u]['nombre']}")
            
    print("\nMaterias:")
    for m in materias:
        print(f"- {m}")
        
    print("\nAlumnos y calificaciones:")
    # Recorremos todo el diccionario de calificaciones
    for alumno in calificaciones:
        nombre_al = usuarios[alumno]['nombre']
        print(f"\n{nombre_al} ({alumno}):")
        
        # Recorremos las calificaciones del alumno usando la tupla de materias
        for m in materias:
            print(f"  {m}: {calificaciones[alumno][m]}")
