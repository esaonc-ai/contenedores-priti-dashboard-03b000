#!/usr/bin/env python3
"""
Apply 3 changes to container-feed.json — CORRIDA Jul 8 5:05 PM PT:
1. REMOVE EITU9363654/RN-5008569 → excluded (WMS CLOSED, cycle complete)
2. PROMOTE SMCU1143199/RN-5008592 → GREEN/EN_YARDA (DOCK62, Daniela Gonzalez, GURUNANDA)
3. PROMOTE BMOU6706676/RN-5008587 → YELLOW/EN_PROCESO (DOCK61, Daniela Gonzalez)
"""
import json
import copy
from datetime import datetime, timezone, timedelta

now_pt = datetime.now(timezone(timedelta(hours=-7)))
ts = now_pt.strftime('%Y-%m-%dT%H:%M:%S-07:00')
ts_short = now_pt.strftime('%I:%M %p PT')

# Load live feed data (fetched from live site at 5:02 PM PT)
with open('public/container-feed.json', 'r') as f:
    feed = json.load(f)

# ============================================================
# CHANGE 1: REMOVE EITU9363654/RN-5008569 → excluded
# ============================================================
eitu_row = None
for i, row in enumerate(feed['rows']):
    if row.get('container') == 'EITU9363654' and row.get('rn') == 'RN-5008569':
        eitu_row = feed['rows'].pop(i)
        break

if eitu_row:
    feed['excluded'].insert(0, {
        "rn": "RN-5008569",
        "container": "EITU9363654",
        "reason": "WMS CLOSED (07/08 23:57 UTC). Receiving TASK-5311282 completed, Putaway TASK-5311461 completed. YMS DOCK_CHECKED_OUT. Cycle complete.",
        "removedAt": ts,
        "recvTask": "TASK-5311282 completed",
        "putTask": "TASK-5311461 completed",
        "wasActive": True,
        "wasColor": "yellow",
        "wasStatus": "EN_PROCESO"
    })
    print(f"✅ CHANGE 1: Removed EITU9363654/RN-5008569 → excluded")
else:
    print("⚠️ CHANGE 1: EITU9363654 not found in rows")

# ============================================================
# CHANGE 2: PROMOTE SMCU1143199/RN-5008592 → GREEN/EN_YARDA
# ============================================================
for row in feed['rows']:
    if row.get('container') == 'SMCU1143199' and row.get('rn') == 'RN-5008592':
        row['color'] = 'green'
        row['status'] = 'EN_YARDA'
        row['inYard'] = True
        row['dock'] = 'DOCK62'
        row['assignedTo'] = 'Daniela Gonzalez'
        row['note'] = '✅ PROMOVIDO 5:05 PM PT: GURUNANDA (ORG-655875). WMS IMPORTED inYard Jul 08 23:40 UTC. TASK-5311587 NEW DOCK62 (Daniela Gonzalez). YMS ET-1120046 WINDOW_CHECKED_IN DOCK62. Anti-estado-viejo: KARAKA mismatch RESUELTO — YMS confirma GURUNANDA LLC. Cita original 07/07 (llegada tardía).'
        row['notes'] = row['note']
        row['lastVerifiedAt'] = ts
        row['verificationSource'] = 'YMS+WMS cross-check 5:05 PM PT — GURUNANDA confirmado'
        row['staleStateGuard'] = True
        # Remove falseGreenCorrected if present
        row.pop('falseGreenCorrected', None)
        # Keep plannedEmailInclusionRule
        row['plannedEmailInclusionRule'] = True
        # Add antiEstadoViejo
        row['antiEstadoViejo'] = True
        # Add greenEvidenceRule
        row['greenEvidenceRule'] = 'YMS ET-1120046 WINDOW_CHECKED_IN DOCK62 + WMS TASK-5311587 DOCK62'
        print(f"✅ CHANGE 2: Promoted SMCU1143199/RN-5008592 → GREEN/EN_YARDA DOCK62")
        break
else:
    print("⚠️ CHANGE 2: SMCU1143199 not found in rows")

# ============================================================
# CHANGE 3: PROMOTE BMOU6706676/RN-5008587 → YELLOW/EN_PROCESO
# ============================================================
for row in feed['rows']:
    if row.get('container') == 'BMOU6706676' and row.get('rn') == 'RN-5008587':
        row['color'] = 'yellow'
        row['status'] = 'EN_PROCESO'
        row['inYard'] = True
        row['dock'] = 'DOCK61'
        row['assignedTo'] = 'Daniela Gonzalez'
        row['note'] = '🟡 PROMOVIDO 5:05 PM PT: WMS TASK-5311586 IN_PROGRESS DOCK61 (Daniela Gonzalez), started Jul 08 23:38 UTC. YMS ET-1120044 DOCK_CHECKED_IN DOCK61, GURUNANDA. Anti-estado-viejo: previamente revertido a NORMAL (falso verde), ahora tiene receiving legítimo IN_PROGRESS + YMS DOCK_CHECKED_IN.'
        row['notes'] = row['note']
        row['lastVerifiedAt'] = ts
        row['verificationSource'] = 'YMS+WMS cross-check 5:05 PM PT — receiving IN_PROGRESS DOCK61'
        row['staleStateGuard'] = True
        row.pop('falseGreenCorrected', None)
        row['plannedEmailInclusionRule'] = True
        row['antiEstadoViejo'] = True
        print(f"✅ CHANGE 3: Promoted BMOU6706676/RN-5008587 → YELLOW/EN_PROCESO DOCK61")
        break
else:
    print("⚠️ CHANGE 3: BMOU6706676 not found in rows")

# ============================================================
# RECALCULATE COUNTS
# ============================================================
green = sum(1 for r in feed['rows'] if r.get('color') == 'green')
yellow = sum(1 for r in feed['rows'] if r.get('color') == 'yellow')
normal = sum(1 for r in feed['rows'] if r.get('color') == 'normal')
red = sum(1 for r in feed['rows'] if r.get('color') == 'red')
total_active = len(feed['rows'])
total_excluded = len(feed['excluded'])

# ============================================================
# UPDATE METADATA
# ============================================================
feed['lastUpdated'] = ts
feed['totalActive'] = total_active
feed['totalExcluded'] = total_excluded
feed['message'] = f"CORRIDA Jul 8 {ts_short} — 3 cambios: EITU9363654/RN-5008569 removido (WMS CLOSED ciclo completo), SMCU1143199/RN-5008592 PROMOVIDO green DOCK62 (GURUNANDA, YMS+WMS confirmado), BMOU6706676/RN-5008587 PROMOVIDO yellow DOCK61 (receiving IN_PROGRESS). {total_active} activos ({green}g/{yellow}y/{normal}n/{red}r). {total_excluded} excluidos."
feed['verificationSource'] = f'YMS+WMS cross-check {ts_short}'

feed['summary'] = {
    "red": red,
    "green": green,
    "normal": normal,
    "yellow": yellow,
    "totalActive": total_active,
    "totalExcluded": total_excluded,
    "excludedThisRun": 1,
    "manualAdditions": 0,
    "rnUpdatesThisRun": 3,
    "dockUpdatesThisRun": 2,
    "reactivatedThisRun": 0,
    "notesUpdatedThisRun": 3,
    "falseGreensCorrected": 0,
    "promotedToGreenThisRun": 1,
    "demotedFromGreenThisRun": 0,
    "promotedToYellowThisRun": 1,
    "appointmentsUpdatedThisRun": 0
}

# ============================================================
# UPDATE ALERTS
# ============================================================
new_alerts = [
    f"✅ CORRIDA {ts_short}: 3 cambios aplicados. {total_active} activos ({green}g/{yellow}y/{normal}n/{red}r). {total_excluded} excluidos.",
    f"🗑️ REMOVIDO {ts_short}: EITU9363654/RN-5008569 — WMS CLOSED. Receiving+Putaway completos. YMS DOCK_CHECKED_OUT. Ciclo completo.",
    f"🟢 PROMOVIDO {ts_short}: SMCU1143199/RN-5008592 → GREEN/EN_YARDA DOCK62 — GURUNANDA (ORG-655875). WMS inYard + TASK-5311587 NEW. YMS ET-1120046 WINDOW_CHECKED_IN DOCK62. KARAKA mismatch RESUELTO.",
    f"🟡 PROMOVIDO {ts_short}: BMOU6706676/RN-5008587 → YELLOW/EN_PROCESO DOCK61 — WMS TASK-5311586 IN_PROGRESS (Daniela Gonzalez). YMS ET-1120044 DOCK_CHECKED_IN. Anti-estado-viejo: recuperado de falso verde.",
    f"📊 POST-CAMBIO: {green} green, {yellow} yellow, {normal} normal, {red} red. Excluidos: {total_excluded}.",
]

# Keep important historical alerts but deduplicate
keep_alerts = []
for a in feed['alerts']:
    if isinstance(a, str) and ('CONTAINER FANTASMA' in a or 'VACÍO' in a or 'NEED_WINDOW_CHECK' in a):
        keep_alerts.append(a)
    elif isinstance(a, dict) and a.get('level') == 'ALERTA_ROLAS':
        keep_alerts.append(a)

feed['alerts'] = new_alerts + keep_alerts

# ============================================================
# UPDATE GUARDRAILS
# ============================================================
feed['guardrails']['closedRemovalRule'] = {
    "status": "ACTIVE",
    "removalNote": f"{ts_short}: 1 removal — EITU9363654/RN-5008569 (WMS CLOSED ciclo completo). {total_excluded} excluidos total.",
    "removalsThisRun": 1,
    "reactivationsThisRun": 0
}
feed['guardrails']['greenEvidenceRule'] = {
    "status": "ACTIVE",
    "promotionNote": f"{ts_short}: 1 PROMOTION — SMCU1143199/RN-5008592 green DOCK62 (GURUNANDA, YMS+WMS confirmado).",
    "demotionsThisRun": 0,
    "promotionsThisRun": 1,
    "falseGreensDetected": 0
}
feed['guardrails']['antiEstadoViejo'] = {
    "note": f"{ts_short}: 2 anti-estado-viejo — SMCU1143199 normal→green, BMOU6706676 normal→yellow.",
    "status": "ACTIVE"
}

# ============================================================
# UPDATE _corrections
# ============================================================
feed['_corrections'] = {
    "alert": f"CORRIDA Jul 8 {ts_short} — 3 cambios: EITU9363654/RN-5008569 removido (WMS CLOSED), SMCU1143199/RN-5008592 → green DOCK62 (GURUNANDA), BMOU6706676/RN-5008587 → yellow DOCK61 (receiving IN_PROGRESS). {total_active} activos ({green}g/{yellow}y/{normal}n/{red}r). {total_excluded} excluidos.",
    "timestamp": ts,
    "ymsCheckNote": "SMCU1143199: YMS ET-1120046 WINDOW_CHECKED_IN DOCK62, GURUNANDA. BMOU6706676: YMS ET-1120044 DOCK_CHECKED_IN DOCK61, GURUNANDA.",
    "demotionsThisRun": [],
    "promotionsThisRun": [
        {
            "rn": "RN-5008592",
            "change": "NORMAL→GREEN EN_YARDA DOCK62",
            "reason": "GURUNANDA confirmado. WMS inYard + TASK-5311587. YMS ET-1120046 WINDOW_CHECKED_IN DOCK62.",
            "container": "SMCU1143199"
        },
        {
            "rn": "RN-5008587",
            "change": "NORMAL→YELLOW EN_PROCESO DOCK61",
            "reason": "WMS TASK-5311586 IN_PROGRESS. YMS ET-1120044 DOCK_CHECKED_IN DOCK61.",
            "container": "BMOU6706676"
        }
    ],
    "excludedThisRun": [
        {
            "rn": "RN-5008569",
            "container": "EITU9363654",
            "reason": "WMS CLOSED. Receiving+Putaway completos. YMS DOCK_CHECKED_OUT."
        }
    ]
}

# ============================================================
# WRITE
# ============================================================
with open('public/container-feed.json', 'w') as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

# Also copy to root
with open('container-feed.json', 'w') as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"\n✅ Feed escrito: {ts}")
print(f"   GREEN: {green}, YELLOW: {yellow}, NORMAL: {normal}, RED: {red}")
print(f"   Total activos: {total_active}")
print(f"   Excluidos: {total_excluded}")
print(f"\n📊 POST-CHANGE EXPECTED: 21 active (2g/6y/13n/0r), 22 excluded")
print(f"📊 ACTUAL: {total_active} active ({green}g/{yellow}y/{normal}n/{red}r), {total_excluded} excluded")
