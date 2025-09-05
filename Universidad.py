class universidad:
    def __init__(self, nombre, ubicacion, NIT, ranking, lista_docentes, lista_facultades, lista_estudiantes, tipo_id, nro_id, presupuesto, Mision, Vision): 
        self.lista_docentes = lista_docentes
        self.lista_facultades = lista_facultades
        self.lista_estudiantes = lista_estudiantes
        self.presupuesto = presupuesto
        self.Mision = Mision
        self.Vision = Vision   
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.ranking = ranking
        self.NIT = NIT
    # Metodos getters           

    def get_nombre(self):
        return self.nombre
    def get_ubicacion(self):
        return self.ubicacion
    def get_NIT(self):
        return self.NIT
    def get_ranking(self):
        return self.ranking
    def get_presupuesto(self):
        return self.presupuesto
    def get_Mision(self):
        return self.Mision
    def get_Vision(self):
        return self.Vision
   
   # Agregar docentes, Estudiantes, Facultades a la universidad
    def agregar_docente(self, docente):
        self.lista_docentes.append(docente)
    
    def agregar_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)
    
    def agregar_facultad(self, facultad):
        self.lista_facultades.append(facultad)

    def info_universidad(self):
        return (f"Universidad: {self.nombre}, Ubicación: {self.ubicacion}, NIT: {self.NIT}, Ranking: {self.ranking}, Presupuesto: {self.presupuesto}, "
                f"Misión: {self.Mision}, Visión: {self.Vision}\n")
    # Metodos setters
    def set_nombre(self, nombre):
        self.nombre = nombre
    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion
    def set_NIT(self, NIT):
        self.NIT = NIT
    def set_ranking(self, ranking):
        self.ranking = ranking
    def set_presupuesto(self, presupuesto):
        self.presupuesto = presupuesto
    def set_Mision(self, Mision):
        self.Mision = Mision
    def set_Vision(self, Vision):
        self.Vision = Vision

    # Metodo para mostrar la informacion de la universidad
    def mostrar_docentes(self):
        for docente in self.lista_docentes:
            print(docente.mostrar_info())
    def mostrar_estudiantes(self):
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info())
    def mostrar_facultades(self):
        for facultad in self.lista_facultades:
            print(facultad.mostrar_info())

