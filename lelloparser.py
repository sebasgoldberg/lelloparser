#!/usr/bin/python
# coding=utf-8
import urllib2
import sys
from bs4 import BeautifulSoup
import os
from els.utils import ElasticFilesGenerator
from datetime import datetime

INDEX = 'condominio'
TYPE = 'condominio'
DEBITO = 4
CREDITO = 5

#$('#tabela_analitica tbody').first().find('tr').each(function(index, value){
#	console.log($(value).find('td').first().text()); 
#});

efg = ElasticFilesGenerator(INDEX, TYPE, 'condominio')

def getImporte(text):
  return float(text.split(' ')[1].replace('.','').replace(',','.'))



def lelloparse(filename):
  with open(filename,'r') as f:
    bs = BeautifulSoup(f.read())

  regnum = 0
  for tbody in bs.find_all('tbody')[:-2]:
      for tr in tbody.find_all('tr'):
          reg = []
          for td in tr.find_all('td'):
              reg.append(td.getText())
          
          try:
            register = {
                'descricao_conta': reg[0],
                'id_conta': reg[1],
                'data': str(datetime.strptime(reg[2],'%d/%m/%Y')),
                'descricao_movimento': reg[3],
                }

            if reg[CREDITO] <> '':
                register['tipo_movimento'] = 'credito'
                register['importe'] = getImporte(reg[CREDITO])
            else:
                register['tipo_movimento'] = 'debito'
                register['importe'] = - getImporte(reg[DEBITO])

            regnum = regnum + 1
            efg.add(register,u'%s[%s]' % (filename, str(regnum)))
          except Exception as e:
            print(reg)


for filename in sys.argv[1:]:
  lelloparse(filename)
