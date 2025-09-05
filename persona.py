class Persona:
    # Metodo constructor
    def __init__(self, nro_id, tipo_id, nombres, apellidos, direccion, telefono, email, rh):
        self.__nro_id = nro_id
        self.__tipo_id = tipo_id
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__rh = rh
    
    # Metodos getters
    
    def get_nro_id(self):
        return self.__nro_id
    
    def get_tipo_id(self):
        return self.__tipo_id
    
    def get_nombres(self):
        return self.__nombres
    
    def get_apellidos(self):
        return self.__apellidos 
    
    def get_direccion(self):
        return self.__direccion
    
    def get_telefono(self):
        return self.__telefono
    
    def get_email(self):
        return self.__email
    
    def get_rh(self):
        return self.__rh
    
    # Metodos setters
    
    def set_nro_id(self, nro_id):
        self.__nro_id = nro_id
        
    def set_tipo_id(self, tipo_id):
        self.__tipo_id = tipo_id
        
    def set_nombres(self, nombres):
        self.__nombres = nombres
    
    def set_apellidos(self, apellidos):
        self.__apellidos = apellidos
        
    def set_direccion(self, direccion):
        self.__direccion = direccion
        
    def set_telefono(self, telefono):
        self.__telefono = telefono
        
    def set_email(self, email):
        self.__email = email
        
    def set_rh(self, rh):
        self.__rh = rh
    
    # Metodo para mostrar la informacion de la persona
    def mostrar_informacion(self):
        info = (
            f"Numero de Identificacion: {self.__nro_id}\n"
            f"Tipo de Identificacion: {self.__tipo_id}\n"
            f"Nombres: {self.__nombres}\n"
            f"Apellidos: {self.__apellidos}\n"
            f"Direccion: {self.__direccion}\n"
            f"Telefono: {self.__telefono}\n"
            f"Email: {self.__email}\n"
            f"RH: {self.__rh}"
        )
        return info
    
    
    