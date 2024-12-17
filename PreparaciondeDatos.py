import pandas as pd
import numpy as np

# Cargar el archivo CSV
input_file = 'games.csv'
output_file = 'games_preparados.csv'

# Leer los datos
df = pd.read_csv(input_file)

# 1. Renombrar las columnas a minúsculas
df.columns = df.columns.str.lower()

# 2. Convertir tipos de datos
# - year_of_release debe ser int (si no es nulo)
# - user_score puede tener "TBD", se manejará como nulo y convertido a float
df['year_of_release'] = pd.to_numeric(df['year_of_release'], errors='coerce').astype('Int64')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')  # TBD se convierte en NaN

# 3. Manejar valores ausentes
# Razonamiento:
# - year_of_release: Sin año, difícil determinar. Se deja en blanco.
# - critic_score, user_score: Valores faltantes se dejan como NaN porque imputarlos podría sesgar análisis.
# - rating: Se deja en blanco ya que no afecta directamente a las ventas.

# Mostrar por qué hay valores ausentes
print("Posibles razones de valores ausentes:")
print("- year_of_release: Juegos antiguos o información perdida.")
print("- critic_score/user_score: Puede que los juegos no hayan sido evaluados.")
print("- rating: Algunos juegos no obtuvieron clasificación oficial.")

# Opcional: llenar valores nulos con valores específicos si es necesario
# Por ejemplo, df['rating'] = df['rating'].fillna('Unknown')

# 4. Calcular las ventas totales (suma de ventas regionales)
df['total_sales'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)

# 5. Exportar el nuevo archivo CSV con los datos preparados
df.to_csv(output_file, index=False)

print(f"Archivo exportado correctamente como '{output_file}'.")
