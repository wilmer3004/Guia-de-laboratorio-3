from persona import Persona

class Docente(Persona):
    # Metodo constructor 
    def __init__(self, Antiguedad, ranking, facultad, area, meritos, nro_id, tipo_id, nombres, apellidos, direccion, telefono, email, rh):
        super().__init__(nro_id, tipo_id, nombres, apellidos, direccion, telefono, email, rh)
        self.__Antiguedad = Antiguedad
        self.__ranking = ranking
        self.__facultad = facultad
        self.__area = area
        self.__meritos = meritos 
    # Metodos getters
    def get_Antiguedad(self):
        return self.__Antiguedad
    def get_ranking(self):
        return self.__ranking
    def get_facultad(self):
        return self.__facultad
    def get_area(self):
        return self.__area
    def get_meritos(self):
        return self.__meritos
    # Metodos setters
    def set_Antiguedad(self, Antiguedad):
        self.__Antiguedad = Antiguedad  
    def set_ranking(self, ranking):
        self.__ranking = ranking
    def set_facultad(self, facultad):
        self.__facultad = facultad
    def set_area(self, area):
        self.__area = area
    def set_meritos(self, meritos):
        self.__meritos = meritos    
    # Metodo para mostrar la informacion del docente
    def mostrar_info(self):
        return (f"Docente: {self.get_nombres()} {self.get_apellidos()}, Antiguedad: {self.__Antiguedad}, Ranking: {self.__ranking}, "
                f"Facultad: {self.__facultad}, Area: {self.__area}, Meritos: {self.__meritos}, Nro ID: {self.get_nro_id()}, "
                f"Tipo ID: {self.get_tipo_id()}, Dirección: {self.get_direccion()}, Teléfono: {self.get_telefono()}, "
                f"Email: {self.get_email()}, RH: {self.get_rh()}\n")
    
    