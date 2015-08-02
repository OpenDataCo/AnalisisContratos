import re

def clanLugar(string):
	#Departamento y Municipio de Ejecuci\u00f3n
	split_str = string.split(":")
	if len(split_str)>1:
		departamento = split_str[0]
		ciudad = split_str[1]

	if len(split_str)==1:
		departamento = split_str[0]
		ciudad = split_str[0]

	departamento = cleanStr(departamento)
	ciudad = cleanStr(ciudad)
	return (departamento, ciudad)



def cleanStr(string):
	return string.strip().lower()

def cleanPrecio(precio):
	return int(re.findall('\d+', precio.strip().replace("$","").replace(",", ""))[0])

def cleanFecha(fecha):

	months_map = {

	  "enero": 1,
	  "febrero":2,
	  "marzo":3,
	  "abril":4,
	  "mayo":5,
	  "junio":6,
	  "julio":7,
	  "agosto":8,
	  "septiembre":9,
	  "octubre":10,
	  "noviembre":11,
	  "diciembre":12,
	  "january":1,
	  "february":2,
	  "march":3,
	  "april":4,
	  "may":5,
	  "june":6,
	  "july":7,
	  "august":8,
	  "september":9,
	  "october":10,
	  "november":11,
	  "december":12
	}

	fecha = cleanStr(fecha)
	print("FECHA:")
	print(fecha)
	try:
		(dia, mes, anio) = re.findall('([\d]+) de ([\w\W]+) de (\d\d\d\d)', fecha)[0]
		dia = int(cleanStr(dia))
		mes = cleanStr(mes)
		mes = int(months_map[mes])
		anio = int(cleanStr(anio))

		date = {"dia":dia, "mes":mes, "año": anio}

		return date
	except Exception:
		return {"dia":-1, "mes":-1, "año": -1}
	

def cleanIdentificacion(identificacion):
	try:
		numero = int(re.findall('\d+', identificacion.strip().replace(".","").replace(",", ""))[0])
		tipo = identificacion.split(" ")[0].lower()
		return numero, tipo
	except Exception:
		return None

def cleanProponentes(proponentes):
	print(proponentes.split("\r\n"))


#cleanFecha("assd")

print(cleanPrecio(" $1000,10000 pesos"))