# Tarea 1 · Algoritmos greedy en LeetCode

**Estudiante:** Miguel Angel Garcia Perez

**Curso:** Análisis de algoritmos · ITM · 2026-2

Este repositorio contiene la solución de los dos ejercicios pedidos, cada uno
con su código, su criterio greedy explicado y la evidencia de `Accepted` en
LeetCode.


---

## 860. Lemonade Change

- **Enlace:** https://leetcode.com/problems/lemonade-change/
- **Código:** [Codigo\LemonadeChange.py](Codigo\LemonadeChange.py)

**Criterio greedy:** A cada cliente que paga con un billete de 20, se le
prefiere dar el cambio con un billete de 10 y uno de 5 (en vez de tres
billetes de 5), porque el billete de 5 es el único cambio posible para un billete 
de 10. Guardar los billetes de 5 da más posibilidades de atender clientes futuros. 
La decisión se toma cliente por cliente, sin retractarse de cambios ya entregados, 
y si en algún punto no hay cambio posible, la respuesta es `false` de inmediato.

- **Complejidad de tiempo:** `O(n)` — una sola pasada sobre `bills`.
- **Complejidad de espacio:** `O(1)` — solo se guardan dos contadores
  (`five`, `ten`).

![Captura — Lemonade Change](capturas/CapturaLemonadeChange.png)

---

## 455. Assign Cookies

- **Enlace:** https://leetcode.com/problems/assign-cookies/
- **Código:** [codigo/AssignCookies](codigo/AssignCookies.py)

**Criterio greedy:** se ordenan `g` (factores de gula) y `s` (tamaños de
galleta) de menor a mayor, y con dos punteros se asigna al niño menos
exigente restante la primera galleta disponible que le alcance. Nunca
conviene usar una galleta grande en un niño fácil de contentar si existe una
más pequeña que también le sirve, porque eso reduce las opciones para
niños más exigentes sin ganar nada a cambio.

- **Complejidad de tiempo:** `O(n log n + m log m)` — debido al ordenamiento de las dos listas. 
El recorrido con dos punteros es `O(n + m)`, pero queda dominado por el costo del ordenamiento.
- **Complejidad de espacio:** `O(1)` adicional adicional para los dos punteros
(sin contar el espacio que use internamente el algoritmo de ordenamiento).

![Captura — Assign Cookies](capturas/CapturaAssignCookies.png)
