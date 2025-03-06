from band_analysis import EG_analysis as eg

# Ruta de la imagen a analizar
ruta_imagen = "C:/Users/EGWER/Desktop/prueba_band/PAGE_exp.png"

# Marcador de peso molecular conocido
ladder = [1200,1000,900,800,700,600,500,400,300]

# Abrir imagen usando openCV
imagen_PAGE = eg.open_cv2_image(ruta_imagen, escala_grises=False, show=True)

# Verificar correcta identificación de bandas
imagen_coloreada = eg.verify_correct_gel(ruta_imagen, show=True)

# Función para obtener marcador de peso molecular experimental
ladder_exp = eg.get_exp_ladder(imagen_PAGE)

# Extraer bandas y el número de bandas
band_info = eg.get_band_info(imagen_PAGE)

# Obtener parámetros de la curva de calibración
parameters = eg.get_calib_param(ladder, ladder_exp, ruta_imagen, show=True)

# Anotar cada banda con su peso molecular aproximado
#eg.assign_mol_wei(ruta_imagen, imagen_coloreada,band_info, parameters, show=True)

# Imagen interactiva para seleccionar bandas
#eg.interactive_image(imagen_PAGE, ladder)

# Organizar resultados en excel
#eg.excel_band_results(ruta_imagen, ladder) 