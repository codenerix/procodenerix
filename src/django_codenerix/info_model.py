class InfoModel:
    '''
    Metodos necesarios
    '''
    class Serializer(object):
        # campos extras para el serializador
        pass

    @staticmethod
    def serializer_fields(info):
        # listado de campos del modelo que se serializaran
        # con la información de la variable 'info' deberiamos de saber el usuario y el rol que tiene
        # esta información se puede obtener de forma automática desde el método __fields__
        pass

    @staticmethod
    def queryset(info):
        # queryset que se aplicará en las vistas
        # con la información de la variable 'info' deberiamos de saber el usuario y el rol que tiene
        pass

    def __fields__(self, info):
        # listado de campos que se retornaran en el listado (meta)
        pass

    def __str__(self):
        # representación gráfica del modelo
        pass

    def __form__(self, info):
        # devuelve la estructura de como se debería representar el formulario
        pass
