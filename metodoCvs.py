# Cargar el paquete tidyverse
#library(tidyverse)
# Leer el archivo CSV con los datos
datos <- read_csv("ruta_del_archivo.csv")
# Visualizar las primeras filas del conjunto de
#atos
#head(datos)
# Verificar la estructura de los datos
str(datos)
# Limpiar los datos
# 1. Eliminar filas duplicadas
datos <- distinct(datos)
# 2. Tratar valores faltantes
# Opción 1: Eliminar filas con valores faltantes
datos <- drop_na(datos)
# Opción 2: Rellenar valores faltantes con la media
#de la columna
datos <- datos %>%
    mutate(columna_con_valores_faltantes =
ifelse(is.na(columna_con_valores_faltantes),
mean(columna_con_valores_faltantes, na.rm = TRUE),
columna_con_valores_faltantes))
# 3. Renombrar columnas (si es necesario)
# datos <- rename(datos, nueva_columna = antigua_columna)
# 4. Convertir tipos de datos (si es necesario)
# datos <- mutate(datos, nueva_columna = as.numeric(nueva_columna))
# 5. Filtrar registros según criterios específicos
# datos <- filter(datos, columna > valor)
# Guardar el conjunto de datos limpio en un nuevo archivo CSV
write_csv(datos, "ruta_del_archivo_limpio.csv")
# Resumen estadístico de los datos limpios summary(datos)  
