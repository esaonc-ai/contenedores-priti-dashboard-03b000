# CORRIDA PRITI MONITORING — Jul 7, 2026 02:25 PT

## 🚨 REMOVIDOS (4) — CLOSED/FORCE_CLOSED → excluded

| Container | RN | RecvTask | PutAway | RN Status | Estaba |
|-----------|-----|----------|---------|-----------|--------|
| MATU2656138 | RN-5008572 | TASK-5309505 CLOSED | TASK-5309552 CLOSED | CLOSED | 🟢 EN YARDA (FALSO VERDE) |
| CSGU6429436 | RN-5008479 | TASK-5306174 CLOSED | TASK-5308957 CLOSED | CLOSED | 🟡 EN PROCESO |
| OOCU5501937 | RN-5008506 | TASK-5307688 FORCE_CLOSED | TASK-5309194 CLOSED | FORCE_CLOSED | 🟡 EN PROCESO |
| GN06302026UNIS-1129 (53169) | RN-188031 | TASK-5306175 FORCE_CLOSED | TASK-5306958 CLOSED | FORCE_CLOSED | 🟡 EN PROCESO |

## 📝 ACTUALIZADOS

### EN PROCESO (6 revalidados Jul 7 02:25)
- JTAU7362561 / RN-5008446 — putaway IN_PROGRESS (Daniela Gonzalez)
- ZCSU7124852 / RN-5008586 — recv FORCE_CLOSED, putaway NEW TASK-5309361 (Caren Cubides, 3 LPs)
- TGBU8815453 / RN-5008570 — recv IN_PROGRESS (Daniela Gonzalez)
- CBHU7024789 / RN-5008507 — recv IN_PROGRESS (Daniela Gonzalez)
- FFAU2426030 / RN-5008480 — recv IN_PROGRESS (Daniela Gonzalez)
- CSNU6323633 / RN-5008483 — recv IN_PROGRESS (Daniela Gonzalez)

### PRE-ENTRY (7 actualizados con citas WMS)
- TGBU7180260 / RN-5008591 — WMS cita Jul 7 05:00 (APPT-6032978)
- SMCU1143199 / RN-5008592 — WMS cita Jul 7 08:00 (APPT-6032979)
- TEMU8901490 / RN-5008566 — WMS cita Jul 7 16:00 (APPT-6032735)
- CMAU4986523 / RN-5008593 — WMS cita Jul 8 08:00 (APPT-6032980)
- BMOU6706676 / RN-5008587 — WMS cita Jul 8 09:00 (APPT-6032937)
- EITU9363654 / RN-5008569 — Cita Jul 3 venció hace 4 días. Posible no-show.
- GN07062026UNIS-1134 (TV53560) / RN-188263 — EQP-262460 YMS registrado Jul 7 01:44

## 📊 TOTALS

| | Antes | Después |
|---|-------|---------|
| Activos | 25 | **21** |
| 🟢 EN YARDA | 2 | **1** |
| 🟡 EN PROCESO | 15 | **12** |
| ⚪ PRE-ENTRY | 8 | **8** |
| Excluidos | 32 | **36** |

## 🔥 ALERTAS ROLAS
1. MATU2656138 FALSO VERDE corregido y removido
2. CSGU6429436 completado y removido
3. OOCU5501937 FORCE_CLOSED y removido
4. GN06302026UNIS-1129 FORCE_CLOSED y removido
5. EITU9363654: cita Jul 3 venció hace 4 días. Posible no-show.
6. 6 PRE-ENTRY actualizados con citas WMS confirmadas
7. 6 EN PROCESO revalidados
8. Único EN YARDA: TGBU3785090 SPOT350 — sin falsos verdes

## Guardrails activos
- Anti-estado-viejo: ✅
- Stale state guard: ✅ Jul 7 02:25 PT
- Closed removal: ✅
- Green evidence rule: ✅
- Planned email inclusion: ✅
