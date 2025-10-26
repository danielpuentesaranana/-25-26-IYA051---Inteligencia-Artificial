# Reto kNN – Daniel Puente

## Ejercicio 01: Diabetes

### ¿Qué tipo de problema de aprendizaje automático se aborda en este ejercicio y por qué se clasifica así?
Se trata de un problema de aprendizaje supervisado de **clasificación binaria**.  
El objetivo es predecir si una persona tiene o no diabetes (etiqueta 1 o 0) a partir de varios atributos medidos.  
Se clasifica así porque el modelo aprende a partir de ejemplos ya etiquetados y la salida pertenece a una de dos categorías posibles.

---

### ¿Qué representan los 8 atributos de entrada y qué tipo de variable es la etiqueta “Categoría”?
Los 8 atributos de entrada representan características físicas y médicas del paciente:
- Embarazos  
- Glucosa  
- Presión arterial  
- Espesor de piel  
- Insulina  
- IMC  
- Histórico de diabetes (índice de predisposición)  
- Edad  

La etiqueta “Categoría” es una variable **categórica binaria**, donde 0 indica “no diabético” y 1 indica “diabético”.

---

### ¿Por qué es importante dividir el conjunto de datos en entrenamiento y test? ¿Qué proporciones se usan aquí?
Es importante dividir los datos para evaluar la capacidad de generalización del modelo.  
Si se entrenara y evaluara con los mismos datos, no podríamos saber si realmente aprende o solo memoriza.  

En este ejercicio se utiliza una división de **60 % para entrenamiento y 40 % para test**, manteniendo la proporción de clases (estratificación).

---

### ¿Cómo afecta el valor de k en el comportamiento del clasificador kNN?  
¿Qué implicaciones tiene un valor muy bajo o muy alto?  
¿Qué significa que la máxima precisión se obtenga con k = 7?

El valor de k controla cuántos vecinos cercanos se usan para clasificar un nuevo caso:
- Si k es muy bajo (1 o 2), el modelo es muy sensible al ruido y puede sobreajustar.  
- Si k es muy alto, el modelo se vuelve demasiado general y puede infraajustar, perdiendo detalle.  

Que la máxima precisión se obtenga con **k = 7** significa que ese valor logra un equilibrio adecuado entre variabilidad y generalización para este conjunto de datos.

---

### Interpreta la matriz de confusión obtenida. ¿Qué representan los valores VP, VN, FP y FN en el contexto de la diabetes?
La matriz de confusión obtenida para k = 7 fue:

|               | Predicho No (0) | Predicho Sí (1) |
|----------------|-----------------|-----------------|
| **Real No (0)** | 165 (VN)        | 36 (FP)         |
| **Real Sí (1)** | 47 (FN)         | 60 (VP)         |

- **VP (60):** Pacientes con diabetes correctamente identificados.  
- **VN (165):** Pacientes sin diabetes correctamente clasificados.  
- **FP (36):** Pacientes sanos que el modelo predijo erróneamente como diabéticos.  
- **FN (47):** Pacientes con diabetes que el modelo no detectó (riesgo importante en la práctica clínica).

---

### Calcula e interpreta las métricas de precisión, recall y f1-score para cada clase. ¿Qué conclusiones puedes extraer?

| Clase | Precisión | Recall | F1-Score | Soporte |
|--------|------------|---------|-----------|----------|
| 0 (No diabetes) | 0.78 | 0.82 | 0.80 | 201 |
| 1 (Diabetes) | 0.62 | 0.56 | 0.59 | 107 |

**Conclusiones:**  
El modelo distingue mejor a los pacientes sin diabetes que a los que sí la tienen.  
La precisión global (accuracy) ronda el **73 %**.  
El recall bajo de la clase 1 indica que el modelo comete bastantes falsos negativos, lo cual es importante porque en la práctica podría dejar casos sin diagnosticar.

---

### ¿Qué indica el valor del área bajo la curva ROC (AUC = 0.7345) sobre el rendimiento del modelo?
Un **AUC de 0.7345** indica un rendimiento moderado.  
El modelo tiene una capacidad aceptable para distinguir entre pacientes diabéticos y no diabéticos, pero todavía hay margen de mejora (un valor de 1 sería perfecto y 0.5 correspondería al azar).

---

### Si se modifica el porcentaje de datos de test a 20 %, ¿cómo crees que afectaría al modelo?
Con 20 % de test y 80 % de entrenamiento:
- Se dispondría de más datos para aprender, lo que podría mejorar ligeramente el modelo.  
- Sin embargo, el test sería más pequeño, por lo que la evaluación del rendimiento sería menos estable (más dependiente de la muestra concreta).  

En general, el cambio no alteraría mucho el comportamiento global del modelo, pero las métricas podrían variar un poco por la menor cantidad de datos de prueba.

---

### ¿Qué predice el modelo para el nuevo paciente con los atributos dados? ¿Es confiable esta predicción?
Para el paciente con los valores:

**(1, 100, 70, 30, 90, 0.3, 0.2, 45)**  
el modelo con k = 7 predice que **no tiene diabetes (Categoría = 0)**.  

Esta predicción no es totalmente confiable, ya que el modelo tiene un recall bajo para los casos positivos (solo detecta un 56 % de los diabéticos).  
Además, el método kNN depende mucho de la escala de las variables y de la distribución de los vecinos, por lo que es posible que esta predicción sea sensible a pequeñas variaciones en los datos.  
En un contexto médico, siempre se debería usar como apoyo al diagnóstico, no como decisión definitiva.

---

## Ejercicio 02: Botánica

### ¿Qué objetivo persigue el botánico con la aplicación del modelo kNN en este caso?
El objetivo es identificar la **especie de una flor** a partir de sus medidas (longitud y anchura de sépalo y de pétalo).  
Para lograrlo, el botánico usa un modelo kNN que compara las medidas de una flor nueva con las de otras flores ya clasificadas para predecir a qué especie pertenece.

---

### ¿Qué variables componen el conjunto de datos Iris y qué tipo de problema de clasificación se plantea?
El conjunto de datos Iris incluye cuatro variables numéricas:
- Sepal length (longitud del sépalo)  
- Sepal width (anchura del sépalo)  
- Petal length (longitud del pétalo)  
- Petal width (anchura del pétalo)  

La variable objetivo es **“species”**, que puede ser *setosa*, *versicolor* o *virginica*.  
Por tanto, se trata de un **problema de clasificación multiclase supervisado** (tres clases posibles).

---

### Explica cómo se dividen los datos en entrenamiento y test, e interpreta los tamaños obtenidos.
Se usó la función `train_test_split` con una división del **75 % para entrenamiento y 25 % para test**, manteniendo la proporción de clases con `stratify=y`.  

Los tamaños obtenidos fueron:
- Entrenamiento: 112 ejemplos  
- Test: 38 ejemplos  

Es importante que el conjunto de entrenamiento represente bien todas las clases para que el modelo aprenda de forma equilibrada, y que el conjunto de test contenga ejemplos no vistos para poder evaluar la capacidad de generalización.

---

### ¿Por qué en este ejercicio se usa k = 1? ¿Qué ventajas o desventajas tiene frente a otros valores de k?
Se utiliza **k = 1** para que el modelo asigne a cada flor la clase de su vecino más cercano.  

**Ventajas:** detecta bien los patrones locales y puede clasificar con gran precisión cuando las clases están bien separadas.  
**Desventajas:** muy sensible al ruido o a los valores atípicos, y una muestra mal etiquetada puede afectar la predicción.

---

### El modelo obtuvo una precisión del 97 %. ¿Qué nos dice este resultado sobre su rendimiento y posible sobreajuste?
Una precisión del **97 %** indica que el modelo clasifica correctamente casi todos los casos de test, demostrando un muy buen rendimiento.  
Como el dataset Iris es sencillo y las clases están bien diferenciadas, este valor no implica sobreajuste en este contexto.  
Sin embargo, con k = 1 podría ajustarse demasiado si los datos tuvieran ruido o menos separación entre clases.

---

### Analiza cómo el modelo identifica correctamente las especies. ¿Qué variables parecen tener mayor peso en la clasificación?
Las variables que mejor separan las especies son la **longitud y anchura de los pétalos**, especialmente *petal length*, que diferencia claramente a *setosa*.  
Las medidas de los sépalos se solapan más entre *versicolor* y *virginica*, por lo que tienen menor peso en la decisión.

---

### Si se introdujera ruido o valores atípicos en las medidas, ¿cómo afectaría al modelo kNN?
El kNN es muy sensible al ruido.  
Si se añaden valores atípicos, estos pueden alterar las distancias y provocar clasificaciones incorrectas.  
Con k = 1 el problema es más grave, ya que una sola muestra anómala puede cambiar la predicción.  
Usar valores de k mayores o aplicar normalización reduce este efecto.

---

### ¿Qué predice el modelo para la flor con sépalo (7, 3 cm) y pétalo (5, 1 cm)? ¿Cómo interpretarías esta salida?
Para la flor con esas medidas, el modelo predice la especie **setosa**.  
Esto significa que sus dimensiones son más parecidas a las de esa especie.  
Sin embargo, podría haber ambigüedad si las medidas están cerca de los límites entre especies.

---

### ¿Qué mejoras podrías aplicar al modelo para aumentar su generalización o robustez?
- Probar distintos valores de k (3 o 5)  
- Estandarizar o normalizar las variables  
- Usar validación cruzada  
- Visualizar y eliminar *outliers*  

Con estas mejoras, el modelo mantendría una alta precisión y sería más estable frente a variaciones en los datos.
