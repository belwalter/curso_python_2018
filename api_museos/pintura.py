import muestra


class Pintura(muestra.Obra_Muestra):

    def __init__(self, artista=None, anio=None, titulo=None, descripcion=None,
                 museo=None, tipo=None, material=None, estilo=None):
        super().__init__(artista, anio, titulo, descripcion, museo)
        self.tipo = tipo
        self.material = material
        self.estilo = estilo
