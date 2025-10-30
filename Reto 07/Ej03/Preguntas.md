### Preguntas Ejercicio 3

## 3.1 Diferencia entre regresión lineal simple de ejercicios anteriores y la múltiple de este.
La regresión lineal simple solo utiliza una variable para predecir la salida, así que la relación es de tipo y = a + b·x. En la múltiple, usamos varias variables input (por ejemplo, temperatura, nivel del mar y masa de glaciar a la vez), y la ecuación suma todos los efectos: y = a + b₁·x₁ + b₂·x₂ + b₃·x₃… Esto permite modelar procesos más complejos y realistas.
## 3.2 Ecuación del modelo obtenido. ¿Qué significa el término independiente de la ecuación? (a nivel físico del caso de uso y a nivel matemático)
La ecuación final con tus datos es:
y = 283.87 + 25.93·Temp + 6.07·NivelMar − 1.51·MasaGlaciar
El término independiente (283.87) representa el valor predicho de CO₂ cuando todas las variables de entrada valen cero. A nivel físico es solo una referencia teórica; a nivel matemático es el punto donde la hiperplano corta el eje y.
## 3.3 ¿De cuántas variables de entrada depende la salida? ¿Podríamos hacerlo de una sola? ¿de qué depende?
La salida depende de tres variables: Temp, NivelMar y MasaGlaciar. El modelo podría construirse solo con una variable, pero estaría perdiendo información importante para la predicción. El número de variables adecuadas depende de los datos disponibles y de la relación real entre los fenómenos.
## 3.4 ¿Qué significa que el coeficiente de la masa glaciar sea negativo en este ejercicio?
Significa que, según el modelo, a mayor masa glaciar, menor CO₂ atmosférico. Muestra una relación inversa, que tiene sentido: menos glaciares suele estar relacionado con más CO₂ debido al calentamiento.
## 3.5 Interpreta los valores obtenidos de R^2 en entrenamiento y test
R² entrenamiento = 0.98: El modelo ajusta casi perfectamente los datos con los que aprende; parece que "entiende" la relación dentro del train.

R² test = -5.61: El modelo falla completamente en los datos nuevos/no vistos, incluso peor que predecir la media de y. Esto refleja sobreajuste, falta de representatividad/MUESTRA del test, o que el modelo lineal no capta toda la complejidad.
## 3.6 Al aumentar el número de variables de entrada, ¿qué ventajas e inconvenientes tendría? Por ejemplo, si incluyésemos la deforestación.
Ventajas:

Un modelo con más variables puede captar mejor la realidad si esas variables realmente están relacionadas con y (por ejemplo, temperatura, nivel del mar y masa glaciar afectan todas al CO₂).

Con variables bien seleccionadas, la predicción suele ser más precisa.

Inconvenientes:

Si añades variables que no aportan información relevante, puedes confundir al modelo y empeorar los resultados (ruido, multicolinealidad).

El riesgo de sobreajuste aumenta: el modelo puede ajustarse demasiado a los datos de entrenamiento y fallar en los test (como se ve que ocurre aquí en tu R² test = -5.61).

El modelo se vuelve más difícil de interpretar.
## 3.7 ¿Crees que es adecuada la regresión lineal múltiple para predecir CO2 en este caso? Explica por qué.
No del todo, aunque te da un R² muy alto en entrenamiento (0.98), en test el modelo falla totalmente (R² = -5.61). Esto sugiere que:

O los datos de test son muy diferentes a los de entrenamiento,

O faltan variables clave o el modelo no puede capturar relaciones no lineales,

O hay sobreajuste por exceso de variables o no suficiente variedad/representatividad en los datos.

Por tanto, la regresión lineal múltiple te permite explorar, comparar y aprender, pero para predecir CO₂ en la práctica, aquí no resulta fiable y haría falta revisar el modelo, los datos y las variables utilizadas.
