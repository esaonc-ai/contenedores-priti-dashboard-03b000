# 📊 CORRIDA COMPLETA — Contenedores Priti en Yarda
**Fecha/Hora:** Domingo 5 Julio 2026, 02:30 AM PT  
**Agente:** Agente Priti Contenedores  
**Repositorio:** esaonc-ai/contenedores-priti-dashboard-03b000  
**Dashboard Live:** https://contenedores-priti-dashboard-03b000.coolify.item.pub/

---

## 📋 RESUMEN

| Métrica | Valor |
|---|---|
| **Total activos** | **25** |
| 🟢 EN YARDA | 8 |
| 🟡 EN PROCESO | 7 |
| 📅 PRE-ENTRY | 9 |
| 📋 TRANSFER | 1 |
| **Excluidos** | 26 |
| **Nuevos agregados** | 0 |
| **Promociones a EN YARDA** | 0 |
| **Promociones a EN PROCESO** | 0 |
| **Removidos (ambos tasks cerrados)** | 0 |
| **Actualizaciones menores** | 2 (assignee + LP count) |

---

## 🔄 CAMBIOS APLICADOS

| # | Contenedor | Cambio | Antes | Después | Razón |
|---|---|---|---|---|---|
| 1 | JTAU7362561 (RN-5008446) | assignedTo | Daniela Gonzalez | **Pedro Avila** | WMS fresh: TASK-5307533 asignado a Pedro Avila |
| 2 | GN07012026UNIS-1132 (RN-188084) | LPs | 31 | **33** | WMS fresh: putaway TASK-5307890 33 LPs procesados |

---

## ✅ VERIFICACIONES POR FUENTE

### Outlook (outlook-agent)
- 17 contenedores en correos recientes (Priti + Rufino + Jonathan)
- TODOS ya registrados en el dashboard
- 0 contenedores nuevos por agregar
- Jonathan reportó EMPTY para 4 contenedores (JTAU7362561, DDDU5053860, TCKU6977609, OOCU5501937) pero WMS contradice

### WMS (wms-agent)
- 24/24 RNs confirmados con cliente **GURUNANDA, LLC** (ORG-655875) ✅
- 7 EN PROCESO: 6 con recv IN_PROGRESS + 1 con recv CLOSED/putaway IN_PROGRESS
- 8 EN YARDA: todos IMPORTED con task NEW y Entry List DATA
- 9 PRE-ENTRY: todos IMPORTED sin task, sin dock, Entry List No Data
- 1 TRANSFER: DN-3236621 LOADED outbound 28 pallets
- **0 removibles** (solo RN-188084 tiene recv CLOSED pero putaway sigue IN_PROGRESS)

### YMS (yms-agent)
- 11/25 con ET verificado en YMS
- 5 DOCK_CHECKED_IN/LIVE_DELIVERY con presencia física confirmada
- 2 GATE_CHECKED_IN con spot asignado
- 4 PRE_ENTRY/NOT_CONFIRMED sin gate-in
- 8 sin ET en YMS (compensados por WMS Entry List o son PRE-ENTRY)
- **0 nuevas llegadas detectadas** (ningún PRE-ENTRY tiene ahora gate-in)

---

## 🚨 ALERTAS ACTIVAS

### 🔴 CRÍTICAS
1. **MATU2656138 (RN-5008572):** PRE-ENTRY, cita Jul 3 VENCIDA. YMS PRE_ENTRY sin gate-in. WMS Entry List inYard=NULL. Rufino Jul 3 dijo "NO tiene RN". Priti quiere el drop pero no hay RN asignado.
2. **RN-5006269 (MAWB 00120698274):** **125+ días** estancado EN YARDA. TASK-5207670 NEW desde Mar 2, 2026. Evaluar cierre con Rufino.
3. **RN-183707 (ALNOR04242026):** **69+ días** estancado EN YARDA. TASK-5252949 NEW desde Abr 27, 2026. Evaluar cierre con Rufino.
4. **Coolify NO está desplegando:** GitHub actualizado correctamente (lastUpdated 02:30 PT) pero live feed muestra datos viejos (01:45 PT). Mismo problema recurrente reportado Jul 4.

### 🟠 DISCREPANCIAS Jonathan vs WMS
5. **JTAU7362561:** Jonathan EMPTY 07/04 | WMS recv IN_PROGRESS TASK-5307533 Pedro Avila DOCK65
6. **DDDU5053860:** Jonathan EMPTY 07/04 | WMS recv IN_PROGRESS TASK-5307692 Pedro Avila DOCK63
7. **TCKU6977609:** Jonathan EMPTY 07/03 | WMS recv IN_PROGRESS TASK-5307690 Pedro Avila DOCK60
8. **OOCU5501937:** Jonathan EMPTY 07/03 | WMS recv IN_PROGRESS TASK-5307688 Pedro Avila DOCK59
9. **CSGU6429436:** 3.5d+ en recibo IN_PROGRESS DOCK68. Jonathan EMPTY 07/02+07/03.

### 🟡 OTROS
10. **5 no-shows** con citas vencidas: EITU9363654, TGBU8815453, LabelKing PO7937, LabelKing PO8357, ITL07012026
11. **LabelKing duplicados:** RN-5008450 (en yarda, PO8423) vs RN-5008449 (PRE-ENTRY, PO7937) vs RN-5008444 (PRE-ENTRY, PO8357) — mismo BOL "07012026"
12. **6 EN PROCESO sin putaway:** Solo RN-188084 tiene putaway task creado. Los otros 6 en recibo IN_PROGRESS no tienen putaway asignado.

---

## 🛡️ GUARDRAILS

| Guardrail | Estado |
|---|---|
| emailMonitor | READ_ONLY — 17 contenedores, todos registrados |
| rnPrimaryKey | ACTIVE — 24/24 RN Gurunanda |
| entryListRule | ACTIVE (Regla Rufino #3) |
| notesIntegrity | ACTIVE |
| ymsReadingRule | ACTIVE (gate check-out ≠ full departure) |
| antiEstadoViejo | ACTIVE — 0 promociones esta corrida |
| staleStateGuard | ACTIVE — todos estados correctos |
| closedRemovalRule | ACTIVE — 26 excluidos |

---

## ⚠️ LIMITACIÓN CONOCIDA

**Coolify no está haciendo auto-deploy.** Los cambios están correctamente pusheados a GitHub (`main` y `master`), confirmados vía raw.githubusercontent.com con lastUpdated 2026-07-05T02:30:00-07:00. El live feed (coolify.item.pub) sigue mostrando 01:45 PT. Este es el mismo problema reportado en corridas anteriores (Jul 2-4). Se requiere intervención manual en Coolify Dashboard para forzar redeploy.
