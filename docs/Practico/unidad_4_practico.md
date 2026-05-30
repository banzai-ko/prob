# Unidad 4

## 65.
Urna: 
    + 7 R
    + 3 B

Se sacan 3 bolas, hallar prob de que las primeras sean rojas y la 3ra blanca
    `__ __ __`

<!-- 7/10 x 6/9 x 3/8 -->
\(
\frac{7}{10}\times\frac{6}{9}\times\frac{3}{8} = \frac{7}{40} = 0.175
\)
probabilidad de que las primeras sean rojas y la 3ra blanca

## 69.
3 Personas esperan el colectivo. H,H,M cuál es la probabilidad
de que la mujer sea la primera o la última en subir a él?
| N | Casos Posibles  | Favorable |
|---|-----------------|-----------|
| 1 | M  - H1 - H2    | Sí        |
| 2 | H1 - M  - H2    | No        |
| 3 | H1 - H2 - M     | Sí        |
| 4 | M  - H2 - H1    | Sí        |
| 5 | H2 - M  - H1    | No        |
| 6 | H2 - H1 - M     | Sí        |

\(
P(A)=\frac{\text{casos favorables}}{\text{casos posibles}}
\)

Probabilidad: \( \frac{4}{6} = \frac{2}{3}\)

## 72.

\(A\) y \(B\) están en paralelo y luego pasan por \(C\) en serie.

Datos:

\(
P(A)=0{,}9; P(B)=0{,}9; P(C)=0{,}8
\)

La probabilidad de que funcionen \(A\) o \(B\) es:

\(
P(A\cup B)=1-(0{,}1)\cdot(0{,}1)
\)

\(
P(A\cup B)=1-0{,}01
\)

\(
P(A\cup B)=0{,}99
\)

Como \(C\) está en serie:

\(
P=0{,}99\cdot0{,}8 = 0{,}792
\)

\(
P=79{,}2\%
\)
Otro:

<!-- (A -B C) + (-A B C) + (A B C) -->
<!-- P= 0,9 . 0,1 . 0,8 + 0,1 . 0.9 . 0.8 + 0,9 . 0,9 . 0,8 = 0,792 -->
\[
\begin{aligned}
P &= (A\overline{B}C)+(\overline{A}BC)+(ABC) \\
  &= (0{,}9\cdot0{,}1\cdot0{,}8)+(0{,}1\cdot0{,}9\cdot0{,}8)+(0{,}9\cdot0{,}9\cdot0{,}8) \\
  &= 0{,}792
\end{aligned}
\]

## 74.
Tiro al blanco:

\(A=\frac{1}{6};\ B=\frac{1}{4};\ C=\frac{1}{3}\)

Hallar la probabilidad p de que exactamente uno de ellos pegue en el blanco

Entonces: 

\(
\overline{A}=1-A=1-\frac{1}{6}=\frac{5}{6}
\)

\(
\overline{B}=1-B=1-\frac{1}{4}=\frac{3}{4}
\)

\(
\overline{C}=1-C=1-\frac{1}{3}=\frac{2}{3}
\)

### Calcular Probabilidad

\(
\begin{aligned}
P &= (\overline{A}\overline{B}C)+(\overline{A}B\overline{C})+(A\overline{B}\overline{C})
\end{aligned}
\)

\(
\begin{aligned}
P &= (\overline{A}\cdot\overline{B}\cdot C)+(\overline{A}\cdot B\cdot\overline{C})+(A\cdot\overline{B}\cdot\overline{C}) \\
  &= \left(\frac{5}{6}\cdot\frac{3}{4}\cdot\frac{1}{3}\right)+\left(\frac{5}{6}\cdot\frac{1}{4}\cdot\frac{2}{3}\right)+\left(\frac{1}{6}\cdot\frac{3}{4}\cdot\frac{2}{3}\right) =\frac{31}{72}
\end{aligned}
\)

<!-- -A-BC + -AB-C + A-B-C -->

## 75.
Proyectil da en el blanco con prob 0,3
¿Cuantos debo disparar para conseguir al menos 80% de prob de dar en el blanco?
Datos:

\(
P(\text{acierto})=0{,}3
\)

\(
P(\text{fallo})=0{,}7
\)
La probabilidad de al menos un acierto en \(n\) disparos es:

\(
P=1-(0{,}7)^n
\)

Se busca:

\(
P\ge0{,}8
\)
### Casos 
Entonces al incrementar n:
\(
n=1 \Rightarrow P=1-(0{,}7)^1=0{,}3
\)

\(
n=2 \Rightarrow P=1-(0{,}7)^2=1-0{,}49=0{,}51
\)

\(
n=3 \Rightarrow P=1-(0{,}7)^3=1-0{,}343=0{,}657
\)

\(
n=4 \Rightarrow P=1-(0{,}7)^4=1-0{,}2401=0{,}7599
\)

\(
n=5 \Rightarrow P=1-(0{,}7)^5=1-0{,}16807=0{,}83193
\)

Rta: Al menos 5c