# 📊 CORRIDA REPORT — Contenedores Priti Dashboard
**Jul 6, 2026 — 22:20 PT** | Tenant: LT | Facility: LT_F1

---

## 🔍 FUENTES CONSULTADAS
- ✅ Outlook: Priti Patel + ImportExport@gurunanda.com (ventana Jun 21 – Jul 11)
- ✅ WMS: 41 RNs activos Gurunanda (ORG-655875)
- ✅ YMS: 6 contenedores verificados individualmente (Entry List + Equipment)
- ✅ Dashboard: feed actual leído y validado

---

## 📦 CONTENEDORES EXTRAÍDOS DE CORREOS
**46 contenedores únicos** extraídos de correos Priti/Gurunanda/ImportExport.

| Período | Cantidad | Destacados |
|---------|----------|------------|
| Jul 6-8 (futuro) | 5 | TGBU7180260, CMAU4986523, SMCU1143199, BMOU6706676, TEMU8901490 |
| Jul 1-3 | 13 | MATU2656138, OOCU5501937, CBHU7024789, FFAU2426030, CSNU6323633, TGBU8815453... |
| Jun 29-30 | 10 | CAIU9453139, JTAU7362598, OOLU9324944... |
| Jun 25-26 | 14 | MATU4542915 (RN-5008399), CAIU9721329, CSNU8888140... |
| Jun 22-24 | 4 | DDDU5053094, CAAU5246296... |

---

## 🔄 CAMBIOS APLICADOS (6)

### 🚨 #1 OCULTO: MATU2656138 (RN-5008572)
- **Evidencia WMS**: RN **CLOSED**. Receiving TASK-5309505 CLOSED (Jul 6 23:00→Jul 7 01:54). Putaway CLOSED.
- **Evidencia YMS**: **DOCK_CHECKED_OUT** Jul 6 18:54. ET-1118768. Gate check-out confirmado.
- **Acción**: Removido de activos → excluded. Ya no está en yarda.
- **⚠️ Este contenedor se mostraba EN YARDA pero ya estaba procesado completamente.**

### 🔧 #2 CORREGIDO: TGBU3785090 (RN-188086)
- **Corrección**: Spot confirmado SPOT780 (YMS ET-1117817: Drop Off Delivery FULL en SPOT780)
- Ya estaba correcto en el feed — verificado.

### 🔧 #3 CORREGIDO: LabelKing07072026 PO8449 (RN-5008571)
- **Antes**: 🟡 EN PROCESO con "recv IN_PROGRESS"
- **Después**: 🟢 EN YARDA con "recv NEW"
- **Evidencia WMS**: RN IMPORTED (no IN_PROGRESS). Receiving task TASK-5307907 en **NEW** (no ha iniciado). En yarda desde Jul 3 17:14.
- **Regla**: Anti-estado-viejo. Si receiving no ha iniciado, no puede ser EN PROCESO.
- **⚠️ ALERTA**: 4+ días en yarda sin iniciar recibo.

### ➕ #4 NUEVO: FUS07062026UNIS-58 (RN-188264)
- **Estado**: 📅 PRE-ENTRY · IMPORTED
- **Origen**: WMS — RN activo Gurunanda creado Jul 7 00:02 por rockygurunanda
- **Nota**: Sin contenedor asignado. NEED_TO_EMAIL_CARRIER. Ref: 1066840-1.

### ➕ #5 NUEVO: CORR007082026UNIS (RN-5008589 + RN-5008588)
- **Estado**: 📅 PRE-ENTRY · 2 RNs mismo contenedor
- **POs**: 8469 (cita Jul 8 18:00) + 8462 (cita Jul 8 17:00)
- **BOL**: CORRU070826UNIS

### 📝 #6 NOTA: TGBU7180260 (RN-5008591)
- Cita Jul 6 22:00-00:00 **EXPIRÓ**. YMS confirma sin gate-in.

---

## 📊 ESTADO FINAL DEL DASHBOARD

| Estado | Count |
|--------|-------|
| 🟢 EN YARDA | **2** |
| 🟡 EN PROCESO | **9** |
| 📅 PRE-ENTRY | **16** |
| 🔴 ALERTA | **0** |
| **Total Activos** | **27** |
| **Excluidos** | **39** |

### 🟢 EN YARDA
| Contenedor | RN | Ubicación | Nota |
|-----------|-----|-----------|------|
| TGBU3785090 | RN-188086 | SPOT780 | YMS confirma Drop Off en SPOT780 |
| LabelKing07072026 | RN-5008571 | DOCK38 | ⚠️ 4+ días en yarda, recv en NEW |

### 🟡 EN PROCESO (9)
JTAU7362561, CSGU6429436, GN07012026UNIS-1130, GN06302026UNIS-1129, OOCU5501937, CORR070626UNIS, CBHU7024789, FFAU2426030, CSNU6323633, ITL07012026, LabelKing07012026 (×2), ZCSU7124852, TGBU8815453

---

## 🚨 ALERTAS

| Prioridad | Alerta |
|-----------|--------|
| 🚨 **CRÍTICA** | MATU2656138 se mostraba EN YARDA pero ya estaba DOCK_CHECKED_OUT/CLOSED — OCULTADO |
| ⚠️ | LabelKing07072026: 4+ días en yarda con receiving en NEW |
| ⚠️ | TGBU7180260: cita expiró sin gate-in |
| ⚠️ | RN-5008571 (LabelKing07072026): anti-estado-viejo corrigió EN PROCESO→EN YARDA |
| 📋 | 2 nuevos RNs Gurunanda detectados en WMS (FUS07062026UNIS-58, CORR007082026UNIS) |
| 📋 | 19 RNs IMPORTED antiguos (2025-May 2026) en WMS que requieren auditoría |

---

## ⚙️ GUARDRAILS

| Guardrail | Estado |
|-----------|--------|
| antiEstadoViejo | ✅ ACTIVO — MATU2656138 ocultado, LabelKing corregido |
| staleStateGuard | ✅ ACTIVO |
| closedRemovalRule | ✅ ACTIVO |
| greenEvidenceRule | ✅ ACTIVO |
| plannedEmailInclusionRule | ✅ ACTIVO |
| preserveAssignments | ✅ ACTIVO |

---

## 📋 PRÓXIMA CORRIDA
Programada para ~22:35 PT. TGBU7180260 y GN07062026UNIS-1134 requieren re-verificación.
