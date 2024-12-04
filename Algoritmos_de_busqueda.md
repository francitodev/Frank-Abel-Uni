Búsqueda no informada:  Se centra en los algoritmos de búsqueda que no utilizan información heurística sobre el problema para guiar la búsqueda. 
• Búsqueda en anchura: Explora el espacio de estados nivel por nivel, garantizando encontrar la solución más corta si existe, pero puede ser ineficiente en problemas de gran tamaño.
• Búsqueda en profundidad: Explora un camino hasta el final antes de retroceder y explorar otros caminos.  Puede encontrar soluciones rápidamente, pero corre el riesgo de quedar atrapado en caminos infinitos.
• Búsqueda en profundidad iterativa: Combina las ventajas de la búsqueda en profundidad y en anchura.  Realiza búsquedas en profundidad con profundidades crecientes hasta encontrar una solución.
• Búsqueda de costo uniforme: Expande el nodo con el menor costo acumulado hasta el momento.  Garantiza encontrar la solución de menor costo, pero puede ser ineficiente en algunos casos.
• Análisis de la complejidad de los algoritmos: Se evalúa el tiempo y espacio necesarios para cada algoritmo de búsqueda.


Búsqueda informada:  Introduce algoritmos de búsqueda que utilizan información heurística para guiar la búsqueda hacia soluciones más prometedoras. 
• Búsqueda A*:  Combina la búsqueda de costo uniforme con una heurística para estimar la distancia al objetivo. Es ampliamente utilizado por su eficiencia y garantías de optimalidad bajo ciertas condiciones.
• Búsqueda Greedy: Selecciona el nodo que parece estar más cerca del objetivo según la heurística, sin considerar el costo acumulado. Es rápido pero no garantiza la solución óptima.
• Búsqueda A* con heurísticas admisibles y consistentes: Se discuten las propiedades de las heurísticas y su impacto en la eficiencia y la optimalidad de A*.
• Heurísticas:  Se exploran diferentes maneras de diseñar heurísticas efectivas para problemas específicos.


Problemas de optimización y búsqueda local: Donde el objetivo no es simplemente encontrar una solución, sino la mejor solución posible dentro de un conjunto de opciones. 
• Búsqueda local:  Métodos que exploran el espacio de soluciones iterativamente, mejorando la solución actual mediante movimientos locales.  Ejemplos incluyen escalada de colinas, recocido simulado.
• Algoritmos genéticos: Técnicas inspiradas en la evolución natural para encontrar soluciones óptimas.
• Programación lineal: Posiblemente se introduce como una técnica alternativa a la búsqueda para problemas de optimización.

