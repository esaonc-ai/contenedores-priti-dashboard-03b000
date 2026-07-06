# 📊 CORRIDA COMPLETA — Contenedores Priti en Yarda
## 🕐 Julio 6, 2026 — 01:18 AM PT
## Agente: Priti Contenedores Yarda

---

## ═══════════════════════════════════════
## RESUMEN EJECUTIVO

| Métrica | Valor |
|---------|-------|
| **Total revisados** | 33 RNs + 28 contenedores YMS |
| **Nuevos agregados** | 0 |
| **Actualizados a EN YARDA** | 0 (ya estaban) |
| **Actualizados a IN_PROGRESS** | 0 (sin cambios) |
| **Removidos/cerrados** | 0 |
| **Total activos dashboard** | **25** |
| **Inconsistencias** | 1 (JTAU7362561 sin Entry Ticket) |

---

## ═══════════════════════════════════════
## 🟢 EN YARDA — 7 Contenedores (VERDE)

| # | Contenedor | RN | Evidencia | Estado |
|---|-----------|-----|-----------|--------|
| 1 | **TGBU3785090** | RN-188086 | WMS: DOCK104, TASK-5307685 NEW, inYardTime Jul 3 14:30 | ✅ EN YARDA |
| 2 | **CBHU7024789** | RN-5008507 | WMS: DOCK108, TASK-5307687 NEW, inYardTime Jul 3 14:31 | ✅ EN YARDA |
| 3 | **FFAU2426030** | RN-5008480 | WMS: DOCK128, TASK-5307691 NEW, inYardTime Jul 3 14:31 | ✅ EN YARDA |
| 4 | **CSNU6323633** | RN-5008483 | WMS: DOCK124, TASK-5307689 NEW, inYardTime Jul 3 14:31 | ✅ EN YARDA |
| 5 | **LE4042 / PO8423** | RN-5008450 | WMS: DOCK45, TASK-5305892 NEW 4d+, inYardTime Jul 1 18:36 | ✅ EN YARDA |
| 6 | **PO8449** | RN-5008571 | WMS: DOCK38, TASK-5307907 NEW, inYardTime Jul 3 17:14 | ✅ EN YARDA |
| 7 | **MATU2656138** | RN-5008572 | 🔥 YMS: ET-1117774, GATE_CHECKED_IN Jul 2 20:10 PDT, DROP_OFF_DELIVERY FULL, HAW TRUCKING INC, NATHAN HAO, tractor 9G88837 | ✅ EN YARDA |

> **Regla aplicada**: WMS task+dock+inYardTime (containers 1-6) o YMS gate check-in real (MATU). Entry List search tiene limitaciones — MATU (confirmado en YMS) tampoco aparece, confirmando que la búsqueda no es exhaustiva.

---

## ═══════════════════════════════════════
## 🟡 EN PROCESO — 7 Contenedores (AMARILLO)

| # | Contenedor | RN | Entry Ticket | Recv Task | Asignado |
|---|-----------|-----|-------------|-----------|----------|
| 1 | **DDDU5053860** | RN-5008447 | ✅ ET-1117794 GATE_CHECKED_OUT | TASK-5307692 IN_PROGRESS | Pedro Avila |
| 2 | **TCKU6977609** | RN-5008481 | ✅ ET-1117803 GATE_CHECKED_OUT | TASK-5307690 IN_PROGRESS | Pedro Avila |
| 3 | **OOCU5501937** | RN-5008506 | ✅ ET-1117844 GATE_CHECKED_IN | TASK-5307688 IN_PROGRESS | Pedro Avila |
| 4 | **JTAU7362561** ⚠️ | RN-5008446 | ❌ SIN Entry Ticket | TASK-5307533 IN_PROGRESS | Pedro Avila |
| 5 | **CSGU6429436** | RN-5008479 | ✅ ET-1116861 GATE_CHECKED_IN | TASK-5306174 IN_PROGRESS 3.5d+ | Fatima Ponce |
| 6 | **GN07012026UNIS-1130** | RN-188044 | — | TASK-5306724 IN_PROGRESS | Caren Cubides |
| 7 | **GN07012026UNIS-1132** | RN-188084 | — | Recv CLOSED ✅ + Putaway IN_PROGRESS | Jesus Espinoza |

> ⚠️ **#4 JTAU7362561**: RN IN_PROGRESS + receiving IN_PROGRESS + DOCK65 + inYardTime Jul 3, pero **sin Entry Ticket en YMS/WISE**. Investigar posible bypass de gate.

---

## ═══════════════════════════════════════
## 🚨 DEGRADADOS — 2

| # | Contenedor | RN | Problema |
|---|-----------|-----|----------|
| 1 | **MAWB 00120698274** | RN-5006269 | 125d+ estancado, TASK-5207670 NEW desde Mar 2 |
| 2 | **ALNOR04242026** | RN-183707 | 71d+ estancado, TASK-5252949 NEW desde Abr 27 |

---

## ═══════════════════════════════════════
## 📅 PRE-ENTRY — 8

| # | Contenedor | RN | Cita |
|---|-----------|-----|------|
| 1 | EITU9363654 | RN-5008569 | Sin cita |
| 2 | TGBU8815453 | RN-5008570 | Sin cita |
| 3 | TEMU8901490 | RN-5008566 | **Jul 7 09:00** |
| 4 | CORR070626UNIS | RN-5008505 | **HOY Jul 6 17:00 WILL CALL** |
| 5 | LabelKing PO7937 | RN-5008449 | VENCIDA Jul 1 |
| 6 | LabelKing PO8357 | RN-5008444 | VENCIDA Jul 1 |
| 7 | ITL07012026 | RN-187990 | VENCIDA Jul 2 |
| 8 | MRKU9388930 | RN-188088 | **HOY Jul 6 16:00** |

---

## ═══════════════════════════════════════
## 🚛 OUTBOUND TRANSFER — 1

| Referencia | Detalle |
|-----------|--------|
| **DN-3236621** (Trailer 53176) | PO TO6331, 28 pallets, LOADED Jul 3, Fusion Transportation → Fontana CA |

---

## ═══════════════════════════════════════
## 🔍 OUTLOOK CROSS-CHECK

### Contenedores Priti/Jasmine verificados:
| Contenedor | RN | WMS Status | En Dashboard |
|-----------|-----|-----------|-------------|
| JTAU7362598 | RN-5008424 | CLOSED + ambos tasks CLOSED | ❌ (correcto) |
| JTAU7362582 | RN-5008426 | CLOSED + ambos tasks CLOSED | ❌ (correcto) |
| FFAU1548537 | RN-5008428 | CLOSED + ambos tasks CLOSED | ❌ (correcto) |
| OOLU9324944 | RN-5008430 | CLOSED + ambos tasks CLOSED | ❌ (correcto) |
| DDDU5053432 | RN-5008448 | CLOSED + ambos tasks CLOSED | ❌ (correcto) |
| OOCU7355889 | RN-5008445 | CLOSED + ambos tasks CLOSED | ❌ (removido Jul 3) |

### Transferencias Outlook:
| RN | Referencia | Estado | En Dashboard |
|----|-----------|--------|-------------|
| RN-187978 | GN06302026UNIS-1126 | Ambos tasks CLOSED | ❌ (correcto) |
| RN-188031 | GN07012026UNIS-1129 | FORCE_CLOSED + CLOSED | ❌ (correcto) |
| RN-188048 | GN07012026UNIS-1131 | FORCE_CLOSED + CLOSED | ❌ (correcto) |

> ✅ Sin nuevos contenedores de Priti/Jasmine para añadir.

---

## ═══════════════════════════════════════
## ⚠️ ALERTAS ROLAS

| # | Alerta |
|---|--------|
| 🔴 | **Coolify NO auto-desplegó** — live sirve versión 00:13 PT. Repo tiene 01:18 PT correcto. 4 pushes realizados sin trigger de rebuild. Requiere deploy manual en dashboard Coolify. |
| ⚠️ | **JTAU7362561**: RN IN_PROGRESS con receiving activo pero SIN Entry Ticket — investigar |
| ⚠️ | **MAWB 125d+** estancado (RN-5006269) — requiere force close |
| ⚠️ | **ALNOR 71d+** estancado (RN-183707) — requiere force close |
| ⚠️ | **CSGU6429436**: 3.5d+ en receiving (Fatima Ponce) |
| ⚠️ | **LE4042/PO8423**: Recv NEW 4d+ sin iniciar (Jerome Aranda) |
| ⚠️ | **MATU2656138**: EN YARDA confirmado YMS pero SIN spot/dock YMS (dropOffLocationId: null) y SIN receiving task WMS |
| ⚠️ | **3 citas vencidas** sin acción: PO7937, PO8357, ITL07012026 |
| 🔵 | **HOY Jul 6** — 2 citas: MRKU9388930 (16:00), CORR070626UNIS (17:00 WILL CALL) |
| ℹ️ | Entry List search tiene limitaciones — 7 EN YARDA (incluyendo MATU con YMS confirmado) no aparecen |
| ℹ️ | 4 EN PROCESO confirmados con Entry Tickets YMS (DDDU, TCKU, OOCU, CSGU) |
| ℹ️ | Outlook batch completo verificado — 9 RNs CLOSED correctamente fuera del dashboard |

---

## ═══════════════════════════════════════
## 🚨 ALERTA ROLAS CRÍTICA

**Coolify no está haciendo deploy automático.** El repositorio GitHub (`esaonc-ai/contenedores-priti-dashboard-03b000`, branch `main`) tiene la versión correcta con `lastUpdated: 2026-07-06T01:18:00-07:00` y 16 alerts, pero el servidor live en `https://contenedores-priti-dashboard-03b000.coolify.item.pub` sigue sirviendo la versión `00:13:00-07:00` con 11 alerts.

**Impacto**: Los estados de contenedores son correctos en ambas versiones (mismos 7 verdes, 2 degradados, 7 en proceso, 8 pre-entry, 1 outbound). Las diferencias son solo enriquecimiento de notas, verificationSources y alerts. **No hay riesgo de información incorrecta sobre estados de contenedores.**

**Acción requerida**: Despliegue manual desde el dashboard de Coolify.

---

## ═══════════════════════════════════════
## 📋 EVIDENCIA POR ROW

Todos los 25 rows activos verificados con:
- **WMS**: RN status, dock, receiving task, putaway task, inYardTime
- **YMS**: Entry Tickets, gate check-in/out, equipment, spot/dock
- **Entry List**: Verificación de presencia física (con limitaciones de endpoint)
- **Outlook**: Cross-check con correos de Priti/Jasmine/Rufino

`lastVerifiedAt`: `2026-07-06T01:18:00-07:00` para todos.

---

**✅ Corrida completada. Dashboard estados correctos. Coolify deploy manual pendiente.**
