from persona import Persona
class Estudiante(Persona):
    def __init__(self,nro_id,nro_Matricula, tipo_id, nombres, apellidos, direccion, telefono, email, rh, carrera, codigo_estudiante, semestre, facultad, valor_matricula, pago_matricula = False):
        super().__init__(nro_id, tipo_id, nombres, apellidos, direccion, telefono, email, rh)
        self.__carrera = carrera
        self.__codigo_estudiante = codigo_estudiante
        self.__semestre = semestre
        self.__facultad = facultad
        self.__pago_matricula = pago_matricula
        self.__valor_matricula = valor_matricula

    # Metodos getters   
    def get_carrera(self):
        return self.__carrera
    
    def get_codigo_estudiante(self):
        return self.__codigo_estudiante
    
    def get_semestre(self):
        return self.__semestre
    
    def get_facultad(self):
        return self.__facultad
    def get_valor_matricula(self):
        return self.__valor_matricula
    def get_pago_matricula(self):
        return self.__pago_matricula
    
    # Metodos setters
    def set_carrera(self, carrera):
        self.__carrera = carrera
    
    def set_codigo_estudiante(self, codigo_estudiante):
        self.__codigo_estudiante = codigo_estudiante
        
    def set_semestre(self, semestre):
        self.__semestre = semestre
    
    def set_facultad(self, facultad):
        self.__facultad = facultad
    def set_valor_matricula(self, valor_matricula):
        self.__valor_matricula = valor_matricula
    def set_pago_matricula(self, pago_matricula):
        self.__pago_matricula = pago_matricula

    
    
    # Metodo de pago de matricula
    def pagar_matricula(self, monto):
        if monto >= self.__valor_matricula:
            self.__pago_matricula = True
            return "Matrícula pagada con éxito."
        else:
            return f"Monto insuficiente para pagar la matrícula, la matricula posee un valor de {self.__valor_matricula} y ustedd realizo un pago de {monto}."
            
    # Metodo para mostrar la informacion del estudiante
    def consultar_info_personal(self):
        return self.mostrar_informacion() + f"\nCarrera: {self.__carrera} \nCódigo Estudiante: {self.__codigo_estudiante} \nSemestre: {self.__semestre} \nFacultad: {self.__facultad} \nValor Matrícula: {self.__valor_matricula} \nPago Matrícula: {'Sí' if self.__pago_matricula else 'No'}"