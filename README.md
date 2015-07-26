# Analsis Contratos

Analizando + Limpiando datos de contratacion publica.


1. Datos generados con: https://github.com/dav009/contra
2. [Descargar dataset](https://github.com/dav009/contra/blob/master/datos_json_contratos_gov_co.torrent?raw=true)


## Limpieza

1. Limpiear Campos: 
	- Transformar campos a snake case 
	- Unificar campos con nombres difernetes?. i.e: `Nombre ó Razón Social del proponente seleccionado` y `Nombre o Razón Social del Contratista`
	- Formatear fechas a un formato consumible. i.e:  "24 de June      de 2015  10:50 A.M."
	- Formatear locaciones .i.e: `Departamento Y Municipio de Ejecucion: "Huila : La Plata"` => `departamento:"huila", "municipip":"la plata" ` 
	- Formatear montos. i.e: `$12,000,000     Peso Colombiano`  => `12000000`
	- Formatear el campo `Calificación definitiva de los proponentes - Orden de elegibilidad` para extraer los proponentes, y el puntaje.

## Analisis

Algunas:


- Quienes obtineen mas contratos?
- Quienes obtuvieron contratos siempre que fueron oferentes?
- Contrataciones con- oferentes unicos?
- Anomalias en duracion de convocatorias
- Companias fantasmas ( sin mucha informacion en internet) (i.e: fundaciones sin mucho PR con 2/3 contratos gigantes)


R magic..

