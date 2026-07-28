# SIGBUNI_ISR401

Sistema Inteligente de Gestión Bibliotecaria Universitaria (SIGBUNI) — Entrega 3 (2A) de Ingeniería de Requerimientos (ISR401), Universidad Técnica Estatal de Quevedo.

## Integrantes y roles

| Integrante | Rol |
|---|---|
| Chavarria Cuenca Tahiny Mel | Analista líder / documentación ERS |
| Cedeño Coronado Wilson Lizandro | Coautor / modelado y evidencias |

**Docente:** Ing. Guerrero Ulloa Gleiston

## Enlaces

- Repositorio: https://github.com/TahinyMel/SIGBUNI_ISR401
- ERS/SRS (LaTeX): [`ERS/SIGBUNI_ISR401.tex`](ERS/SIGBUNI_ISR401.tex)
- Bibliografía: [`ERS/referencias.bib`](ERS/referencias.bib)
- Trazabilidad: [`Trazabilidad/matriz_trazabilidad.csv`](Trazabilidad/matriz_trazabilidad.csv)
- Priorización: [`Trazabilidad/priorizacion_moscow_kano.csv`](Trazabilidad/priorizacion_moscow_kano.csv)
- MVP: [`MVP/README.md`](MVP/README.md) (código ejecutable pendiente)
- Experimento: [`Experimento/`](Experimento/) (Enfoque 1 humano vs LLM)
- OSF / Zenodo: pendientes de registro/depósito (no inventar DOI)

## Contenido del repositorio

```
SIGBUNI_ISR401/
  ERS/                 # Documento ERS/SRS (.tex + .bib + images)
  Evidencias/          # Consentimientos, audio, cuestionario, ...
  Modelado/            # UML + mockups Visily
  Trazabilidad/        # CSV matriz y priorización
  MVP/                 # Enlace/instrucciones del producto mínimo
  Experimento/         # Protocolo, prompts, scripts
  Publicacion/         # Dataset FAIR + análisis de revistas
```

## Reproducir el análisis experimental (cuando existan datos)

```bash
cd Experimento/Scripts_Analisis
python3 analyze_quality.py --input ../Resultados/raw_scores.csv --out ../Resultados/
```

## Licencias

- Código del MVP: MIT (cuando se publique el repositorio de código).
- Datos y documentación: Creative Commons Attribution 4.0 International (CC BY 4.0).
