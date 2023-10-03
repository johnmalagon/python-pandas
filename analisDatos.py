import pandas as pd
# Cargar el archivo de datos
data = pd.read_csv('ruta_del_archivo.csv')
# Visualizar los primeros registros del conjunto de datos
print("Antes de la limpieza:")
print(data.head())
# Eliminar registros duplicados
data = data.drop_duplicates()
# Eliminar valores faltantes
data = data.dropna()
# Realizar otras transformaciones y limpiezas según sea necesario
# ...
# Guardar el conjunto de datos limpio en un nuevo archivo
data.to_csv('ruta_del_archivo_limpo.csv',
index=False)
# Visualizar los primeros registros del conjunto de datos limpio
print("Después de la limpieza:")
print(data.head())
