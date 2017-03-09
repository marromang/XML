#!/usr/bin/env python
# -*- coding: utf-8 -*-
#2. Cuenta el numero de centros de cada tipo

from lxml import etree
doc = etree.parse("2015centsanitario.xml")

raiz = doc.getroot()

tipos  = raiz.findall("features/attributes/TIPO")


listaTipos = []
contador = 0

for tip in tipos:
	if tip.text not in listaTipos:
		listaTipos.append(tip.text)

for ltipo in listaTipos:
	for tip in tipos:
		if tip.text == ltipo:
			contador = contador + 1
	print ltipo, contador
	contador = 0		

