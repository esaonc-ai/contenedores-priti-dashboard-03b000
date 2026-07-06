# CORRIDA PRITI/GURUNANDA — Jul 05 19:45 PT
## Resumen Ejecutivo

| Métrica | Valor |
|---|---|
| **Total activos** | 25 |
| 🟢 EN YARDA | 9 |
| 🟡 EN PROCESO | 7 |
| 🟠 DEGRADADOS | 2 |
| 🔵 PRE-ENTRY | 6 |
| 🔵 OUTBOUND | 1 |
| Excluidos/Removidos | 27 |
| **Cambios de estado** | 0 (sin cambios requeridos) |
| **ANTI-STALE** | ✅ CLEAN |

---

## Validación YMS+WMS de TODOS los 25 activos:

### 🟢 EN YARDA (9) — TODOS CONFIRMADOS
| # | Contenedor | RN | Evidencia YMS | WMS Status |
|---|---|---|---|---|
| 1 | TGBU3785090 | RN-188086 | SPOT780 DROP_OFF_DELIVERY Jul 2 | IMPORTED, TASK-5307685 NEW |
| 2 | CBHU7024789 | RN-5008507 | YARD_CHECK Jul 2 (buenaguard) | IMPORTED, TASK-5307687 NEW |
| 3 | FFAU2426030 | RN-5008480 | YARD_CHECK Jul 2 (buenaguard) | IMPORTED, TASK-5307691 NEW |
| 4 | CSNU6323633 | RN-5008483 | YARD_CHECK Jul 2 (buenaguard) | IMPORTED, TASK-5307689 NEW |
| 5 | LE4042 (PO8423) | RN-5008450 | LIVE_DELIVERY DOCK45 Jul 1 | IMPORTED, TASK-5305892 NEW |
| 6 | LabelKing PO8449 | RN-5008571 | WINDOW_CHECKED_IN DOCK38 Jul 3 | IMPORTED, TASK-5307907 NEW |
| 7 | MATU2656138 | RN-5008572 | GATE_CHECKED_IN DROP_OFF Jul 2 | IMPORTED, sin recv task |
| 8 | EITU9363654 | RN-5008569 | YARD_CHECK Jul 3 noche | IMPORTED, sin recv task |
| 9 | TGBU8815453 | RN-5008570 | YARD_CHECK Jul 3 noche | IMPORTED, sin recv task |

### 🟡 EN PROCESO (7) — TODOS CONFIRMADOS
| # | Contenedor | RN | Recv Task | YMS | Putaway |
|---|---|---|---|---|---|
| 10 | DDDU5053860 ⚠️ | RN-5008447 | TASK-5307692 IN_PROGRESS | DOCK_CHECKED_IN SPOT675 | Pendiente |
| 11 | TCKU6977609 ⚠️ | RN-5008481 | TASK-5307690 IN_PROGRESS | DOCK_CHECKED_IN SPOT775 | Pendiente |
| 12 | OOCU5501937 ⚠️ | RN-5008506 | TASK-5307688 IN_PROGRESS | DOCK_CHECKED_IN SPOT688 | Pendiente |
| 13 | JTAU7362561 ⚠️ | RN-5008446 | TASK-5307533 IN_PROGRESS | DOCK_CHECKED_IN DOCK65 | Pendiente |
| 14 | CSGU6429436 | RN-5008479 | TASK-5306174 IN_PROGRESS | DOCK_CHECKED_IN DOCK45 | Pendiente |
| 15 | GN07012026UNIS-1130 | RN-188044 | TASK-5306724 IN_PROGRESS | DOCK_CHECKED_OUT DOCK41 | Pendiente |
| 16 | GN07012026UNIS-1132 | RN-188084 | TASK-5307686 CLOSED ✅ | NEED_WINDOW_CHECK_IN | TASK-5307890 IN_PROGRESS |

### 🟠 DEGRADADOS (2)
| # | Referencia | RN | Días estancado |
|---|---|---|---|
| 17 | MAWB 00120698274 | RN-5006269 | 125d+ DOCK62 |
| 18 | ALNOR04242026 | RN-183707 | 71d+ DOCK65 |

### 🔵 PRE-ENTRY (6) — Sin evidencia de llegada en YMS
| # | Contenedor | RN | Cita |
|---|---|---|---|
| 19 | TEMU8901490 | RN-5008566 | Jul 7 09:00 |
| 20 | CORR070626UNIS | RN-5008505 | Jul 6 17:00 WILL CALL |
| 21 | LabelKing PO7937 | RN-5008449 | Jul 1 (VENCIDA) |
| 22 | LabelKing PO8357 | RN-5008444 | Jul 1 (VENCIDA) |
| 23 | ITL07012026 | RN-187990 | Jul 2 (VENCIDA) |
| 24 | MRKU9388930 | RN-188088 | Jul 6 16:00 |

### 🔵 OUTBOUND (1)
| # | Referencia | Estado |
|---|---|---|
| 25 | DN-3236621 (Trailer 53176) | LOADED, 28 pallets |

---

## 🔴 HALLAZGOS CRÍTICOS

### 1. DISCREPANCIA JONATHAN HEREDIA vs YMS/WMS
Jonathan reportó EMPTY para 4 contenedores (DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561) el 07/04.
- **YMS**: NINGUNO tiene gate check-out de vacío (empty pickup)
- **WMS**: Los 4 tienen receiving task IN_PROGRESS (no cerrado)
- **Conclusión**: WMS ES AUTORITATIVO. Se mantienen EN PROCESO. ⚠️ Verificar físicamente si ya están vacíos.

### 2. YARD_CHECK sin gate check-in
5 contenedores (CBHU7024789, FFAU2426030, CSNU6323633, EITU9363654, TGBU8815453) tienen solo YARD_CHECK como evidencia YMS — sin gate check-in formal. YARD_CHECK es escaneo físico por personal de yarda = presencia real. Se mantienen EN YARDA.

### 3. ANTI-ESTADO-VIEJO: CLEAN
0 PRE-ENTRY con evidencia física de llegada. Todos verificados contra YMS.

### 4. Sin remociones nuevas
Ningún RN tiene receiving + putaway ambos cerrados. GN07012026UNIS-1132 (RN-188084) tiene recv CLOSED pero putaway IN_PROGRESS.

---

## Fuentes de verificación
- YMS Agent: verificación de 16 ETs, 9 sin ET (búsqueda por equipment/paging)
- WMS Agent: verificación de 25 RNs, estados de recibo y tareas
- Outlook Agent: 12 contenedores en correos Priti Jun 29-Jul 4
- BI Agent: dashboard feed live, 25 activos confirmados

---
*Corrida ejecutada: Jul 05 19:45 PT por Agente Priti*
