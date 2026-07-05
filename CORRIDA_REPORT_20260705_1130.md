# 📊 CORRIDA COMPLETA — Contenedores Priti en Yarda
**Fecha/Hora:** Domingo 5 Julio 2026, 11:15–11:35 AM PT
**Agente:** Agente Priti Contenedores
**Repositorio:** esaonc-ai/contenedores-priti-dashboard-03b000
**Dashboard Live:** https://contenedores-priti-dashboard-03b000.coolify.item.pub/

---

## 🚨 ALERTA ROLAS CRÍTICA: COOLIFY DEPLOYMENT DOWN

**Coolify management server (`coolify.item.pub`) NO RESPONDE.** 
- Último deploy exitoso: ~11:05 PT
- Commits acumulados sin deploy: 8
- Tiempo sin deploy: ~30 min (y contando)
- El dashboard live muestra datos de la corrida 11:05 PT
- **MATU2656138 sigue como PRE-ENTRY en el live (debe ser EN YARDA)**

---

## 📋 RESUMEN EJECUTIVO

| Métrica | Repo (listo) | Live (stale) |
|---|---|---|
| **Total activos** | 25 | 25 |
| 🟢 EN YARDA | **2** (TGBU3785090 + MATU2656138) | 1 (solo TGBU3785090) |
| 🟡 EN PROCESO | 7 | 7 |
| 📅 PRE-ENTRY | 14 | **15** (incluye MATU2656138 mal) |
| 🟠 DEGRADADOS | 2 | 2 |
| 📋 TRANSFER | 1 | 1 |
| **Excluidos** | **39** | 26 |
| **lastUpdated** | 2026-07-05T11:27:02-07:00 | 2026-07-05T11:05:00-07:00 |

---

## 🔄 CAMBIOS APLICADOS (en repo, pendientes de deploy)

### #1 MATU2656138: PRE-ENTRY → EN YARDA 🟢
| Campo | Antes (live) | Después (repo) |
|---|---|---|
| Color | normal (PRE-ENTRY) | **green (EN YARDA)** |
| inYard | false | **true** |
| ET | ET-1117982 (shell sin equipo) | **ET-1117774** (GATE_CHECKED_IN real) |
| Dock | SIN DOCK | PENDIENTE (sin spot/dock en YMS) |
| Recv Task | — | NINGUNO |
| Gate Check-in | — | **2026-07-02T20:11:19 PDT** |

**Evidencia YMS**: ET-1117774, GATE_CHECKED_IN Jul 2 20:11 PDT, operador buenaguard, DROP_OFF_DELIVERY MATU2656138 FULL. HAW TRUCKING INC / NATHAN HAO / 9G88837. Evidencia fotográfica de entrada. Sin dock/spot asignado (dropOffLocationId null).

**Corrección ET**: ET-1117982 es un pre-checkin administrativo (shell sin equipo, creado por aismael Jul 3 08:03) que comparte RN-5008572 pero NO corresponde al contenedor MATU2656138. Corregido a ET-1117774.

### #2 SMCU1114360 → Excluded
- RN-5008384
- Recv TASK-5303878: FORCE_CLOSED ✅
- Putaway TASK-5304043: CLOSED ✅
- Completado Jun 30. Cita Jun 29.
- Agregado a excluded con evidencia WMS.

### #3 12 Contenedores Históricos → Excluded
Todos verificados CLOSED en WMS (Phase 1: Jun 22-24, Phase 2: Jun 25-26):

| Contenedor | RN | Cerrado |
|---|---|---|
| EITU8174300 | RN-5008303 | Jun 25, jlnieves |
| CAAU5246296 | RN-5008296 | Jun 24, jlnieves |
| DDDU5053448 | RN-5008297 | Jun 25, employee882504 |
| DDDU5053469 | RN-5008298 | Jun 25, employee882504 |
| CSNU8563588 | RN-5008300 | Jun 26, jlnieves |
| BEAU6015134 | RN-5008320 | Jun 26, pedrofas39 |
| FCIU9601208 | RN-5008321 | Jun 26, employee882504 |
| FFAU6121609 | RN-5008322 | Jun 26, employee882504 |
| CAAU8362068 | RN-5008373 | Jun 29, jlnieves |
| SEKU4670025 | RN-5008325 | Jun 29, jlnieves |
| TCNU1243715 | RN-5008340 | Jun 27, jeespinoza |
| TIIU7745643 | RN-5008341 | Jun 27, employee882504 |

---

## 🔍 ESTADO WMS DETALLADO (verificado 11:19 PT)

### 🟢 EN YARDA (2)
| Contenedor | RN | Recv Task | Putaway Task | Dock |
|---|---|---|---|---|
| TGBU3785090 | RN-188086 | TASK-5307685 NEW ⚠️ | — | 768 |
| MATU2656138 | RN-5008572 | NINGUNO ⚠️ | — | PENDIENTE |

### 🟡 EN PROCESO (7)
| Contenedor | RN | Recv Task | Putaway Task | Dock |
|---|---|---|---|---|
| DDDU5053860 | RN-5008447 | TASK-5307692 IN_PROGRESS | — | 568 |
| TCKU6977609 | RN-5008481 | TASK-5307690 IN_PROGRESS | — | 565 |
| OOCU5501937 | RN-5008506 | TASK-5307688 IN_PROGRESS | — | 571 |
| JTAU7362561 | RN-5008446 | TASK-5307533 IN_PROGRESS | — | 573 |
| CSGU6429436 | RN-5008479 | TASK-5306174 IN_PROGRESS | — | 574 |
| GN07012026UNIS-1130 (53693) | RN-188044 | TASK-5306724 IN_PROGRESS ⚠️ DOCK_CHECK_IN estancado | — | 553 |
| GN07012026UNIS-1132 (53170) | RN-188084 | TASK-5307686 CLOSED ✅ | TASK-5307890 IN_PROGRESS (33 LPs) | 769 |

### 📅 PRE-ENTRY (14)
CBHU7024789, FFAU2426030, CSNU6323633, LabelKing PO8423/PO8449/PO7937/PO8357, EITU9363654, TGBU8815453, TEMU8901490, CORR070626UNIS, ITL07012026, MRKU9388930

### 🟠 DEGRADADOS (2)
MAWB 00120698274 (RN-5006269, 125d+), ALNOR04242026 (RN-183707, 71d+)

### 📋 TRANSFER (1)
DN-3236621 (Trailer 53176), TO6331, DOCK54

---

## 🔍 VERIFICACIÓN YMS (11:19 PT)

| Contenedor | YMS | Detalle |
|---|---|---|
| MATU2656138 | ✅ GATE_CHECKED_IN | ET-1117774, Jul 2 20:11 PDT, HAW TRUCKING |
| TGBU3785090 | ❌ API no encontró | Limitación del API YMS, verificado por WMS Entry List |
| DDDU5053860–OOCU5501937 (6) | ❌ API no encontró | Limitación del API YMS |
| CBHU7024789 | ❌ Sin gate check-in | PRE-ENTRY confirmado |
| FFAU2426030 | ❌ Sin gate check-in | PRE-ENTRY confirmado |
| CSNU6323633 | ❌ Sin gate check-in | PRE-ENTRY confirmado |
| EITU9363654 | ❌ Sin cambios | No-show |
| TGBU8815453 | ❌ Sin cambios | No-show |

---

## 📧 OUTLOOK (verificado 11:15 PT)

41 contenedores rastreados de correos de Priti (Jun 22 – Jul 3):
- 13 activos Jul 1-3
- 12 Phase 1/2 ya cerrados (agregados a excluded)
- 8 Phase 3 (Jun 29-30) — 7 ya en excluded, SMCU1114360 recién agregado
- 8 Phase 4 (Jul 1-3) — 9 en yarda/en proceso, 4 PRE-ENTRY sin confirmar

Correos de Jonathan Heredia / Rufino Munguia: 5 reportes operativos (Jun 25 – Jul 3) con actualizaciones de vacíos (empty pickups) para DDDU5053860, DDDU5053432, JTAU7362561, OOCU7355889, CSGU6429436, MRKU6829749, MRKU9748297, TCKU6977609, OOCU5501937.

---

## 🛡️ VALIDACIONES

| Validación | Estado |
|---|---|
| Anti-stale-state (ningún PRE-ENTRY con gate check-in) | ✅ PASS |
| MATU2656138 color=green, inYard=true, et=ET-1117774 | ✅ PASS (repo) |
| SMCU1114360 en excluded | ✅ PASS (repo) |
| Feed JSON válido | ✅ PASS |
| HTTP 200 dashboard | ✅ PASS |
| HTTP 200 feed | ✅ PASS |
| lastUpdated actualizado | ✅ PASS (repo) |
| Deploy a Coolify | ❌ FAIL — Coolify DOWN |

---

## 🚨 ALERTAS GENERADAS

| # | Severidad | Alerta |
|---|---|---|
| 1 | 🔴🔴🔴 CRÍTICA | **Coolify management server DOWN** — `coolify.item.pub` no responde. Dashboard live está stale (11:05 PT). Cambios no se pueden desplegar. |
| 2 | 🔴🔴 | **MATU2656138 sigue PRE-ENTRY en live** — Rufino ve datos viejos. Debe ser EN YARDA (YMS ET-1117774 GATE_CHECKED_IN Jul 2 20:11). |
| 3 | 🔴 | **SMCU1114360 (RN-5008384) no visible** — Ambas tasks cerradas, debe estar en excluded. |
| 4 | ⚠️ | **MATU2656138 sin receive task** — RN-5008572 existe pero sin tarea. Sin dock/spot. |
| 5 | ⚠️ | **TGBU3785090 recv NEW 2d+** — Sin iniciar recibo. Cita Jul 6 15:00. |
| 6 | ⚠️ | **GN07012026UNIS-1130 (RN-188044)** — DOCK_CHECK_IN estancado desde Jul 2. OFFLOAD nunca empezó. |
| 7 | ⚠️ | **API YMS no filtra por equipment** — search-by-paging ignora filtros. Búsqueda manual requerida. |

---

**Conclusión**: Corrida completada exitosamente en cuanto a verificación y actualización del feed. Los 3 cambios principales (MATU2656138 → EN YARDA, SMCU1114360 → excluded, 12 históricos → excluded) están aplicados en el repo de GitHub (main y master). **NO se pueden desplegar porque Coolify está caído.** El dashboard live muestra datos de la corrida anterior (11:05 PT). Se requiere restaurar Coolify para que Rufino vea los datos actualizados.
