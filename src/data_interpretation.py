# -*- coding: utf-8 -*-
# src/data_interpretation.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
from typing import List, Optional

ICA_ORDER = ['Buena', 'Moderada', 'Dañina para grupos sensibles', 'Muy dañina', 'Peligrosa']
ICA_PALETTE = {
    'Buena': '#2ECC71',
    'Moderada': '#F1C40F',
    'Dañina para grupos sensibles': '#E67E22',
    'Muy dañina': '#E74C3C',
    'Peligrosa': '#8E44AD'
}

DEFAULT_COLS = ['pm2_5','pm10','co','no','no2','o3','so2','nh3']


# -------- 1) Tabla de referencia (exactamente como la tenía) --------
def show_ica_health_table() -> pd.DataFrame:
    ica_health_table = pd.DataFrame({
        'Categoría ICA': ['Buena', 'Moderada', 'Dañina para grupos sensibles', 'Muy dañina', 'Peligrosa'],
        'Rango PM2.5 (µg/m³)': ['0–12', '12.1–35.4', '35.5–55.4', '55.5–150.4', '>150.4'],
        'Impacto en la salud': [
            'Sin efectos visibles',
            'Leve irritación en personas sensibles',
            'Riesgo respiratorio leve',
            'Efectos respiratorios y cardíacos',
            'Riesgo alto para toda la población'
        ]
    })

    return ica_health_table


# -------- 2) Distribución por categoría (usa df_clean['ica_category']) --------
def category_distribution(df_clean: pd.DataFrame, cat_col: str = "ica_category") -> Optional[pd.DataFrame]:
    if cat_col not in df_clean.columns:
        print(" No se encontró la columna 'ica_category'. Asegúrate de ejecutar la sección de procesamiento de datos.")
        return None

    categoria_counts = (
        df_clean[cat_col]
        .value_counts(dropna=False)
        .rename_axis('Categoría')
        .reset_index(name='conteo')
    )
    categoria_counts['porcentaje'] = (categoria_counts['conteo'] / categoria_counts['conteo'].sum()) * 100
    return categoria_counts
