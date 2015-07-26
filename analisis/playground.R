# path a: http://d3kbcqa49mib13.cloudfront.net/spark-1.4.1-bin-hadoop2.6.tgz
spark_path <- ="/Users/dav009/Downloads/spark_home4"
driver_memory <- "12g"
path_to_contracts_data <-  "/Users/dav009/contracts_data/contract_data_july_28_2015_cleaned.json"
# Setting up Spark

Sys.setenv(SPARK_HOME=spark_path)
Sys.setenv(SPARK_MEM=driver_memory)
.libPaths(c(file.path(Sys.getenv("SPARK_HOME"), "R", "lib"), .libPaths()))

# Initializing Spark
library(SparkR)
sc <- sparkR.init(master="local[8]")
sqlContext <- sparkRSQL.init(jsc = sc)
contratos <- read.df(sqlContext, path_to_contracts_data, "json") 
registerTempTable(contratos, "contratos")
contratos_nombres <- SparkR:::sql(sqlContext, "SELECT `Cuantía Definitiva del Contrato` as cuantia, `Nombre o Razón Social del Contratista` as nombre FROM contratos ")

library(dplyr)
library(ggplot2)

contratos_nombres <- SparkR:::collect(contratos_nombres)

trim <- function (x) gsub("^\\s+|\\s+$", "", x)

library(stringr)
cleanPrecio <- function(precio){
  strtoi(trim(gsub("Peso Colombiano", "", gsub("\\$","",gsub(",", "", precio)))))
}

cleanName <- function(name){
  toupper(str_trim( iconv(name,"WINDOWS-1252","UTF-8")))
}



datos_limpios<-dplyr:::mutate(contratos_nombres, 
                    nombre_limpio = cleanName(`nombre`) ,
                    #segmento_limpio = cleanName(`Segmento`),
                     precio = cleanPrecio(`cuantia`))

head(datos_limpios)



grouped_by_nombre = dplyr::group_by(datos_limpios, nombre_limpio)
totales <- dplyr::summarise(grouped_by_nombre,
                   count = n(),
                   total = sum(precio, na.rm = TRUE))



totales <- dplyr::filter(totales, grepl( "FUNDACION",totales$nombre))
totales <- dplyr::filter(totales, totales$count<10000)
totales <- dplyr::filter(totales, totales$count>10)
head(totales)
nrow(totales)


ggplot(data=totales, aes(x=nombre_limpio, y=count)) +
  geom_point(alpha=.4, aes(size=total), color="#880011") +theme(axis.text.x=element_text(angle=90,hjust=1,vjust=0.5))  #+ facet_grid(Segmento ~ .)



