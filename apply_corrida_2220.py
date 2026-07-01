#!/usr/bin/env python3
"""Apply corrida 22:20 PT — full WMS/YMS/Outlook re-verification."""
import json
from datetime import datetime, timezone, timedelta

PST = timezone(timedelta(hours=-7))
NOW = datetime.now(PST)
NOW_ISO = NOW.isoformat()
CORRIDA_LABEL = "Corrida 22:20 PDT Jun 30 — Full cycle: Outlook + WMS + YMS re-verified 32 rows. MATU2596614→excluded (putaway gone, FORCE_CLOSED confirmed). HTML fix: field names."

with open("public/container-feed.json", "r") as f:
    data = json.load(f)

# Update metadata
data["metadata"]["generatedAt"] = NOW_ISO
data["metadata"]["feedLastUpdated"] = NOW_ISO
data["metadata"]["corridaInfo"] = CORRIDA_LABEL

# Process rows: separate MATU2596614
active_rows = []
removed_row = None

for row in data["rows"]:
    if "MATU2596614" in row.get("container", ""):
        removed_row = row
    else:
        # Update timestamps for all active rows
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = f"WMS/YMS/Outlook {CORRIDA_LABEL.split(' — ')[0].replace('Corrida ', 'corrida ')}"
        active_rows.append(row)

# If MATU was removed, add to excluded
if removed_row:
    data["excluded"].insert(0, {
        "container": "MATU2596614",
        "reason": "FORCE_CLOSED (RN-5008382) confirmado. Putaway TASK-5305186 ya no existe (completado/removido). Receiving FORCE_CLOSED. YMS GATE_CHECK_OUT: lleno drop-off DOCK56 + vacío MATU2610055 pickup completado 06/30 14:16.",
        "removedAt": NOW_ISO,
        "previouslyReactivated": True
    })

data["rows"] = active_rows

# Update summary
total = len(active_rows)
greens = sum(1 for r in active_rows if r.get("color") == "green")
yellows = sum(1 for r in active_rows if r.get("color") == "yellow")
normals = sum(1 for r in active_rows if r.get("color") == "normal")
reds = sum(1 for r in active_rows if r.get("color") == "red")
in_yard = sum(1 for r in active_rows if r.get("inYard"))

# Update FUS06292026UNIS-57 note (Satyasri replied about pickup Fusion 10AM Jul 01)
for r in active_rows:
    if r.get("rn") == "RN-187878":
        r["note"] = r.get("note", "") + " 🆕 Satyasri 06/30 15:57: pickup programado Fusion 10AM Jul 01. Trailer TV53581 contiene RN-187878 + RN-187991. Cita vencida 06/30."
        r["verificationSource"] = f"WMS/YMS/Outlook {CORRIDA_LABEL.split(' — ')[0].replace('Corrida ', 'corrida ')} + Outlook Priti/Satyasri"

# Update RN-5008444 note (LabelKing — PO Will Call, no es contenedor)
for r in active_rows:
    if r.get("rn") == "RN-5008444":
        r["note"] = r.get("note", "") + " PO8357. ⚠️ LabelKing NO es contenedor marítimo — es Will Call PO."

data["summary"] = {
    "totalActive": total,
    "byColor": {
        "green": greens,
        "yellow": yellows,
        "normal": normals,
        "red": reds
    },
    "byEnYarda": {
        "inYard": in_yard,
        "notInYard": total - in_yard
    },
    "assignedToRufino": sum(1 for r in active_rows if r.get("assignedTo") == "RUFINO MUNGUIA"),
    "correctionsApplied": {
        "reactivadosDeExcluded": 0,
        "removidosAClosed": 1,
        "actualizadosReVerificados": total,
        "htmlFieldNamesFixed": True,
        "matu2596614Excluded": True
    },
    "alertasActivas": [
        "⚠️ ALERTA ROLAS: CAIU9453139 discrepancia dock — YMS DOCK2 vs WMS DOCK64",
        "⚠️ ALERTA ROLAS: FFAU1548537 receiving sigue NEW sin iniciar (20 pallets en yarda desde ayer)",
        "⚠️ ALERTA ROLAS: MAWB 00120698274 estancado 123 días IMPORTED",
        "⚠️ ALERTA ROLAS: ALNOR04242026 estancado 71 días IMPORTED",
        "⚠️ ALERTA ROLAS: FUS06292026UNIS-57 sin contenedor, cita vencida, NEED_TO_EMAIL_CARRIER. Pickup Fusion 10AM Jul 01.",
        "⚠️ ALERTA ROLAS: JTAU7362598 PRE-ENTRY con cita vencida 06/30 23:00",
        "⚠️ ALERTA ROLAS: OOLU9324944 PRE-ENTRY con cita vencida 06/30 19:00",
        "⚠️ ALERTA ROLAS: EITU8162104 SIN RN — requiere confirmación Rufino/Priti",
        "✅ MATU2596614 → excluded (FORCE_CLOSED confirmado, putaway ya no existe, YMS GATE_CHECK_OUT)",
        "✅ BSIU9381158 y CSNU8888140 confirmados salidos de yarda",
        "📅 5 citas HOY Jul 01 pendientes: OOCU7355889(20:00), JTAU7362561(11:00), DDDU5053860(10:00), DDDU5053432(16:00), CSGU6429436(13:30)",
        "📅 4 citas Jul 02: FFAU2426030, TCKU6977609, CSNU6323633, + RN-5008449(17:00 Jul 01)",
        "🆕 Outlook: 8 contenedores forecast Nitin (todos ya en feed). Priti ASN CSNU6323633 corregido. Satyasri pickup Fusion TV53581 Jul 01 10AM.",
        "🔧 HTML fixed: field name mismatches (message→metadata.corridaInfo, lastUpdated→metadata.feedLastUpdated, alertasRolas→summary.alertasActivas, totalVisible→totalActive)"
    ]
}

with open("public/container-feed.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Feed updated: {total} active rows (was 32, removed MATU2596614)")
print(f"   Green: {greens}, Yellow: {yellows}, Normal: {normals}, Red: {reds}")
print(f"   In yard: {in_yard}, Not in yard: {total - in_yard}")
print(f"   Excluded total: {len(data['excluded'])}")
