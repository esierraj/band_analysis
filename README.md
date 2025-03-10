# Análisis de Imágenes de Electroforesis

## Descripción

Este paquete en Python permite el análisis de imágenes de electroforesis en gel, proporcionando herramientas para:

- Detección automática de bandas incluso en condiciones de bajo contraste.
- Identificación del marcador de peso molecular y ajuste de curvas en base a su distribución de bandas.
- Identificación de carriles y asignación automática del peso molecular aproximado de cada banda.
- Construcción automática de dataframes para análisis masivo de datos de imagen de geles de electroforesis.

## Paquete y módulo

El paquete `band_analysis` está compuesto por el módulo llamado `EG_analysis`, que contiene todas las funciones necesarias para el análisis.

## Funciones principales
- `interactive_image`: función para generar una matriz interactiva que muestre el peso molecular aproximado de bandas seleccionadas con el ratón.
- `excel_band_results`: función para generar un dataframe y archivo en excel con el peso molecular aproximado de cada banda, en cada uno de los carriles identificados.
- `get_exp_ladder`: función para obtener las coordenadas en el eje vertical de las bandas del marcador de peso molecular.
- `get_band_info`: función para agrupar pixeles pertenecientes a una misma banda y contar el número total de estas.
- `get_calib_param`: función para realizar una regresión cuadrática a partir de la distribución de bandas en el marcador de peso molecular.
- `assign_mol_wei`: función para marcar cada banda con su peso molecular aproximado.

En el repositorio se incluye el archivo [documentation.md](documentation.md), que aporta una descripción breve de cada función, así como de sus variables de entrada y salida.

## Instalación y uso

Para instalar el paquete con pip:
```bash
pip install band_analysis
```

- En caso de no poder hacer la instalación mediante pip, deberá descargarse el módulo `EG_analysis.py` y colocarlo en el mismo directorio que el script desde el cual deseas ejecutarlo.
- Se recomienda instalar el paquete en un entorno virtual para evitar conflictos de versiones, ya que al instalar `band_analysis` mediante pip, automáticamente se descargará la versión 1.26.4 de NumPy.
- El código puede probarse con la imagen del gel subida al repositorio llamada [electro_gel_test.png](electro_gel_test.png), que tiene bandas en el marcador de peso molecular con los siguientes pesos: 1200, 1000, 900, 800, 700, 600, 500, 400 y 300 bp.

### Ejemplo básico de uso:
```bash
from band_analysis import EG_Analysis as eg

ruta_imagen = "ruta/al/archivo.png"
imagen_PAGE = eg.open_cv2_image(ruta_imagen, escala_grises=False)
ladder = [1200,1000,900,800,700,600,500,400,300]
eg.interactive_image(imagen_PAGE, ladder)
```
## Requisitos

### Este paquete requiere las siguientes dependencias:

- Python 3.8+

- OpenCV

- NumPy

- SciPy

- Matplotlib

Para instalarlas:

```bash
pip install -r requirements.txt
```

## Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork del repositorio.

2. Crea una nueva rama (git checkout -b nueva-funcionalidad).

3. Realiza tus cambios y haz commit (git commit -m "Descripción del cambio").

4. Envía un pull request.

## Licencia
Este proyecto está bajo la licencia MIT.

---
Este paquete facilita la automatización del análisis de geles de electroforesis, asegurando precisión en la detección de bandas y asignación de pesos moleculares. ¡Esperamos que sea de utilidad!

