# CORRIDA Jul 6, 2026 11:01 AM PT — Priti/Gurunanda Dashboard

## Resumen
- **Total activos:** 19 (↓ de 20)
- **EN YARDA (green):** 6
- **WILL CALL (yellow):** 3
- **PRE-ENTRY (normal):** 10
- **Excluidos:** 33 (+2)

## Cambios aplicados

### 🗑️ Removidos (2)
| Contenedor | RN | Razón |
|-----------|-----|-------|
| DDDU5053860 | RN-5008447 | RN CLOSED + recv TASK-5307692 CLOSED + Gate Checked Out YMS |
| TCKU6977609 | RN-5008481 | RN CLOSED + recv TASK-5307690 CLOSED + Gate Checked Out YMS |

### 🆕 Nuevo (1)
| Contenedor | RN | Detalle |
|-----------|-----|---------|
| BMOU6706676 | PENDIENTE | ETA Jul 8 2-4 AM, reportado por Jasmine (Priti). Sin RN ni ET. |

### 📌 Spots actualizados (YMS verified)
- OOCU5501937: SPOT159 → SPOT688 (YMS ET-1117844)
- TGBU3785090: SPOT121 → SPOT780 (YMS ET-1117817)

### 🧹 Datos limpios (WMS confirmed)
- CBHU7024789 (RN-5008507): sin receiving task, sin Entry List → dock/recv removidos
- FFAU2426030 (RN-5008480): sin receiving task, sin Entry List → dock/recv removidos
- CSNU6323633 (RN-5008483): sin receiving task, sin Entry List → dock/recv removidos

### 📝 Notas actualizadas
- CORR070626UNIS: APPT-6032610 hoy Jul 6 5pm
- LabelKing PO8449: ET-1118515 PRE_ENTRY creado Jul 6 09:56
- JTAU7362561: LIVE_DELIVERY, equipmentNo=NULL en YMS ET-1117729

## Verificación cruzada
- **WMS**: 20/20 RNs verificados ✅
- **YMS**: 8/8 ETs verificados ✅
- **Outlook**: 3 correos no leídos (Nitin OVER 48hrs, Tyler ASN PO8449, Jasmine BMOU6706676)

## Alertas activas
1. 🚨 MATU2656138 ~100h SIN SPOT ni receiving task
2. ⚠️ Nitin OVER 48hrs: JTAU7362561, CSGU6429436, GN07012026UNIS-1130
3. ⚠️ TGBU3785090 recv NEW pese a Entry List ✅
4. ⚠️ OOCU5501937 + GN07012026UNIS-1130: putaway NONE
5. 🔴 3 falsos green corregidos (CBHU, FFAU, CSNU)
6. 📋 TEMU8901490 cita MAÑANA Jul 7 09:00-11:00
7. 📋 CORR070626UNIS APPT-6032610 HOY 5pm

## Fuentes
- WMS: Entry List + RN status + tasks
- YMS: GET /level2/entry-ticket/{id} por ET específico
- Outlook: revisión de correos Priti/Nitin/Jasmine
- Feed previo: container-feed.json 09:50 PT
