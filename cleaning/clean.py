# -*- coding: utf-8 -*-
import codecs
import json
import argparse

from transformations import cleanIdentificacion, cleanProponentes, cleanFecha, cleanPrecio, cleanProponentes, cleanLugar

class Parser:

	def __init__(self, path):
		self.lines = codecs.open(path, 'r', 'utf-8')

	def parseJson(self, line):
		return json.loads(line)

	def getLines(self):
		return (self.parseJson(line) for line in self.lines)


class FieldSelector:

	@staticmethod
	"""
	retorna las llaves dentro de jsonObject que cumplen la funcion `condicion`

	"""
	def fieldSelector(jsonObject, condition):
		return filter( condition, jsonObject.keys())

	@staticmethod
	"""
	retorna las llaves dentro de jsonObject que contienen la palabra word
	"""
	def fieldContains(jsonObject, word):
		f = lambda key: word.lower() in key.lower()
		return FieldSelector.fieldSelector(jsonObject, f)



class Cleaner:

	def __init__(self, json_object):

		self.json_object = json_object

		self.lista_de_fechas = [
			"Creación de Proceso",
			"Fecha de Inicio de Ejecución del Contrato",
			"Celebración de Contrato",
			"Fecha de Firma del Contrato",
			"Liquidación de Contrato"
		]

		self.lista_de_identificaciones = [
			"Identificación del Representante Legal",
			"Identificación del Contratista"
		]

		self.lista_de_precios = [
			"Cuantía Definitiva del Contrato",
			"Cuantía a Contratar",
			"Valor estimado del contrato",
			"Valor del Contrato",
			"Valor Contrato Interventoría Externa"
		]

		self.lista_de_ubicaciones =[
			"País y Departamento/Provincia de ubicación del Contratista",
			"Departamento y Municipio de Ejecución"
		]

		self.lista_de_aplicantes = [
			"Calificación definitiva de los proponentes - Orden de elegibilidad"
		]

	def cleanList(self, list_of_keys, cleaning_function):
		for i in list_of_keys:
			keys = FieldSelector.fieldContains(self.json_object, i)
			for key in keys:
				self.json_object[key] = cleaning_function(self.json_object[key])

	def clean(self):
		self.cleanList(self.lista_de_fechas, cleanFecha)
		self.cleanList(self.lista_de_identificaciones, cleanIdentificacion)
		self.cleanList(self.lista_de_precios, cleanPrecio)
		self.cleanList(self.lista_de_ubicaciones, cleanLugar)
		self.cleanList(self.lista_de_aplicantes, cleanProponentes)

		return self.json_object


def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("--input")
	parser.add_argument("--output")
	args = parser.parse_args()

	input_arg = args.input
	output_arg = args.output 

	out = codecs.open(output_arg, 'w', 'utf-8')
	counter = 0 
	for j in Parser(input_arg).getLines():
		counter = counter + 1
		print(str(counter)+"\r")
		cleaned_j = Cleaner(j).clean()
		out.write(json.dumps(cleaned_j)+"\n")
	out.close()

if __name__ == "__main__":
	main()

