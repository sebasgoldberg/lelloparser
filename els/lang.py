#!/usr/bin/python
#encoding=utf8

class Lang:

    instance = None

    @staticmethod
    def get_instance():
        
        if Lang.instance is None:
            Lang.instance = Lang()
        
        return Lang.instance

    def __init__(self):

        self.types = {}
        self.types['descricao_conta'] = 'string'
        self.types['id_conta'] = 'string'
        self.types['data'] = 'date'
        self.types['descricao_movimento'] = 'string'
        self.types['tipo_movimento'] = 'string'
        self.types['importe'] = 'double'

    def get_fieldtype(self, field):
        return self.types[field]

