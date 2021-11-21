# Proyecto de Simulación
> Luis Alejandro Lara Rojas \
> C-412

## Problema:
### 6. Poblado en Evolución:
Se dese conocer la evolución de la población de una determinada región.
Se conoce que la probabilidad de fallecer de una persona distribuye uniforme
y se corresponde, según su edad y sexo, con la siguiente tabla: \
Edad    Hombre  Mujer \
0-12    0.25    0.25  \
12-45   0.1     0.15  \
45-76   0.3     0.35  \
76-125  0.7     0.65

Del mismo modo, se conoce que la probabilidad de una mujer se embarace
es uniforme y está relacionada con la edad: \
Edad    Probabilidad Embarazarce \
12-15   0.2 \
15-21   0.45 \
21-35   0.8 \
35-45   0.4 \
45-60   0.2 \
60-125  0.05

Para que una mujer quede embarazada debe tener pareja y no haber tenido
el número máximo de hijos que deseaba tener ella o su pareja en ese momento.
El número de hijos que cada persona desea tener distribuye uniforme según la
tabla siguiente: \
Número      Probabilidad \
1           0.6 \
2           0.75 \
3           0.35 \
4           0.2 \
5           0.1 \
más de 5    0.05

Para que dos personas sean pareja deben estar solas en ese instante y deben
desear tener pareja. El desear tener pareja está relacionado con la edad: \
Edad    Probabilidad Querer Pareja \
12-15   0.6 \
15-21   0.65 \
21-35   0.8 \
35-45   0.6 \
45-60   0.5 \
60-125  0.2

Si dos personas de diferente sexo están solas y ambas desean querer tener
parejas entonces la probabilidad de volverse pareja está relacionada con la diferencia de edad: \
Diferencia de Edad  Probabilidad Establecer Pareja \
0-5                 0.45 \
5-10                0.4 \
10-15               0.35 \
15-20               0.25 \
20 o más           0.15

Cuando dos personas están en pareja la probabilidad de que ocurra una ruptura distribuye uniforme y es de 0.2. Cuando una persona se separa, o enviuda,
necesita estar sola por un período de tiempo que distribuye exponencial con un
parámetro que está relacionado con la edad: \
Edad    λ \
12-15   3 meses \
15-21   6 meses \
21-35   6 meses \
35-45   1 año \
45-60   2 años \
60-125  4 años 

Cuando están dadas todas las condiciones y una mujer queda embarazada
puede tener o no un embarazo múltiple y esto distribuye uniforme acorde a las
probabilidades siguientes: \
Número de Bebés     Probabilidad \
1                   0.7 meses \
2                   0.18 \
3                   0.08 \
4                   0.04 \
5                   0.02

La probabilidad del sexo de cada bebé nacido es uniforme 0,5.
Asumiendo que se tiene una población inicial de M mujeres y H hombres y
que cada poblador, en el instante incial, tiene una edad que distribuye uniforme
(U(0,100). Realice un proceso de simulación para determinar como evoluciona
la población en un período de 100 años.

## Principales ideas seguidas para la solución del problema:
Para la resolución del problema, la simulación se ha dividido por eventos.

Los eventos principales son: \
. Birth: parto de una mujer embarazada. \
. Birthday: Cumpleaños de una persona. \
. Desease: Fallecimiento de una persona. \
. Relationship: Comienzo de una relación amorosa entre un hombre y una mujer. \
. Pregnancy: Embarazo de una mujer. \
. Breakup: Ruptura de una relación amorosa. \
. After breakup: terminación del tiempo de espera de una persona después de una separación, antes de volver a buscar pareja.

La idea principal de esta simulación es tener en todo momento un conjunto de eventos, donde cada evento tiene su fecha de ejecución, que es el momento en que va a suceder.

Al ejecutarse un evento puede o no desencadenar otros eventos. Por ejemplo: la ejecución del evento Relationship puede desencadenar un evento Pregnancy, y este a su vez desencadena un evento Birth en 9 meses.

El protocolo entonces sería en cada iteración seleccionar del conjunto de eventos el más próximo, ejecutarlo y agregar al conjunto los eventos desencadenados por él. En el momento en que no hayan más eventos o se alcance el tiempo límite se detiene la ejecución.

El archivo a ejecutar sería main.py, en el cual al inicio hay 3 variables globales: \
. women_amount: es la cantidad de mujeres inicial. \
. men_amount: la cantidad de hombres inicial. \
. duration: la cantidad de tiempo máxima de la simulación(en meses).

Por facilidad a la hora de implementar la simulación el tiempo está dado en meses. Por tanto, a la hora de ejecutar la simulación, se imprimirán cada uno de los eventos que vayan ocurriendo en el tiempo. Cada evento mostrará algunas propiedades como el mes en que sucede, las personas involucradas, etc. Luego de los eventos también se imprimen los resultados que son, el total de personas que ha existido, la cantidad de fallecidos y la cantidad de personas vivas al final de la simulación.

## Modelo de Simulación de Eventos Discretos desarrollado para resolver el problema:

### Variables:
#### Tiempo:
t: cantidad de meses transcurridos

#### Contadoras:
CP: cantidad total de personas. \
CF: cantidad de personas fallecidas. \
CS: cantidad de sobrevivientes. \
CH: cantidad de hombres. \
CM: cantidad de mujeres.

#### Estado del sistema:
Por cada persona se almacena: \
. id: identificador de la persona. \
. is_dead: indica si la persona está fallecida. \
. is_male: indica si la persona es hombre o mujer. \
. actual_age: indica la edad de la persona. \
. childs: la cantidad de hijos que tiene. \
. has_couple: indica si tiene pareja. \
. wants_couple: indica si la persona está buscando pareja. \
. expected_childs: la cantidad máxima de hijos que la persona espera.
. is_pregnant: si es mujer y está embarazada. \
. can_get_pregnancy: si es mujer y puede embarazarse.

#### Tipos de evento:
. Birth. \
. Birthday. \
. Desease. \
. Breakup. \
. AfterBreakup.

### Inicialización:
. lista_personas: se va a inicializar una cantidad inicial de personas con edad aleatoria entre 1 y 100, y se van a almacenar en esta lista. \
. lista_eventos: se va a inicializar esta lista con los eventos de fallecimiento y del siguiente cumpleaños de cada una de las personas. \
. t = 0. \
. CH = CH0, donde CH0 es la cantidad inicial de hombres \
. CM = CM0, donde CM0 es la cantidad inicial de mujeres. \
. CP = CM + CH. \
. CF = 0. \
. CS = CP. \
. next_event = min(lista_eventos)

### Si next_event es Birth:
. CP++ \
. Generar la cantidad de hijos. \
. Por cada hijo:
Generar el sexo de la persona,
agregar la persona a lista_personas,
CM++ si es mujer,
CH++ si es hombre,
agregar a lista_eventos el evento Birthday con fecha t + 12. \
. mother.childs++ \
. father.childs++ \
. mother.is_pregnant = False

### Si next_event es Birthday:
. persona.actual_age++ \
. Si la persona no tiene pareja, generar aleatoriamente si quiere pareja, luego si consigue pareja y si se embaraza en caso de ser mujer. \
. En caso de conseguir pareja, generar si hay ruptura o no, y su fecha. Agregar correspondientemente un evento Breakup a lista_eventos. \
. En caso de embarazarse, generar un evento Birth a la lista de eventos con fecha t + 9.

### Si next_event es Desease:
. person.is_dead = True. \
. CF++. \
. CS--. \
. establecer propiedad has_couple en False para esa persona y para su pareja en caso de que tenga alguna relación. \
. Agregar a lista_eventos un evento Breakup con fecha t.

### Si next_event es Breakup:
. establecer propiedad has_couple en False para ambas personas.
. generar un tiempo de espera para buscar nueva pareja, crear un evento AfterBreakup con ese tiempo, y agregar ese evento a lista_eventos.

### Si next_event es After_Breakup:
. generar aleatoriamente si la persona quiere pareja, luego si consigue pareja y si se embaraza en caso de ser mujer. \
. En caso de conseguir pareja, generar si hay ruptura o no, y su fecha. Agregar correspondientemente un evento Breakup a lista_eventos. \
. En caso de embarazarse, generar un evento Birth a la lista de eventos con fecha t + 9. 

## Consideraciones obtenidas a partir de la ejecución de las simulaciones del problema:
Teniendo en cuenta los resultados obtenidos a partir de numerosas simulaciones de una población para diferentes datos de entrada, todos tuvieron un resultado en común, y es que en todos ellos la población disminuye conforme avanza el tiempo. Este resultado se debe en gran parte a la baja cantidad de embarazos que se dan con los datos brindados, sumado a la alta probabilidad de tener pocos hijos(1 o 2) o de fallecer en edades tempranas. \
Esto nos muestra que para que la población aumente sería necesario en gran medida erradicar estas características en una sociedad.

## Enlace al repositorio de github:

https://github.com/LuisLara-UH/discrete-events-simulation