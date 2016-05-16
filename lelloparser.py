#!/usr/bin/python
# coding=utf-8
import urllib2
import sys
from bs4 import BeautifulSoup
import os

raw = sys.stdin.read()
bs = BeautifulSoup(raw)

#$('#tabela_analitica tbody').first().find('tr').each(function(index, value){
#	console.log($(value).find('td').first().text()); 
#});

for tbody in bs.find_all('tbody')[:-2]:
    for tr in tbody.find_all('tr'):
        reg = []
        for td in tr.find_all('td'):
            reg.append(td.getText())
        print(reg)

