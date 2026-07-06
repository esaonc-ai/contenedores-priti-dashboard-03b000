# CORRIDA REPORT — 00:54 PT Jul 6 2026

## RESUMEN
- **Total activos**: 25 (sin cambio)
- **Nuevos agregados**: 0
- **RN encontrados**: 0 nuevos
- **En yarda confirmados por Entry List**: 4 (TGBU3785090, LE4042/PO8423, PO8449, MATU2656138)
- **En proceso**: 7
- **Falsos green corregidos esta corrida**: 3
- **Removidos por receiving+putaway cerrados**: 0 nuevos
- **Alertas críticas**: 1 (3 falsos green corregidos)

## 🔴 ACCIÓN CRÍTICA: 3 FALSOS GREEN DEGRADADOS

Los siguientes 3 contenedores fueron DEGRADADOS de EN YARDA (verde) a FALSO GREEN (naranja):

| Contenedor | RN | Dock | Evidencia |
|---|---|---|---|
| **CBHU7024789** | RN-5008507 | DOCK108 | Entry List ❌ No Data · YMS solo YARD_CHECK ET-1117841 (sin gate-in) |
| **FFAU2426030** | RN-5008480 | DOCK128 | Entry List ❌ No Data · YMS solo YARD_CHECK ET-1117840 (sin gate-in) |
| **CSNU6323633** | RN-5008483 | DOCK124 | Entry List ❌ No Data · YMS solo YARD_CHECK ET-1117846 (sin gate-in) |

**Razón**: WMS Entry List search devuelve **No Data** para los tres contenedores (verificado tanto por containerNO como por receiptId). YMS solo tiene YARD_CHECK records (NEW, sin gate-in, sin equipment, sin driver — creados por `buenaguard`). Regla Rolas #3: Dock asignado, RN IMPORTED, inYardTime ambiguo o receiving task NEW NO bastan por sí solos. Sin Entry List ✅ DATA o YMS gate-in real = NO VERDE.

Estos 3 habían sido re-promovidos en la corrida 00:13 PT basándose en WMS tasks+docks+inYardTime. Esta corrida aplicó la Regla #3 estrictamente con verificación cruzada WMS+WISE+YMS.

## 🟢 4 VERDES REALES CONFIRMADOS

| Contenedor | Entry List | Evidencia Adicional |
|---|---|---|
| **TGBU3785090** | ✅ DATA ET-1117817 (Gate Checked Out) | YMS gate-in SPOT780 Jul 2 |
| **LE4042/PO8423** | ✅ DATA ET-1116794 (Gate Checked Out) | YMS LIVE_DELIVERY DOCK45 Jul 1 |
| **PO8449** | ✅ DATA ET-1118067 (Window Checked In) | YMS WINDOW_CHECKED_IN DOCK38 Jul 3 |
| **MATU2656138** | ✅ DATA ET-1117774 (Gate Checked In) | YMS GATE_CHECKED_IN Jul 2 HAW TRUCKING |

## 🟡 7 EN PROCESO (sin cambios)
DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561, CSGU6429436, GN07012026UNIS-1130, GN07012026UNIS-1132

## 🚨 5 DEGRADADOS TOTAL
3 nuevos (CBHU/FFAU/CSNU) + 2 existentes (MAWB 125d+, ALNOR 71d+)

## 📅 8 PRE-ENTRY (sin cambios)
EITU9363654, TGBU8815453, TEMU8901490, CORR070626UNIS, LabelKing PO7937, LabelKing PO8357, ITL07012026, MRKU9388930

## 🔵 CITAS HOY Jul 6
- MRKU9388930: 16:00 (20 pallets Alnor)
- CORR070626UNIS: 17:00 (WILL CALL)
- TGBU3785090: 15:00 (NEED_TO_EMAIL_CARRIER)

## ⚠️ ALERTAS PENDIENTES
- MAWB 125d+ y ALNOR 71d+ requieren force close (Rufino)
- LE4042/PO8423: recv NEW 4d+ (Jerome Aranda)
- CSGU6429436: recv IN_PROGRESS 3.5d+ (Fatima)
- MATU2656138: en yarda sin spot ni receiving task
- CBHU/FFAU/CSNU: en limbo — WMS tasks+docks existen pero sin Entry List ni YMS gate-in. Requieren investigación física

## 🔧 VERIFICACIÓN CRUZADA
- WMS Entry List: verificado para los 7 EN YARDA originales → 3 sin datos
- YMS gate-in: verificado para todos los contenedores
- WMS receiving/putaway tasks: 4 removidos confirmados (MRKU9748297, DDDU5053432, MRKU6829749, OOCU7355889)
- Outlook: ambos flujos revisados (Priti + Rufino/forward), sin nuevos contenedores

## 📊 DISTRIBUCIÓN FINAL
- 🟢 En Yarda: 4
- 🟡 En Proceso: 7
- 🚨 Degradados: 5
- 📅 PRE-ENTRY: 8
- 🚛 Transfer: 1
- Total: 25 activos | 27 excluidos
- Falsos green total histórico: 8
