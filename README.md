# Análisis de Imágenes de Electroforesis

## Descripción

Este paquete en Python permite el análisis de imágenes de electroforesis en gel, proporcionando herramientas para:

- Detección automática de bandas incluso en condiciones de bajo contraste.
- Identificación del marcador de peso molecular y ajuste de curvas en base a su distribución de bandas.
- Asignación automática del peso molecular aproximado de cada banda.
- Construcción automática de dataframes para análisis masivo de datos de imagen.

## Instalación

Para instalar el paquete, clona el repositorio y usa:
```bash
pip install
```

O si está disponible en PyPI:

```bash
pip install nombre_del_paquete
```


## Uso

### Ejemplo básico de uso:
```bash
import EG_Analysis as eg

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

### Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork del repositorio.

2. Crea una nueva rama (git checkout -b nueva-funcionalidad).

3. Realiza tus cambios y haz commit (git commit -m "Descripción del cambio").

4. Envía un pull request.

### Licencia

Este proyecto está bajo la licencia MIT.

