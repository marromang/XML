#!/usr/bin/env python
# -*- coding: utf-8 -*-
#3. Pide la titularidad del centro y muestra el numero que hay y de que tipos son.
from lxml import etree
doc = etree.parse("2015centsanitario.xml")

raiz = doc.getroot()

titulares = raiz.findall("features/attributes/TITULAR")
tiposRaiz = raiz.findall("features/attributes/TIPO")
listaTitulares = []
contador = 0
tipos = []
listaTipos = [ ]

for titu in titulares:
	if titu.text not in listaTitulares:
		listaTitulares.append(titu.text)
print "POSIBLES TITULARES: "
for i in listaTitulares:
	print i

titular = raw_input("Introduce un titular del centro: ")

for i in xrange (0, len(titulares)):
	if titulares[i].text == titular:
		contador = contador + 1
		tip = tiposRaiz[i].text
		if tip not in listaTipos:
			listaTipos.append(tip)

print titular, contador
for e in listaTipos:
	print e		
