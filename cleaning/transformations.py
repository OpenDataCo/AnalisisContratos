import re

def cleanLugar(string):
  """
  i.e: " Valle del  Cauca : Cali"
      => {'departamento': "valle del cauca", "ciudad": "cali"}
  """
  split_str = string.split(":")
  if len(split_str)>1:
    departamento = split_str[0]
    ciudad = split_str[1]

  if len(split_str)==1:
    departamento = split_str[0]
    ciudad = split_str[0]

  departamento = cleanStr(departamento)
  ciudad = cleanStr(ciudad)
  lugar = {"departamento": departamento, "ciudad": ciudad}
  return lugar

def cleanStr(string):
  return string.strip().lower()

def cleanPrecio(precio):
  """
  i.e: "$10,000,123 pesos"
      => "10000123"
  """
  return int(re.findall('\d+', precio.strip().replace("$","").replace(",", ""))[0])

def cleanFecha(fecha):
  """
   i.e 13 de March de 2012
   => {'dia': 13, 'mes':3, 'anio':2012}
  """

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
  try:
    (dia, mes, anio) = re.findall('([\d]+) de ([\w\W]+) de (\d\d\d\d)', fecha)[0]
    dia = int(cleanStr(dia))
    mes = cleanStr(mes)
    mes = int(months_map[mes])
    anio = int(cleanStr(anio))

    date = {"dia":dia, "mes":mes, "anio": anio}

    return date
  except Exception:
    return {"dia":-1, "mes":-1, "anio": -1}


def cleanIdentificacion(identificacion):
  '''
    i.e: "c.c 123456"
    => { "numero": 123456, "tipo":"cc" }
  '''
  try:
    identificacion = identificacion.strip().lower()
    re_cc_and_id = r'\s*([a-z]+)\s*(\d+)\s*'

    match = re.search(re_cc_and_id, re.sub(r'\.|\,', '', identificacion ))
    tipo   = match.group(1)
    numero = int(match.group(2))
    return {"numero": numero, "tipo": tipo}
  except Exception:
    return {"numero": int(identificacion), "tipo": ""}

def cleanProponentes(proponentes):
  return proponentes.split("\r\n")



