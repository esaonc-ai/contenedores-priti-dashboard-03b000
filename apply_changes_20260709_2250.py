#!/usr/bin/env python3
"""Apply changes: Remove CMAU8611150/RN-5008676, update notes on 4 rows, fix CAAU7998380 green→normal."""

import json, copy, datetime

with open('container-feed.json', 'r') as f:
    feed = json.load(f)

now_pt = datetime.datetime(2026, 7, 9, 0, 0, 0)  # Approx; will be overridden
timestamp = "2026-07-09T00:00:00-07:00"

# ─────────────────────────────────────────────────
# 1. REMOVE CMAU8611150 / RN-5008676 from active
# ─────────────────────────────────────────────────
removed_row = None
for r in feed['rows']:
    if r.get('rn') == 'RN-5008676' and 'CMAU8611150' in r.get('container', ''):
        removed_row = copy.deepcopy(r)
        break

if removed_row:
    feed['rows'] = [r for r in feed['rows'] if not (r.get('rn') == 'RN-5008676' and 'CMAU8611150' in r.get('container', ''))]
    
    # Build excluded entry
    excluded_entry = {
        "rn": "RN-5008676",
        "reason": "WMS RN CLOSED. Recv TASK-5311612 CLOSED. DOCK65. Fecha remocion: 2026-07-08 ~22:50 PT.",
        "container": "CMAU8611150",
        "removedAt": "2026-07-08T22:50:00-07:00",
        "wasActive": True,
        "wasColor": "yellow",
        "wasStatus": "EN_PROCESO",
        "wasDock": "DOCK65",
        "recvTask": "TASK-5311612 CLOSED"
    }
    feed['excluded'].insert(0, excluded_entry)
    print("✓ REMOVED CMAU8611150/RN-5008676 → excluded")
else:
    print("✗ CMAU8611150/RN-5008676 NOT FOUND in active rows")

# ─────────────────────────────────────────────────
# 2. Update MRKU9388930 / RN-188088
# ─────────────────────────────────────────────────
for r in feed['rows']:
    if r.get('rn') == 'RN-188088':
        r['dock'] = 'DOCK63'
        r['note'] = (
            "RECEIVING IN_PROGRESS. TASK-5311340 OFFLOAD (Caren). DOCK63. ET-1119932. "
            "YMS confirms EN YARDA DOCK63, EMPTY_AFTER_OFFLOADED, ET-1119932, gate check-in Jul 8 13:19, "
            "yard check EMPTY Jul 8 21:04. ⚠️ Priti reporta vacío/ready pickup."
        )
        r['notes'] = r['note']
        r['lastVerifiedAt'] = '2026-07-08T22:50:00-07:00'
        r['verificationSource'] = 'YMS cross-check 22:50 PT — EMPTY_AFTER_OFFLOADED DOCK63'
        print("✓ Updated MRKU9388930/RN-188088 — YMS verification, DOCK63")
        break

# ─────────────────────────────────────────────────
# 3. Update CAAU7998380 / RN-5008646 — green→normal
# ─────────────────────────────────────────────────
for r in feed['rows']:
    if r.get('rn') == 'RN-5008646':
        r['color'] = 'normal'
        r['status'] = 'PRE_ENTRY'
        r['inYard'] = True  # WMS says yes, but YMS has no physical evidence
        r['note'] = (
            "⚠️ WMS confirms inYard since Jul 8 09:12, IMPORTED, no receive task yet. "
            "Sin evidencia YMS física (sin gate-in/yard-check/drop). "
            "Per greenEvidenceRule: YMS physical evidence required for green. Mantener NORMAL/PRE-ENTRY."
        )
        r['notes'] = r['note']
        r['lastVerifiedAt'] = '2026-07-08T22:50:00-07:00'
        r['verificationSource'] = 'WMS cross-check 22:50 PT — WMS inYard=true, YMS sin evidencia física → NORMAL'
        r['falseGreenCorrected'] = True
        # Remove any green-related fields
        r.pop('antiEstadoViejo', None)
        print("✓ Updated CAAU7998380/RN-5008646 — green→normal, WMS note")
        break

# ─────────────────────────────────────────────────
# 4. Update TGSU5157420 / RN-5008666
# ─────────────────────────────────────────────────
for r in feed['rows']:
    if r.get('rn') == 'RN-5008666':
        r['note'] = (
            "UFB-128971. WMS IMPORTED APPT-6033193. Batch TGSU5157420+TGSU5157415. "
            "Anunciado por ImportExport (Jasmine) 07/08 12:26 PT. "
            "⚠️ Drop window Jul 8 20:00-22:00 VENCIDO. Sin gate-in. Posible no-show."
        )
        r['notes'] = r['note']
        r['lastVerifiedAt'] = '2026-07-08T22:50:00-07:00'
        print("✓ Updated TGSU5157420/RN-5008666 — expired drop window note")
        break

# ─────────────────────────────────────────────────
# 5. Update FFAU2426030 / RN-5008480
# ─────────────────────────────────────────────────
for r in feed['rows']:
    if r.get('rn') == 'RN-5008480':
        r['note'] = (
            "⚠️ Daniela reporta vacío 07/08. WMS shows assigned to Fatima Ponce. "
            "Recv TASK-5307691 CLOSED. No putaway task yet. "
            "YMS: YARD_CHECK Spot 565, TRAILER EMPTY."
        )
        r['notes'] = r['note']
        r['lastVerifiedAt'] = '2026-07-08T22:50:00-07:00'
        print("✓ Updated FFAU2426030/RN-5008480 — Fatima Ponce assignment note")
        break

# ─────────────────────────────────────────────────
# Recalculate counts
# ─────────────────────────────────────────────────
active_rows = feed['rows']
total_active = len(active_rows)
green = sum(1 for r in active_rows if r.get('color') == 'green')
yellow = sum(1 for r in active_rows if r.get('color') == 'yellow')
normal = sum(1 for r in active_rows if r.get('color') == 'normal')
red = sum(1 for r in active_rows if r.get('color') == 'red')

total_excluded = len(feed['excluded'])

# Update all counts
feed['totalActive'] = total_active
feed['totalExcluded'] = total_excluded
feed['summary'] = {
    'red': red, 'green': green, 'normal': normal, 'yellow': yellow,
    'totalActive': total_active, 'totalExcluded': total_excluded,
    'excludedThisRun': 1, 'manualAdditions': 0, 'rnUpdatesThisRun': 0,
    'dockUpdatesThisRun': 1, 'reactivatedThisRun': 0, 'notesUpdatedThisRun': 4,
    'falseGreensCorrected': 1, 'promotedToGreenThisRun': 0,
    'demotedFromGreenThisRun': 1, 'promotedToYellowThisRun': 0,
    'appointmentsUpdatedThisRun': 0
}

now_str = "2026-07-08T22:50:00-07:00"
feed['lastUpdated'] = now_str

# Update message
feed['message'] = (
    f"CORRECCIÓN Jul 8 2026-07-08 22:50 PT — "
    f"REMOVIDO: CMAU8611150 (RN-5008676) WMS RN CLOSED (recv TASK-5311612). "
    f"CAAU7998380 green→normal (sin evidencia YMS). "
    f"{total_active} activos ({green}g/{yellow}y/{normal}n/{red}r). {total_excluded} excluidos."
)

# Update _corrections
feed['_corrections'] = {
    "alert": feed['message'],
    "timestamp": now_str,
    "ymsCheckNote": "CMAU8611150 WMS RN CLOSED. CAAU7998380: WMS inYard=true pero YMS sin evidencia física → NORMAL.",
    "removalsThisRun": [{"rn": "RN-5008676", "reason": "WMS RN CLOSED. Recv TASK-5311612 CLOSED. DOCK65.", "container": "CMAU8611150"}],
    "additionsThisRun": [],
    "demotionsThisRun": [{"rn": "RN-5008646", "from": "green", "to": "normal", "reason": "Sin evidencia física YMS per greenEvidenceRule"}],
    "promotionsThisRun": [],
    "notesUpdatedThisRun": ["RN-188088", "RN-5008646", "RN-5008666", "RN-5008480"]
}

# Update guardrails
feed['guardrails']['closedRemovalRule'] = {
    "status": "ACTIVE",
    "removalNote": f"Jul 8 2026-07-08 22:50 PT: 1 removal (CMAU8611150). {total_excluded} excluidos total.",
    "removalsThisRun": 1,
    "reactivationsThisRun": 0
}
feed['guardrails']['greenEvidenceRule'] = {
    "status": "ACTIVE",
    "promotionNote": f"Jul 8 2026-07-08 22:50 PT: 1 demotion (CAAU7998380 green→normal). {green} green activos. YMS physical evidence required.",
    "demotionsThisRun": 1,
    "promotionsThisRun": 0,
    "falseGreensDetected": 1
}

# Update alerts
feed['alerts'] = [
    f"✅ CORRECCIÓN 2026-07-08 22:50 PT: REMOVIDO CMAU8611150 (RN-5008676) WMS RN CLOSED. CAAU7998380 green→normal. {total_active} activos ({green}g/{yellow}y/{normal}n/{red}r). {total_excluded} excluidos.",
    "📝 CMAU8611150 (RN-5008676): REMOVIDO. WMS RN CLOSED. Receive TASK-5311612 CLOSED. DOCK65.",
    "📝 CAAU7998380 (RN-5008646): green→normal. Sin evidencia física YMS. WMS inYard confirmado pero greenEvidenceRule requiere YMS.",
    "⚠️ MRKU9388930 (RN-188088): YMS confirma EMPTY_AFTER_OFFLOADED DOCK63. Yard check EMPTY Jul 8 21:04.",
    "⚠️ TGSU5157420 (RN-5008666): Drop window Jul 8 20:00-22:00 VENCIDO. Posible no-show.",
    "🟠 ALERTA ROLAS: FFAU2426030 (RN-5008480) — Reportado VACÍO por Daniela. WMS assigned Fatima Ponce.",
    "🔴 ALERTA ROLAS CRÍTICA: CSGU6429436 (RN-5008479) — CONTENEDOR FANTASMA en DOCK45.",
    "⚠️ TIIU6675897: Sin RN WMS aún. Drop 07/09 12:00-14:00. PENDIENTE item setup.",
    "⚠️ TGSU5157375: Sin RN WMS. Anunciado Jasmine 07/08 17:47 PT."
]

feed['verificationSource'] = f"WMS+YMS cross-check 2026-07-08 22:50 PT — 1 removal (CMAU8611150 CLOSED), 1 demotion (CAAU7998380 green→normal)"

# Write root feed
with open('container-feed.json', 'w') as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

# Also write to public/
with open('public/container-feed.json', 'w') as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"\n=== FINAL COUNTS ===")
print(f"Active: {total_active} (green={green}, yellow={yellow}, normal={normal}, red={red})")
print(f"Excluded: {total_excluded}")
print(f"Expected: 21 active (0g/6y/15n), 26 excluded")
print(f"Match: {'✅' if total_active==21 and green==0 and yellow==6 and normal==15 and total_excluded==26 else '❌'}")
