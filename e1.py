#!/usr/bin/env python
# -*- coding: utf-8 -*-
#1.Lista los tipos de centros.

from lxml import etree
doc = etree.parse("2015centsanitario.xml")

raiz = doc.getroot()

tipos  = raiz.findall("features/attributes/TIPO")
listaTipos = []

for tip in tipos:
	if tip.text not in listaTipos:
		listaTipos.append(tip.text)

for i in listaTipos:
	print i
