from persona import Persona
 
class Administrativo(Persona):

    #Metodo constructor 
    def __init__(self, nro_id, tipo_id, nombres, apellidos, direccion, telefono, email, rh, salario, eps, estudiante = {}):
        super().__init__(nro_id, tipo_id, nombres, apellidos, direccion, telefono, email, rh)
        self.__salario = salario
        self.__eps = eps
        self.__estudiante = estudiante
    
    #Metodos getters
    def get_salario(self):
        return self.__salario
    
    def get_estudiante(self):
        return self.__estudiante
    
    def get_eps(self):
        return self.__eps
    
    #Metodos setters
    def set_salario(self, salario):
        self.__salario = salario
        
    def set_estudiante(self, estudiante):
        self.__estudiante = estudiante
    
    def set_eps(self, eps):
        self.__eps = eps

    #Metodo para mostrar la informacion del administrativo
    def consultar_info_personal(self):
        return self.mostrar_informacion() + f"\nSalario: {self.__salario} \nEPS: {self.__eps}"
    
    # Metodo para listar los estudiantes a cargo del administrativo
    def listar_estudiantes(self):
        if not self.__estudiante:
            return "No hay estudiantes a cargo."
        return self.__estudiante