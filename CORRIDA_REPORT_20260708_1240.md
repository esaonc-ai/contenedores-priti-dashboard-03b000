# 📊 CORRIDA PRITI/GURUNANDA — 2026-07-08 12:40 PT

## 🔢 Totales Finales

| | Antes (repo 22:20 PT Jul 7) | **Actualizado (12:40 PT)** |
|---|---|---|
| 🟢 Green | 2 | **8** |
| 🟡 Yellow | 6 | **6** |
| ⚪ Normal | 15 | **13** |
| 🔴 Red | 0 | 0 |
| **Total Activos** | 23 | **27** |
| **Total Excluidos** | 11 | **17** |

---

## 🔴 REMOVIDOS (closedRemovalRule)

| Contenedor | RN | Motivo |
|---|---|---|
| **TEMU8901490** | RN-5008566 | Receiving TASK-5310655 CLOSED + Putaway TASK-5310957 CLOSED |

---

## 🟢 PROMOVIDOS A GREEN / EN YARDA (antiEstadoViejo)

| Contenedor | RN | Evidencia YMS |
|---|---|---|
| **SMCU1143199** | RN-5008592 | Gate check-in 2026-07-08 01:38, ET-1119613 |
| **TGBU7180260** | RN-5008591 | Yard check FULL 07-Jul 21:44, ET-1118984 |
| **MRKU9388930** | RN-188088 | Yard check FULL 07-Jul 21:11, ET-1118963 |

---

## 🟡 PROMOVIDOS A YELLOW / EN PROCESO (antiEstadoViejo)

| Contenedor | RN | Evidencia |
|---|---|---|
| **EITU9363654** | RN-5008569 | Gate check-in 08-Jul 12:22, DOCK65, TASK-5311282 IN_PROGRESS (Caren) |

---

## ➕ NUEVOS CONTENEDORES (Outlook + WMS)

| Contenedor | RN | Cita | Origen |
|---|---|---|---|
| **TGSU5157420** | RN-5008666 | 07/08 20:00-22:00 | ImportExport (Jasmine) |
| **TGSU5157415** | RN-5008667 | 07/09 16:00-18:00 | ImportExport (Jasmine) |
| **GN07082026UNIS-1137** | RN-188400 | Sin cita | WMS |
| **TIIU6675897** | SIN RN | 07/09 12:00-14:00 | Jasmine (corrección TIIU6671567) |

---

## 📝 RNs ENRIQUECIDOS

| Contenedor | RN Nuevo |
|---|---|
| ZCSU7781965 | RN-5008664 |
| TGBU5468303 | RN-5008665 |

---

## ⚠️ NOTAS ACTUALIZADAS

- **TIIU6671567 (RN-5008661)**: ⚠️ Jasmine corrigió este contenedor a TIIU6675897
- **FFAU2426030 (RN-5008480)**: YMS yard check EMPTY. Putaway TASK-5311289 NEW
- **CMAU8611150**: SIN RN. Item setup pendiente WSP-162550

---

## 🔔 ALERTAS GENERADAS

### 🔴 ALERTA ROLAS CRÍTICA
- **CMAU8611150** — SIN RN en WMS, físicamente en DOCK132 desde Jul 6. Item setup WSP-162550 pendiente.
- **CSGU6429436 (RN-5008479)** — CONTENEDOR FANTASMA en DOCK45. RN cerrado pero equipo físico presente desde Jul 1.

### 🟠 ALERTA ROLAS
- **LabelKing07072026 (RN-5008571)** — 4 DÍAS en yarda sin receiving completado.
- **FFAU2426030 (RN-5008480)** — YMS yard check EMPTY. Posible vacío listo para pickup.
- **TIIU6671567 (RN-5008661)** — Número corregido por Jasmine a TIIU6675897. Verificar.
- **TGBU8815453** — Confirmado EMPTY en yarda, listo para pickup por Daniela Gonzalez.

### ℹ️ INFORMACIÓN
- 9 contenedores sin actividad YMS (citas futuras/no llegados aún)
- YMS API search-by-paging devuelve error 500 — posible problema técnico

---

## 🛠️ DEPLOY

- Commit `4da476b`: feed actualizado
- Commit `1abff35`: FORCE_DEPLOY trigger
- Rama: main → GitHub: esaonc-ai/contenedores-priti-dashboard-03b000
