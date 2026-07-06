# 📊 CORRIDA PRITI — 2026-07-06 03:47 PT

## Resumen
- **Total activos:** 23
- **EN YARDA (verde):** 4 (↑3) — MATU2656138, CBHU7024789, FFAU2426030, CSNU6323633
- **EN PROCESO (amarillo):** 5 — DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561, CSGU6429436
- **NORMAL/DEGRADADOS:** 2 — EITU9363654, TGBU8815453
- **PRE-ENTRY:** 12 — Sin cambios
- **Excluidos:** 27 (sin cambios)
- **Nuevos agregados:** 0
- **Removidos:** 0

## 🟢 PROMOCIONES ANTI-STALE (Rule #6)
3 contenedores promovidos de NORMAL a EN YARDA:
- **CBHU7024789** (RN-5008507): WMS inYardTime Jul 3 14:31 + DOCK108 + TASK-5307687 NEW. YMS ET-1117841 ELIMINADO.
- **FFAU2426030** (RN-5008480): WMS inYardTime Jul 3 14:31 + DOCK128 + TASK-5307691 NEW. YMS ET-1117840 ELIMINADO.
- **CSNU6323633** (RN-5008483): WMS inYardTime Jul 3 14:31 + DOCK124 + TASK-5307689 NEW. YMS ET-1117846 ELIMINADO.

## 🚨 ALERTAS ACTIVAS
| Alerta | Contenedor | Detalle |
|--------|-----------|--------|
| 🚨 SIN SPOT | MATU2656138 | Gate-in desde Jul 2, sin spot YMS ni receiving task |
| 🚨 YMS ET ELIMINADOS | CBHU/FFAU/CSNU | Promovidos solo por WMS, YMS ETs borrados |
| 🚨 4.5d+ RECIBO | CSGU6429436 | TASK-5306174 activo desde Jul 1 |
| 🚨 PLACEHOLDER YMS | JTAU7362561 | Driver "0000", datos fantasma |
| 🚨 FALSOS GREEN | EITU9363654, TGBU8815453 | YARD_CHECKs FANTASMA corregidos |
| ⚠️ EMPTY REPORTS | DDDU/TCKU/OOCU/JTAU/CSGU | Jonathan reportó empty pero WMS muestra receiving activo |
| ⚠️ SIN GATE-OUT | OOCU5501937 | Desde Jul 2 sin registro de salida |

## Fuentes verificadas
- Outlook (Priti + Rufino/Jonathan reports): ✅
- WMS Entry List + RN status (11 containers): ✅
- YMS/WISE gate-in/out (11 containers): ✅
- WMS Entry List PRE-ENTRY (12 containers): ✅
- Dashboard live feed: ✅ HTTP 200
