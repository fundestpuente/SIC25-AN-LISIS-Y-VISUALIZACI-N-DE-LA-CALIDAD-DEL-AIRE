# 🌍 Análisis y Visualización de la Calidad del Aire  
**Una exploración de contaminantes atmosféricos y su relación con el PM2.5**

**Curso:** Samsung Innovation Campus – Módulo de Python (Ecuador 2025)  
**Sección:** EC03  
**Carpeta:** `/SIC25-AN-LISIS-Y-VISUALIZACI-N-DE-LA-CALIDAD-DEL-AIRE`

---

## 👥 Integrantes del Grupo
- Josue Malla
- Paul Altafuya
- Vladimir Espinoza 
- Patricio Quishpe

---

## 📝 Descripción del Proyecto
La contaminación atmosférica es uno de los principales desafíos ambientales a nivel mundial, con un gran impacto directo y severo en la salud humana.  
Según la **Organización Mundial de la Salud (OMS)**, la exposición prolongada al aire contaminado provoca más de **7 millones de muertes prematuras cada año**.

Entre los contaminantes más peligrosos se encuentra el **material particulado fino (PM2.5)**, compuesto por diminutas partículas en suspensión con un diámetro menor a 2.5 micrómetros.  
Estas partículas son tan pequeñas que pueden penetrar profundamente en los pulmones, ingresar al torrente sanguíneo e incluso llegar a otros órganos, provocando enfermedades respiratorias y cardiovasculares graves.

El problema radica en que no siempre resulta sencillo comprender cómo otros contaminantes atmosféricos, como el **monóxido de carbono (CO)**, el **óxido nítrico (NO)** o el **dióxido de nitrógeno (NO₂)**, influyen en el incremento del PM2.5.  
Estas interacciones son complejas y dependen de múltiples factores ambientales como el tráfico vehicular, la quema de combustibles fósiles, la temperatura y la humedad del aire.

Frente a esta problemática, el presente proyecto tiene como objetivo desarrollar una **herramienta automatizada de análisis y visualización** que facilite la comprensión de la interacción entre distintos contaminantes y su impacto en la calidad del aire, con especial énfasis en el PM2.5.  
Se combinan técnicas de análisis estadístico, algoritmos y visualización de datos para detectar patrones de contaminación y evaluar el impacto ambiental.

---

## ⚙️ Instrucciones de Instalación y Ejecución

### Requisitos
- **Python 3.13+**
- **Librerías:** incluidas en `requirements.txt`
- **Jupyter Notebook** o **VS Code** con la extensión de Jupyter

---

### 🪜 Pasos de Ejecución

1. **Clonar el repositorio o ubicarte en la carpeta del proyecto:**
   ```bash
   git clone https://github.com/fundestpuente/SIC25-AN-LISIS-Y-VISUALIZACI-N-DE-LA-CALIDAD-DEL-AIRE.git
   cd "SIC25-AN-LISIS-Y-VISUALIZACI-N-DE-LA-CALIDAD-DEL-AIRE"
   ```

2. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
      ```

3. **Abrir el notebook principal:**
   ```bash
   jupyter notebook main.ipynb
      ```
   o directamente desde VS Code con la extensión de Jupyter.

---

## 📂 Estructura del Código (sugerida)
```
ANÁLISIS Y VISUALIZACIÓN DE LA CALIDAD DEL AIRE/
│
├── data/                       # Archivos de datos
│   └── delhiaqi.csv
│
├── graphs/                     # Gráficos generados automáticamente
│   ├── correlated_co_pm25.png
│   ├── correlated_no_pm25.png
│   ├── correlated_pm10_pm25.png
│   ├── correlation_matrix.png
│   ├── heatmap_pm25.png
│   ├── ica_distribution.png
│   ├── time_series_pm25_pm10_co_no_no2.png
│   └── top10_contaminated_days.png
│
├── src/                        # Código fuente de los módulos
│   ├── data_acquisition.py
│   ├── data_interpretation.py
│   └── data_processing.py
│   └── data_visualization.py
│
├── main.ipynb                  # Notebook principal del proyecto
├── requirements.txt            # Dependencias del entorno
├── .gitignore
└── README.md

```

---

## ✅ Herramientas Implementadas
- **Lenguaje:** Python 3.13+
- **Librerías principales:** `pandas, numpy, matplotlib, seaborn`
- **Otras herramientas:** `Jupyter Notebook / VS Code, Git + GitHub`

---

## 🌱 Impacto del Proyecto

Este análisis contribuye a:

- **Concientizar** sobre la contaminación ambiental y sus efectos en la salud.  
- **Visualizar patrones de contaminación** mediante gráficos interpretativos.  
- **Identificar relaciones** entre contaminantes atmosféricos, especialmente aquellos que influyen en el PM2.5.  
- **Fomentar la toma de decisiones basadas en datos**, en beneficio del medio ambiente y la salud pública.  

> “La ciencia no es solo conocimiento; es una herramienta para cambiar el mundo.”  
> — *Carl Sagan*

