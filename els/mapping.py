#!/usr/bin/python
#encoding=utf8

from utils import MappingFileGenerator
from lang import Lang

L = Lang.get_instance()

condominio = MappingFileGenerator()
condominio.add('descricao_conta')
condominio.add('id_conta')
condominio.add('data')
condominio.add('descricao_movimento')
condominio.add('tipo_movimento')
condominio.add('importe')
condominio.save('mapping.json')

