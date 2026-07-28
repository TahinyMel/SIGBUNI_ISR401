# Prompt LLM — generación de RF (Enfoque 1)

## Metadatos de replicabilidad

- Modelo: `_completar p.ej. gpt-4o-2024-08-06_`
- Temperatura: `0.2`
- top-p: `1.0`
- top-k: `n/a` (si aplica)
- Semilla: `_completar_`
- Fecha/hora (UTC): `_completar antes de ejecutar_`
- Operador: equipo SIGBUNI

## Prompt exacto

```text
A partir del siguiente material fuente anonimizado sobre el Sistema Inteligente
de Gestión Bibliotecaria Universitaria (SIGBUNI), redacta requisitos funcionales
con los ocho atributos de la plantilla del sílabo:
ID, Nombre, Descripción, Actor principal, Entrada, Proceso, Salida,
Prioridad MoSCoW, Evidencia (usa EV-XX del material cuando exista).

No inventes procesos fuera del material fuente. Produce al menos 50 RF
individuales, numerados RF-LLM-01 en adelante.
---
MATERIAL FUENTE:
<<PEGAR AQUÍ TRANSCRIPCIÓN/HALLAZGOS ANONIMIZADOS>>
```

## Salida

Guardar la respuesta completa en `Experimento/Resultados/` como
`YYYY-MM-DD_llm_rf_setA.json` sin editar el texto generado.
