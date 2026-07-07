# 📊 CORRIDA 12:00 PT — Jul 7, 2026
## Agente Priti Contenedores en Yarda — Monitoreo Continuo

---

## ✅ VERIFICACIONES COMPLETADAS

### Fuentes consultadas:
- ✅ **Outlook**: Priti Patel, ImportExport@gurunanda.com, búsqueda "Priti gurunanda"
- ✅ **Dashboard Live**: 22 activos, lastUpdated 2026-07-07T11:03:00-07:00 (⚠️ STALE)
- ✅ **WMS**: 19 RNs verificados (estados, tasks, docks)
- ✅ **YMS/WISE**: 22 contenedores verificados (gate check-in, dock, spot, arrival)

---

## 🔧 CORRECCIONES APLICADAS (8)

### FALSE GREENS CORREGIDOS → YELLOW (2):

| # | Contenedor | RN | Razón |
|---|---|---|---|
| 1 | **GN07062026UNIS-1134** | RN-188263 | YMS sin gate-in ni evidencia física. WMS IMPORTED TASK-5309896 NEW. Cita expirada. |
| 2 | **LabelKing07072026 PO8449** | RN-5008571 | YMS sin gate-in ni evidencia física. WMS IMPORTED TASK-5307907 NEW. Cita expirada. |

### PROMOVIDO A GREEN (1):

| # | Contenedor | RN | Evidencia |
|---|---|---|---|
| 3 | **CMAU8611150** | — (sin RN) | YMS ET-1118934 GATE_CHECKED_IN 2026-07-06 23:11:26, DOCK132. Drop-off delivery. UNIS espera item setup. |

### RNs ASIGNADOS (2):

| # | Contenedor | RN Asignado | Detalle |
|---|---|---|---|
| 4 | **CAAU7998380** | RN-5008646 | WMS IMPORTED, APPT-6033035 Jul 9 8AM, ET-1119189 |
| 5 | **FUS07072026UNIS-59** | RN-188301 | WMS IMPORTED, APPT-6033054 Jul 8 5PM, ET-1119229 ⚠️ NEED_TO_EMAIL_CARRIER |

### ACTUALIZACIONES DE DATOS (3):

| # | Contenedor | Cambio |
|---|---|---|
| 6 | **FUS07062026UNIS-58** | Cita actualizada: Jul 8 8PM, APPT-6033045, ET-1119213 ⚠️ NEED_TO_EMAIL_CARRIER |
| 7 | **TGBU3785090** | Dock corregido: DOCK61 → SPOT780 (YMS ET-1117817 DOCK_CHECKED_IN desde Jul 2) |
| 8 | **CSNU6323633** | Notas: YMS NEED_WINDOW_CHECK_IN, gate check-in NUNCA completado (Jul 6 18:21) |

---

## 📈 RESUMEN POST-CORRECCIÓN

| Color | Count | Contenedores |
|---|---|---|
| 🟢 GREEN | **1** | CMAU8611150 (DOCK132, sin RN) |
| 🟡 YELLOW | **9** | GN07012026UNIS-1130, TGBU3785090, CBHU7024789, FFAU2426030, CSNU6323633, ZCSU7124852, TGBU8815453, GN07062026UNIS-1134, LabelKing PO8449 |
| ⚪ NORMAL | **12** | MRKU9388930, TGBU7180260, EITU9363654, TEMU8901490, BMOU6706676, SMCU1143199, CMAU4986523, FUS07062026UNIS-58, CORR PO8469, CORR PO8462, CAAU7998380, FUS07072026UNIS-59 |
| 🔴 RED | **0** | — |
| **Total Active** | **22** | |
| **Total Excluded** | **40** (acumulado) | |

---

## 🚨 ALERTAS

### CRÍTICAS:
1. **🚨 COOLIFY NO DESPLEGANDO**: GitHub repo (`esaonc-ai/contenedores-priti-dashboard-03b000`) tiene el feed corregido (commit f9c3ec1), pero el dashboard live sigue mostrando datos de las 11:03 PT. Los FALSE GREENS GN07062026UNIS-1134 y LabelKing PO8449 siguen visibles como GREEN en producción.

2. **⚠️ FALSE GREENS ACUMULADOS: 5** en las últimas 2 horas (3 en corrida 10:00 + 2 en corrida 12:00). El guardrail `antiEstadoViejo` requiere ajuste: YARD_CHECK no debe contar como evidencia de yarda.

### OPERACIONALES:
3. **⚠️ CMAU8611150**: EN YARDA en DOCK132 desde Jul 6 23:11, sin RN, UNIS espera item setup `11-16-5CT-40402-6A`. Cita HOY 1:00-3:00 PM. ¡URGENTE!
4. **⚠️ CBHU7024789**: EN_PROCESO sin receiving ni putaway tasks. Anomalía persistente.
5. **⚠️ CSNU6323633**: NEED_WINDOW_CHECK_IN. Gate check-in nunca completado.
6. **⚠️ TGBU8815453**: DOCK_CHECKED_OUT sin gate-out. Reportado VACÍO.
7. **⚠️ NEED_TO_EMAIL_CARRIER**: FUS07062026UNIS-58 (Jul 8 8PM), FUS07072026UNIS-59 (Jul 8 5PM)
8. **⚠️ Citas vencidas**: MRKU9388930 (Jul 6), EITU9363654 (Jul 3 - 4 días), SMCU1143199 (hoy 01:00 AM), TGBU7180260 (hoy 05:00 AM)

---

## 🔍 VERIFICACIÓN CRUZADA OUTLOOK

Todos los contenedores anunciados por Priti/ImportExport están visibles en el dashboard:

| Email | Contenedor | Dashboard |
|---|---|---|
| Priti Jul 7 10:32 AM | CMAU8611150 | ✅ GREEN (DOCK132) |
| Priti Jul 7 10:32 AM | CAAU7998380 | ✅ NORMAL (RN-5008646) |
| Priti Jul 6 2:59 PM | SMCU1143199 | ✅ NORMAL |
| Priti Jul 6 2:59 PM | CMAU4986523 | ✅ NORMAL |
| Priti Jul 6 2:59 PM | TGBU7180260 | ✅ NORMAL |
| ImportExport Jul 6 9:57 AM | BMOU6706676 | ✅ NORMAL |
| Priti Jul 6 11:19 AM | ZCSU7124852 | ✅ YELLOW |
| Nitin Receiving Pendencies | FFAU2426030, CSNU6323633, CBHU7024789, EITU9363654, TGBU8815453 | ✅ Todos visibles |

---

## 📋 ESTADO GUARDRAILS

| Guardrail | Estado |
|---|---|
| Schedule (cada 15 min) | ✅ ACTIVE |
| RN Primary Key | ✅ ACTIVE |
| Anti-Estado-Viejo | ⚠️ GENERANDO FALSE GREENS (5 acumulados) |
| Closed Removal Rule | ✅ ACTIVE |
| Green Evidence Rule | ✅ ACTIVE (corrigiendo) |
| Planned Email Inclusion Rule | ✅ ACTIVE |
| Stale State Guard | ✅ ACTIVE |

---

## 🔧 ACCIÓN REQUERIDA

**Rufino**: Se necesita acceso al panel Coolify para forzar el redeploy del recurso `contenedores-priti-dashboard-03b000`. El código en GitHub (`main`) está correcto pero el dashboard live está stale con 2 FALSE GREENS activos.

*Reporte generado: 2026-07-07 12:16 PT | Agente Priti Contenedores en Yarda*
