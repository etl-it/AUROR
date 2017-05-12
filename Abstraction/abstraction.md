
Se quiere una mecanización del chequeo del sistema. Para ello se irán definiendo una serie de bloques, de forma que se irán 
agrupando por módulos el conjunto de todas las verificaciones que el programa es capaz de realizar.


AUROR_TESTS

El núcleo de todo es "CATCHER" [<What 's an Auror? - A dark wizard catcher>,Ron Weasly]. A partir de ahí habrá clases más específicas que heredarán de Catcher. Catcher hereda de Object.

De momento el segundo nivel está constituido por 3 clases : HARDWARE, SOFTWARE y MIX, siendo MIX aquellos tests que se podrían
incluir tanto dentro de los tests de Hardware como de los de Software.

POSIBLES IDEAS A IMPLEMENTAR: 

- MANJEJO DE EXCEPCIONES

- INICIALIZACIÓN DE LOS TESTS : -> Esto más o menos ya se hace (CATCHER- HARDWARE, SOFTWARE, MIX)
     Varios tests utilizan un mismo objeto que debe ser inicializado de una determinada manera para poder realizar los tests
     
     Uso de Factory (especie de clases para Python). Guarda ciertas similitudes con el conecpto de clases abastractas en Java

    
