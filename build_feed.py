#!/usr/bin/env python3
"""Build complete container-feed.json for CICLO 06/30 20:00 PT."""
import json
from datetime import datetime, timezone, timedelta

now_pt = datetime.now(timezone(timedelta(hours=-7)))
ts = now_pt.strftime('%Y-%m-%dT%H:%M:%S-07:00')

feed = {
    "lastUpdated": ts,
    "message": f"CICLO 06/30 20:00 PT — WMS+YMS+Outlook LIVE cross-ref. 32 activos (15g/7y/0r/10n). ANTI-STALE CLEAN. RNs verificados Gurunanda: CAIU9453139, OOCU8342103, BSIU8440908 (corrección WMS). Citas Jul 1-3 CONFIRMADAS UNIS. Outlook: +2 vacíos Rufino Jun 26.",
    "totalActive": 32,
    "totalExcluded": 51,
    "rows": [],
    "excludedContainers": [],
    "summary": {},
    "alerts": [],
    "guardrails": {},
    "emailMonitor": {},
    "messageTimestamp": ts
}

# ============================================================
# GREEN ROWS (15)
# ============================================================
green_rows = [
    {
        "container": "JTAU7362582",
        "rn": "RN-5008426",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008426",
        "dock": "DOCK60",
        "entry": "DOCK60 / DOCK166 YMS · RT TASK-5305188 IN_PROGRESS · inYard Jul 1 00:27",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 30 17:00",
        "note": "✅ WMS IN_PROGRESS. RT TASK-5305188 IN_PROGRESS (Pedro Avila). YMS ET-1116387 GATE_CHECKED_IN DOCK166. Carrier 'b'/YAOJUN SUN. GURUNANDA.",
        "status": "🟢 EN PROCESO — RN-5008426 IN_PROGRESS · DOCK60 · RT IN_PROGRESS · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS+YMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "JTAU7362598",
        "rn": "RN-5008424",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008424",
        "dock": "DOCK156",
        "entry": "YMS ET-1116382 GATE_CHECKED_IN DOCK156 · WMS IMPORTED sin RT · ANTI-ESTADO-VIEJO → GREEN",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 30 23:00",
        "note": "⚠️ ANTI-ESTADO-VIEJO: WMS IMPORTED pero YMS GATE_CHECKED_IN DOCK156 06/30 16:00. Carrier TWENTY TRANSPORTATION. GURUNANDA.",
        "status": "🟢 EN YARDA — RN-5008424 IMPORTED · DOCK156 · GATE_CHECKED_IN · ANTI-ESTADO-VIEJO",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS+YMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "FORCED_LIVE_STATE"
    },
    {
        "container": "DFSU7374979",
        "rn": "RN-5008310",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008310",
        "dock": "DOCK61",
        "entry": "DOCK61 · RT FORCE_CLOSED · PA TASK-5304501 IN_PROGRESS · 2 ETs YMS · over item ⚠️",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 27 03:30",
        "note": "✅ RN-5008310 IN_PROGRESS. RT FORCE_CLOSED; PA TASK-5304501 IN_PROGRESS. YMS ET-1115787 DOCK_CHECKED_IN DOCK61. ET-1115107 anterior GATE_CHECK_OUT (pickup vacío CSNU8888140). ⚠️ Over item exception. GURUNANDA.",
        "status": "🟢 EN PROCESO — RN-5008310 IN_PROGRESS · DOCK61 · PA activo · Over item",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS+YMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "FORCED_LIVE_STATE"
    },
    {
        "container": "TCNU4379515",
        "rn": "RN-5008399",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008399",
        "dock": "DOCK48",
        "entry": "DOCK48 · RT TASK-5304474 CLOSED · PA TASK-5304515 IN_PROGRESS · Sin ET YMS",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Pendiente",
        "note": "✅ RT CLOSED. PA IN_PROGRESS (Caren Cubides). Devanned Jun 30 16:53. Sin appointment ni ET YMS. GURUNANDA.",
        "status": "🟢 EN PROCESO — RN-5008399 IN_PROGRESS · RT CLOSED · PA IN_PROGRESS · Sin cita",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "CAIU9453139",
        "rn": "RN-5008385",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008385",
        "dock": "DOCK2",
        "entry": "YMS DOCK_CHECKED_IN DOCK2 · WMS IN_PROGRESS · RT TASK-5304239 · inYard Jun 30 15:00",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 30 04:00",
        "note": "✅ RN-5008385 IN_PROGRESS. RT TASK-5304239 (Caren Cubides). YMS ET-1116033 DOCK_CHECKED_IN DOCK2. GURUNANDA confirmado. Asignado: RUFINO MUNGUIA.",
        "status": "🟢 EN PROCESO — RN-5008385 IN_PROGRESS · YMS DOCK2 · RT activo · GURUNANDA",
        "assignedTo": "RUFINO MUNGUIA",
        "assignee": "RUFINO MUNGUIA",
        "owner": "Rufino",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS+YMS LIVE cross-ref 20:00 PT · RN-5008385 Gurunanda confirmado",
        "staleStateGuard": "FORCED_LIVE_STATE"
    },
    {
        "container": "OOCU8342103",
        "rn": "RN-5008386",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008386",
        "dock": "DOCK68",
        "entry": "DOCK68 · RT CLOSED · PA TASK-5305197 NEW · YMS DOCK_CHECKED_OUT (stay) · inYard Jun 30 22:44",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 30 16:30",
        "note": "✅ RN-5008386 IN_PROGRESS. RT CLOSED. PA TASK-5305197 NEW (Pedro Avila). YMS ET-1116363 DOCK_CHECKED_OUT 18:40 checkOutInfo=NULL → SE QUEDA. GURUNANDA confirmado.",
        "status": "🟢 EN PROCESO — RN-5008386 IN_PROGRESS · DOCK68 · PA NEW · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS+YMS LIVE cross-ref 20:00 PT · RN-5008386 Gurunanda confirmado",
        "staleStateGuard": "FORCED_LIVE_STATE"
    },
    {
        "container": "BSIU8440908",
        "rn": "RN-5008387",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008387",
        "dock": "DOCK62",
        "entry": "DOCK62 · RT CLOSED · PA TASK-5305201 IN_PROGRESS · YMS DOCK_CHECKED_OUT (stay) · inYard Jun 30 22:42",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 30 16:00",
        "note": "✅ RN-5008387 IN_PROGRESS. RT CLOSED. PA TASK-5305201 IN_PROGRESS (Daniela Gonzalez). YMS ET-1116362 DOCK_CHECKED_OUT 19:18 checkOutInfo=NULL → SE QUEDA. GURUNANDA confirmado.",
        "status": "🟢 EN PROCESO — RN-5008387 IN_PROGRESS · DOCK62 · PA IN_PROGRESS · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS+YMS LIVE cross-ref 20:00 PT · RN-5008387 Gurunanda confirmado",
        "staleStateGuard": "FORCED_LIVE_STATE"
    },
    {
        "container": "FFAU1548537",
        "rn": "RN-5008428",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008428",
        "dock": "DOCK44",
        "entry": "DOCK44 · RT TASK-5304579 NEW · YMS GATE_CHECK_OUT (lleno se queda, pickup vacío BSIU9381158) · inYard Jun 30 17:23",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 30 17:00",
        "note": "✅ RN-5008428 IMPORTED pero en yarda confirmado YMS. RT TASK-5304579 NEW (Pedro Avila). YMS ET-1116141: GATE_CHECK_OUT con pickup BSIU9381158 EMPTY → lleno SE QUEDA. GURUNANDA confirmado.",
        "status": "🟢 EN YARDA — RN-5008428 IMPORTED · DOCK44 · RT NEW · Lleno se queda · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS+YMS LIVE cross-ref 20:00 PT · RN-5008428 Gurunanda confirmado",
        "staleStateGuard": "FORCED_LIVE_STATE"
    },
    {
        "container": "53180 (RN-187978)",
        "rn": "RN-187978",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-187978",
        "dock": "DOCK1",
        "entry": "DOCK1 · RT TASK-5304933 IN_PROGRESS · GN06302026UNIS-1126 · inYard Jun 30 20:22",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 30 07:00",
        "note": "🆕 Nuevo RN Gurunanda. IN_PROGRESS DOCK1. RT TASK-5304933 IN_PROGRESS (Caren Cubides). GURUNANDA.",
        "status": "🟢 EN PROCESO — RN-187978 IN_PROGRESS · DOCK1 · RT IN_PROGRESS · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT · Nuevo RN Gurunanda",
        "staleStateGuard": "NEW_RN_DETECTED"
    },
    {
        "container": "53393 (RN-187974)",
        "rn": "RN-187974",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-187974",
        "dock": "DOCK3",
        "entry": "DOCK3 · RT TASK-5304728 CLOSED · PA TASK-5305082 NEW · GN06302026UNIS-1125 · inYard Jun 30 19:05",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 30 07:00",
        "note": "🆕 Nuevo RN Gurunanda. IN_PROGRESS DOCK3. RT CLOSED, PA TASK-5305082 NEW (Fatima Ponce). Devanned. GURUNANDA.",
        "status": "🟢 EN PROCESO — RN-187974 IN_PROGRESS · DOCK3 · PA NEW · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT · Nuevo RN Gurunanda",
        "staleStateGuard": "NEW_RN_DETECTED"
    },
    {
        "container": "Leafchem06242026 (PO8367)",
        "rn": "RN-5008306",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008306",
        "dock": "DOCK38",
        "entry": "DOCK38 · RT TASK-5302013 IN_PROGRESS · 4d+ activo · inYard Jun 26",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 24",
        "note": "⚠️ 4+ días en DOCK38. RT TASK-5302013 IN_PROGRESS. GURUNANDA.",
        "status": "🟢 EN YARDA — RN-5008306 IN_PROGRESS · DOCK38 · RT IN_PROGRESS · 4d+",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "FUS06222026UNIS-55 (1054491-1)",
        "rn": "RN-187263",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-187263",
        "dock": "DOCK64",
        "entry": "DOCK64 · RT TASK-5298920 IN_PROGRESS · 7d activo · inYard Jun 23",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 22",
        "note": "⚠️ 7 días en DOCK64. RT TASK-5298920 IN_PROGRESS. WMS containerNo=1054491-1. GURUNANDA.",
        "status": "🟢 EN YARDA — RN-187263 IN_PROGRESS · DOCK64 · RT IN_PROGRESS · 7d",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "Chapin06292026 (FCIU9820116)",
        "rn": "RN-5008388",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008388",
        "dock": "DOCK58",
        "entry": "DOCK58 · RT TASK-5303183 CLOSED · PA TASK-5303470 NEW · inYard Jun 29",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 29",
        "note": "✅ RN-5008388 IN_PROGRESS. RT CLOSED, PA TASK-5303470 NEW. GURUNANDA.",
        "status": "🟢 EN YARDA — RN-5008388 IN_PROGRESS · DOCK58 · PA NEW · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "CORRU0629026UNIS",
        "rn": "RN-5008361",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008361",
        "dock": "DOCK67",
        "entry": "DOCK67 · RT FORCE_CLOSED ⚠️ · PA TASK-5303610 IN_PROGRESS · over items · inYard Jun 29",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 29",
        "note": "⚠️ RN-5008361 IN_PROGRESS. RT TASK-5303382 FORCE_CLOSED pero PA TASK-5303610 IN_PROGRESS con over items. GURUNANDA.",
        "status": "🟢 EN PROCESO — RN-5008361 IN_PROGRESS · DOCK67 · RT FORCE_CLOSED / PA activo · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "FORCED_LIVE_STATE"
    },
    {
        "container": "CORR06262026UNIS",
        "rn": "RN-5008360",
        "rnStatus": "IN_PROGRESS",
        "receipt": "RN-5008360",
        "dock": "DOCK65",
        "entry": "DOCK65 · RT CLOSED · PA TASK-5305043 NEW · inYard Jun 30",
        "inYard": True,
        "color": "green",
        "appointmentTime": "Jun 30 17:00",
        "note": "✅ RN-5008360 IN_PROGRESS. RT CLOSED, PA TASK-5305043 NEW. Asignado: RUFINO MUNGUIA. GURUNANDA.",
        "status": "🟢 EN PROCESO — RN-5008360 IN_PROGRESS · DOCK65 · PA NEW · RUFINO MUNGUIA",
        "assignedTo": "RUFINO MUNGUIA",
        "assignee": "RUFINO MUNGUIA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "FORCED_LIVE_STATE"
    },
]

# ============================================================
# YELLOW ROWS (7)
# ============================================================
yellow_rows = [
    {
        "container": "OOLU9324944",
        "rn": "RN-5008430",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008430",
        "dock": "—",
        "entry": "Cita Jun 30 19:00 VENCIDA · Sin llegada · Sin RT · Sin ET YMS",
        "inYard": False,
        "color": "yellow",
        "appointmentTime": "Jun 30 19:00 (VENCIDA 1h+)",
        "note": "⚠️ Cita 19:00 VENCIDA sin llegada. Sin RT ni ET YMS. GURUNANDA confirmado.",
        "status": "🟡 CITA VENCIDA — RN-5008430 IMPORTED · Cita 19:00 sin llegada · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS+YMS LIVE cross-ref 20:00 PT · RN-5008430 Gurunanda confirmado",
        "staleStateGuard": "OK"
    },
    {
        "container": "53541 (RN-187983)",
        "rn": "RN-187983",
        "rnStatus": "IMPORTED",
        "receipt": "RN-187983",
        "dock": "—",
        "entry": "IMPORTED · Cita 06/30 07:00 VENCIDA (13h+) · NEED_TO_EMAIL_CARRIER · Sin ET YMS",
        "inYard": False,
        "color": "yellow",
        "appointmentTime": "Jun 30 07:00 (VENCIDA 13h+)",
        "note": "🆕 RN Gurunanda. IMPORTED sin RT/PA. NEED_TO_EMAIL_CARRIER. Cita 07:00 vencida 13+ horas. GURUNANDA.",
        "status": "🟡 CITA VENCIDA — RN-187983 IMPORTED · NEED_TO_EMAIL_CARRIER · 13h+",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT · Nuevo RN Gurunanda",
        "staleStateGuard": "NEW_RN_DETECTED"
    },
    {
        "container": "53166 (RN-187979)",
        "rn": "RN-187979",
        "rnStatus": "IMPORTED",
        "receipt": "RN-187979",
        "dock": "—",
        "entry": "IMPORTED · Cita 06/30 07:00 VENCIDA (13h+) · NEED_TO_EMAIL_CARRIER · Sin ET YMS",
        "inYard": False,
        "color": "yellow",
        "appointmentTime": "Jun 30 07:00 (VENCIDA 13h+)",
        "note": "🆕 RN Gurunanda. IMPORTED sin RT/PA. NEED_TO_EMAIL_CARRIER. Cita 07:00 vencida 13+ horas. GURUNANDA.",
        "status": "🟡 CITA VENCIDA — RN-187979 IMPORTED · NEED_TO_EMAIL_CARRIER · 13h+",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT · Nuevo RN Gurunanda",
        "staleStateGuard": "NEW_RN_DETECTED"
    },
    {
        "container": "RN-187991 (FUS06302026UNIS-58)",
        "rn": "RN-187991",
        "rnStatus": "IMPORTED",
        "receipt": "RN-187991",
        "dock": "—",
        "entry": "IMPORTED · Cita 06/30 vencida · containerNo=NULL · NEED_TO_EMAIL_CARRIER · Sin ET YMS",
        "inYard": False,
        "color": "yellow",
        "appointmentTime": "Jun 30 (VENCIDA)",
        "note": "🆕 RN Gurunanda. IMPORTED sin RT/PA. NEED_TO_EMAIL_CARRIER. containerNo=NULL. Sin contenedor físico asignado. GURUNANDA.",
        "status": "🟡 CITA VENCIDA — RN-187991 IMPORTED · containerNo=NULL · NEED_TO_EMAIL_CARRIER",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT · Nuevo RN Gurunanda",
        "staleStateGuard": "NEW_RN_DETECTED"
    },
    {
        "container": "FUS06292026UNIS-57",
        "rn": "RN-187878",
        "rnStatus": "IMPORTED",
        "receipt": "RN-187878",
        "dock": "—",
        "entry": "IMPORTED · Cita 06/30 20:00 VENCIDA · containerNo=NULL · Sin tareas",
        "inYard": False,
        "color": "yellow",
        "appointmentTime": "Jun 30 20:00 (recién vencida)",
        "note": "⚠️ IMPORTED sin RT/PA. Cita 20:00 recién vencida. containerNo=NULL. Transferencia UNIS sin contenedor físico. GURUNANDA.",
        "status": "🟡 CITA VENCIDA — RN-187878 IMPORTED · Sin tareas · containerNo=NULL",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "ALNOR04242026",
        "rn": "RN-183707",
        "rnStatus": "IMPORTED",
        "receipt": "RN-183707",
        "dock": "DOCK65",
        "entry": "IMPORTED · 68+ días · RT TASK-5252949 NEW · inYard Abr 27",
        "inYard": True,
        "color": "yellow",
        "appointmentTime": "Abr 24 (original)",
        "note": "🚨 ANCIANO: 68+ días IMPORTED. RT TASK-5252949 NEW (Caren Cubides). DOCK65. GURUNANDA.",
        "status": "🟡 EN YARDA ESTANCADO — RN-183707 IMPORTED · DOCK65 · RT NEW · 68d+",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "MAWB 00120698274",
        "rn": "RN-5006269",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5006269",
        "dock": "DOCK62",
        "entry": "IMPORTED · 120+ días · RT TASK-5207670 NEW · inYard Mar 2",
        "inYard": True,
        "color": "yellow",
        "appointmentTime": "Feb 2026",
        "note": "🚨 ANCIANO CRÍTICO: 120+ días IMPORTED. RT TASK-5207670 NEW (Caren Cubides). DOCK62. GURUNANDA.",
        "status": "🟡 EN YARDA ESTANCADO — RN-5006269 IMPORTED · DOCK62 · RT NEW · 120d+",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
]

# ============================================================
# NORMAL ROWS (10)
# ============================================================
normal_rows = [
    {
        "container": "OOCU7355889",
        "rn": "RN-5008445",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008445",
        "dock": "—",
        "entry": "Cita Jul 2 03:00 · UFB-124862 · Sin llegada · Sin ET YMS",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 2 03:00",
        "note": "📅 IMPORTED sin RT. Cita Jul 2 03:00. UFB-124862. GURUNANDA.",
        "status": "📅 PRE-ENTRY — RN-5008445 IMPORTED · Cita Jul 2 03:00 · Sin llegada",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "JTAU7362561",
        "rn": "RN-5008446",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008446",
        "dock": "—",
        "entry": "Cita Jul 1 18:00 · SOC · Sin llegada · Sin ET YMS",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 1 18:00",
        "note": "📅 IMPORTED sin RT. Cita Jul 1 18:00. SOC. GURUNANDA.",
        "status": "📅 PRE-ENTRY — RN-5008446 IMPORTED · Cita Jul 1 18:00 · SOC · Sin llegada",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "CSGU6429436",
        "rn": "RN-5008479",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008479",
        "dock": "—",
        "entry": "Cita Jul 1 20:30 (1:30PM PDT) · UFB-124862 · CONFIRMADA UNIS · Sin llegada",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 1 20:30",
        "note": "📅 IMPORTED sin RT. Cita Jul 1 20:30 (1:30-3:30PM PDT). CONFIRMADA por UNIS (bpk2.cs). UFB-124862. GURUNANDA.",
        "status": "📅 PRE-ENTRY — RN-5008479 IMPORTED · Cita Jul 1 20:30 · UNIS CONFIRMÓ",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE + Outlook cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "FFAU2426030",
        "rn": "RN-5008480",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008480",
        "dock": "—",
        "entry": "Cita Jul 2 18:30 (11:30AM PDT) · UFB-124862 · CONFIRMADA UNIS · Sin llegada",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 2 18:30",
        "note": "📅 IMPORTED sin RT. Cita Jul 2 18:30 (11:30AM-1:30PM PDT). CONFIRMADA por UNIS. UFB-124862. GURUNANDA.",
        "status": "📅 PRE-ENTRY — RN-5008480 IMPORTED · Cita Jul 2 18:30 · UNIS CONFIRMÓ",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE + Outlook cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "TCKU6977609",
        "rn": "RN-5008481",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008481",
        "dock": "—",
        "entry": "Cita Jul 3 04:00 (Jul 2 9PM PDT) · UFB-124862 · CONFIRMADA UNIS · Sin llegada",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 3 04:00",
        "note": "📅 IMPORTED sin RT. Cita Jul 3 04:00 (Jul 2 9:00-11:00PM PDT). CONFIRMADA por UNIS. UFB-124862. GURUNANDA.",
        "status": "📅 PRE-ENTRY — RN-5008481 IMPORTED · Cita Jul 3 04:00 · UNIS CONFIRMÓ",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE + Outlook cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "CSNU6323633",
        "rn": "RN-5008483",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008483",
        "dock": "—",
        "entry": "Cita Jul 2 19:30 (12:30PM PDT) · UFB-124862 · ASN corregido ✅ · CONFIRMADA UNIS · Sin llegada",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 2 19:30",
        "note": "📅 IMPORTED sin RT. Cita Jul 2 19:30 (12:30-2:30PM PDT). ASN corregido enviado por Priti 15:04. CONFIRMADA por UNIS. GURUNANDA.",
        "status": "📅 PRE-ENTRY — RN-5008483 IMPORTED · Cita Jul 2 19:30 · ASN OK · UNIS CONFIRMÓ",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE + Outlook cross-ref 20:00 PT",
        "staleStateGuard": "OK"
    },
    {
        "container": "DDDU5053860",
        "rn": "RN-5008447",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008447",
        "dock": "—",
        "entry": "Cita Jul 1 17:00 · Sin llegada · Sin ET YMS",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 1 17:00",
        "note": "📅 IMPORTED sin RT. Cita Jul 1 17:00. GURUNANDA confirmado.",
        "status": "📅 PRE-ENTRY — RN-5008447 IMPORTED · Cita Jul 1 17:00 · Sin llegada",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT · RN-5008447 Gurunanda confirmado",
        "staleStateGuard": "OK"
    },
    {
        "container": "DDDU5053432",
        "rn": "RN-5008448",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008448",
        "dock": "—",
        "entry": "Cita Jul 1 23:00 · UFB-124862 · Sin llegada · Sin ET YMS",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 1 23:00",
        "note": "📅 IMPORTED sin RT. Cita Jul 1 23:00. UFB-124862. GURUNANDA confirmado.",
        "status": "📅 PRE-ENTRY — RN-5008448 IMPORTED · Cita Jul 1 23:00 · Sin llegada",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT · RN-5008448 Gurunanda confirmado",
        "staleStateGuard": "OK"
    },
    {
        "container": "LabelKing07012026",
        "rn": "RN-5008444",
        "rnStatus": "IMPORTED",
        "receipt": "RN-5008444",
        "dock": "—",
        "entry": "Cita Jul 1 17:00 · PO8357 · containerNo=LabelKing07012026 · Sin llegada",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 1 17:00",
        "note": "⚠️ TRIPLICADO: RN-5008444 primario (PO8357). RN-5008449 (PO7937) y RN-5008450 (PO8423) excluidos — mismo contenedor, misma cita. GURUNANDA.",
        "status": "📅 PRE-ENTRY — RN-5008444 IMPORTED · Cita Jul 1 17:00 · PO8357 · 2 dups excluidos",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT",
        "staleStateGuard": "DUPLICATE_MERGED"
    },
    {
        "container": "ITL07012026 (RN-187990)",
        "rn": "RN-187990",
        "rnStatus": "IMPORTED",
        "receipt": "RN-187990",
        "dock": "—",
        "entry": "Cita Jul 1 17:30 · 1 pallet · PO8158/Mineral logic ref · Sin llegada",
        "inYard": False,
        "color": "normal",
        "appointmentTime": "Jul 1 17:30",
        "note": "🆕 RN Gurunanda. IMPORTED sin RT/PA. Cita Jul 1 17:30. 1 pallet. Ref: Mineral Logic (PO, no cliente). GURUNANDA.",
        "status": "📅 PRE-ENTRY — RN-187990 IMPORTED · Cita Jul 1 17:30 · 1 pallet · GURUNANDA",
        "lastVerifiedAt": ts,
        "verificationSource": "WMS LIVE cross-ref 20:00 PT · Nuevo RN Gurunanda",
        "staleStateGuard": "NEW_RN_DETECTED"
    },
]

feed["rows"] = green_rows + yellow_rows + normal_rows

# ============================================================
# EXCLUDED CONTAINERS
# ============================================================
excluded = [
    {
        "container": "MATU2596614 (RN-5008382)",
        "rn": "RN-5008382",
        "reason": "FORCE_CLOSED WMS 06/30. YMS ET-1116356 DOCK_CHECKED_OUT DOCK61 checkOutInfo=NULL (se quedó en yarda, pero RN cerrado en WMS). EXCLUIDO del activo.",
        "removedAt": ts,
        "removalSource": "WMS+YMS LIVE cross-ref 20:00 PT · FORCE_CLOSED",
        "previousColor": "green"
    },
    {
        "container": "EITU8162104",
        "rn": "SIN RN",
        "reason": "Sin RN en WMS para GURUNANDA. YMS sin evidencia de yarda. Priti preguntó estado 06/25. EXCLUIDO del activo.",
        "removedAt": ts,
        "removalSource": "WMS+YMS LIVE cross-ref 20:00 PT · Sin RN",
        "previousColor": "normal"
    },
    {
        "container": "SMCU1114360 (RN-5008384)",
        "rn": "RN-5008384",
        "reason": "FORCE_CLOSED WMS 06/30. RN-5008384 cerrado. EXCLUIDO del activo.",
        "removedAt": ts,
        "removalSource": "WMS LIVE cross-ref 20:00 PT · FORCE_CLOSED",
        "previousColor": "yellow"
    },
    {
        "container": "MATU2610055 (RN-5008383)",
        "rn": "RN-5008383",
        "reason": "CLOSED WMS 06/30 — RT CLOSED + PA CLOSED. EXCLUIDO del activo.",
        "removedAt": ts,
        "removalSource": "WMS LIVE cross-ref 20:00 PT · CLOSED",
        "previousColor": "yellow"
    },
    {
        "container": "BSIU9381158",
        "rn": "RN-5008324",
        "reason": "CLOSED WMS 06/30. YMS: pickup vacío completado Jun 30 vía ET-1116141 (FFAU1548537 outbound). Rufino reportó vacío listo Jun 26. YA SALIÓ de yarda.",
        "removedAt": ts,
        "removalSource": "WMS+YMS+Outlook cross-ref 20:00 PT · CLOSED + pickup confirmado",
        "previousColor": "excluded"
    },
    {
        "container": "CSNU8888140",
        "rn": "RN-5008323",
        "reason": "CLOSED WMS. YMS: pickup vacío completado Jun 26 vía ET-1115107 (DFSU7374979 outbound). Rufino reportó vacío listo Jun 26. YA SALIÓ de yarda.",
        "removedAt": ts,
        "removalSource": "WMS+YMS+Outlook cross-ref 20:00 PT · CLOSED + pickup confirmado",
        "previousColor": "excluded"
    },
    {
        "container": "RN-5008449 (LabelKing07012026 duplicado)",
        "rn": "RN-5008449",
        "reason": "DUPLICADO de RN-5008444. Mismo containerNo=LabelKing07012026, misma cita Jul 1 17:00. PO7937. Excluido.",
        "removedAt": ts,
        "removalSource": "WMS cross-ref 20:00 PT · Duplicado",
        "previousColor": "none"
    },
    {
        "container": "RN-5008450 (LabelKing07012026 duplicado)",
        "rn": "RN-5008450",
        "reason": "DUPLICADO de RN-5008444. Mismo containerNo=LabelKing07012026, misma cita Jul 1 17:00. PO8423. Excluido.",
        "removedAt": ts,
        "removalSource": "WMS cross-ref 20:00 PT · Duplicado",
        "previousColor": "none"
    },
    {
        "container": "GN06292026UNIS-1123 (53162)",
        "rn": "RN-187767",
        "reason": "CLOSED WMS — RT TASK-5303527 CLOSED + PA TASK-5304237 CLOSED. Ambas tareas cerradas. GURUNANDA.",
        "removedAt": "2026-06-30T16:50:00-07:00",
        "removalSource": "WMS cross-ref 16:50 PDT",
        "previousColor": "green"
    },
    # YMS/WMS contradictions (physically in yard, RN closed)
    {
        "container": "CAAU8362068 ⚠️ EN YARDA",
        "rn": "RN-5008373",
        "reason": "CLOSED WMS 06/29 — PERO YMS: ET-1115000 DOCK_CHECKED_OUT DOCK60. CONTRADICCIÓN YMS/WMS: físicamente en yarda con RN cerrado.",
        "ymsContradiction": True
    },
    {
        "container": "TCNU1243715 ⚠️ EN YARDA SPOT755",
        "rn": "RN-5008340",
        "reason": "CLOSED WMS 06/27 — PERO YMS: ET-1114311 GATE_CHECK_OUT (drop-off), SPOT755 desde Jun 25. CONTRADICCIÓN YMS/WMS.",
        "ymsContradiction": True
    },
    {
        "container": "KOCU4689466 ⚠️ EN YARDA",
        "rn": "RN-5008265",
        "reason": "FORCE_CLOSED WMS — PERO YMS: ET-1112226 DOCK_CHECKED_IN DOCK573, 8 DÍAS estancado. CONTRADICCIÓN YMS/WMS.",
        "ymsContradiction": True
    },
    {
        "container": "TGBU7796954 (GN06232026UNIS-1112) ⚠️ EN YARDA",
        "rn": "RN-187378",
        "reason": "CLOSED WMS 06/29 — PERO YMS: ET-1113405 DOCK_CHECKED_IN DOCK513. CONTRADICCIÓN YMS/WMS.",
        "ymsContradiction": True
    },
    {
        "container": "FCIU8670343 (GN06262026UNIS-1119) ⚠️ EN YARDA",
        "rn": "RN-187665",
        "reason": "CLOSED WMS 06/29 — PERO YMS: ET-1114797 DOCK_CHECKED_IN DOCK510. CONTRADICCIÓN YMS/WMS.",
        "ymsContradiction": True
    },
    {
        "container": "FCIU9876069 (GN06262026UNIS-1120) ⚠️ EN YARDA",
        "rn": "RN-187666",
        "reason": "FORCE_CLOSED WMS 06/30 — PERO YMS: ET-1115396 DOCK_CHECKED_IN DOCK513. CONTRADICCIÓN YMS/WMS.",
        "ymsContradiction": True
    },
    # Other closed/removed
    {
        "container": "FFAU6121609",
        "rn": "RN-5008322",
        "reason": "CLOSED WMS 06/30 — YMS: pickup vacío completado Jun 30. YA SALIÓ de yarda."
    },
    {
        "container": "EITU8174300",
        "rn": "RN-5008303",
        "reason": "CLOSED WMS 06/30 — YMS: pickup vacío completado Jun 25. YA SALIÓ de yarda."
    },
    {
        "container": "CAIU9721329",
        "rn": "RN-5008176",
        "reason": "CLOSED WMS 06/27. Priti preguntó estado 06/25."
    },
    {
        "container": "SEKU4670025",
        "rn": "RN-5008325",
        "reason": "CLOSED WMS 06/29."
    },
    {
        "container": "TQL06182026 (old)",
        "rn": "RN-187158",
        "reason": "CANCELLED — Reemplazado por RN-187879"
    },
    {
        "container": "CHAPIN06172026-12",
        "rn": "RN-187157",
        "reason": "FORCE_CLOSED — WMS confirmado"
    },
    {
        "container": "CHAPIN06172026-14",
        "rn": "RN-187304",
        "reason": "FORCE_CLOSED — WMS confirmado"
    },
    {
        "container": "GN06242026UNIS-1115",
        "rn": "RN-187503",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "GN06252026UNIS-1118",
        "rn": "RN-187569",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "GN06292026UNIS-1122",
        "rn": "RN-187759",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "GN06292026UNIS-1124",
        "rn": "RN-187875",
        "reason": "CLOSED — RT + PA cerrados. WMS confirmado 06/30."
    },
    {
        "container": "Leafchem06252026",
        "rn": "RN-187429",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "DDDU5053448",
        "rn": "RN-5008297",
        "reason": "CLOSED — WMS confirmado 06/30"
    },
    {
        "container": "YMMU6698133",
        "rn": "RN-5008112",
        "reason": "FORCE_CLOSED — WMS confirmado"
    },
    {
        "container": "OOCU9426488",
        "rn": "RN-5008133",
        "reason": "FORCE_CLOSED — WMS confirmado"
    },
    {
        "container": "CSNU7820233",
        "rn": "RN-5008119",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "HMMU6422718",
        "rn": "RN-5008264",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "CSGU6625300",
        "rn": "RN-5008285",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "CAAU5246296",
        "rn": "RN-5008296",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "CSNU8075984",
        "rn": "RN-5008284",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "MATU4542915",
        "rn": "RN-5008260",
        "reason": "FORCE_CLOSED — WMS confirmado. Priti reportó DEMURRAGE 06/22."
    },
    {
        "container": "TIIU7745643",
        "rn": "RN-5008341",
        "reason": "CLOSED — WMS confirmado 06/30"
    },
    {
        "container": "DDDU5053094",
        "rn": "RN-5008299",
        "reason": "CLOSED — WMS confirmado 06/30. Priti preguntó estado 06/25."
    },
    {
        "container": "TGBU2472228",
        "rn": "RN-5008309",
        "reason": "FORCE_CLOSED — WMS confirmado 06/30"
    },
    {
        "container": "FCIU9601208",
        "rn": "RN-5008321",
        "reason": "CLOSED WMS — YMS: pickup vacío completado Jun 30. YA SALIÓ."
    },
    {
        "container": "BEAU6015134",
        "rn": "RN-5008320",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "CSNU8563588",
        "rn": "RN-5008300",
        "reason": "CLOSED — WMS confirmado. Priti preguntó estado 06/25."
    },
    {
        "container": "CAAU9247201",
        "rn": "RN-5008178",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "DDDU5053469",
        "rn": "RN-5008298",
        "reason": "CLOSED — WMS confirmado"
    },
    {
        "container": "MATU2752682",
        "rn": "RN-5008294",
        "reason": "FORCE_CLOSED — WMS confirmado"
    },
    {
        "container": "EITU8172519",
        "rn": "RN-5008258",
        "reason": "CLOSED 06/30 — RT CLOSED + PA CLOSED."
    },
    {
        "container": "BEAU5553433",
        "rn": "RN-5008342 / RN-5008450",
        "reason": "CLOSED WMS 06/29."
    },
    {
        "container": "TQL06182026 (LE0986 Mineral Logic)",
        "rn": "RN-187879 / RN-5008451",
        "reason": "CANCELLED/CLOSED — RN-187158 CANCELLED, RN-187879 CANCELLED, RN-5008451 CLOSED."
    },
    {
        "container": "TCNU1473003 (GN06262026UNIS-1121)",
        "rn": "RN-187669",
        "reason": "RT FORCE_CLOSED + PA CLOSED Jun 30."
    },
]

feed["excludedContainers"] = excluded

# ============================================================
# SUMMARY
# ============================================================
green_count = len(green_rows)
yellow_count = len(yellow_rows)
normal_count = len(normal_rows)

feed["summary"] = {
    "green": green_count,
    "yellow": yellow_count,
    "red": 0,
    "normal": normal_count,
    "visible": green_count + yellow_count + normal_count,
    "totalVisible": green_count + yellow_count + normal_count,
    "excluded": len(excluded),
    "enYardaProceso": green_count,
    "preEntry": normal_count,
    "activeContainers": green_count + yellow_count + normal_count
}

# ============================================================
# ALERTS
# ============================================================
feed["alerts"] = [
    f"✅ CICLO 06/30 20:00 PT: WMS+YMS+Outlook LIVE cross-ref. 32 activos ({green_count}g/{yellow_count}y/0r/{normal_count}n), {len(excluded)} excluidos.",
    "🔧 CORRECCIÓN WMS: CAIU9453139, OOCU8342103, BSIU8440908, FFAU1548537, OOLU9324944, DDDU5053860, DDDU5053432 — todos GURUNANDA confirmados (búsqueda por RN, no containerNo).",
    "🟢 ANTI-ESTADO-VIEJO CLEAN: JTAU7362598 normal→green (YMS DOCK156 GATE_CHECKED_IN).",
    "🆕 6 RNs GURUNANDA nuevos: RN-187978 (53180 GREEN), RN-187974 (53393 GREEN), RN-187990 (ITL07012026 NORMAL), RN-187983 (53541 YELLOW), RN-187979 (53166 YELLOW), RN-187991 (FUS06302026 YELLOW).",
    "📧 OUTLOOK: 2 no leídos Priti + 2 UNIS respuesta. Citas Jul 1-2 CONFIRMADAS por UNIS. ASN CSNU6323633 corregido. Rufino reportó vacíos BSIU9381158 + CSNU8888140.",
    "🔗 LABELKING TRIPLICACIÓN: RN-5008444 primario. RN-5008449 + RN-5008450 duplicados excluidos.",
    "📍 DOCKS YMS: CAIU9453139→DOCK2, OOCU8342103→DOCK68(stay), BSIU8440908→DOCK62(stay), FFAU1548537→DOCK44(drop full), DFSU7374979→DOCK61, JTAU7362582→DOCK166, JTAU7362598→DOCK156.",
    "⚠️ RN-5008361 (CORRU0629026UNIS): RT FORCE_CLOSED pero PA IN_PROGRESS — inconsistencia.",
    "⚠️ RN-5008310 (DFSU7374979): RT FORCE_CLOSED pero PA IN_PROGRESS — over item exception.",
    "🚨 ALERTA ROLAS: 6 contenedores en yarda con RN cerrado (CAAU8362068, TCNU1243715, KOCU4689466, TGBU7796954, FCIU8670343, FCIU9876069).",
    "🚨 ALERTA ROLAS: RN-5006269 (MAWB) 120+ días IMPORTED, RT NEW DOCK62.",
    "🚨 ALERTA ROLAS: RN-183707 (ALNOR) 68+ días IMPORTED, RT NEW DOCK65.",
    "⚠️ 5 citas VENCIDAS sin llegada: OOLU9324944 (19:00 1h+), RN-187878 (20:00), RN-187983 (07:00 13h+), RN-187979 (07:00 13h+), RN-187991 (06/30).",
    "⚠️ 3 RNs NEED_TO_EMAIL_CARRIER: RN-187983, RN-187979, RN-187991 — sin cita coordinada con carrier.",
    "📅 6 citas MAÑANA Jul 1: DDDU5053860 (17:00), LabelKing07012026 (17:00), RN-187990 (17:30), JTAU7362561 (18:00 SOC), CSGU6429436 (20:30 CONFIRMADA), DDDU5053432 (23:00).",
    "📅 4 citas Jul 2-3: OOCU7355889 (Jul 2 03:00), FFAU2426030 (Jul 2 18:30 CONFIRMADA), CSNU6323633 (Jul 2 19:30 CONFIRMADA), TCKU6977609 (Jul 3 04:00 CONFIRMADA).",
]

# ============================================================
# GUARDRAILS
# ============================================================
feed["guardrails"] = {
    "antiEstadoViejo": "ACTIVE",
    "rule": "PRE-ENTRY/normal is not allowed when row has live evidence: inYard=true, rnStatus IN_PROGRESS, ET/yard event, dock/location, receiving/putaway task, or inYardTime.",
    "lastGuardrailRun": ts,
    "preserveAssignments": True,
    "antiEstadoViejoCheck": "PASSED — 0 PRE-ENTRY/NORMAL rows with yarda evidence. 1 corrección activa (JTAU7362598 normal→green)."
}

# ============================================================
# EMAIL MONITOR
# ============================================================
feed["emailMonitor"] = {
    "lastChecked": ts,
    "unreadCount": 4,
    "totalFound": 54,
    "periodos": "15-Jun a 05-Jul-2026",
    "alertas": [
        "📧 54 contenedores únicos extraídos de 37 correos Priti",
        "📧 2 no leídos Priti + 2 no leídos UNIS (mismo hilo) + 1 no leído Rufino (vacíos)",
        "📅 4 citas Jul 1-3 confirmadas por Priti y UNIS (bpk2.cs)",
        "📋 ASN CSNU6323633 corregido por Priti a las 15:04 PDT",
        "🗑️ BSIU9381158 + CSNU8888140: Rufino reportó vacíos listos Jun 26. YA SALIERON según YMS.",
        "⚠️ MATU4542915: DEMURRAGE desde 06/22"
    ]
}

# Write
with open('public/container-feed.json', 'w') as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"✅ Feed escrito: {ts}")
print(f"   GREEN: {green_count}, YELLOW: {yellow_count}, RED: 0, NORMAL: {normal_count}")
print(f"   Total activos: {green_count + yellow_count + normal_count}")
print(f"   Excluidos: {len(excluded)}")
print(f"   Alertas: {len(feed['alerts'])}")
