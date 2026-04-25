
# Combinatoria

## Principio de Multiplicación - Diagrama de Árbol 

<!-- A - R, C, L - MC, ML, MC, ML, MC, ML - A, B, A, B, A, B, A, B, A, B, A, B -->

<div style="flex: 2;">
  <img src="./img/arbol_horizontal.png" alt="Árbol" width="600">
</div>

La cantidad de opciones bien podría contarse confeccionando un diagrama de árbol o realizando el producto 3 x 2 x 2. Si la situación cuyas posibilidades que se calculan consta de varias etapas de manera tal que en la primera etapa hay "m" opciones, en la segunda hay "n" opciones y en la tercera "p" opciones y así sucesivamente, el número total sería " m x n x p ..."

### Ejemplo 
supongamos que una placa de automóvil consta de 2 letras distintas seguidas de 3 dígitos de los cuales el primero no es cero. ¿Cuántas placas podrían grabarse?

Tomamos 26 letras(sin ñ)
+ Placa: _ _ _ _ _ _
+ LETRA - LETRA(sin repetir) - NUM (no 0) - NUM - NUM

**Posible solución**
 26 x 25 x 9 x 10 x 10 = 585000  

 
## Variaciones

### Problema
 ¿De cuántas formas pueden sentarse 4 personas a,b,c,d en 3 butacas contiguas?

 **Resolución**
 4 x 3 x 2 = 24 (un elemento Excluye al otro).

 Todos los grupos se forman diferente entre sí, no solo por que cambian sus elementos sino también porque cambia el orden en el que se den. No es lo mismo si tenemos a, b, c que c, a, b (se cambió el orden).

 <!-- V(m,n) = m . (m-1) . (m -2) . (m -3) ... (m- (n-1))-->

 \(
V(m,n) = m \cdot (m-1) \cdot (m-2) \cdot (m-3) \cdot \ldots \cdot (m-(n-1))
\)

<!-- V(4,3) = 4 . 3 . 2 = 24 -->

\(
V(4,3) = 4 \cdot (3) \cdot (2) = 24
\)
Hay otra forma
**Relación con Factoriales**
<!-- V(m,n) = m! / (m-n)! -->
<!-- V(4,3) = 4! / (4-3)! -->

\(
V(m,n) = \frac{m!}{(m-n)!}
\)

\(
V(4,3) = 4 \cdot (3) \cdot (2) = 24
\)

\(
V(4,3) = \frac{4!}{(4-3)!} = \frac{24}{1} = 24
\)


### Ejemplo
¿Cuántos números de tres cifras distintas es posible armar con los dígitos del uno 1 al 5?

<!-- V(5,3) = 5 . 4 .3 = 60 -->
+ Número de 3 cifras con dígitos del 1 al 5

`      __       __       __  `
      1 al 5 - 1 al 5 - 1 al 5 

\(
V(5,3) = 5 \cdot (4) \cdot (3) = 60
\)

otra forma: 
\(
V(5,3) = \frac{5!}{(5-3)!} = \frac{5!}{2!}
\)

mismo resultado
\(
V(5,3) = \frac{120}{2} = 60
\)

**Ejemplo B**

\(
V(30,12) = 30 \cdot 29 \cdot 28 \cdot 27 \cdot 26 \cdot 25 \cdot 24 \cdot 23 \cdot 22 \cdot 21 \cdot 20 \cdot 19
\)
`_______________________________`
`12`

\(
V(30,12) = \frac{30!}{(30-12)!} = \frac{30!}{18!}
\)

\( 
\frac{30!}{18!} =  5\,379\,616\,000\,000 
\)


## Permutaciones

¿De cuántas maneras pueden disponerse en fila 3 personas?

en fila a, b, c

``__ __ __ `

3 x 2 x 1


<!-- Pn = n! = n . (n-1) . (n-2) ...-->

\( P_ n = n! = n \cdot (n-1) \cdot (n-2) \cdot \dots \)

El análisis que debemos hace es similar al de las variaciones con la particularidad de que cada grupo que formes está integrado por todos los elementos que tienes para agrupar 

**Ejemplo**

Se quiere conocer la cantidad de maneras en que podemos ordenar 6 libros diferentes en un estante.

\( P_6 = 6! = 720 \)

\( P_n = 6 \cdot 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 720 \)


## Combinaciones 

### Problema

En el Truco ¿Cuántas flores (3 cartas del mismo palo) distintas puedo armar con el 1, 2, 3, 4 y 5 de copas?
<!-- 5 x 4 x 3 x 1 / 3! = 60 / 6 = 10-->

\( \frac{5 \cdot 4 \cdot 3 \cdot 1}{3!} = \frac{60}{3!} = \frac{60}{6} = 10\)

Con las 5 cartas de copas formamos grupos de 3 cartas pero si en cada grupo permutamos los elementos seguiremos teniendo la misma flor. Los grupos difieren entre sí, solo si cambia alguno de sus elementos.

#### Ejemplo

Entre 7 personas se desea elegir 4 de ellas para integrar una comisión ¿Cuántas comisiones distintas se pueden formar?

<!--C = V(7,4) / P4 --> 

\( C = \frac{V(7,4)}{P_4} \)

\( V(7,4) = \frac{7!}{(7-4)!} = \frac{7!}{3!} = 7 \cdot 6 \cdot 5 \cdot 4 = 840 \)

\( P_4 = 4! = 4 \cdot 3 \cdot 2 \cdot 1 = 24 \)

\( C = \frac{840}{24} = 35 \)

## Variación con Repetición

¿Cuántos números de 3 cifras se pueden formar con los dígitos del 5 al 9?

`__ __ __` 

5 x 5 x 5


Puesto que en cada cifra podemos colocar alguno de los 5 dígitos el cálculo que debemos hacer es 5 . 5 . 5. Entre estos 125(5^3) números habrá n que tengan cifras repetidas: 667, 555, 899, etc
<!-- V'(m,n) = m^n -->

\( V'(m,n) = m^n \)

### Ejemplo:  
Se dispone de 2 cajas para ubicar en 3 estantes ¿De cuántas maneras pueden acomodarse?
**Resolución**
\( V'(3,2) = 3^2 = 9 \)

### Ejemplo 2

Se disponen de 3 cajas c1, c2 y c3 para ubicar en 2 estantes ¿Si todas las cajas deben ubicarse, de cuántas maneras pueden acomodarse?

**Resolución**

\( V'(2,3) = 2^3 = 8 \)





