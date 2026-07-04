# CORRIDA REPORT — Jul 4, 2026 14:22 PT

## Resumen
- **Activos**: 25 (2 green, 7 yellow, 16 normal, 0 red)
- **Excluidos**: 26
- **Verificación**: Outlook + WMS Entry List + YMS + WMS full cross-check

---

## Cambios Aplicados

### 🗑️ 1 REMOVIDO (receiving + putaway CLOSED)
| Contenedor | RN | Razón |
|---|---|---|
| GN07022026UNIS-1133 (53393) | RN-188094 | recv TASK-5307936 FORCE_CLOSED + putaway TASK-5308246 CLOSED |

### 🔻 4 FALSOS GREEN CORREGIDOS → normal
| Contenedor | RN | Razón downgrade |
|---|---|---|
| LabelKing PO8423 | RN-5008450 | Entry List No Data + YMS sin rastro |
| MAWB 00120698274 | RN-5006269 | Entry List No Data + YMS sin rastro (127d+ ABANDONADO) |
| ALNOR04242026 | RN-183707 | Entry List No Data + YMS sin rastro (67d+ ABANDONADO) |
| LabelKing PO8449 | RN-5008571 | Entry List No Data + YMS PRE_ENTRY (NO ha llegado) |

### ✅ 2 GREEN CONFIRMADOS (Entry List + YMS evidence)
| Contenedor | RN | Evidencia |
|---|---|---|
| TGBU3785090 | RN-188086 | Entry List FOUND + YMS drop full SPOT780 |
| MATU2656138 | RN-5008572 | Entry List FOUND + YMS gate check-in (⚠️ SIN SPOT, 39h+) |

### 📝 12 Filas actualizadas con WMS+YMS frescos
Incluye: DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561, CSGU6429436, GN07012026UNIS-1130, GN07012026UNIS-1132, CBHU7024789, FFAU2426030, CSNU6323633, EITU9363654, TGBU8815453

---

## EN YARDA (GREEN) — 2
- TGBU3785090 (RN-188086) — DOCK104 / SPOT780 — Cita Jul 6
- MATU2656138 (RN-5008572) — SIN SPOT ⚠️ — 39h+ esperando

## EN PROCESO (YELLOW) — 7
- JTAU7362561 (RN-5008446) — DOCK65 recv IN_PROGRESS
- CSGU6429436 (RN-5008479) — DOCK68 recv IN_PROGRESS 2d+
- GN07012026UNIS-1130 (RN-188044) — DOCK41 recv IN_PROGRESS
- DDDU5053860 (RN-5008447) — DOCK63 recv IN_PROGRESS
- TCKU6977609 (RN-5008481) — DOCK60 recv IN_PROGRESS
- OOCU5501937 (RN-5008506) — DOCK59 recv IN_PROGRESS
- GN07012026UNIS-1132 (RN-188084) — DOCK107 recv CLOSED / putaway IN_PROGRESS

## PENDIENTES POR LLEGAR (NORMAL) — 16
Incluye 4 recién downgradeados, 3 con Entry List FOUND pero YMS sin confirmar, 2 con YMS PRE_ENTRY, y transfer DN-3236621

---

## 🚨 ALERTAS ROLAS CRÍTICAS

1. **🚨 COOLIFY STUCK** — Live feed muestra datos de Jul 3 20:07 PT (18h+ old). Ambos repos (main + master) actualizados pero Coolify no despliega. El dashboard muestra 4 FALSOS GREEN que ya fueron corregidos en el feed del repo.

2. **🚨 MATU2656138 (RN-5008572)** — 39h+ desde gate check-in (Jul 2 20:11 PT). SIN SPOT, SIN receiving task. Cita Jul 3 20:00 venció.

3. **⚠️ 4 EMPTY reportados por Jonathan Heredia pero WMS contradice** — DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561: Jonathan reporta EMPTY 07/03 pero WMS muestra recv IN_PROGRESS.

4. **⚠️ CSGU6429436** — 2d+ en recibo IN_PROGRESS. Jonathan reportó EMPTY 07/02.

5. **🔴 RN-5006269 + RN-183707 ABANDONADOS** — 127d+ y 67d+ sin progreso. Entry List No Data.

---

## OUTLOOK — Correos monitoreados
- ~27 no leídos (Jul 2-4)
- Jonathan Heredia: receiving progress 2nd shift + 4 vacíos listos 07/03
- Priti Patel: MATU2656138 cambios de cita
- Rufino: MATU2656138 sin RN (resuelto: RN-5008572 creado)
- Jerome Aranda: Fusion transfer DN-3236621
- WISE alerts: sin contenedores específicos

## REPOS
- ✅ `esaonc-ai/contenedores-priti-dashboard-03b000` (main): actualizado, pushed
- ✅ `esaonc-ai/contenedores-priti-dashboard` (master): sincronizado, pushed
- ❌ Coolify: STUCK, no despliega desde ~Jul 3 14:17 PT

## REGLA ENTRY LIST
- **ACTIVA**: Entry List No Data + sin YMS = NO verde
- 4 falsos green corregidos en esta corrida
- Guardrail: `entryListRule: "ACTIVE — Entry List No Data = NO verde"`
