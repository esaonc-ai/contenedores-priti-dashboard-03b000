#!/usr/bin/env python3
"""
apply_corrida_1200.py — Priti/Gurunanda Dashboard Update
July 9, 2026 ~12:00 PM PT
Cross-referenced: Outlook, WMS, YMS, BI
"""

import json
import os
from datetime import datetime, timezone, timedelta

FEED_PATH = os.path.join(os.path.dirname(__file__), "container-feed.json")
NOW_PT = datetime(2026, 7, 9, 12, 0, 0, tzinfo=timezone(timedelta(hours=-7)))
NOW_ISO = NOW_PT.isoformat()

print("=" * 60)
print("CORRIDA 12:00 PM PT — July 9, 2026")
print("=" * 60)

# Load current feed
with open(FEED_PATH, "r") as f:
    data = json.load(f)

rows = data.get("rows", [])
excluded = data.get("excluded", [])

print(f"\nBefore: {len(rows)} active, {len(excluded)} excluded")

# ============================================================================
# HELPER: build a proper row
# ============================================================================
def make_row(container, rn, color, status, in_yard, dock, note, **kwargs):
    row = {
        "container": container,
        "receipt": rn,
        "rn": rn,
        "color": color,
        "status": status,
        "inYard": in_yard,
        "dock": dock,
        "note": note,
        "notes": note,
        "lastVerifiedAt": NOW_ISO,
        "staleStateGuard": True,
        "verificationSource": "WMS+YMS+Outlook cross-check 12:00 PM PT corrida",
    }
    row.update(kwargs)
    return row

def make_excluded(container, rn, reason):
    return {
        "container": container,
        "rn": rn,
        "receipt": rn,
        "color": "normal",
        "status": "EXCLUDED",
        "inYard": False,
        "note": reason,
        "excludeReason": reason,
        "lastVerifiedAt": NOW_ISO,
        "verificationSource": "WMS cross-check 12:00 PM PT corrida",
    }

# ============================================================================
# CHANGE 1: REMOVE FFAU2426030 (RN-5008480) — WMS CLOSED
# ============================================================================
print("\n[1] REMOVING FFAU2426030 (RN-5008480) — WMS CLOSED 08:31 AM PT")
rows = [r for r in rows if r.get("rn") != "RN-5008480"]
excluded.append(make_excluded(
    "FFAU2426030", "RN-5008480",
    "WMS CLOSED Jul 09 08:31 AM PT — receiving TASK-5307691 CLOSED + putaway TASK-5311289 CLOSED"
))

# ============================================================================
# CHANGE 2: UPDATE CORR007082026UNIS PO8469 (RN-5008589) — stuck state
# ============================================================================
print("\n[2] UPDATING CORR007082026UNIS PO8469 (RN-5008589) — OFFLOAD CLOSED, awaiting putaway")
for r in rows:
    if r.get("rn") == "RN-5008589":
        r["note"] = "⚠️ OFFLOAD TASK-5311156 FORCE_CLOSED. Putaway TASK-5311911 CLOSED. RN sigue IN_PROGRESS (receiptCloseTiming: AFTER_PUT_AWAY). Pendiente cierre final. DOCK45."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS cross-check 12:00 PM PT — ambos tasks cerrados, RN stuck IN_PROGRESS"
        r["staleStateGuard"] = True

# ============================================================================
# CHANGE 3: PROMOTE CMAU4986523 (RN-5008593) → GREEN
# ============================================================================
print("\n[3] PROMOTING CMAU4986523 (RN-5008593) → GREEN/EN_YARDA")
for r in rows:
    if r.get("rn") == "RN-5008593":
        r["color"] = "green"
        r["status"] = "EN_YARDA"
        r["inYard"] = True
        r["dock"] = None
        r["note"] = "🟢 EN YARDA. WMS inYardTime Jul 09 10:13 AM PT. Priti: Drop. Cita original Jul 08 08:00. Sin receive task aún."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO
        r["antiEstadoViejo"] = True
        r["staleStateGuard"] = True
        r["verificationSource"] = "WMS cross-check 12:00 PM PT — inYard confirmado"
        r["greenEvidenceRule"] = "WMS inYardTime Jul 09 10:13 AM"
        print("   ✅ Promoted to GREEN")

# ============================================================================
# CHANGE 4: PROMOTE GN07072026UNIS-1136 (RN-188312) → GREEN
# ============================================================================
print("\n[4] PROMOTING GN07072026UNIS-1136 (RN-188312) → GREEN/EN_YARDA")
for r in rows:
    if r.get("rn") == "RN-188312":
        r["color"] = "green"
        r["status"] = "EN_YARDA"
        r["inYard"] = True
        r["dock"] = "DOCK11"
        r["note"] = "🟢 EN YARDA. WMS inYardTime Jul 09 09:39 AM PT. Receive task TASK-5312008 NEW en DOCK11. Transfer Gurunanda TV53581."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO
        r["antiEstadoViejo"] = True
        r["staleStateGuard"] = True
        r["verificationSource"] = "WMS cross-check 12:00 PM PT — inYard confirmado + receive task creado"
        r["greenEvidenceRule"] = "WMS inYardTime Jul 09 09:39 AM + TASK-5312008 NEW"
        print("   ✅ Promoted to GREEN")

# ============================================================================
# CHANGE 5: PROMOTE GN07082026UNIS-1137 (RN-188400) → YELLOW
# ============================================================================
print("\n[5] PROMOTING GN07082026UNIS-1137 (RN-188400) → YELLOW/EN_PROCESO")
for r in rows:
    if r.get("rn") == "RN-188400":
        r["color"] = "yellow"
        r["status"] = "EN_PROCESO"
        r["inYard"] = True
        r["dock"] = "DOCK44"
        r["note"] = "⚠️ EN_PROCESO. WMS inYard 14:30 PT. OFFLOAD TASK-5311752 FORCE_CLOSED. Putaway TASK-5312177 NEW. Transfer Gurunanda 53170."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO
        r["antiEstadoViejo"] = True
        r["staleStateGuard"] = True
        r["verificationSource"] = "WMS cross-check 12:00 PM PT — IN_PROGRESS with putaway pending"
        print("   ✅ Promoted to YELLOW")

# ============================================================================
# CHANGE 6: PROMOTE GN07082026UNIS-1138 (RN-188512) → YELLOW
# ============================================================================
print("\n[6] PROMOTING GN07082026UNIS-1138 (RN-188512) → YELLOW/EN_PROCESO")
for r in rows:
    if r.get("rn") == "RN-188512":
        r["color"] = "yellow"
        r["status"] = "EN_PROCESO"
        r["inYard"] = True
        r["dock"] = "DOCK55"
        r["note"] = "⚠️ EN_PROCESO. WMS inYard 17:06 PT. Receiving TASK-5312086 IN_PROGRESS (17:08→). Transfer Gurunanda 53761."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO
        r["antiEstadoViejo"] = True
        r["staleStateGuard"] = True
        r["verificationSource"] = "WMS cross-check 12:00 PM PT — IN_PROGRESS receiving active"
        print("   ✅ Promoted to YELLOW")

# ============================================================================
# CHANGE 7: UPDATE TIIU6675897 — add RN-5008683
# ============================================================================
print("\n[7] UPDATING TIIU6675897 → RN-5008683, appt Jul 09 19:00")
for r in rows:
    if r.get("container") == "TIIU6675897":
        r["rn"] = "RN-5008683"
        r["receipt"] = "RN-5008683"
        r["note"] = "WMS IMPORTED RN-5008683. Cita Jul 09 19:00 (7PM PT, corregida de 12-2PM). ImportExport: Drop (corrige TIIU6671567)."
        r["notes"] = r["note"]
        r["appointment"] = "2026-07-09 19:00"
        r["appointmentTime"] = "2026-07-09 19:00"
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS+Outlook cross-check 12:00 PM PT"
        print("   ✅ Updated RN-5008683")

# ============================================================================
# CHANGE 8: UPDATE TGSU5157375 — add RN-5008681, change appt
# ============================================================================
print("\n[8] UPDATING TGSU5157375 → RN-5008681, appt Jul 10 08:00-10:00")
for r in rows:
    if r.get("container") == "TGSU5157375":
        r["rn"] = "RN-5008681"
        r["receipt"] = "RN-5008681"
        r["note"] = "WMS IMPORTED RN-5008681. Cita actualizada: Jul 10 08:00-10:00 (Jasmine Jul 09 11:43 AM — cambió de Jul 09 23:00)."
        r["notes"] = r["note"]
        r["appointment"] = "2026-07-10 08:00"
        r["appointmentTime"] = "2026-07-10 08:00"
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS+Outlook cross-check 12:00 PM PT"
        print("   ✅ Updated RN-5008681 + appt Jul 10 08:00")

# ============================================================================
# CHANGE 9: UPDATE TGBU5468303 appt
# ============================================================================
print("\n[9] UPDATING TGBU5468303 (RN-5008665) → appt Jul 09 02:00")
for r in rows:
    if r.get("rn") == "RN-5008665":
        r["note"] = "WMS IMPORTED. Cita Jul 09 02:00 (cambió de 19:00). ImportExport: Drop. ⚠️ PAST DUE — no llegada aún."
        r["notes"] = r["note"]
        r["appointment"] = "2026-07-09 02:00"
        r["appointmentTime"] = "2026-07-09 02:00"
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS cross-check 12:00 PM PT"
        print("   ✅ Updated appt")

# ============================================================================
# CHANGE 10: UPDATE TGSU5157420 appt
# ============================================================================
print("\n[10] UPDATING TGSU5157420 (RN-5008666) → appt Jul 09 03:00")
for r in rows:
    if r.get("rn") == "RN-5008666":
        r["note"] = "WMS IMPORTED. Cita Jul 09 03:00 (cambió de 20:00). ImportExport: Drop. ⚠️ PAST DUE — no llegada aún."
        r["notes"] = r["note"]
        r["appointment"] = "2026-07-09 03:00"
        r["appointmentTime"] = "2026-07-09 03:00"
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS cross-check 12:00 PM PT"
        print("   ✅ Updated appt")

# ============================================================================
# CHANGE 11: UPDATE TGSU5157415 appt
# ============================================================================
print("\n[11] UPDATING TGSU5157415 (RN-5008667) → appt Jul 09 23:00")
for r in rows:
    if r.get("rn") == "RN-5008667":
        r["note"] = "WMS IMPORTED. Cita Jul 09 23:00 (4PM PT). ImportExport: Drop."
        r["notes"] = r["note"]
        r["appointment"] = "2026-07-09 23:00"
        r["appointmentTime"] = "2026-07-09 23:00"
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS cross-check 12:00 PM PT"
        print("   ✅ Updated appt")

# ============================================================================
# CHANGE 12: ADD TIIU6675500 (RN-5008692) — NEW
# ============================================================================
print("\n[12] ADDING TIIU6675500 (RN-5008692) — NEW from Jasmine email Jul 09 09:42 AM")
new_row = make_row(
    container="TIIU6675500",
    rn="RN-5008692",
    color="normal",
    status="PRE_ENTRY",
    in_yard=False,
    dock=None,
    note="WMS IMPORTED RN-5008692. Cita Jul 11 06:00. ImportExport (Jasmine Jul 09 09:42 AM): Drop.",
    appointment="2026-07-11 06:00",
    appointmentTime="2026-07-11 06:00",
    source="outlook_email",
    operationType="Drop",
    plannedEmailInclusionRule=True,
    customer="GURUNANDA",
)
rows.append(new_row)
print("   ✅ Added TIIU6675500")

# ============================================================================
# UPDATE OTHER YELLOW ROWS with fresh verification
# ============================================================================
print("\n[*] Refreshing other active rows...")

# GN07062026UNIS-1134 (RN-188263) — still IN_PROGRESS
for r in rows:
    if r.get("rn") == "RN-188263":
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS cross-check 12:00 PM PT — still IN_PROGRESS DOCK44"

# CORR007082026UNIS PO8462 (RN-5008588) — putaway IN_PROGRESS
for r in rows:
    if r.get("rn") == "RN-5008588":
        r["note"] = "⚠️ OFFLOAD TASK-5311067 FORCE_CLOSED. Putaway TASK-5311916 IN_PROGRESS. DOCK44. PO8462."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS cross-check 12:00 PM PT — putaway IN_PROGRESS"

# MRKU9388930 (RN-188088) — stuck state
for r in rows:
    if r.get("rn") == "RN-188088":
        r["note"] = "⚠️ EN_PROCESO. OFFLOAD TASK-5311340 FORCE_CLOSED. Putaway TASK-5311954 NEW. DOCK63. YMS DOCK_CHECKED_OUT pero RN sigue IN_PROGRESS. Priti reporta vacío."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS+YMS cross-check 12:00 PM PT — stuck, putaway pending"

# ZCSU7781965 (RN-5008664) — putaway IN_PROGRESS
for r in rows:
    if r.get("rn") == "RN-5008664":
        r["note"] = "⚠️ EN_PROCESO. Receiving TASK-5311621 CLOSED 15:58. Putaway TASK-5311899 IN_PROGRESS (17:29→). DOCK41→. Daniela."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS cross-check 12:00 PM PT — putaway IN_PROGRESS"

# CAAU7998380 (RN-5008646) — still in yard awaiting receiving
for r in rows:
    if r.get("rn") == "RN-5008646":
        r["note"] = "🟢 EN YARDA. WMS inYard Jul 08 09:12 AM. IMPORTED — sin receive task aún. Cita Jul 09 08:00 (PAST DUE). YMS: equipment exists, no active visit."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO
        r["verificationSource"] = "WMS+YMS cross-check 12:00 PM PT"

# FUS07062026UNIS-58 (RN-188264)
for r in rows:
    if r.get("rn") == "RN-188264":
        r["note"] = "IMPORTED. Cita Jul 08 20:00 (PAST DUE). CLIENT_PORTAL, 0 líneas. Sin evidencia de llegada."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO

# FUS07072026UNIS-59 (RN-188301)
for r in rows:
    if r.get("rn") == "RN-188301":
        r["note"] = "IMPORTED. Fusion Transfer. Cita Jul 08 17:00 (PAST DUE). CLIENT_PORTAL, 0 líneas. Sin evidencia de llegada."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO

# FUS07082026UNIS-60 (RN-188511)
for r in rows:
    if r.get("rn") == "RN-188511":
        r["note"] = "IMPORTED. Fusion Transfer. Cita Jul 08 07:00 (PAST DUE). Sin evidencia de llegada."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO

# TIIU8088862 (RN-5008654)
for r in rows:
    if r.get("rn") == "RN-5008654":
        r["note"] = "WMS IMPORTED. Cita Jul 09 03:00 (PAST DUE). ImportExport: Drop. Sin evidencia YMS/WISE. No llegada aún."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO

# CMAU6679803 (RN-5008655)
for r in rows:
    if r.get("rn") == "RN-5008655":
        r["note"] = "WMS IMPORTED. Cita Jul 09 08:00 (PAST DUE). ImportExport: Drop. Sin evidencia YMS/WISE. No llegada aún."
        r["notes"] = r["note"]
        r["lastVerifiedAt"] = NOW_ISO

# ============================================================================
# UPDATE SUMMARY
# ============================================================================
green_count = sum(1 for r in rows if r.get("color") == "green")
yellow_count = sum(1 for r in rows if r.get("color") == "yellow")
normal_count = sum(1 for r in rows if r.get("color") == "normal")
red_count = sum(1 for r in rows if r.get("color") == "red")

data["totalActive"] = len(rows)
data["totalExcluded"] = len(excluded)
data["lastUpdated"] = NOW_ISO
data["summary"] = {
    "totalActive": len(rows),
    "totalExcluded": len(excluded),
    "green": green_count,
    "yellow": yellow_count,
    "normal": normal_count,
    "red": red_count,
}
data["verificationSource"] = "WMS+YMS+Outlook cross-check 12:00 PM PT corrida Jul 09 2026"
data["message"] = f"🔄 Corrida 12:00 PM PT — {len(rows)} activos ({green_count}🟢 {yellow_count}🟡 {normal_count}⚪ {red_count}🔴) {len(excluded)} excluidos. Correcciones: +2 green, +2 yellow, -1 removido, +1 nuevo TIIU6675500."

# Add alerts
data["alerts"] = [
    "🔴 ALERTA ROLAS CRÍTICA: Feed estuvo 10.5h stale (01:25 AM → 12:00 PM). Correcciones masivas aplicadas.",
    "🔴 ALERTA ROLAS: FFAU2426030 removido — WMS CLOSED 08:31 AM con ambos tasks cerrados.",
    "🟠 ALERTA ROLAS: CMAU4986523 promovido a GREEN — inYard desde 10:13 AM, estaba como PRE_ENTRY falso.",
    "🟠 ALERTA ROLAS: GN07072026UNIS-1136 promovido a GREEN — inYard desde 09:39 AM, estaba como PRE_ENTRY falso.",
    "🟠 ALERTA ROLAS: GN07082026UNIS-1137 y 1138 promovidos a YELLOW — ya en proceso, estaban como PRE_ENTRY.",
    "🟡 Stuck states: MRKU9388930 (RN-188088), CORR PO8469 (RN-5008589), CORR PO8462 (RN-5008588), GN07082026UNIS-1137 (RN-188400) — OFFLOAD cerrado pero RN no cierra.",
    "🟡 TIIU6675500 (RN-5008692) NUEVO — anunciado Jasmine Jul 09, appt Jul 11 06:00.",
    "🟢 CMAU4986523 en yarda sin receive task — puede necesitar creación manual de tarea.",
]

# ============================================================================
# WRITE
# ============================================================================
with open(FEED_PATH, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n{'='*60}")
print(f"FINAL STATE: {len(rows)} active, {len(excluded)} excluded")
print(f"Colors: {green_count}🟢 {yellow_count}🟡 {normal_count}⚪ {red_count}🔴")
print(f"{'='*60}")

# Print row summary
for i, r in enumerate(rows):
    print(f"  [{i}] {r['color']:8s} | {r.get('container','?'):35s} | {r.get('rn','?'):18s} | {r.get('status','?'):15s} | {r.get('dock','-') or '-'}")

print(f"\n✅ Feed written to {FEED_PATH}")
print(f"✅ Ready for commit + push + deploy")
