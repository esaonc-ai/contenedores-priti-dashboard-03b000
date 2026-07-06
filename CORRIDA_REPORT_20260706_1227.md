# 📊 CORRIDA MONITOREO — Priti Dashboard — 2026-07-06 12:14-12:27 PT

**Agente:** Priti Containers Yarda Agent  
**Modo:** SOLO LECTURA (Outlook/YMS/WISE/WMS)  
**Frecuencia:** Cada 15 min, 24/7  
**Dashboard:** https://contenedores-priti-dashboard-03b000.coolify.item.pub/

---

## 🔍 FUENTES CONSULTADAS

| Fuente | Estado | Resultados |
|--------|--------|------------|
| **Outlook** | ✅ | 32 correos Priti/Gurunanda, 46 contenedores extraídos |
| **Dashboard HTTP** | ✅ | 200 OK, nginx 1.31.2 |
| **Dashboard Feed** | ✅ | JSON válido, sin raw.githubusercontent.com real |
| **YMS/WISE** | ✅ | 21 contenedores verificados (3 OK, 17 sin ET, 1 parcial) |
| **WMS** | ✅ | 22 RNs activos verificados + 37 contenedores email cruzados |

---

## 📬 OUTLOOK — Correos Priti (ventana 21-Jun a 11-Jul-2026)

- **32 correos** de `priti@gurunanda.com` (Priti Patel)
- **46 contenedores** formato 4L+7D extraídos
- **1 MAWB cancelado**: 00120698274 (confirmado por Priti Jul 6)
- **1 ticket UNIS**: UFB-124862
- **Contenedor HOY**: ZCSU7124852 — Live Unloading Jul 6 12:00-14:00 (ya en dash PRE-ENTRY)
- **Destacados**: OOCU7355889 (cambio cita), DDDU5053860 (cambio cita), CAIU9721329 (múltiples cambios)

---

## 🔄 CORRECCIONES APLICADAS

### 🚨 FALSE GREEN CORREGIDO → PRE-ENTRY
| Contenedor | RN | De | A | Evidencia |
|-----------|-----|----|---|-----------|
| **EITU9363654** | RN-5008569 | 🟢 EN YARDA | 📅 PRE-ENTRY | YMS: PRE_ENTRY sin llegada. WMS: sin inYard, sin receiving task. Cita APPT-6032800 venció Jul 03. |

### ❌ REMOVIDO → EXCLUDED
| RN | Contenedor | Motivo |
|----|-----------|--------|
| **RN-188031** | GN06302026UNIS-1129 (53169) | receiving FORCE_CLOSED + putaway CLOSED. RN PARTIAL_RECEIVED pero ambas tareas cerradas. |

### 🟢 PROMOVIDOS A VERDE (WMS reconfirmado)
| Contenedor | RN | Evidencia |
|-----------|-----|-----------|
| **CBHU7024789** | RN-5008507 | WMS: inYard Jul 3, DOCK108, TASK-5307687 NEW (Caren Cubides) |
| **FFAU2426030** | RN-5008480 | WMS: inYard Jul 3, DOCK128, TASK-5307691 NEW (Caren Cubides) |
| **CSNU6323633** | RN-5008483 | WMS: inYard Jul 3, DOCK124, TASK-5307689 NEW (Caren Cubides) |
| **LabelKing07072026** | RN-5008571 | YMS: WINDOW_CHECKED_IN DOCK38 + WMS: inYard + TASK-5307907 NEW |

### ✅ MANTENIDOS SIN CAMBIO
| Contenedor | RN | Estado | Nota |
|-----------|-----|--------|------|
| TGBU3785090 | RN-188086 | 🟢 EN YARDA SPOT780 | YMS Drop Full confirmado |
| MATU2656138 | RN-5008572 | 🟢 EN YARDA SIN SPOT | YMS GATE_CHECKED_IN Jul 2, 3.7d sin spot |
| JTAU7362561 | RN-5008446 | 🟡 EN PROCESO DOCK65 | putaway IN_PROGRESS |
| CSGU6429436 | RN-5008479 | 🟡 EN PROCESO DOCK68 | putaway IN_PROGRESS |
| GN07012026UNIS-1130 | RN-188044 | 🟡 EN PROCESO DOCK3 | receiving IN_PROGRESS |
| OOCU5501937 | RN-5008506 | 🟡 EN PROCESO DOCK59 | putaway IN_PROGRESS |
| LabelKing PO8423 | RN-5008450 | 🟡 EN PROCESO DOCK45 | putaway NEW |
| LabelKing PO7937 | RN-5008449 | 🟡 EN PROCESO DOCK41 | putaway NEW |
| LabelKing PO8357 | RN-5008444 | 🟡 EN PROCESO DOCK38 | putaway NEW |
| TGBU8815453 | RN-5008570 | 📅 PRE-ENTRY | Cita Jul 03 venció, sin llegada |
| TEMU8901490 | RN-5008566 | 📅 PRE-ENTRY | Cita Jul 07 |
| CORR070626UNIS | RN-5008505 | 📅 PRE-ENTRY | Cita Jul 06 |
| ITL07012026 | RN-187990 | 📅 PRE-ENTRY | Sin cita |
| MRKU9388930 | RN-188088 | 📅 PRE-ENTRY | Sin cita |
| BMOU6706676 | RN-5008587 | 📅 PRE-ENTRY | Cita Jul 08 |
| ZCSU7124852 | RN-5008586 | 📅 PRE-ENTRY | Cita HOY Jul 06 12-14 Live |

---

## 📊 ESTADO FINAL DEL DASHBOARD

| Color | Cantidad | Significado |
|-------|----------|-------------|
| 🟢 **green** | **6** | EN YARDA (5 WMS confirmado + 1 TGBU3785090 YMS Drop Full) |
| 🟡 **yellow** | **7** | EN PROCESO (receiving/putaway activo) |
| 📅 **normal** | **8** | PRE-ENTRY (sin llegada confirmada) |
| ⬜ **excluded** | **32** | CLOSED/FORCE_CLOSED/CANCELLED |
| **TOTAL ACTIVOS** | **21** | |

---

## 📦 37 CONTENEDORES EMAIL VERIFICADOS (cruce WMS)

| Estado | Cantidad |
|--------|----------|
| CLOSED | 27 |
| FORCE_CLOSED | 8 |
| IMPORTED (activo) | 1 (ZCSU7124852 — ya en dash) |
| SIN RN | 1 (EITU8162104) |

**Conclusión:** Ningún contenedor nuevo requiere ser agregado. Todos los procesados ya están cerrados.

---

## 🚨 ALERTAS DETECTADAS

### 🔴 ALERTA ROLAS CRÍTICA (2)
1. **FALSE GREEN EITU9363654** — Estaba EN YARDA pero YMS PRE_ENTRY sin llegada, WMS sin inYard ni task. **CORREGIDO:** demoted a PRE-ENTRY.
2. **MATU2656138 SIN SPOT** — 3.7 días en yarda desde GATE_CHECKED_IN Jul 2 20:11. Sin dock asignado, sin receiving task.

### 🟠 ALERTA ROLAS (5)
3. **RN-188031 removido** — receiving FORCE_CLOSED + putaway CLOSED. Removido a excluded.
4. **CBHU/FFAU/CSNU verde por WMS** — Promovidos a verde con evidencia WMS (inYard+dock+task) pero YMS ET no localizado. Verificar Entry List.
5. **LabelKing PO8449 verde** — YMS WINDOW_CHECKED_IN + WMS inYard+task confirman EN YARDA.
6. **ZCSU7124852 en PRE-ENTRY** — Cita HOY 12:00-14:00 Live Unloading. Monitorear próxima corrida.
7. **EITU9363654 sin llegada** — Cita venció Jul 03, YMS PRE_ENTRY. ¿Cancelar RN?

### 🔵 INFO (2)
8. Todos los RN son cliente GURUNANDA, LLC (ORG-655875). ✅
9. MAWB 00120698274 confirmado cancelado por Priti (Jul 6), ya excluido del dashboard.

---

## 🛡️ WATCHDOG TÉCNICO

| Verificación | Estado |
|-------------|--------|
| Dashboard HTTP | ✅ 200 OK (nginx/1.31.2) |
| Feed JSON válido | ✅ |
| raw.githubusercontent.com | ✅ Ausente (solo en texto de alerta) |
| Sin duplicados activos | ✅ |
| Feed GitHub actualizado | ✅ Commit 8b32307 (21 rows) |
| Feed Dashboard servido | ⚠️ Coolify sin recoger deploy (sirve versión 19:18 con 22 rows) |

---

## ⚠️ INCIDENCIA DE DESPLIEGUE

El commit `8b32307` con el feed corregido (21 rows) está en GitHub `esaonc-ai/contenedores-priti-dashboard-03b000` pero Coolify no ha recogido el cambio. El dashboard aún sirve la versión anterior (lastUpdated 19:18, 22 rows).

**Archivo corregido disponible:** `container-feed-CORREGIDO-20260706-1226PT.json` (65.5 KB)

**Acción requerida:** Forzar redeploy en Coolify o desplegar manualmente al servidor.

---

## 📋 PRÓXIMA CORRIDA

- **ZCSU7124852**: Verificar si ya tiene gate check-in (cita Live Unloading hoy 12:00-14:00)
- **CORR070626UNIS (RN-5008505)**: Cita hoy Jul 06 17:00 — verificar llegada
- **MATU2656138**: Monitorear asignación de spot/dock
- **EITU9363654**: Evaluar si se debe cancelar el RN (cita venció Jul 03, sin llegada)
- **Coolify**: Verificar si el deploy ya se aplicó

---

*Reporte generado: 2026-07-06T12:27:00-07:00 | Próxima corrida: ~12:30 PT*
