#!/usr/bin/env python
# -*- coding: utf-8 -*-
#4. Pide un gestor y muestra los centros que gestiona con sus observaciones.
from lxml import etree
doc = etree.parse("2015centsanitario.xml")

raiz = doc.getroot()

posiblesG = []

gestores = raiz.findall("features/attributes/GESTION")
observaciones = raiz.findall("features/attributes/OBSERVACIO")
nombres = raiz.findall("features/attributes/NOMBRE")

gestor = raw_input ("Introduce un gestor: ")

for i in xrange(0,len(gestores)-1):
	if gestor == gestores[i].text:
		print nombres[i].text,observaciones[i].text

