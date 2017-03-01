# WatchIAOwner

Nuestro proyecto nace, dentro del marco de cyberseguridad en IoT, enfocado al control automatizado y externo de estos dispositivos para detectar posibles ataques 
que puedan sufrir.

El principal problema que observamos es que estos sistemas embebidos cuentan con muy poca capacidad de procesamiento, además de su enorme diversidad, 
por lo que resultaría muy complejo crear software especifico para securizarlos.

Nuestra propuesta se basa en el análisis centralizado de la información que trasmiten y reciben, en este caso a través de una red wifi (podría implementarse 
para cualquier protocolo de comunicaciones), de una manera eficaz y automática (a través de un micro controlador: raspberry pi)

Un rasgo importante, en el que se basa nuestra idea, es que la mayoría de elementos de IoT emiten paquetes que contienen muy poca información o valores, 
y lo hacen dentro de un rango muy concreto. 
 
A través de Scapy, una herramienta de análisis y manipulación de paquetes (con licencia open source), y un script de python, realizamos un sniffing a 
las IP’s de los elementos de IoT que podamos encontrar en nuestra red local. Posteriormente comparamos los paquetes obtenidos con una base de datos de 
paquetes seguros, les aplicamos el algoritmo tlsh (un algoritmo de hashing open source) y procesamos matemáticamente los hash obtenidos para generar 
una variación estadística.

La comparación de los paquetes recibidos con una base de datos seguros (desarrollada por nosotros) tiene como objetivo evitar que la suplantación de 
paquetes se produzca en el primer paso, tras el sniffing.

Del mismo modo, utilizamos un algoritmo de hash para evitar esta suplantación y, por otro lado, para unificar los protocolos de comunicación y tipos 
de datos de los paquetes a analizar, ya que estos son tan diversos como IoT’s existen. 


# Packages you need to run WatchIAOwner
```
scapy
tlsh
math
random
```




