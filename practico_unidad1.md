# Unidad 1 - Datos estadísticos

## 1
Piezas Defectuosas - Piezas rechazadas por lote
|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
| 0 | 7 | 2 | 4 | 1 | 2 | 1 | 5 | 4 | 3 |
| 6 | 2 | 6 | 1 | 0 | 2 | 4 | 7 | 5 | 1 |

elaborar la distribucion de frecuencias para la variable aleatoria discreta

 
#### Conteo

| x (piezas rechazadas) | cantidad |
|-----------------------|----------|
| 0                     | 2        |
| 1                     | 4        |
| 2                     | 4        |
| 3                     | 1        |
| 4                     | 3        |
| 5                     | 2        |
| 6                     | 2        |
| 7                     | 2        |

<!--Data: [2,4,4,1,3,2,2,2] -->
**Total:**  
- n = 20  


#### Distribución de frecuencias

| x | fi | fir  | fir% | Fk  | fkr  | fkr% |
|---|----|------|------|-----|------|------|
| 0 | 2  | 0.10 | 10%  | 2   | 0.10 | 10%  |
| 1 | 4  | 0.20 | 20%  | 6   | 0.30 | 30%  |
| 2 | 4  | 0.20 | 20%  | 10  | 0.50 | 50%  |
| 3 | 1  | 0.05 | 5%   | 11  | 0.55 | 55%  |
| 4 | 3  | 0.15 | 15%  | 14  | 0.70 | 70%  |
| 5 | 2  | 0.10 | 10%  | 16  | 0.80 | 80%  |
| 6 | 2  | 0.10 | 10%  | 18  | 0.90 | 90%  |
| 7 | 2  | 0.10 | 10%  | 20  | 1.00 | 100% |

    Fk = [2, 6, 10, 11, 14, 16, 18, 20 ]
#### Media

Media aritmética = promedio
<!-- n=20 -->
<!-- X= 63 / 20 -->
Total de fallos: (0 + 7 + 2 + 4 + 1 + 2 + 1 + 5 + 4 + 3 + 6 + 2 + 6 + 1 + 0 + 2 + 4 + 7 + 5 + 1)

\( t = 63 \)
\( n = 20 \)
\( \bar{x} = \frac{63}{20} = 3.15 \)


#### Mediana 
ordenar de menos a mayor:
+ Si el número total es impar mediana es elemento central
+ Si es par promedio de elemento central y n +1

entonces:  
| Posición | Fallos |
|----------|--------|
| 1        | 0      |
| 2        | 0      |
| 3        | 1      |
| 4        | 1      |
| 5        | 1      |
| 6        | 1      |
| 7        | 2      |
| 8        | 2      |
| 9        | 2      |
| 10       | 2      | -> 3+2/2
| 11       | 3      |
| 12       | 4      |
| 13       | 4      |
| 14       | 4      |
| 15       | 5      |
| 16       | 5      |
| 17       | 6      |
| 18       | 6      |
| 19       | 7      |
| 20       | 7      |

\(\tilde{x} = \frac{3+2}{2} = \frac{5}{2} = 2.5\)

#### Varianza

##### Tabla resumen para cálculo de varianza

| x (fallos) | fi (lotes) | fi·x | fi·x² |
|------------|------------|------|-------|
| 0          | 2          | 0    | 0     |
| 1          | 4          | 4    | 4     |
| 2          | 4          | 8    | 16    |
| 3          | 1          | 3    | 9     |
| 4          | 3          | 12   | 48    |
| 5          | 2          | 10   | 50    |
| 6          | 2          | 12   | 72    |
| 7          | 2          | 14   | 98    |
| **Totales**| **20**     | **63** | **297** |


##### Fórmulas

Media:


\(
\bar{x} = \frac{\sum f_i \cdot x_i}{n} = \frac{63}{20} = 3.15
\)

**Varianza:**

\(
s^2 = \frac{\sum f_i \cdot x_i^2}{n} - \bar{x}^2
\)

Sustituyendo valores:

\(
s^2 = \frac{297}{20} - (3.15)^2 = 14.85 - 9.9225 = 4.9275
\)


#### Desviación estándar:

\(s = \sqrt{s^2}\)
en este caso

\(
s = \sqrt{4.9275} = 2,219797288
\)


### Gráficos 

#### Frecuencias Absolutas
##### Diagrama de Barras

![Fallas por lote](./img/barras_frecuencia_pco.png)

#### #Histograma

![Fallas por lote](./img/histograma_pco.png)


#### Frecuencias Acumuladas

##### Ojiva

![Ojiva](./img/ojiva_pco.png)

## 2.
Tabla de Pesos, en Kg
|       |       |       |       |       |       |       |       |       |       |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| 92.3  | 94.0  | 94.4  | 95.7  | 96.1  | 96.4  | 97.2  | 97.5  | 97.9  | 98.3  |
| 98.4  | 98.5  | 98.6  | 98.9  | 99.3  | 99.6  | 100.0 | 100.0 | 100.1 | 100.3 |
| 100.5 | 100.7 | 100.8 | 101.1 | 101.2 | 101.5 | 102.1 | 102.5 | 102.9 | 103.8 |


Usamos:

- Límite inferior inicial: \( 92.0 \)
- Tamaño de clase: \( 2.0 \)
- Número total de datos: \( 30 \)

Los intervalos de clase serán:

- \( 92.0 \) a \( <94.0 \)
- \( 94.0 \) a \( <96.0 \)
- \( 96.0 \) a \( <98.0 \)
- \( 98.0 \) a \( <100.0 \)
- \( 100.0 \) a \( <102.0 \)
- \( 102.0 \) a \( <104.0 \)

Número total de datos:

\(
n=30
\)

| Clase | Intervalo (Kg) | \(fi\) | \(fir\) | \(fir\%\) | \(Fk\) | \(fkr\) | \(fkr\%\) |
|-------|----------------|--------|---------|-----------|-------|----------|-----------|
| 1     | 92–94          |  1     | 0.0333  | 3.33%     | 1     | 0.0333   | 3.33%     |
| 2     | 94–96          |  3     | 0.1000  | 10.00%    | 4     | 0.1333   | 13.33%    |
| 3     | 96–98          |  5     | 0.1667  | 16.67%    | 9     | 0.3000   | 30.00%    |
| 4     | 98–100         |  7     | 0.2333  | 23.33%    | 16    | 0.5333   | 53.33%    |
| 5     | 100–102        | 10     | 0.3333  | 33.33%    | 26    | 0.8667   | 86.67%    |
| 6     | 102–104        |  4     | 0.1333  | 13.33%    | 30    | 1.0000   | 100.00%   |

donde:

- \(fi\): frecuencia absoluta.
- \(fir\): frecuencia relativa.
- \(fir\%\): frecuencia relativa porcentual.
- \(Fk\): frecuencia acumulada.
- \(fkr\): frecuencia relativa acumulada.
- \(fkr\%\): frecuencia relativa acumulada porcentual.

donde:

- \(fi\): frecuencia absoluta.
- \(fir\): frecuencia relativa.
- \(fir\%\): frecuencia relativa porcentual.
- \(Fk\): frecuencia acumulada.
- \(fkr\): frecuencia relativa acumulada.
- \(fkr\%\): frecuencia relativa acumulada porcentual.
### Mediana
\(\bar{X} = \frac{\sum}{n}\)
Si
\(
\sum = 2994.3
\)
entonces: 
Con valores exactos
\(\bar{X} = \frac{2994.3}{30} = 99,81\)
Si lo hago con valores agrupados

\(\bar{X} = \frac{2978}{30} = 99,2666\)

### Moda
\(\text{Mo} \)
La fórmula de la moda para datos agrupados es:

\(
\text{Mo} = L_i + \frac{(f_m - f_{m-1})}{(f_m - f_{m-1}) + (f_m - f_{m+1})} \cdot h
\)

donde:

- \(L_i\): límite inferior de la clase modal.
- \(f_m\): frecuencia de la clase modal.
- \(f_{m-1}\): frecuencia de la clase anterior.
- \(f_{m+1}\): frecuencia de la clase siguiente.
- \(h\): amplitud del intervalo.

---

La clase modal es:

\(100\text{–}102\)

porque tiene la mayor frecuencia.

Entonces:

- \(L_i = 100\)
- \(f_m = 10\)
- \(f_{m-1} = 7\)
- \(f_{m+1} = 4\)
- \(h = 2\)

Sustituyendo:

\(
\text{Mo} = 100 + \frac{(10-7)}{(10-7)+(10-4)} \cdot 2 = 100 + \frac{(3)}{(3)+(6)} \cdot 2
\)

Entonces:

\(
\text{Mo} = 100 + \frac{3}{3+6}\cdot2 = 100 + \frac{3}{9}\cdot2
\)

\(
\text{Mo} = 100 + 0.6666
\)

\(
\text{Mo} \approx 100.66
\)

Por lo tanto, la moda agrupada es:

\(
\boxed{100.67\text{ kg}}
\)


3. Frecuecia de Diámetros
