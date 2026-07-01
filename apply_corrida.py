#!/usr/bin/env python3
"""Apply corrida Jul 01 05:25 UTC (Jun 30 22:25 PT) updates to container-feed.json"""

import json
from datetime import datetime, timezone, timedelta

tz_pdt = timezone(timedelta(hours=-7))
now = datetime.now(tz_pdt)
ts = now.strftime("%Y-%m-%dT%H:%M:%S-07:00")

with open("public/container-feed.json", "r") as f:
    data = json.load(f)

rows = data["rows"]
updates = {
    "green_to_yellow": 0,
    "notes_updated": 0,
    "total": 0
}

# Helper to find row
def find_row(container_substr):
    for r in rows:
        if container_substr.lower() in r["container"].lower():
            return r
    return None

# ============================================================
# 1. ALNOR04242026: green → yellow (YMS ET-1087611 GATE_CHECK_OUT 2+ meses)
# ============================================================
r = find_row("ALNOR04242026")
if r:
    r["color"] = "yellow"
    r["entry"] = "⚠️ ANOMALÍA · YMS ET-1087611 GATE_CHECK_OUT Abr 27 · WMS IMPORTED con task NEW · 71d"
    r["status"] = "🟡 ANOMALÍA — RN-183707 IMPORTED · YMS visita salió Abr 27 · WMS sigue IMPORTED con receiving TASK-5252949 NEW en DOCK65"
    r["note"] = "🚨 YMS ET-1087611 GATE_CHECK_OUT desde Abr 27 (2+ meses). NO hay visita YMS activa. WMS RN-183707 sigue IMPORTED con receiving TASK-5252949 NEW (Caren C, DOCK65). DISCREPANCIA: YMS dice salió, WMS dice activo. 71 días. Alnor oils PO6252. GURUNANDA."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
    r["staleStateGuard"] = "YMS_DISCREPANCY"
    updates["green_to_yellow"] += 1

# ============================================================
# 2. MAWB 00120698274: green → yellow (YMS ET-1069983 GATE_CHECK_OUT 4 meses)
# ============================================================
r = find_row("MAWB 00120698274")
if r:
    r["color"] = "yellow"
    r["entry"] = "⚠️ ANOMALÍA · YMS ET-1069983 GATE_CHECK_OUT Mar 2 · WMS IMPORTED con task NEW · 123d"
    r["status"] = "🟡 ANOMALÍA — RN-5006269 IMPORTED · YMS visita salió Mar 2 · WMS sigue IMPORTED con receiving TASK-5207670 NEW en DOCK62"
    r["note"] = "🚨 YMS ET-1069983 GATE_CHECK_OUT desde Mar 2 (4 meses). NO hay visita YMS activa. WMS RN-5006269 sigue IMPORTED con receiving TASK-5207670 NEW (Caren C, DOCK62). DISCREPANCIA: YMS dice salió, WMS dice activo. 123 días. PO 6550. GURUNANDA."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
    r["staleStateGuard"] = "YMS_DISCREPANCY"
    updates["green_to_yellow"] += 1

# ============================================================
# 3. FFAU1548537: actualizar nota (WMS confirmado IMPORTED, YMS drop-off confirmado)
# ============================================================
r = find_row("FFAU1548537")
if r:
    r["note"] = "✅ En yarda confirmado YMS. RN-5008428 IMPORTED, inYard 06/30. Receiving TASK-5304579 sigue NEW (Pedro A, DOCK66). 0/20 pallets recibidos. YMS ET-1116141: drop-off FFAU1548537 en DOCK44 + pick-up vacío BSIU9381158, truck salió GATE_CHECK_OUT. Contenedor SE QUEDA. ⚠️ 12h+ sin iniciar receiving. WMS dock=DOCK66, YMS dock=DOCK44."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
    updates["notes_updated"] += 1

# ============================================================
# 4. Actualizar notas de todas las filas verde con datos frescos WMS
# ============================================================
green_updates = {
    "DFSU7374979": "✅ WMS IN_PROGRESS. Devanned 06/30. Putaway TASK-5304501 IN_PROGRESS (user 1850, 33 LPs, última act. Jul 1 03:58). Recv TASK-5303877 FORCE_CLOSED (Caren C, DOCK61). YMS ET-1115787 DOCK_CHECKED_IN DOCK61. SIZE_53.",
    "Leafchem06242026": "⚠️ 5+ días en DOCK38. WMS IN_PROGRESS. Receiving TASK-5302013 IN_PROGRESS (Caren C) desde Jun 26. Sin putaway task. GURUNANDA. ⚠️ RECEIVING ESTANCADO.",
    "FUS06222026UNIS-55": "⚠️ 8 días en DOCK64. WMS IN_PROGRESS. Receiving TASK-5298920 IN_PROGRESS (Caren C) desde Jun 23. Sin putaway task. GURUNANDA. ⚠️ RECEIVING ESTANCADO.",
    "Chapin06292026": "GURUNANDA · WMS IN_PROGRESS. Recv TASK-5303183 CLOSED (Caren C, DOCK58). Putaway TASK-5303470 NEW (Caren C). YMS ET-1115475 DOCK_CHECKED_IN (live delivery, BOX_TRUCK).",
    "CAIU9453139": "✅ WMS IN_PROGRESS. Receiving TASK-5304239 IN_PROGRESS (Pedro A, DOCK64, iniciado Jul 1 02:13). Sin putaway. ⚠️ YMS ET-1116033 DOCK2 vs WMS DOCK64 — discrepancia dock. Asignado RUFINO MUNGUIA.",
    "CORRU0629026UNIS": "✅ WMS IN_PROGRESS. Recv TASK-5303382 FORCE_CLOSED (Caren C, DOCK67). Putaway TASK-5303610 IN_PROGRESS (José Luis Nieves, 8 LPs).",
    "TCNU4379515": "✅ WMS IN_PROGRESS. Devanned 06/30. Putaway TASK-5304515 IN_PROGRESS (Caren C, 2 LPs — casi terminado). YMS ET-1116105 DOCK_CHECKED_IN DOCK48. Doble dock check-out/in (09:53/09:54).",
    "JTAU7362582": "✅ WMS IN_PROGRESS. Devanned dagonzalez 07/01 04:04. Putaway TASK-5305219 IN_PROGRESS (Daniela G, 32 LPs). YMS ET-1116418 DOCK_CHECKED_OUT truck (contenedor se queda). 5 líneas, SIZE_40.",
    "OOCU8342103": "✅ WMS IN_PROGRESS. Devanned dagonzalez 07/01 01:40. Putaway TASK-5305197 NEW (Pedro A). Recv TASK-5305126 CLOSED (Daniela G, DOCK68). YMS ET-1116363 DOCK_CHECKED_OUT truck. 34 pallets.",
    "BSIU8440908": "✅ WMS IN_PROGRESS. Devanned dagonzalez 07/01 02:18. Putaway TASK-5305201 IN_PROGRESS (Jesús E). Recv TASK-5305125 CLOSED (Daniela G, DOCK62). YMS ET-1116362 DOCK_CHECKED_OUT truck. 27 pallets.",
    "GN06302026UNIS-1125": "GURUNANDA · WMS IN_PROGRESS. Recv TASK-5304728 CLOSED (Fátima P, DOCK3). Putaway TASK-5305082 NEW (Fátima P). Container WMS: 53393. Transfer Nitin 06/30.",
    "GN06302026UNIS-1126": "GURUNANDA · WMS IN_PROGRESS. Receiving TASK-5304933 IN_PROGRESS (Caren C, DOCK1). Sin putaway aún. Container WMS: 53180. Transfer Nitin 06/30.",
}

for key, note in green_updates.items():
    r = find_row(key[:15])  # partial match
    if r:
        r["note"] = note
        r["lastVerifiedAt"] = ts
        r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
        updates["notes_updated"] += 1

# ============================================================
# 5. Actualizar amarillos existentes (RN-5008382, FUS06292026UNIS-57, etc.)
# ============================================================
r = find_row("MATU2596614")
if r:
    r["note"] = "🚨 RN-5008382 FORCE_CLOSED (qty match) pero putaway TASK-5305186 IN_PROGRESS (user 1850, 28 LPs). Última act. Jul 1 04:46. Recv TASK-5305121 FORCE_CLOSED. YMS ET-1116284 GATE_CHECK_OUT (drop-off normal, contenedor se queda). ANOMALÍA PERSISTE: RN cerrado + putaway activo. REACTIVADO."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
    updates["notes_updated"] += 1

r = find_row("FUS06292026UNIS-57")
if r:
    r["note"] = "GURUNANDA · IMPORTED sin RT/PA. Cita 06/30 20:00 no cumplida (no show). WMS containerNo=NULL. WMS appointmentStatus=NEED_TO_EMAIL_CARRIER. Trailer TV53581. estimatedTimeOfDeparture=Jul 1 08:00."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
    updates["notes_updated"] += 1

r = find_row("GN06302026UNIS-1127")
if r:
    r["note"] = "GURUNANDA · IMPORTED sin tareas. Container WMS: 53166. Sin appointment — NEED_TO_EMAIL_CARRIER. Transfer Nitin 06/30."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/Outlook corrida 22:25 PT Jun 30"
    updates["notes_updated"] += 1

r = find_row("GN06302026UNIS-1128")
if r:
    r["note"] = "GURUNANDA · IMPORTED sin tareas. Container WMS: 53541. Sin appointment — NEED_TO_EMAIL_CARRIER. Transfer Nitin 06/30."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/Outlook corrida 22:25 PT Jun 30"
    updates["notes_updated"] += 1

r = find_row("RN-5008449")
if r:
    r["note"] = "⚠️ GURUNANDA · IMPORTED sin RT/PA. Cita 07/01 17:00. ET-1116103 PRE_ENTRY (sin gate check-in). ⚠️ MISMO containerNo 'LabelKing07012026' que RN-5008444. Verificar si es duplicado intencional."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
    updates["notes_updated"] += 1

r = find_row("RN-5008444")
if r:
    r["note"] = "Priti · GURUNANDA. IMPORTED sin RT/PA. Creado por aismael. APPT-6032450. ⚠️ NO es contenedor, es PO Will Call LabelKing. ⚠️ MISMO containerNo 'LabelKing07012026' que RN-5008449 (PO 7937). Este es PO 8357."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
    updates["notes_updated"] += 1

# ============================================================
# 6. Actualizar PRE-ENTRY con datos frescos
# ============================================================
preentry_updates = {
    "OOLU9324944": "GURUNANDA · IMPORTED sin RT/PA. Cita 06/30 19:00 VENCIDA (no show). Sin ET YMS. DO pendiente UNIS.",
    "JTAU7362598": "GURUNANDA · IMPORTED sin RT/PA. Cita 06/30 23:00 VENCIDA (no show). Sin ET YMS. DO pendiente UNIS.",
    "OOCU7355889": "GURUNANDA · IMPORTED sin RT/PA. Cita Jul 1 20:00. Sin ET YMS aún. DO pendiente.",
    "JTAU7362561": "GURUNANDA · IMPORTED sin RT/PA. Cita Jul 1 11:00. Sin ET YMS aún. DO pendiente.",
    "DDDU5053860": "GURUNANDA · IMPORTED sin RT/PA. Cita Jul 1 10:00. Sin ET YMS aún. DO pendiente.",
    "DDDU5053432": "GURUNANDA · IMPORTED sin RT/PA. Cita Jul 1 16:00. Sin ET YMS aún. DO pendiente.",
    "CSGU6429436": "GURUNANDA · IMPORTED sin RT/PA. Cita Jul 1 13:30. Creado por aismael. Carrier WILL CALL. UFB-124862. Sin ET YMS aún.",
    "FFAU2426030": "GURUNANDA · IMPORTED sin RT/PA. Cita Jul 2 11:30. Creado por aismael. Carrier WILL CALL. UFB-124862. Sin ET YMS aún.",
    "TCKU6977609": "GURUNANDA · IMPORTED sin RT/PA. Cita Jul 2 21:00. Creado por aismael. Carrier WILL CALL. UFB-124862. Sin ET YMS aún.",
    "CSNU6323633": "GURUNANDA · IMPORTED sin RT/PA. Cita Jul 2 12:30. Creado por aismael. ASN corregido por Priti 06/30 15:04. Carrier WILL CALL. UFB-124862. Sin ET YMS aún.",
}

for key, note in preentry_updates.items():
    r = find_row(key[:15])
    if r:
        r["note"] = note
        r["lastVerifiedAt"] = ts
        r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
        updates["notes_updated"] += 1

# ============================================================
# 7. EITU8162104: sin cambios (sigue sin RN)
# ============================================================
r = find_row("EITU8162104")
if r:
    r["note"] = "🔴 SIN RN en WMS (re-verificado 06/30 22:25 PT). Priti preguntó 06/25 si estaba vacío. YMS: no aparece. WMS: búsqueda por containerNo = 0 resultados. Posiblemente vacío retirado. Requiere confirmación de Rufino/Priti."
    r["lastVerifiedAt"] = ts
    r["verificationSource"] = "WMS/YMS/Outlook corrida 22:25 PT Jun 30"
    updates["notes_updated"] += 1

# ============================================================
# 8. Actualizar metadata y summary
# ============================================================
data["metadata"]["generatedAt"] = ts
data["metadata"]["feedLastUpdated"] = ts
data["metadata"]["corridaInfo"] = "Corrida 22:25 PT Jun 30 — ALNOR04242026 y MAWB degradados green→yellow (YMS visita salió hace meses vs WMS activo). Coolify 6.5h atrasado. TODOS 32 rows re-verificados WMS+YMS. Priti Outlook: 33 correos procesados, sin nuevos contenedores para dashboard."

# Recalcular summary
greens = sum(1 for r in rows if r["color"] == "green")
yellows = sum(1 for r in rows if r["color"] == "yellow")
normals = sum(1 for r in rows if r["color"] == "normal")
reds = sum(1 for r in rows if r["color"] == "red")
in_yard = sum(1 for r in rows if r.get("inYard"))

data["summary"]["totalActive"] = len(rows)
data["summary"]["byColor"] = {"green": greens, "yellow": yellows, "normal": normals, "red": reds}
data["summary"]["byEnYarda"] = {"inYard": in_yard, "notInYard": len(rows) - in_yard}
data["summary"]["correctionsApplied"]["actualizadosWMSReVerificados"] = len(rows)
data["summary"]["correctionsApplied"]["dockDiscrepancyNoted"] = 1
data["summary"]["alertasActivas"] = [
    "🚨 ALERTA ROLAS CRÍTICA: MATU2596614 REACTIVADO — RN-5008382 FORCE_CLOSED pero putaway TASK-5305186 IN_PROGRESS (28 LPs). Anomalía persiste.",
    "🟡 ALERTA ROLAS: ALNOR04242026 YMS ET-1087611 GATE_CHECK_OUT Abr 27 — WMS sigue IMPORTED con task NEW. Discrepancia YMS/WMS.",
    "🟡 ALERTA ROLAS: MAWB 00120698274 YMS ET-1069983 GATE_CHECK_OUT Mar 2 — WMS sigue IMPORTED con task NEW. Discrepancia YMS/WMS.",
    "⚠️ ALERTA ROLAS: CAIU9453139 discrepancia dock — YMS DOCK2 vs WMS DOCK64",
    "⚠️ ALERTA ROLAS: FFAU1548537 12h+ con receiving NEW sin iniciar (20 pallets en yarda)",
    "⚠️ ALERTA ROLAS: Leafchem06242026 + FUS06222026UNIS-55 con receiving estancado 5-8 días",
    "⚠️ ALERTA ROLAS: FUS06292026UNIS-57 sin contenedor, cita vencida, NEED_TO_EMAIL_CARRIER",
    "⚠️ ALERTA ROLAS: JTAU7362598 + OOLU9324944 PRE-ENTRY con citas vencidas 06/30",
    "🔴 ALERTA ROLAS: EITU8162104 SIN RN — Priti preguntó estado 06/25, requiere confirmación",
    "⚠️ ALERTA ROLAS: RN-5008444 y RN-5008449 comparten containerNo 'LabelKing07012026' — posible duplicado",
    "📅 6 citas Jul 1 pendientes (DDDU5053860 10:00, JTAU7362561 11:00, CSGU6429436 13:30, DDDU5053432 16:00, LabelKing 17:00, OOCU7355889 20:00)",
    "📅 4 citas Jul 2-3 confirmadas",
    "🚨 ALERTA ROLAS: Dashboard live 6.5h desactualizado — Coolify no desplegó último cambio",
    "📊 Priti Outlook: 33 correos procesados. MATU4542915 demurrage alerta Jun 22 (ya en excluded)."
]

# Guardar
with open("public/container-feed.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Feed actualizado: {ts}")
print(f"   Greens: {greens} (eran 15)")
print(f"   Yellows: {yellows} (eran 5)")
print(f"   Normals: {normals} (eran 11)")
print(f"   Reds: {reds} (era 1)")
print(f"   Total: {len(rows)}")
print(f"   green→yellow: {updates['green_to_yellow']}")
print(f"   notes updated: {updates['notes_updated']}")
