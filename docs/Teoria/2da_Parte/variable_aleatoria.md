# Variable Aleatoria

## Problema 1
Considera el siguiente experimento.
Tiramos un dado y observamos si sale o no 4. Si sale 4 entonces "1" y si no "0"; podemos así definir una función, relacionando a cada resultado del experimento aleatorio con los números 0 y 1.

<img src="/prob/img/diagrama_relacion.jpg" width="500px">

## Problema 2 
El experimento consiste en tirar una moneda 3 veces consecutivas y contar cantidad de caras que se obtienen. Si a cada elemento del espacio muestral que resulta de este experimento, lo asociamos con los números 0, 1, 2 y 3, queda definida una función.

\(
\text{S-S-S} \rightarrow 0
\)

\(
\left.
\begin{aligned}
\text{C-S-S} \\
\text{S-C-S} \\
\text{S-S-C}
\end{aligned}
\right\}
\rightarrow 1
\)

\(
\left.
\begin{aligned}
\text{C-C-S} \\
\text{C-S-C} \\
\text{S-C-C}
\end{aligned}
\right\}
\rightarrow 2
\)

\(
\text{C-C-C} \rightarrow 3
\)

La variable aleatoria "x" es discreta si su recorrido es un conjunto finito o infinito numeral. en cambio si si recorrido puede tomar todos los valores de un cierto intervalo real(infinito NO numerable) se dice que la variable es continua.

## Función de Probabilidad o Distribución de Probabilidad
<!-- P(x=) = 1/8 Reales(x=1) = 3/8 R= (x=2) = 3/8 P(x=3) = 1/8 -->

\( 
P(x=0)=1/8,\;
P(x=1)=3/8,\;
P(x=2)=3/8,\;
P(x=3)=1/8
\)
Probabilida de que sea 0, 1, 2 o 3 en base a las tiradas de probabilidad.
<img src="/prob/img/distribucion_probabilidad.jpg" width="500px">

| x   | 0   | 1   | 2   | 3   |
|-----|-----|-----|-----|-----|
|P(x) | 1/8 | 3/8 | 3/8 | 1/8 |


\(
P(x)=
\begin{cases}
P(x=0)=\dfrac{1}{8} \\
P(x=1)=\dfrac{3}{8} \\
P(x=2)=\dfrac{3}{8} \\
P(x=3)=\dfrac{1}{8}
\end{cases}
\)

La función de probabilidad de x, es una función que le hace corresponder a cada valor tomado por la variable aleatoria un único numero real comprendido en 0 y 1.
Para arribar a la función de probabilidad necesitamos conocer los valores que la variable aleatoria puede tomar y la posibilidad de cada uno de dichos valores. La función de probabilidad satisface las siguientes propiedades

+ \(
0 \leq p(x) \leq 1
\qquad \forall x \in \mathbb{R}(x)
\) Toda probabilidad entre 0 y 1.



+ \(
\sum_{i=1}^{n} P(x_i)=1
\) La sumatoria de probabilidades = 1.
 
 ## Problema 
 En una urna hay 10 bolillas iguales y enumeradas del 0 al 9, de ellas 3 son blancas y 7 son negras. Se extraen 4 bolillas aleatoriamente y se considera la variable aleatoria x: "numero de bolillas negras extraídas", se pide: 
 a. Hallar el recorrido de la función.
 b. Hallar la función de probabilidad de la variable x.
 c. Graficar la función de probabilidad.
 d. Graficar la función de acumulación.

 x "número de bolillas negras extraídas"

### Respuestas

 a. \( R(x) = \{1,2,3,4\} \)

 b. Función de probabilidad


\(
P(x=1)=\dfrac{\binom{7}{1}\binom{3}{3}}{\binom{10}{4}}
=\dfrac{1}{30}
\)

\[
\]

\(
P(x=2)=\dfrac{\binom{7}{2}\binom{3}{2}}{\binom{10}{4}}
=\dfrac{3}{10}
\)

\[
\]

\(
P(x=3)=\dfrac{\binom{7}{3}\binom{3}{1}}{\binom{10}{4}}
=\dfrac{1}{2}
\)

\(
P(x=4)=\dfrac{\binom{7}{4}\binom{3}{0}}{\binom{10}{4}}
=\dfrac{1}{6}
\)

c. 

<img src="/prob/img/funcion_probabilidad.jpg" width="500px">

d. 

\(
\left.
\begin{array}{ll}
-\infty < x \le 1 & 0 \\[8pt]
1 < x \le 2 & \dfrac{1}{30} \\[8pt]
2 < x \le 3 & \dfrac{3}{10} \\[8pt]
3 < x \le 4 & \dfrac{5}{10} \\[8pt]
4 < x \le +\infty & 1
\end{array}
\right\}
F(x)
\)

e. <img src="/prob/img/funcion_acumulacion.jpg" width="500px">