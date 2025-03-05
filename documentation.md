# Documentación de funciones del módulo EG_analysis

## Funciones principales

### 1. `open_cv2_image`

**Descripción:**
Carga una imagen de electroforesis en gel en formato PNG usando OpenCV.

**Parámetros:**
- `ruta_imagen` (str): Ruta de la imagen a cargar.
- `escala_grises` (bool, opcional): Si es `True`, carga la imagen en escala de grises. Por defecto, `False`.

**Retorna:**
- `imagen` (numpy.ndarray): Imagen cargada en formato OpenCV.

---

### 2. `resize_image`

**Descripción:**
Redimensiona una imagen reduciendo su tamaño en un porcentaje determinado.

**Parámetros:**
- `ruta_imagen` (str): Ruta de la imagen a cargar.
- `porcentaje_reduccion` (float, opcional): Porcentaje de reducción del tamaño (0 a 100). Por defecto, `0`.

**Retorna:**
- `imagen_redimensionada` (numpy.ndarray): Imagen redimensionada en formato OpenCV.

---

### 3. `get_new_name`

**Descripción:**
Genera un nuevo nombre de archivo basado en la ruta original, agregando un sufijo y cambiando el formato si es necesario.

**Parámetros:**
- `ruta_original` (str): Ruta completa del archivo original, incluyendo su nombre y extensión.
- `sufijo` (str, opcional): Texto adicional agregado antes de la extensión. Por defecto, `"_modificada"`.
- `formato` (str, opcional): Nueva extensión del archivo (ejemplo: `".png"`, `".xlsx"`). Por defecto, `".png"`.

**Retorna:**
- `nueva_ruta` (str): Nueva ruta del archivo con el sufijo y formato especificado.

---

### 4. `get_exp_ladder`

**Descripción:**
Extrae las posiciones verticales de las bandas del ladder experimental en una imagen de electroforesis.

**Parámetros:**
- `imagen_cv2` (numpy.ndarray): Imagen en formato OpenCV.

**Retorna:**
- `ladder_exp` (list): Lista de coordenadas Y correspondientes a las bandas detectadas en el ladder experimental.

---

### 5. `get_band_info`

**Descripción:**
Procesa una imagen de electroforesis para detectar y segmentar bandas mediante umbralización de Otsu y análisis de componentes conectados.

**Parámetros:**
- `imagen_cv2` (numpy.ndarray): Imagen en formato OpenCV.

**Retorna:**
- `band_info` (tuple): Tupla con:
    - `num_labels` (int): Número total de bandas detectadas (incluyendo el fondo).
    - `labels` (numpy.ndarray): Matriz de etiquetas donde cada píxel está asignado a un componente identificado.

### 6. `verify_correct_gel`

**Descripción:**
Verifica si una imagen de electroforesis en gel es válida, segmentando las bandas y resaltando sus centros con colores.

**Parámetros:**
- `ruta_imagen` (str): Ruta del archivo de imagen que se analizará.

**Retorna:**
- `imagen_coloreada` (numpy.ndarray): Imagen procesada con bandas coloreadas y centros de masa resaltados.

---

### 7. `get_calib_param`

**Descripción:**
Calcula los parámetros de calibración para la estimación del peso molecular ajustando una curva cuadrática a los datos experimentales.

**Parámetros:**
- `ladder` (list): Lista con los valores teóricos del peso molecular del marcador.
- `ladder_exp` (list): Lista con las posiciones experimentales del marcador en el gel.
- `ruta_imagen` (str): Ruta de la imagen asociada al gel de electroforesis.

**Retorna:**
- `parametros` (tuple): Tupla con los coeficientes óptimos `(a, b, c)` del ajuste cuadrático.

---

### 8. `assign_mol_wei`

**Descripción:**
Asigna un peso molecular a cada componente identificado en la imagen de electroforesis, colorea las bandas y etiqueta cada banda con el peso molecular estimado.

**Parámetros:**
- `ruta_imagen` (str): Ruta de la imagen original utilizada para la anotación.
- `imagen_coloreada` (numpy.ndarray): Imagen donde se asignarán los colores a las bandas detectadas.
- `band_info` (tuple): Tupla con el número total de etiquetas (`num_labels`) y la matriz de etiquetas (`labels`).
- `parametros` (tuple): Tupla con los coeficientes `(a_opt, b_opt, c_opt)` de la función cuadrática para estimar el peso molecular.

**Retorna:**
- `imagen_texto` (numpy.ndarray): Imagen con las bandas coloreadas y los pesos moleculares etiquetados.

---

### 9. `interactive_image`

**Descripción:**
Abre una imagen de electroforesis interactiva donde, al hacer clic en una banda, se muestra su peso molecular estimado.

**Parámetros:**
- `imagen_cv2` (numpy.ndarray): Imagen del gel de electroforesis, previamente cargada.
- `ladder` (list): Lista con los valores teóricos del peso molecular del marcador.

**Retorna:**
- Imagen interactiva donde, al hacer clic en una banda, se muestra su peso molecular estimado.

---

### 10. `listas_a_diccionario`

**Descripción:**
Convierte una lista de listas de tuplas en un diccionario ordenado.

**Parámetros:**
- `lista_de_listas` (list): Lista que contiene sublistas de tuplas `(x, y)`.

**Retorna:**
- `diccionario_ordenado` (dict): Diccionario con claves en orden ascendente.

---

### 11. excel_band_results(ruta_imagen, ladder)

**Descripción:**
Analiza una imagen de electroforesis en gel y genera un archivo Excel con las bandas detectadas, asignando pesos moleculares a cada columna.

**Parámetros:**  
- **ruta_imagen (str)**: Ruta de la imagen a analizar.  
- **ladder (list)**: Lista con los valores teóricos del peso molecular del marcador.  

**Retorna:**
- Se genera un archivo Excel con los pesos moleculares calculados para cada banda en las diferentes columnas del gel.


---

 


