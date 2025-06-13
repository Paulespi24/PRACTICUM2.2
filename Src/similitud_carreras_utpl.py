import pandas as pd
from sentence_transformers import SentenceTransformer, util

# === CARGA DEL ARCHIVO ===
archivo_excel = r"C:\Users\Usuario iTC\Downloads\base-datos-abiertos_oferta-academica_05022025.xlsx"
df = pd.read_excel(archivo_excel, skiprows=10)
columnas_validas = df.iloc[2].tolist()
df_limpio = df.iloc[3:].copy()
df_limpio.columns = columnas_validas
df_limpio.dropna(how='all', inplace=True)
df_limpio.reset_index(drop=True, inplace=True)

# === AGREGAR COLUMNAS DE ORIGEN ===
df_limpio["ID_CARRERA_ORIGEN"] = ["CAR{:03}".format(i+1) for i in range(len(df_limpio))]
df_limpio["UNIVERSIDAD_ORIGEN"] = df_limpio["NOMBRE_IES"]
df_limpio["CARRERA_ORIGEN"] = df_limpio["NOMBRE_CARRERA"]

# === LISTA REAL DE CARRERAS UTPL ===
carreras_utpl = [
    "Administración de Empresas", "Agronegocios", "Agropecuaria", "Alimentos", "Arquitectura",
    "Artes Escénicas", "Artes Visuales", "Biología", "Bioquímica y Farmacia", "Ciencias Políticas y Relaciones Internacionales",
    "Computación", "Comunicación", "Contabilidad y Auditoría", "Derecho", "Economía", "Educación Básica",
    "Educación Inicial", "Enfermería", "Finanzas", "Fisioterapia", "Gastronomía", "Geología", "Gestión Ambiental",
    "Ingeniería Ambiental", "Ingeniería Civil", "Ingeniería Industrial", "Ingeniería Química", "Logística y Transporte",
    "Medicina", "Nutrición y Dietética", "Pedagogía de la Lengua y la Literatura",
    "Pedagogía de las Ciencias Experimentales (Pedagogía de la Química y Biología)",
    "Pedagogía de las Ciencias Experimentales (Pedagogía de las Matemáticas y la Física)",
    "Pedagogía de los Idiomas Nacionales y Extranjeros", "Pedagogía en Ciencias Sociales y Humanidades",
    "Psicología", "Psicología Clínica", "Psicopedagogía", "Redes y Analítica de Datos",
    "Seguridad y Salud Ocupacional", "Tecnologías de la Información", "Telecomunicaciones", "Turismo"
]

# Crear contexto para UTPL
df_utpl = pd.DataFrame({
    "ID_CARRERA_UTPL": [f"CARUTPL{i+1:03}" for i in range(len(carreras_utpl))],
    "CARRERA_UTPL": carreras_utpl
})
df_utpl["CONTEXTUAL_UTPL"] = "Carrera universitaria en " + df_utpl["CARRERA_UTPL"]

# === CARGAR MODELO ===
modelo = SentenceTransformer("paraphrase-MiniLM-L6-v2")
embeddings_utpl = modelo.encode(df_utpl["CONTEXTUAL_UTPL"].tolist(), convert_to_tensor=True)

# === FUNCIÓN DE SIMILITUD CON CONTEXTO ===
def similitud_con_contexto(carrera):
    contexto = f"Carrera universitaria en {str(carrera)}"
    emb = modelo.encode(contexto, convert_to_tensor=True)
    scores = util.cos_sim(emb, embeddings_utpl)[0]
    idx = scores.argmax().item()
    return pd.Series([
        df_utpl.loc[idx, "ID_CARRERA_UTPL"],
        df_utpl.loc[idx, "CARRERA_UTPL"],
        round(scores[idx].item() * 100)
    ])

# === APLICAR ===
df_limpio[["ID_CARRERA_UTPL", "CARRERA_SIMILAR_UTPL", "SCORE_SIMILITUD"]] = df_limpio["CARRERA_ORIGEN"].apply(similitud_con_contexto)

# === GUARDAR ===
df_limpio.to_excel(r"C:\Users\Usuario iTC\Desktop\resultado_semantico_mejorado.xlsx", index=False)
print("[OK] Resultado con contexto guardado en el escritorio.")
