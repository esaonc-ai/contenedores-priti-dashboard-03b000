# CORRIDA PRITI/GURUNANDA — 11:30 PT Jul 7, 2026

**Dashboard:** https://contenedores-priti-dashboard-03b000.coolify.item.pub/
**Feed:** https://contenedores-priti-dashboard-03b000.coolify.item.pub/container-feed.json
**Repo:** esaonc-ai/contenedores-priti-dashboard-03b000
**Ejecutado por:** dynamic-agent-corrida-11-30-PT
**Timestamp:** 2026-07-07T11:30:00-07:00

---

## 📊 RESUMEN

| Métrica | Valor |
|---------|-------|
| **Total Activos** | 22 |
| 🟢 EN YARDA (green) | 2 |
| 🟡 EN PROCESO (yellow) | 7 |
| 📅 PRE-ENTRY (normal) | 13 |
| 🔴 RED | 0 |
| **Total Excluidos** | 44 |
| **Nuevos Excluidos esta corrida** | 4 |
| **Falsos Verdes Corregidos** | 3 |
| **Adiciones Manuales (email)** | 3 |

---

## 🟢 EN YARDA (2)

| Container | RN | Dock | Notas |
|-----------|-----|------|-------|
| GN07062026UNIS-1134 | RN-188263 | DOCK44 | WMS+YMS confirmado. ET-1119085 WINDOW_CHECKED_IN, LIVE_DELIVERY |
| LabelKing07072026 PO8449 | RN-5008571 | DOCK38 | WMS+YMS confirmado. ⚠️ 4 días en yarda sin receive. Cita hoy 17:00 |

## 🟡 EN PROCESO (7)

| Container | RN | Dock | Notas |
|-----------|-----|------|-------|
| GN07012026UNIS-1130 | RN-188044 | DOCK3 | Recv CLOSED, Putaway pendiente. ~30 LPs |
| TGBU3785090 | RN-188086 | DOCK61 | 20K/25K kg recibidos. Glicerina |
| CBHU7024789 | RN-5008507 | DOCK63 | ⚠️ ANOMALÍA sin tasks visibles. Reportado VACÍO |
| FFAU2426030 | RN-5008480 | DOCK60 | OFFLOAD NEW, Caren Cubides |
| CSNU6323633 | RN-5008483 | DOCK65 | OFFLOAD IN_PROGRESS. Reportado VACÍO |
| ZCSU7124852 | RN-5008586 | DOCK45 | Recv CLOSED, Putaway pendiente. 1000KG |
| TGBU8815453 | RN-5008570 | DOCK68 | Recv CLOSED, Putaway IN_PROGRESS. APPT-6032801 CHECKED_IN |

## 📅 PRE-ENTRY (13)

| Container | RN | Cita | Notas |
|-----------|-----|------|-------|
| MRKU9388930 | RN-188088 | Jul 6 16:00 vencida | FALSE GREEN corregido |
| TGBU7180260 | RN-5008591 | Jul 7 05:00 vencida | FALSE GREEN corregido |
| EITU9363654 | RN-5008569 | Jul 3 13:30 vencida | FALSE GREEN corregido |
| TEMU8901490 | RN-5008566 | Jul 7 09:00 vencida | Sin evidencia yarda |
| BMOU6706676 | RN-5008587 | Jul 8 02:00-04:00 | Drop mañana |
| SMCU1143199 | RN-5008592 | Jul 7 01:00-03:00 vencida | Sin gate-in |
| CMAU4986523 | RN-5008593 | Jul 8 01:00-03:00 | Drop mañana |
| FUS07062026UNIS-58 | RN-188264 | — | Nuevo, sin verif. YMS |
| CORR007082026UNIS PO8469 | RN-5008589 | — | Sin verif. WMS |
| CORR007082026UNIS PO8462 | RN-5008588 | — | Sin verif. WMS |
| CMAU8611150 | — | Jul 7 13:00-15:00 | ⚠️ ALERTA: Sin RN. Cita HOY |
| CAAU7998380 | — | Jul 9 01:00-03:00 | Sin RN. UNIS confirmó |
| FUS07072026UNIS-59 | — | Pendiente | Fusion Transfer. RN pendiente |

---

## ❌ NUEVOS EXCLUIDOS (4)

| RN | Container | Motivo |
|----|-----------|--------|
| RN-5008481 | TCKU6977609 | CLOSED Jul 6 17:14 — ciclo completo |
| RN-188048 | GN07012026UNIS-1131 | FORCE_CLOSED Jul 6 15:48 — ciclo completo |
| RN-188084 | GN07022026UNIS-1132 | CLOSED Jul 6 14:42 — ciclo completo |
| RN-187978 | GN06302026UNIS-1126 | CLOSED Jul 3 15:27 — ciclo completo |

---

## 🚨 ALERTAS

| Nivel | Alerta |
|-------|--------|
| 🔴 | **CMAU8611150** — Sin RN en WMS ni appointment YMS. Cita HOY 13:00-15:00 PT (en ~1.5h). UNIS pidió item setup pendiente |
| 🟠 | **Coolify NO ha desplegado** — feed live sigue en versión 11:03 PT. Cambios en GitHub (commit 9fa965d). Requiere redeploy manual |
| 🟡 | **LabelKing 4 días en yarda** sin receive iniciado |
| 🟡 | **3 contenedores reportados VACÍO** por Daniela (CBHU7024789, CSNU6323633, TGBU8815453) |
| 🟡 | **3 citas vencidas** sin gate-in: TEMU8901490 (09:00), SMCU1143199 (01:00), TGBU7180260 (05:00) |

---

## 🛡️ GUARDRAILS

| Guardrail | Estado |
|-----------|--------|
| antiEstadoViejo | ACTIVE — Ajustado: YARD_CHECK no cuenta sin gate-in/Entry List |
| closedRemovalRule | ACTIVE — 4 removals esta corrida |
| plannedEmailInclusionRule | ACTIVE — 6 additions total |
| greenEvidenceRule | ACTIVE — 3 false greens detectados y corregidos |

---

## ⚠️ DEPLOY STATUS

- ✅ **GitHub**: Commits 9fa965d y ef06df1 pusheados a main
- ✅ **JSON válido**: 22 activos, 12 excluidos (array), todos los campos correctos
- ❌ **Coolify Live**: Sirviendo versión 11:03 PT (stale). Docker build pendiente
- 🔧 **Acción requerida**: Redeploy manual en Coolify Dashboard > contenedores-priti-dashboard-03b000 > Force Redeploy
