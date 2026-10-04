# Taller · Cinco familias en LeetCode

**Curso:** Análisis de algoritmos · ITM · 2026-2

**Lenguaje:** Python 3

| # | Problema | Familia | Evidencia |
| --- | --- | --- | --- |
| 1 | 56. Merge Intervals | Ordenamiento | [Imagen](Capturas/56.%20Merge%20Intervals.png) |
| 2 | 200. Number of Islands | Grafos | [Imagen](Capturas/200.%20Number%20of%20Islands.png) |
| 3 | 1143. Longest Common Subsequence | Programación dinámica | [Imagen](Capturas/1143.%20Longest%20Common%20Subsequence.png) |
| 4 | 435. Non-overlapping Intervals | Greedy | [Imagen](Capturas/435.%20Non-overlapping%20Intervals.png) |
| 5 | 39. Combination Sum | Backtracking | [Imagen](Capturas/39.%20Combination%20Sum.png) |

---

## 56. Merge Intervals

Enlace: https://leetcode.com/problems/merge-intervals/

**Familia:** ordenamiento (ordenamiento por cubetas / *counting sort* sobre `start` + una pasada de fusión)

**Idea:** la clave de ordenamiento es el extremo izquierdo `start`. Como el enunciado garantiza `0 <= start <= end <= 10^4`, no hace falta comparar: se usa un arreglo `max_end` de tamaño `10001` indexado por `start`, donde `max_end[s]` guarda el mayor `end` de los intervalos que empiezan en `s` (`-1` si no hay ninguno). Recorrer ese arreglo de `0` a `10000` ya entrega los intervalos **ordenados por `start`**, sin ningún `.sort()`. En esa misma pasada se mantiene el intervalo «abierto»: si `s <= cur_end` (solape o contacto) se ensancha `cur_end = max(cur_end, max_end[s])`; si no, se cierra el actual y se abre otro.

**Complejidad** (`n` = número de intervalos, `K = 10001` = rango de valores):
- Tiempo: `O(n + K)` (llenar el arreglo + recorrerlo); como `K` es constante por el enunciado, es lineal en `n`. Es más rápido que el `O(n log n)` de un ordenamiento por comparación, pero solo funciona porque los valores están acotados.
- Espacio: `O(K)` por `max_end` más `O(n)` para la salida.

![Captura — Merge Intervals](Capturas/56.%20Merge%20Intervals.png)

---

## 200. Number of Islands

Enlace: https://leetcode.com/problems/number-of-islands/

**Familia:** grafos

**Modelo:** cada celda `'1'` es un **vértice**; hay una **arista** entre dos celdas `'1'` adyacentes en las 4 direcciones (arriba, abajo, izquierda, derecha; sin diagonales). Grafo **no dirigido** e implícito en la grilla. Contar islas = contar **componentes conexas**.

**Idea:** se recorre la grilla; cada vez que aparece un `'1'` no visitado se suma 1 y se lanza un DFS (con pila explícita, para no depender del límite de recursión) que «hunde» la isla completa poniendo sus celdas en `'0'`. Las celdas `'0'` nunca se expanden.

**Complejidad** (`m` filas, `n` columnas):
- Tiempo: **`Θ(m·n)`** (cada celda se visita una vez al barrer y entra a la pila a lo sumo una vez).
- Espacio: `O(m·n)` en el peor caso (pila del DFS); se modifica la grilla in-place como marca de visitado.

![Captura — Number of Islands](Capturas/200.%20Number%20of%20Islands.png)

---

## 1143. Longest Common Subsequence

Enlace: https://leetcode.com/problems/longest-common-subsequence/

**Familia:** programación dinámica

**Estado:** `dp[i][j]` = longitud de la LCS de `text1[0..i)` y `text2[0..j)`.

**Base:** `dp[0][j] = dp[i][0] = 0` (un prefijo vacío no tiene subsecuencia común).

**Recurrencia:**
- si `text1[i-1] == text2[j-1]`: `dp[i][j] = 1 + dp[i-1][j-1]`
- si no: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`

**Respuesta:** `dp[n][m]`, con `n = len(text1)` y `m = len(text2)`.

**Idea:** la tabla de prefijos evita el árbol exponencial de la recursión sin memo, y un greedy de «primera coincidencia» falla. Como la fila `i` solo depende de la `i-1`, se guardan **dos filas**, y se toma como columnas la cadena más corta.

**Complejidad:**
- Tiempo: **`Θ(n·m)`**.
- Espacio: **`Θ(min(n, m))`** (dos filas; la tabla completa serían `Θ(n·m)`).

![Captura — Longest Common Subsequence](Capturas/1143.%20Longest%20Common%20Subsequence.png)

---

## 435. Non-overlapping Intervals

Enlace: https://leetcode.com/problems/non-overlapping-intervals/

**Familia:** greedy (selección de actividades, contada al revés)

**Criterio greedy:** ordenar los intervalos por **`end` creciente** (merge sort propio) y, recorriéndolos, **aceptar el siguiente que no pisa al último aceptado** (`start >= last_end`; si uno termina justo cuando el otro empieza, no hay solape). Entre los que aún caben, se queda con el que **termina antes**, que es el que deja más espacio libre. Maximizar los que se quedan equivale a minimizar los que se borran: respuesta = `n − aceptados`.

**Complejidad** (`n` = número de intervalos):
- Tiempo: **`O(n log n)`** (el sort domina; la pasada greedy es `O(n)`).
- Espacio: `O(n)` (el merge sort propio crea listas auxiliares; `O(1)` extra si se ordenara in-place).

![Captura — Non-overlapping Intervals](Capturas/435.%20Non-overlapping%20Intervals.png)

---

## 39. Combination Sum

Enlace: https://leetcode.com/problems/combination-sum/

**Familia:** backtracking

**Estado de la búsqueda:** `(start, remaining, path)`: índice desde el que se puede tomar, lo que falta para el `target` y la combinación actual.

**Qué se elige:** un `candidates[i]` con `i >= start`, que se agrega a `path` y se baja con `backtrack(i, remaining - c)` (mismo `i`, porque puede reutilizarse). No se vuelve a índices menores, así `[2,2,3]` y `[2,3,2]` no se generan dos veces.

**Qué se deshace:** al regresar de la llamada se hace `path.pop()` y se prueba el siguiente candidato.

**Casos de corte:** `remaining == 0` → se copia `path` a la respuesta; `c > remaining` → poda de esa rama.

**Complejidad** (`n = len(candidates)`, `t = target`, `min` = candidato más pequeño):
- Tiempo: exponencial, cota **`O(n^{t/min})`** (profundidad máxima `t/min`, con hasta `n` ramas por nivel); en el peor caso, además, copiar cada combinación cuesta hasta `O(t/min)`.
- Espacio: `O(t/min)` de pila de recursión y de `path`, más el tamaño de la salida.

![Captura — Combination Sum](Capturas/39.%20Combination%20Sum.png)
