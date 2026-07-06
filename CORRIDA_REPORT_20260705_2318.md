# 📊 CORRIDA COMPLETA — Contenedores Priti en Yarda
## Domingo 5 de Julio 2026 — 23:18 PT (inicio) → 23:30 PT (cierre)

**verifiedBy:** Agente Priti Contenedores en Yarda para Rufino  
**Tipo:** Triple verificación Outlook + WMS + YMS  
**Facility:** LT_F1 | **Tenant:** LT  
**Dashboard:** https://contenedores-priti-dashboard-03b000.coolify.item.pub  

---

## 📋 RESUMEN EJECUTIVO

| Métrica | Valor |
|---|---|
| **Total revisados** | **25** (todos los rows activos) |
| **Nuevos agregados** | 0 |
| **Actualizados a EN YARDA** | 0 (ya estaban; verificados) |
| **Actualizados a EN PROCESO** | 0 (ya estaban; verificados) |
| **Removidos/cerrados** | 0 (los completados ya estaban removidos) |
| **Inconsistencias** | 1 (Coolify deploy atrasado) |
| **Errores** | 0 |

---

## 🟢 EN YARDA (7) — VERIFICADOS

| # | Contenedor | RN | Dock | Recv Task | Evidencia | Veredicto |
|---|---|---|---|---|---|---|
| 1 | **TGBU3785090** | RN-188086 | DOCK104 | TASK-5307685 NEW | ✅ YMS GATE_CHECKED_IN + fotos | SÓLIDO |
| 2 | **CBHU7024789** | RN-5008507 | DOCK108 | TASK-5307687 NEW | ⚠️ YMS PRE_ENTRY sin gate-in. WMS dock+task. Rule #5. | EN YARDA (WMS) |
| 3 | **FFAU2426030** | RN-5008480 | DOCK128 | TASK-5307691 NEW | ⚠️ YMS sin rastro. WMS dock+task. Rule #5. | EN YARDA (WMS) |
| 4 | **CSNU6323633** | RN-5008483 | DOCK124 | TASK-5307689 NEW | ⚠️ YMS sin rastro. WMS dock+task. Rule #5. | EN YARDA (WMS) |
| 5 | **LE4042/PO8423** | RN-5008450 | DOCK45 | TASK-5305892 NEW 4d+ | ✅ YMS LIVE_DELIVERY + ET | SÓLIDO ⚠️ 4d+ |
| 6 | **PO8449** | RN-5008571 | DOCK38 | TASK-5307907 NEW | ✅ YMS WINDOW_CHECKED_IN | SÓLIDO |
| 7 | **MATU2656138** | RN-5008572 | Sin spot | **SIN task** 🔴 | ✅ YMS GATE_CHECKED_IN + fotos | **LLENO EN YARDA SIN RECV TASK** |

---

## 🟡 EN PROCESO (7) — TODOS CON DOCK CHECK-IN CONFIRMADO

| # | Contenedor | RN | Recv Task | Dock Check-in | Putaway |
|---|---|---|---|---|---|
| 8 | DDDU5053860 | RN-5008447 | IN_PROGRESS | BIN ZHANG Jul 3 22:41 | Pendiente |
| 9 | TCKU6977609 | RN-5008481 | IN_PROGRESS | JOSE ME CAMPOS Jul 3 22:36 | Pendiente |
| 10 | OOCU5501937 | RN-5008506 | IN_PROGRESS | ROBERT ALAN ORMEROD Jul 3 22:33 | Pendiente |
| 11 | JTAU7362561 | RN-5008446 | IN_PROGRESS | Jul 3 03:32 | Pendiente |
| 12 | CSGU6429436 | RN-5008479 | IN_PROGRESS 3.5d+ | SAMI MECHIL ELABED Jul 3 00:09 | Pendiente |
| 13 | GN...1130 (53693) | RN-188044 | IN_PROGRESS | Caren Cubides | Pendiente |
| 14 | GN...1132 (53170) | RN-188084 | CLOSED + Putaway IN_PROGRESS | Jesus Espinoza | 31 LPs activo |

---

## 🚨 DEGRADADOS (2) — ESTANCADOS

| # | Contenedor | RN | Días | Bloqueo |
|---|---|---|---|---|
| 15 | MAWB 00120698274 | RN-5006269 | **127d+** 🔴 | UOM configuration |
| 16 | ALNOR04242026 | RN-183707 | **70d+** 🔴 | Live Unload fantasma |

---

## 📅 PRE-ENTRY (8)

| # | Contenedor | RN | Cita/Estado |
|---|---|---|---|
| 17 | EITU9363654 | RN-5008569 | YARD_CHECK fantasma ET-1118256 |
| 18 | TGBU8815453 | RN-5008570 | YARD_CHECK fantasma ET-1118242 |
| 19 | TEMU8901490 | RN-5008566 | Jul 7 16:00 (DO no UNIS) |
| 20 | CORR070626UNIS | RN-5008505 | Jul 6 17:00 WILL CALL |
| 21 | LabelKing PO7937 | RN-5008449 | VENCIDA Jul 1 |
| 22 | LabelKing PO8357 | RN-5008444 | VENCIDA Jul 1 |
| 23 | ITL07012026 | RN-187990 | VENCIDA Jul 2 |
| 24 | MRKU9388930 | RN-188088 | Jul 6 16:00 |

---

## 🚛 OUTBOUND (1)

| 25 | DN-3236621 (53176) | LOADED Jul 3 → Fontana CA | Pendiente pickup |

---

## 🔍 HALLAZGOS CLAVE DE ESTA CORRIDA

### 1. MATU2656138 — 🔴 CRÍTICO: SIN RECEIVING TASK
- YMS confirma **GATE_CHECKED_IN Jul 2 20:11** con fotos del contenedor lleno
- HAW TRUCKING, driver NATHAN HAO
- RN-5008572 existe en WMS (IMPORTED) pero **NO tiene receiving task generado**
- El lleno está físicamente en yarda desde hace 3 días sin que nadie pueda recibirlo
- **ACCIÓN REQUERIDA: Generar receiving task urgentemente**

### 2. FFAU2426030 + CSNU6323633 — ⚠️ Sin evidencia YMS
- WMS: IMPORTED, dock asignado, receiving task NEW
- YMS: Sin rastro (sin ET, sin gate-in)
- Creados en lote por ccubides el Jul 3 14:31. Sin dock check-in.
- Promovidos a EN YARDA por Rule #5 (WMS evidence)
- **RECOMENDACIÓN: Verificar físicamente en yarda**

### 3. CBHU7024789 — ⚠️ YMS PRE_ENTRY sin gate-in
- YMS: ET-1116970 PRE_ENTRY NOT_CONFIRMED, sin gate-in
- WMS: DOCK108 + TASK-5307687 NEW (mismo batch ccubides)
- **RECOMENDACIÓN: Verificar físicamente**

### 4. MAWB + ALNOR — Evaluar force close
- MAWB: 127 días, UOM config bloquea
- ALNOR: 70 días, Live Unload nunca ejecutado
- Ambos tienen el trailer que ya salió de yarda hace meses
- **ACCIÓN REQUERIDA: Decisión de Rufino**

### 5. LE4042/PO8423 — Recibo 4d+ sin iniciar
- Jerome Aranda asignado, TASK-5305892 NEW desde Jul 1
- YMS LIVE_DELIVERY confirmado
- **ACCIÓN REQUERIDA: Iniciar recibo**

### 6. Completados confirmados (ya removidos del dashboard)
- OOCU7355889 (RN-5008445): Receiving+Putaway CLOSED ✅
- DDDU5053432 (RN-5008448): Receiving+Putaway CLOSED ✅
- RN-187978, RN-188031, RN-188048, RN-188094: Tasks cerrados ✅

### 7. YARD_CHECK fantasmas — Confirmados
- ET-1118256 (EITU9363654): NEW, sin equipment, sin gate-in, sin driver
- ET-1118242 (TGBU8815453): NEW, sin equipment, sin gate-in, sin driver
- Ambos creados por buenaguard — ya degradados a PRE-ENTRY

---

## 🚨 ALERTAS ROLAS

| # | Tipo | Detalle |
|---|---|---|
| **ALERTA-1** | 🔴 CRÍTICA | **MATU2656138: Lleno en yarda 3 días SIN receiving task.** RN-5008572 sin task generado. |
| **ALERTA-2** | 🟠 | **Coolify deploy atrasado.** GitHub tiene feed 23:18 PT pero live muestra 22:38 PT. |
| **ALERTA-3** | 🟠 | **FFAU2426030 + CSNU6323633: Sin evidencia YMS.** Promovidos por Rule #5/WMS. Verificar físicamente. |
| **ALERTA-4** | 🟡 | **MAWB 127d + ALNOR 70d:** Evaluar force close con Rufino. |
| **ALERTA-5** | 🟡 | **LE4042/PO8423: 4d+ sin iniciar recibo.** Jerome Aranda. |
| **ALERTA-6** | 🟡 | **3 citas vencidas:** PO7937, PO8357 (Jul 1), ITL07012026 (Jul 2). Sin novedad. |

---

## 🔌 ESTADO DE INFRAESTRUCTURA

| Recurso | Estado |
|---|---|
| **GitHub (03b000 main)** | ✅ Actualizado — feed 23:18 PT |
| **GitHub (master privado)** | ✅ Sincronizado — feed 23:18 PT |
| **Coolify Live Page** | ✅ HTTP 200 (pero versión 22:38 PT) |
| **Coolify Live Feed** | ⚠️ Muestra 22:38 PT (debe ser 23:18 PT) |
| **WMS** | ✅ Respondió — 17 RNs verificados |
| **YMS** | ✅ Respondió — 13 contenedores verificados |
| **Outlook** | ✅ Revisado — correos Priti/Rufino |

---

## ⚠️ NOTA SOBRE COOLIFY DEPLOY

El feed de esta corrida (23:18 PT) fue correctamente subido a ambos repositorios GitHub:
- `esaonc-ai/contenedores-priti-dashboard-03b000` (main)
- `esaonc-ai/contenedores-priti-dashboard` (master)

Sin embargo, Coolify no ha desplegado la actualización — el servidor live sigue mostrando la versión 22:38 PT. Esto es un patrón conocido (outage de ~14.5h el 2-3 de Julio). El contenido de GitHub es correcto y se reflejará cuando Coolify complete el redeploy.

---

*Reporte generado por: Agente Priti Contenedores en Yarda para Rufino*  
*Corrida: Domingo 5 Julio 2026, 23:18–23:30 PT*  
*Fuentes: Outlook (Priti Patel, Rufino, Jasmine ImportExport), WMS (17 RNs), YMS (13 ETs)*
