import cv2
# Emily Barraza NC = 0025
# Cargar la imagen
imagen = cv2.imread("hipopotamo.jpg")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("No se pudo cargar la imagen.")
    exit()

# Aplicar filtro Gaussiano
imagen_suavizada = cv2.GaussianBlur(
    imagen,
    (7, 7),
    0
)

# Mostrar imágenes
cv2.imshow("Imagen original 0025", imagen)
cv2.imshow("Imagen suavizada 0025", imagen_suavizada)

# Guardar resultado
cv2.imwrite(
    "hipopotamo.jpg",
    imagen_suavizada
)

print("Filtro Gaussiano aplicado correctamente.")
print("Resultado guardado en:")
print("hipopotamo.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()
print("Emily Barraza NC = 0025")


