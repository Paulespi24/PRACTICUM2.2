# PRACTICUM2.2
Repositorio para el análisis semántico de carreras universitarias en Ecuador usando NLP con Python y visualización en Power BI. Incluye limpieza de datos, similitud con modelo MiniLM y dashboard interactivo.

# 🧠 Similitud Semántica entre Carreras y Oferta Académica UTPL

Este proyecto analiza la similitud semántica entre las carreras universitarias ofertadas en Ecuador y la oferta académica de la Universidad Técnica Particular de Loja (UTPL), utilizando procesamiento de lenguaje natural (NLP) con Python y visualización interactiva en Power BI.

---

## 📁 Estructura del Proyecto

```
📦 raiz-del-proyecto
├── data/
│   ├── base-datos-abiertos_oferta-academica_05022025.xlsx
│   └── resultado_semantico_mejorado.xlsx
├── src/
│   └── similitud_carreras_utpl.py
├── powerbi/
│   └── dashboard UTPL.pbix
├── docs/
│   ├── Informe_Similitud_Carreras_Tablas.docx
│   └── Capturas/
├── README.md
```

---

## ⚙️ Tecnologías Utilizadas

- Python 3.13
- pandas, openpyxl, sentence-transformers, rapidfuzz
- Modelo NLP: `paraphrase-MiniLM-L6-v2`
- Power BI Desktop
- Dataset SENESCYT (2025) + carreras UTPL

---

## 🧠 Metodología

1. **Limpieza del Dataset**
   - Eliminación de encabezados y filas vacías
   - Estandarización y asignación de identificadores únicos

2. **Cálculo de Similitud Semántica**
   - Modelo `MiniLM` para comparar nombres de carreras con las de la UTPL
   - Asignación de carrera UTPL más similar y score (0 a 100)

3. **Visualización con Power BI**
   - Dashboard con filtros por universidad, modalidad y provincia
   - KPIs, gráficos de barras, matriz de coincidencias y análisis por carrera UTPL

---

## 📊 Dashboard Power BI

- Archivo: `powerbi/dashboard.pbix`
- Páginas del panel:
  - **Resumen General**: KPIs y relación carrera-provincia
  - **Vista Interactiva**: Segmentadores dinámicos y análisis comparativo
  - **Análisis por Carrera UTPL**: Filtro individual y detalle de relaciones

---

## 📂 Archivos Relevantes

| Archivo                                 | Descripción |
|----------------------------------------|-------------|
| `similitud_carreras_utpl.py`           | Código Python principal |
| `resultado_semantico_mejorado.xlsx`    | Dataset final con score y carrera UTPL asignada |
| `dashboard.pbix`                       | Dashboard Power BI |
| `Informe_Similitud_Carreras_Tablas.docx` | Informe técnico del proyecto |
| `base-datos-abiertos_...xlsx`          | Dataset original de SENESCYT |

---

## ✅ Cómo Ejecutar el Código

```bash
# Instalar dependencias
pip install pandas openpyxl sentence-transformers rapidfuzz

# Ejecutar análisis semántico
python src/similitud_carreras_utpl.py
```

> El archivo Excel con resultados será generado en el escritorio o ruta especificada.

---

## 🤝 Contribuciones

Este proyecto fue realizado como parte de un reto académico. Es adaptable para otros análisis semánticos relacionados con educación superior, matching de perfiles, u orientación vocacional.

---

## 📚 Bibliografía

- [SentenceTransformers](https://www.sbert.net/)
- [Power BI Docs](https://learn.microsoft.com/en-us/power-bi/)
