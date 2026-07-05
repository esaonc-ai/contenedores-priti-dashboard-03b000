# 📊 CORRIDA — MATU2656138 PROMOCIÓN DEGRADADO→EN YARDA
**Fecha/Hora:** Domingo 5 Julio 2026, 04:50 AM PT  
**Agente:** PritiAgent (via Agente Priti Contenedores)  
**Repositorio:** esaonc-ai/contenedores-priti-dashboard-03b000  
**Dashboard Live:** https://contenedores-priti-dashboard-03b000.coolify.item.pub/

---

## 📋 RESUMEN

| Métrica | Antes | Después |
|---|---|---|
| 🟢 EN YARDA | 6 | **7** |
| 🟡 EN PROCESO | 7 | 7 |
| 🟠 DEGRADADOS | 3 | **2** |
| 📅 PRE-ENTRY | 8 | 8 |
| 📋 TRANSFER | 1 | 1 |
| **Total activos** | 25 | 25 |
| **Excluidos** | 26 | 26 |

---

## 🔄 CAMBIO APLICADO

### MATU2656138 (RN-5008572): DEGRADADO → EN YARDA 🟢

**Evidencia que soporta la promoción (Regla Rolas #3 cumplida):**

| Evidencia | Detalle |
|---|---|
| **WMS Entry List** | ✅ ET-1117774 — CONFIRMED. Gate Checked In by NATHAN HAO, HAW TRUCKING INC, DROP_OFF_DELIVERY |
| **YMS** | GATE_CHECKED_IN Jul 2 20:11 PT, sin check-out |
| **RN** | RN-5008572 (existe en WMS, IMPORTED, sin receiving task) |
| **Dock** | Sin dock asignado |
| **PO** | PO# 8190/8107/8144 |

**Estado anterior:** 🟠 DEGRADADO — degradado en corrida 04:05 PT por "Entry List NO DATA" y "dropOffLocationId null"  
**Estado nuevo:** 🟢 EN YARDA — Entry List ✅ + YMS GATE_CHECKED_IN confirmado

**Campos modificados:**
- `color`: orange → green
- `inYard`: se mantiene True
- `status`: Actualizado a "🟢 EN YARDA — Entry List ✅ ET-1117774 · Gate Check-In confirmado · Sin receiving task · RN-5008572"
- `entry`: Actualizado con evidencia de Entry List
- `note`: Narración completa de la promoción
- `alerta`: Degradado a informativo (sin receiving task)
- `ymsStatus`: Actualizado con DROP_OFF_DELIVERY y Entry List
- `lastVerifiedAt`: 2026-07-05T04:50:00-07:00
- `verificationSource`: WMS Entry List ET-1117774 + YMS GATE_CHECKED_IN
- `staleStateGuard`: Actualizado
- `promotionReason`: Documentado con evidencia
- **Removidos**: degradedAt, degradedFrom, degradedReason, notesCleanupReason, antiFalseGreenRule

---

## ✅ VERIFICACIONES

### GitHub (raw.githubusercontent.com)
- ✅ `lastUpdated`: 2026-07-05T04:50:00-07:00
- ✅ `enYarda`: 7, `degradados`: 2
- ✅ MATU2656138: `color=green`, `inYard=True`
- ✅ `main` y `master` sincronizados

### Coolify Live
- ⚠️ **NO DESPLEGADO** — Mismo problema recurrente reportado desde Jul 2-4
- El feed live muestra datos de la corrida 04:35 PT (sin la promoción)
- Se requiere intervención manual en Coolify Dashboard para forzar redeploy

---

## ⚠️ ALERTA ROLAS CRÍTICA

**Coolify no está haciendo auto-deploy.** Los cambios están correctamente en GitHub (`main` y `master`, commit 3f7c09d). El live feed (coolify.item.pub) sigue mostrando la corrida 04:35 PT sin la promoción de MATU2656138.

**Acción requerida:** Intervención manual en Coolify Dashboard > Proyecto contenedores-priti-dashboard-03b000 > Force Redeploy.

**Mientras tanto**, los datos correctos están disponibles en:
- https://raw.githubusercontent.com/esaonc-ai/contenedores-priti-dashboard-03b000/main/public/container-feed.json
