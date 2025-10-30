## Preguntas Ejercicio 4

### 4.1 Diferencias entre regresión lineal y polinómica
La regresión lineal solo busca una recta que se ajuste a los datos. La regresión polinómica permite ajustar curvas (por ejemplo, parábolas, cúbicas…) creando ecuaciones de mayor grado que pueden adaptarse mejor a relaciones no lineales entre las variables.
### 4.2 ¿Para qué se usa la función np.poly() en el código?
En el código realmente se usa np.polyfit() y np.poly1d(), pero sirven para encontrar y definir los coeficientes del polinomio que mejor se adapta (en sentido de mínimos cuadrados) a los datos. Así obtenemos la ecuación matemática óptima del polinomio de grado elegido.
### 4.3 Explica la métrica utilizada para evaluar la calidad de ajuste de cada modelo polinómico
Se utiliza el Error Cuadrático Medio (ECM), que mide la diferencia media al cuadrado entre lo que predice el modelo y los valores reales. Un ECM más bajo significa mejor ajuste.
En  resultados:
ECM grado 3: 9.59
ECM grado 4: 1.54
ECM grado 5: 0.76
### 4.4 Por qué el modelo de grado 5 tiene menos error que los de grado 3 y 4
Porque los polinomios de más grado tienen más flexibilidad y pueden ajustarse mejor a la forma exacta de los datos, “siguiendo” mejor la tendencia y reduciendo el error de predicción sobre esos mismos datos de entrenamiento.
### 4.5 Explica el overfitting o sobreajuste en el contexto del ejemplo.
El overfitting ocurre cuando el modelo de grado alto (como el 5 o más) se ajusta tanto a los puntos de entrenamiento que empieza a “memorizar el ruido” y no generaliza bien para valores nuevos: sería muy preciso en train pero malo en datos que no ha visto. Ojo porque un ECM muy bajo puede indicar sobreajuste si el modelo sigue demasiado los puntos concretos.
### 4.6 ¿Para qué se usa la función np.polyval() en el código? Diferencias con np.poly() ¿Por qué empiezan por np. ambas?
np.polyval() se usa para calcular el valor del polinomio ajustado en cualquier x que le des; básicamente, te da la predicción del modelo.
np.polyfit() y np.poly1d() (no np.poly()) sirven para calcular los coeficientes y definir el polinomio matemáticamente.
Empiezan por np. porque pertenecen a la librería NumPy, utilizada para trabajo con arrays y cálculos matemáticos en Python.
### 4.7 Si siguiésemos aumentando el grado del polinomio del modelo que efectos podrían observarse. ¿Con qué grado te quedarías tú y por qué?
Si aumentas mucho el grado, el polinomio pasará exactamente por todos los puntos pero será muy inestable y hará cosas extrañas fuera de los puntos conocidos (sobreajuste). El ECM de train seguiría bajando pero el modelo sería menos útil para predecir valores nuevos.
Yo elegiría el grado con el que el ECM no solo sea bajo, sino que al graficar el ajuste no presente oscilaciones extrañas y siga la tendencia general: aquí, el grado 4 o 5 parece suficiente porque el ECM baja bastante y el ajuste es bueno sin ser excesivamente complejo.
