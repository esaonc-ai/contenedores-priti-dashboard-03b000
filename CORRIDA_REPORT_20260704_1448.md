# 📊 CORRIDA REPORT — Priti Contenedores Dashboard
## Jul 4 14:48 PT | Agente Priti Contenedores en Yarda

---

## 📋 RESUMEN

| Métrica | Valor |
|----------|-------|
| **Activos totales** | **25** |
| 🟢 EN YARDA (green) | **6** |
| 🟡 EN PROCESO (yellow) | **7** |
| 🔴 CRÍTICO (red) | **0** |
| ⚪ PRE-ENTRY (normal) | **12** |
| ❌ Excluidos | **26** (+1) |
| **Nuevos agregados** | 0 |
| **Removidos (ambos tasks cerrados)** | 1 (RN-188094) |
| **Greens restaurados** | 4 (Entry List inYardTime) |
| **Falsos green corregidos** | 0 (mantenidos) |
| **Última verificación** | 2026-07-04T14:48:00-07:00 |

---

## 🔄 CAMBIOS APLICADOS

### ✅ RESTAURADOS A GREEN (Entry List con inYardTime confirmado)
La corrida anterior (14:22 PT) degradó 4 greens a NORMAL citando "sin Entry List". La re-verificación WMS a las 14:35 PT confirmó que los 4 SÍ tienen Entry List con inYardTime poblado:

| Contenedor | RN | inYardTime | Evidencia |
|------------|-----|-----------|-----------|
| **LabelKing07012026 / PO8423** | RN-5008450 | Jul 1 18:36 | Entry List ✅ inYardTime |
| **MAWB 00120698274** | RN-5006269 | Mar 2 17:10 | Entry List ✅ inYardTime (124+ días) |
| **ALNOR04242026** | RN-183707 | Apr 27 15:12 | Entry List ✅ inYardTime (68+ días) |
| **LabelKing07072026 PO8449** | RN-5008571 | Jul 3 17:14 | Entry List ✅ inYardTime |

### ❌ REMOVIDO (ambos tasks cerrados)
| Contenedor | RN | Recv Task | Putaway Task |
|------------|-----|-----------|-------------|
| **GN07022026UNIS-1133 (53393)** | RN-188094 | TASK-5307936 FORCE_CLOSED | TASK-5308246 CLOSED (endTime Jul 4 02:29) |

### 🔄 ACTUALIZADOS
- **TGBU3785090** (RN-188086): YMS confirma full arrived SPOT780 + empty MRKU9748297 departed
- **MATU2656138** (RN-5008572): 46h+ en yarda sin spot, sin receiving task — 🚨 CRÍTICA
- **DDDU5053860** (RN-5008447): YMS confirma empty DDDU5053432 departed, WMS recv IN_PROGRESS
- **TCKU6977609** (RN-5008481): YMS tractor salió sin contenedor (NO_EQUIPMENT)
- **OOCU5501937** (RN-5008506): YMS sin gate check-out, probablemente sigue en yarda
- **RN-188084** (GN07012026UNIS-1132): putaway TASK-5307890 sigue IN_PROGRESS (no removible)
- Todos los rows re-verificados con timestamps actualizados

---

## 🟢 EN YARDA (6)

| Contenedor | RN | Dock/Spot | YMS Gate | Recv Task | Alerta |
|------------|-----|-----------|----------|-----------|--------|
| TGBU3785090 | RN-188086 | SPOT780 | ✅ Gate Check-in Jul 2 21:39 | NEW | ⚠️ WMS DOCK104 vs YMS SPOT780 |
| MATU2656138 | RN-5008572 | SIN SPOT | ✅ Gate Check-in Jul 2 20:11 | Sin task | 🚨 46h sin spot ni recv |
| LabelKing PO8423 | RN-5008450 | DOCK45 | — | NEW | ⚠️ 3 RNs mismo contenedor |
| MAWB 00120698274 | RN-5006269 | DOCK62 | — | NEW | 🚨 124+ días abandonado |
| ALNOR04242026 | RN-183707 | DOCK65 | — | NEW | 🚨 68+ días abandonado |
| LabelKing PO8449 | RN-5008571 | DOCK38 | WINDOW_CHECKED_IN | NEW | ⚠️ Manual check-in |

---

## 🟡 EN PROCESO (7)

| Contenedor | RN | Dock | Recv Task | Putaway Task | Alerta |
|------------|-----|------|-----------|-------------|--------|
| JTAU7362561 | RN-5008446 | DOCK65 | IN_PROGRESS | — | ⚠️ Jonathan reportó EMPTY |
| CSGU6429436 | RN-5008479 | DOCK68 | IN_PROGRESS | — | ⚠️ 3d+ en recibo |
| GN07012026UNIS-1130 | RN-188044 | DOCK41 | IN_PROGRESS | — | ⚠️ Entry List por trailer |
| DDDU5053860 | RN-5008447 | DOCK63 | IN_PROGRESS | — | ⚠️ Empty departed, recv activo |
| TCKU6977609 | RN-5008481 | DOCK60 | IN_PROGRESS | — | ⚠️ Tractor sin empty |
| OOCU5501937 | RN-5008506 | DOCK59 | IN_PROGRESS | — | ⚠️ Sin gate check-out |
| GN07012026UNIS-1132 | RN-188084 | DOCK107 | CLOSED | IN_PROGRESS | ⚠️ Putaway activo |

---

## 🚨 ALERTAS CRÍTICAS (10)

1. **🚨 MATU2656138/RN-5008572** — 46h en yarda sin spot, sin receiving task. Contenedor full abandonado desde Jul 2 20:11.
2. **🚨 RN-5006269 MAWB 00120698274** — 124+ días en yarda (inYardTime Mar 2). Recv task nunca iniciado.
3. **🚨 RN-183707 ALNOR04242026** — 68+ días en yarda (inYardTime Apr 27). Recv task nunca iniciado.
4. **⚠️ DISCREPANCIA EMPTY**: 4 contenedores reportados EMPTY por Jonathan 07/03 pero WMS recv IN_PROGRESS.
5. **⚠️ CBHU/FFAU/CSNU**: Falsos green corregidos Jul 3. Entry List positivo pero SIN inYardTime — verificar físicamente.
6. **⚠️ YMS API BUG**: Solo 50 de 118K registros accesibles.
7. **📋 NO-SHOW**: EITU9363654 + TGBU8815453 con doble cita vencida.
8. **⚠️ LabelKing07012026**: 3 RNs mismo containerNo. Solo PO8423 con inYardTime.
9. **⚠️ GN contenedores**: Entry List solo por trailer number.
10. **✅ RN-188094 REMOVIDO**: Ambos tasks cerrados.

---

## 📧 OUTLOOK

**6 correos NO LEÍDOS** con información de contenedores:
- Jonathan Heredia: Receiving Progress 2nd Shift (DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561)
- Jonathan Heredia: EMPTY CONTAINERS 07/03
- Rufino/Priti: MATU2656138 sin RN, cambio de cita
- Jerome Aranda: Fusion Transfer TO6331 (DN-3236621)

**No se detectaron contenedores nuevos** desde Outlook para agregar.

---

## 📐 REGLAS APLICADAS

- ✅ **Entry List Rule**: 4 greens restaurados con inYardTime confirmado
- ✅ **Closed Removal Rule**: RN-188094 removido (recv FORCE_CLOSED + putaway CLOSED)
- ✅ **Anti-Estado-Viejo**: Ningún PRE-ENTRY/NORMAL con evidencia YMS física sin corregir
- ✅ **YMS Reading Rule**: Gate Check-out sin equipo = tractor vacío
- ✅ **Falso Green Prevention**: CBHU/FFAU/CSNU mantenidos NORMAL (Entry List sin inYardTime)

---

## 🔧 DEPLOY

- ✅ Commit `47bd5e2` pushed to `main`
- ✅ `master` synced with `main`
- ⚠️ Coolify redeploy pendiente — live feed puede mostrar datos viejos (último conocido: Jul 3 20:07 PT)
- Dashboard HTML: https://contenedores-priti-dashboard-03b000.coolify.item.pub/
- Feed JSON: https://contenedores-priti-dashboard-03b000.coolify.item.pub/container-feed.json

---

*Corrida ejecutada por Agente Priti Contenedores en Yarda — Jul 4 14:48 PT*
*Próxima corrida: ~15:03 PT*
