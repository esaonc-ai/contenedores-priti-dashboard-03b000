# 🏗️ CORRIDA PRITI/GURUNANDA — Jul 4 2026 21:32 PT

## 📊 RESUMEN EJECUTIVO

| Métrica | Valor |
|----------|-------|
| **Activos totales** | **25** (6 🟢 green, 7 🟡 yellow, 12 ⚪ normal) |
| **Excluidos** | 26 (recv+putaway cerrados) |
| **Nuevos agregados** | 0 |
| **RN nuevos encontrados** | 0 (sin RN nuevos desde 20:10 PT) |
| **En yarda confirmados YMS** | 6 con equipo físico + 1 débil (LabelKing) |
| **En proceso** | 7 (6 recv IN_PROGRESS + 1 putaway IN_PROGRESS) |
| **Pendientes por llegar** | 12 (8 PRE-ENTRY sin YMS + 3 CBHU/FFAU/CSNU + 1 transfer) |
| **Falsos green corregidos** | 0 nuevos (ya corregidos en corridas previas) |
| **Removidos** | 0 (ningún RN con ambos tasks cerrados) |
| **Alertas** | 10 |

---

## 🔍 VERIFICACIONES REALIZADAS

### ✅ Paso 1: Outlook — COMPLETO
- Jonathan Heredia (Jul 4 04:46 UTC): 4 contenedores EMPTY ready pickup → **ALERTA: WMS contradice**
- Todos los contenedores de correos ya están en dashboard

### ✅ Paso 2: WMS — 24 RNs verificados
- 7 recv IN_PROGRESS, 17 IMPORTED
- Docks corregidos: JTAU7362561→DOCK65, DDDU5053860→DOCK63, OOCU5501937→DOCK59
- RN-188084: recv CLOSED, putaway IN_PROGRESS (53 LPs) — se mantiene activo

### ✅ Paso 3: YMS/WISE — 18 contenedores verificados
- **6 FULL confirmados con equipo físico**: CSGU6429436, DDDU5053860, TCKU6977609, OOCU5501937, TGBU3785090, MATU2656138
- **Gate-out tracking**: DDDU5053860→driver salió con vacío DDDU5053432, TCKU6977609→tractor-only, TGBU3785090→driver salió con MRKU9748297
- **8 sin entry ticket YMS**: CBHU, FFAU, CSNU, TGBU8815453, TEMU8901490, CORR070626UNIS, MRKU9388930, GN07012026UNIS-1130

### ✅ Paso 4: Anti-estado-viejo
- CBHU7024789, FFAU2426030, CSNU6323633: WMS dock+tasks NEW pero YMS sin gate-in → **PRE-ENTRY mantenido** ✅
- Ningún PRE-ENTRY/NORMAL con evidencia física sin confirmar

### ✅ Paso 5-6: Receiving + Putaway
- Ningún contenedor con ambos tasks cerrados → **0 removidos esta corrida**
- RN-188084: único con putaway activo (TASK-5307890 IN_PROGRESS)

### ✅ Paso 7: Repo + Deploy
- Push exitoso a `main` y `master` (commit `88f3f21`)
- ⚠️ **Coolify NO ha desplegado** el commit más reciente — live feed muestra 21:30 PT (repo tiene 21:37 PT)
- El commit pendiente contiene: Jonathan EMPTY alerts detalladas, gate-out tracking, YMS/WMS discrepancies

### ✅ Paso 8: Validación Live
- Dashboard HTML: **HTTP 200** ✅
- Feed JSON: **HTTP 200** ✅
- lastUpdated: `2026-07-04T21:30:00-07:00`
- 25 activos, 6G/7Y/12N — correcto

---

## 🚨 ALERTAS CRÍTICAS

1. **🚨 MATU2656138/RN-5008572**: 48h+ SIN SPOT, SIN receiving task. YMS confirma GATE_CHECKED_IN + DROP_OFF_DELIVERY con equipo EQP-260333
2. **🚨 RN-5006269 (125 días) + RN-183707 (69 días)**: Abandonados en yarda
3. **🚨 CSGU6429436**: 3.5d recv IN_PROGRESS, YMS DOCK69 ≠ WMS DOCK68, Jonathan reportó EMPTY
4. **🚨 Jonathan Heredia Jul 4**: Reporta 4 EMPTY (DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561) pero WMS muestra los 4 recv IN_PROGRESS
5. **⚠️ Coolify**: Commit `88f3f21` no desplegado. Live feed ~7 min atrasado respecto al repo.

---

## 📋 DISCREPANCIAS YMS vs WMS

| Contenedor | YMS | WMS |
|-----------|-----|-----|
| DDDU5053860 | SPOT675 | DOCK63 |
| TCKU6977609 | SPOT775 | DOCK60 |
| OOCU5501937 | SPOT688 | DOCK59 |
| CSGU6429436 | DOCK69 | DOCK68 |
| TGBU3785090 | SPOT780 | DOCK104 |

---

## 📝 COMMIT PENDIENTE (88f3f21)

El commit en repo contiene mejoras adicionales que se reflejarán cuando Coolify despliegue:
- Alertas individuales por contenedor del reporte Jonathan EMPTY Jul 4
- Detalles gate-out: DDDU5053432 vacío, tractor-only TCKU6977609, MRKU9748297 vacío
- YMS/WMS dock discrepancies en notas de cada contenedor
- MATU2656138: confirmación equipo EQP-260333/MATU2656138/SIZE_40/FULL
- RN-188084: YMS NEED_WINDOW_CHECK_IN noted

---

**Corrida completada: Jul 4 21:32 PT. Próxima corrida programada ~21:47 PT.**
