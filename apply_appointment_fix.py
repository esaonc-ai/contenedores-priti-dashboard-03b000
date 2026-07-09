#!/usr/bin/env python3
"""Apply appointment time corrections for TGSU5157420 and TGBU5468303."""
import json
import sys

with open("container-feed.json", "r") as f:
    feed = json.load(f)

changes = 0

for row in feed["rows"]:
    rn = row.get("rn", "")
    container = row.get("container", "")

    # TGSU5157420 (RN-5008666): appointment Jul 08 20:00-22:00 → Jul 09 03:00
    if rn == "RN-5008666" or container == "TGSU5157420":
        old_appt = row.get("appointment", "")
        old_appt_time = row.get("appointmentTime", "")
        row["appointment"] = "2026-07-09 03:00"
        row["appointmentTime"] = "2026-07-09T03:00:00-07:00"
        row["note"] = "UFB-128971. WMS IMPORTED APPT-6033193. Batch TGSU5157420+TGSU5157415. Anunciado por ImportExport (Jasmine) 07/08 12:26 PT. ⚠️ Cita actualizada WMS: Jul 09 03:00 (antes Jul 08 20:00-22:00)."
        row["notes"] = row["note"]
        row["lastVerifiedAt"] = "2026-07-09T04:10:00-07:00"
        print(f"✅ TGSU5157420 (RN-5008666): appointment {old_appt} → 2026-07-09 03:00")
        changes += 1

    # TGBU5468303 (RN-5008665): appointment Jul 08 19:00-21:00 → Jul 09 02:00
    if rn == "RN-5008665" or container == "TGBU5468303":
        old_appt_time = row.get("appointmentTime", "")
        row["appointmentTime"] = "2026-07-09T02:00:00-07:00"
        row["note"] = "Anunciado por ImportExport (Jasmine) 07/08 10:45 AM. WMS APPT-6033184. ⚠️ Cita actualizada WMS: Jul 09 02:00 (antes Jul 08 19:00-21:00)."
        row["notes"] = row["note"]
        row["lastVerifiedAt"] = "2026-07-09T04:10:00-07:00"
        print(f"✅ TGBU5468303 (RN-5008665): appointmentTime {old_appt_time} → 2026-07-09T02:00:00-07:00")
        changes += 1

# Update timestamps
new_ts = "2026-07-09T04:10:00-07:00"
feed["lastUpdated"] = new_ts
feed["message"] = "CORRECCIÓN Jul 9 04:10 PT — Actualización de citas: TGSU5157420 → Jul 09 03:00, TGBU5468303 → Jul 09 02:00 (WMS). 21 activos (1g/6y/14n/0r). 26 excluidos."
feed["verificationSource"] = "WMS appointment update 04:10 PT — 2 appointment corrections (TGSU5157420, TGBU5468303)"

# Update summary
feed["summary"]["appointmentsUpdatedThisRun"] = changes
feed["summary"]["notesUpdatedThisRun"] = changes

# Update _corrections
feed["_corrections"] = {
    "alert": "CORRECCIÓN Jul 9 04:10 PT — Actualización de citas WMS: TGSU5157420 → Jul 09 03:00, TGBU5468303 → Jul 09 02:00. 21 activos (1g/6y/14n/0r). 26 excluidos.",
    "timestamp": new_ts,
    "appointmentUpdates": [
        {"container": "TGSU5157420", "rn": "RN-5008666", "old": "2026-07-08 20:00-22:00", "new": "2026-07-09 03:00"},
        {"container": "TGBU5468303", "rn": "RN-5008665", "old": "2026-07-08 19:00-21:00", "new": "2026-07-09 02:00"}
    ],
    "removalsThisRun": [],
    "additionsThisRun": [],
    "demotionsThisRun": [],
    "promotionsThisRun": [],
    "notesUpdatedThisRun": ["TGSU5157420 appointment updated", "TGBU5468303 appointment updated"]
}

# Prepend alert
feed["alerts"].insert(0, f"✅ CORRECCIÓN 2026-07-09 04:10 PT: Actualización de citas WMS. TGSU5157420 → Jul 09 03:00, TGBU5468303 → Jul 09 02:00. 21 activos (1g/6y/14n/0r). 26 excluidos.")

# Update guardrails notes
feed["guardrails"]["antiEstadoViejo"]["note"] = "Jul 9 04:10 PT: TGSU5157420 + TGBU5468303 appointment times updated from WMS. CAAU7998380 GREEN confirmed."
feed["guardrails"]["closedRemovalRule"]["removalNote"] = "Jul 9 04:10 PT: 0 removals. 26 excluidos total."

with open("container-feed.json", "w") as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"\n✅ Applied {changes} appointment corrections")
print(f"✅ lastUpdated: {new_ts}")
print(f"✅ Summary: {feed['summary']['green']}g/{feed['summary']['yellow']}y/{feed['summary']['normal']}n/{feed['summary']['red']}r")
print(f"✅ Total: {feed['totalActive']} active / {feed['totalExcluded']} excluded")
