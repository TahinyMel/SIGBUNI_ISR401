# Dataset Zenodo (paquete FAIR) — borrador

Licencia prevista: **CC BY 4.0**.

## Contenido previsto

| Artefacto | Formato | Estado |
|---|---|---|
| Transcripciones anonimizadas | JSON | Pendiente |
| Respuestas de cuestionario | CSV | Pendiente exportación |
| Corpus RF/RNF etiquetado | JSON | Pendiente |
| Matriz de trazabilidad | CSV | Disponible en `/Trazabilidad` |
| Prompts/respuestas LLM | MD/JSON | Carpeta lista |
| Scripts de análisis | Python | Plantilla lista |

## Diccionario de datos (mínimo)

- `rf_id`: identificador del requisito
- `origin`: `human` | `llm`
- `dimension`: completitud | ambiguedad | verificabilidad | correccion | consistencia
- `score`: entero 1–5
- `rater_id`: evaluador anonimizado
- `ev_id`: evidencia fuente cuando aplique

## Citación

Usar `CITATION.cff` del repositorio. Completar DOI tras el depósito en Zenodo.
