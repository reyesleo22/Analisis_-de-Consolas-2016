# Análisis de Ventas de Videojuegos

## Descripción del Proyecto
Este proyecto realiza un **análisis exhaustivo** de las ventas de videojuegos utilizando datos históricos. Se investigan las plataformas más rentables, las preferencias por género, las diferencias regionales y el impacto de las calificaciones de críticos y usuarios en las ventas.

El análisis se centra en:
- Identificar plataformas y géneros con mayores ventas.
- Comparar ventas en diferentes regiones: **América del Norte (NA), Europa (UE) y Japón (JP)**.
- Probar hipótesis estadísticas para determinar diferencias significativas en calificaciones y ventas.
- Generar visualizaciones y conclusiones útiles para el mercado de videojuegos.

---

## Estructura del Repositorio

### Archivos Principales:
1. **`games.csv`**:
   - Archivo original con datos crudos sobre videojuegos, plataformas, géneros y ventas.
   - Incluye información regional y calificaciones de usuarios y críticos.

2. **`games_preparados.csv`**:
   - Archivo limpio y preparado después de realizar una transformación de los datos en el archivo `PreparaciondeDatos.py`.
   - Contiene datos listos para el análisis en el Jupyter Notebook.

3. **`reporte.ipynb`**:
   - Notebook de Jupyter que contiene todo el análisis realizado, incluyendo:
     - Exploración inicial de los datos.
     - Visualización de tendencias de ventas por plataforma, región y género.
     - Pruebas de hipótesis estadísticas.
     - Gráficos y tablas para apoyar las conclusiones.
   - El notebook culmina con una **conclusión final** que resume los hallazgos del análisis.

4. **`PreparaciondeDatos.py`**:
   - Script en Python encargado de la limpieza y preparación de los datos.
   - Las operaciones realizadas incluyen:
     - Conversión de tipos de datos.
     - Manejo de valores nulos.
     - Creación de nuevas columnas, como ventas totales.
     - Exportación del archivo `games_preparados.csv`.

5. **`.gitignore`**:
   - Archivo que define los archivos y carpetas que deben ser ignorados por Git.

---

## Requisitos del Proyecto
Para reproducir el análisis, asegúrate de tener instaladas las siguientes bibliotecas de Python:
```bash
pandas
matplotlib
seaborn
scipy
