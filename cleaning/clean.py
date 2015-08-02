
# -*- coding: utf-8 -*-
import codecs
import json

from transformations import cleanIdentificacion, cleanProponentes, cleanFecha


class Parser:

	def __init__(self, path):
		self.lines = codecs.open(path, 'r', 'utf-8')

	def parseJson(self, line):
		print(line)
		return json.loads(line)

	def getLines(self):
		return (self.parseJson(line) for line in self.lines)


class FieldSelector:

	@staticmethod
	def fieldSelector(jsonObject, condition):
		return filter( condition, jsonObject.keys())

	@staticmethod
	def fieldContains(jsonObject, word):
		f = lambda key: word.lower() in key.lower()
		return FieldSelector.fieldSelector(jsonObject, f)



class Cleaner:

	def __init__(self, json_object):

		self.lista_de_fechas = [
			"Creación de Proceso",
			"Fecha de Inicio de Ejecución del Contrato",
			"Celebración de Contrato",
			"Fecha de Firma del Contrato"
		]

		self.lista_de_identificaciones = [
			"Identificación del Representante Legal",
			"Identificación del Contratista"
		]

		self.lista_de_precios = [
			"Cuantía Definitiva del Contrato",
			"Cuantía a Contratar"
		]

		self.lista_de_ubicaciones =[
			"País y Departamento/Provincia de ubicación del Contratista",
			"Departamento y Municipio de Ejecución"
		]

		self.lista_de_aplicantes = [
			"Calificación definitiva de los proponentes - Orden de elegibilidad"
		]

		pass

	def clean(self):
		pass


	def cleanIdentifcaciones(self):
		pass

def main():
	Parser("/Users/dav009/contracts_data/10000_entries").getLines()
	for j in Parser("/Users/dav009/contracts_data/10000_entries").getLines():
		keys = FieldSelector.fieldContains(j, u"Creación de Proceso")
		for key in keys:
			print("------")
			print(key)
			#if u"identificación" in key.lower():
			print(j[key])
			print(cleanFecha(j[key]))
			print("---")

main()
