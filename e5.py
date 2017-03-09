#!/usr/bin/env python
# -*- coding: utf-8 -*-
#5. Pide un numero minimo de camas, muestra los centros que superan ese numero, con su tipo y características como nombre, UCI(si tiene o no), tipo de centro, quién lo gestiona.
from lxml import etree
doc = etree.parse("2015centsanitario.xml")

raiz = doc.getroot()

gestores = raiz.findall("features/attributes/GESTION")
observaciones = raiz.findall("features/attributes/OBSERVACIO")
nombres = raiz.findall("features/attributes/NOMBRE")
camas = raiz.findall("features/attributes/CAMAS")
tipos = raiz.findall("features/attributes/TIPO")
ucis = raiz.findall("features/attributes/UCI")

num = raw_input ("Introduce un numero de camas: ")

for i in xrange(0,len(gestores)-1):
	if num <= camas[i].text:
		print nombres[i].text,observaciones[i].text, gestores[i].text, tipos[i].text, ucis[i].text
