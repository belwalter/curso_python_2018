
class validarPinturaException(Exception):

    def __init__(self, campo):
        self.msg = "atributo de clase sin valor"
        self.campo = campo

    def __str__(self):
        return "Error en el campo " + self.campo + " " + self.msg

    def get_campo(self):
        if(self.campo == "estilo"):
            return 0
        elif(self.campo == "material"):
            return 1
        elif(self.campo == "tipo"):
            return 2
        elif(self.campo == "artista"):
            return 3
        elif(self.campo == "descripcion"):
            return 4
        else:
            return -1

    def get_msg(self):
        return "Debe complear el campo " + self.campo
