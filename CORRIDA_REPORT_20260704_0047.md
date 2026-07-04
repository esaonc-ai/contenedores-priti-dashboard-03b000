# 🏁 REPORTE FINAL — Corrida Priti/Gurunanda
## Jul 4, 2026 00:47 PT | Tenant LT | Facility LT_F1

---

## 📊 RESUMEN DE CAMBIOS APLICADOS

| Cambio | Detalle |
|---|---|
| **Removido** | RN-188094 (GN07022026UNIS-1133, 53393) → ambos tasks cerrados (recv FORCE_CLOSED + putaway CLOSED) |
| **Degradado** | RN-5008450 GREEN→NORMAL (LabelKing PO8423) — sin evidencia YMS, Entry List "No Data" |
| **Degradado** | RN-5006269 GREEN→NORMAL (MAWB 00120698274) — 123+ días, sin evidencia YMS |
| **Degradado** | RN-183707 GREEN→NORMAL (ALNOR04242026) — 67+ días, sin evidencia YMS |
| **Actualizados** | 25 rows con verificación fresh WMS+YMS+Outlook 00:47 PT |

---

## 📈 ESTADO FINAL DEL DASHBOARD

| Métrica | Antes | Después |
|---|---|---|
| **Activos** | 26 | **25** |
| **Excluidos** | 25 | **26** |
| 🟢 Green | 6 | **3** |
| 🟡 Yellow | 8 | **7** |
| 🔴 Red | 0 | 0 |
| ⚪ Normal | 12 | **15** |

---

## 🟢 EN YARDA (3) — Evidencia YMS confirmada

| Container | RN | Ubicación | Nota |
|---|---|---|---|
| TGBU3785090 | RN-188086 | SPOT780 | YMS gate-in Jul 2 + drop-off. Recv NEW. Cita Jul 6 |
| MATU2656138 | RN-5008572 | SIN SPOT ⚠️ | YMS gate-in Jul 2, huérfano. 36h+ sin atención |
| LabelKing PO8449 | RN-5008571 | DOCK38 | LIVE_DELIVERY anticipado. Recv NEW |

---

## 🟡 EN PROCESO (7)

| Container | RN | Dock | Recv | Putaway |
|---|---|---|---|---|
| DDDU5053860 | RN-5008447 | DOCK63 | IN_PROGRESS (Pedro Avila) | — |
| TCKU6977609 | RN-5008481 | DOCK60 | IN_PROGRESS (Pedro Avila) | — |
| OOCU5501937 | RN-5008506 | DOCK59 | IN_PROGRESS (Pedro Avila) | — |
| JTAU7362561 | RN-5008446 | DOCK65 | IN_PROGRESS (Daniela Gonzalez) | — |
| CSGU6429436 | RN-5008479 | DOCK68 | IN_PROGRESS (Fatima) 2d+ | — |
| 53693 | RN-188044 | DOCK41 | IN_PROGRESS (Caren) | — |
| 53170 | RN-188084 | DOCK107 | CLOSED (Fatima) | IN_PROGRESS (Jorge Franco) |

---

## ⚪ PRE-ENTRY (15)

Incluye 3 degradados (RN-5008450, RN-5006269, RN-183707), 3 falsos green corregidos (CBHU7024789, FFAU2426030, CSNU6323633), 2 citas vencidas (EITU9363654, TGBU8815453), y 7 pendientes normales.

---

## 🚨 ALERTAS ROLAS CRÍTICAS

1. **🔴 COOLIFY NO ESTÁ DESPLEGANDO** — Live feed en `2026-07-03T20:07:00` (~8h stale). GitHub repo correcto (`2026-07-04T00:47:00`). Dashboard muestra datos viejos: RN-188094 sigue en activo, 3 degradados siguen como green.

2. **🔴 MATU2656138/RN-5008572** — 36h+ en yarda SIN SPOT, SIN receiving task. Contenedor huérfano en YMS (sin customer, sin RN en YMS). Cita WMS 20:00 vencida.

3. **🔴 RN-5006269** — 123+ días. Degradado GREEN→NORMAL. Entry List "No Data". Posiblemente ni existe en yarda.

---

## 🟠 ALERTAS ROLAS

4. RN-183707 — 67+ días, degradado, Entry List "No Data"
5. CSGU6429436 — DISCREPANCIA 2d+: recv IN_PROGRESS pero Jonathan reportó EMPTY 07/02
6. 4 EMPTY según Jonathan (DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561) pero recv IN_PROGRESS en WMS
7. EITU9363654 y TGBU8815453 — citas dobles vencidas, no-show
8. CBHU7024789, FFAU2426030, CSNU6323633 — WMS dock+task sin evidencia YMS
9. YMS API bug — múltiples contenedores sin verificación completa
10. RN-5008450 — degradado, falta verificación física DOCK45

---

## 📧 OUTLOOK — Correos NO LEÍDOS

- Jonathan Heredia Jul 3 21:38: EMPTY CONTAINERS (4)
- Jonathan Heredia Jul 3 21:46: 2nd Shift Receiving Progress
- Rufino Jul 3 07:37: MATU2656138 "does not have an RN number"
- Priti Patel: MATU2656138 appointment changes

---

## ✅ REPO STATUS

- **GitHub main/master**: ACTUALIZADO ✅ (commit `460e0de`)
- **Raw JSON**: `lastUpdated: 2026-07-04T00:47:00-07:00` ✅
- **25 activos, 26 excluidos** ✅
- **Coolify Live**: ❌ STALE (2026-07-03T20:07:00, ~8h old)

---

## 🔧 PENDIENTE

**Forzar redeploy Coolify manualmente** — los commits están pusheados a main y master, pero Coolify no está haciendo auto-deploy. El dashboard/feed live sigue mostrando datos de hace 8h. Se requiere intervención manual en Coolify.
