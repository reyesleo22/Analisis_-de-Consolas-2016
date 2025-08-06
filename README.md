# 🎮 Análisis de Ventas de Videojuegos

Este proyecto realiza un análisis exhaustivo de las **ventas de videojuegos** utilizando datos históricos 📊. Se exploran tendencias globales y regionales, preferencias de género, impacto de calificaciones y más, con el fin de obtener conclusiones útiles para el mercado gamer 🎯.

---

## 📌 Objetivos del Análisis

- 🔍 Identificar **plataformas** y **géneros** con mayores ventas.
- 🌎 Comparar ventas en diferentes regiones:  
  - América del Norte (NA)  
  - Europa (EU)  
  - Japón (JP)
- 🧪 Probar **hipótesis estadísticas** sobre calificaciones y ventas.
- 📈 Generar **visualizaciones** que respalden las conclusiones del análisis.

---

## 🗂️ Estructura del Repositorio
📁 Análisis-Ventas-Videojuegos/
├── games.csv
├── games_preparados.csv
├── PreparaciondeDatos.py
├── reporte.ipynb
├── .gitignore

### 📄 Archivos Principales

- **`games.csv`**  
  📦 Dataset original con datos crudos sobre videojuegos, plataformas, géneros y ventas por región. Incluye calificaciones de críticos y usuarios.

- **`games_preparados.csv`**  
  🧹 Dataset limpio y transformado mediante `PreparaciondeDatos.py`, listo para análisis en el notebook.

- **`PreparaciondeDatos.py`**  
  ⚙️ Script en Python que realiza la limpieza de datos:  
  - Conversión de tipos  
  - Manejo de nulos  
  - Creación de columnas (como `ventas_totales`)  
  - Exportación del dataset final

- **`reporte.ipynb`**  
  📓 Notebook con el análisis completo:
  - Exploración inicial  
  - Visualización de tendencias  
  - Pruebas estadísticas (como t-tests o ANOVA)  
  - Conclusiones respaldadas con gráficos y tablas

- **`.gitignore`**  
  🚫 Archivos y carpetas ignoradas por Git (e.g., archivos temporales, entornos virtuales, etc.)

---

## 🛠️ Requisitos del Proyecto

Para correr el análisis, asegúrate de tener instaladas las siguientes bibliotecas de Python 🐍:

```bash
pip install pandas matplotlib seaborn scipy
