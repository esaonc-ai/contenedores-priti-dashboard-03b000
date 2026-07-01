#!/usr/bin/env python3
"""
CORRIDA Jul 1 13:40 PT — Cross-ref WMS+YMS fresh queries (13:32 PT).
Changes:
  1. REMOVE TCNU4379515 (RN-5008399) — WMS CLOSED (receive + putaway CLOSED)
  2. REMOVE OOLU9324944 (RN-5008430) — YMS GATE_CHECK_OUT, WMS IMPORTED sin inYardTime
  3. UPDATE OOCU8342103 dock: DOCK68 → DOCK574 (WMS confirmed)
  4. UPDATE BSIU8440908 dock: DOCK62 → DOCK566 (WMS confirmed)
  5. UPDATE FFAU1548537: latest WMS shows receive task TASK-5304579 NEW
  6. Mark RN-5008444+RN-5008449 duplicate alert
  7. Incremental update — preserve all other rows and metadata
"""

import json
from datetime import datetime, timezone, timedelta

now_pt = datetime.now(timezone(timedelta(hours=-7)))
ts = now_pt.strftime('%Y-%m-%dT%H:%M:%S-07:00')

# Load live feed (fetched from Coolify at 13:42 PT)
with open('public/container-feed.json', 'r') as f:
    feed = json.load(f)

rows = feed.get('rows', [])
excluded = feed.get('excludedContainers', [])

# ============================================================
# 1. REMOVE TCNU4379515 → CLOSED
# ============================================================
tcn_row = None
for i, r in enumerate(rows):
    if r.get('rn') == 'RN-5008399' or 'TCNU4379515' in r.get('container', ''):
        tcn_row = rows.pop(i)
        break

if tcn_row:
    excluded.append({
        "container": "TCNU4379515",
        "rn": "RN-5008399",
        "reason": "CLOSED WMS Jul 1 20:30 — receive TASK-5304474 CLOSED + putaway TASK-5304515 CLOSED. Corrida 13:40 PT.",
        "removedAt": ts,
        "removalSource": "WMS live read-only Jul 1 13:32 PT",
        "previousColor": "green"
    })
    print("✅ REMOVIDO: TCNU4379515 (RN-5008399) — CLOSED")

# ============================================================
# 2. REMOVE OOLU9324944 → YMS GATE_CHECK_OUT, no WMS arrival
# ============================================================
oolu_row = None
for i, r in enumerate(rows):
    if r.get('rn') == 'RN-5008430' or 'OOLU9324944' in r.get('container', ''):
        oolu_row = rows.pop(i)
        break

if oolu_row:
    excluded.append({
        "container": "OOLU9324944",
        "rn": "RN-5008430",
        "reason": "YMS GATE_CHECK_OUT Jun 30 23:46. WMS IMPORTED sin inYardTime ni receiving. Sin evidencia de llegada formal. Corrida 13:40 PT.",
        "removedAt": ts,
        "removalSource": "WMS+YMS live read-only Jul 1 13:32 PT",
        "previousColor": "green"
    })
    print("✅ REMOVIDO: OOLU9324944 (RN-5008430) — YMS departed, sin llegada WMS")

# ============================================================
# 3. UPDATE docks: OOCU8342103 → DOCK574, BSIU8440908 → DOCK566
# ============================================================
for r in rows:
    rn = r.get('rn', '')
    if rn == 'RN-5008386':  # OOCU8342103
        old_dock = r.get('dock', '')
        r['dock'] = 'DOCK574'
        if 'DOCK68' in r.get('status', ''):
            r['status'] = r['status'].replace('DOCK68', 'DOCK574')
        if 'DOCK68' in r.get('entry', ''):
            r['entry'] = r['entry'].replace('DOCK68', 'DOCK574')
        r['note'] = r.get('note', '') + ' | Dock actualizado DOCK574 (WMS Jul 1 13:32).'
        r['lastVerifiedAt'] = ts
        r['verificationSource'] = 'WMS live read-only Jul 1 13:32 PT'
        print(f"✅ UPDATED dock: OOCU8342103 {old_dock} → DOCK574")
    
    if rn == 'RN-5008387':  # BSIU8440908
        old_dock = r.get('dock', '')
        r['dock'] = 'DOCK566'
        if 'DOCK62' in r.get('status', ''):
            r['status'] = r['status'].replace('DOCK62', 'DOCK566')
        if 'DOCK62' in r.get('entry', ''):
            r['entry'] = r['entry'].replace('DOCK62', 'DOCK566')
        r['note'] = r.get('note', '') + ' | Dock actualizado DOCK566 (WMS Jul 1 13:32).'
        r['lastVerifiedAt'] = ts
        r['verificationSource'] = 'WMS live read-only Jul 1 13:32 PT'
        print(f"✅ UPDATED dock: BSIU8440908 {old_dock} → DOCK566")
    
    if rn == 'RN-5008428':  # FFAU1548537 — latest WMS shows receive task NEW
        if 'TASK-5304579' in r.get('status', '') and 'IN_PROGRESS' in r.get('status', ''):
            r['status'] = r['status'].replace('IN_PROGRESS', 'NEW')
        if 'TASK-5304579' in r.get('entry', '') and 'IN_PROGRESS' in r.get('entry', ''):
            r['entry'] = r['entry'].replace('IN_PROGRESS', 'NEW')
        r['note'] = r.get('note', '') + ' | Último WMS Jul 1 13:32: RT TASK-5304579 → NEW.'
        r['lastVerifiedAt'] = ts
        r['verificationSource'] = 'WMS live read-only Jul 1 13:32 PT'
        print(f"✅ UPDATED: FFAU1548537 receive task → NEW")

# Add duplicate alert for LabelKing
for r in rows:
    if r.get('rn') == 'RN-5008444':
        r['note'] = r.get('note', '') + ' | ⚠️ DUPLICADO con RN-5008449 (mismo containerNo LabelKing07012026, mismo bolNo).'
        break

# ============================================================
# Recalculate summary
# ============================================================
green_count = sum(1 for r in rows if r.get('color') == 'green')
yellow_count = sum(1 for r in rows if r.get('color') == 'yellow')
red_count = sum(1 for r in rows if r.get('color') == 'red')
normal_count = sum(1 for r in rows if r.get('color') == 'normal')

feed['summary'] = {
    "green": green_count,
    "yellow": yellow_count,
    "red": red_count,
    "normal": normal_count
}

feed['totalActive'] = len(rows)
feed['totalExcluded'] = len(excluded)

# Update timestamp
feed['lastUpdated'] = ts
feed['message'] = f"Corrida Jul 1 13:40 PT: removidos TCNU4379515 (CLOSED) + OOLU9324944 (YMS departed); docks OOCU8342103→DOCK574, BSIU8440908→DOCK566; FFAU1548537 RT→NEW; duplicado RN-5008444/RN-5008449."

# Add alerts
new_alerts = [
    f"🔄 CORRIDA Jul 1 13:40 PT: WMS/YMS fresh cross-ref.",
    f"🗑️ REMOVIDOS: TCNU4379515/RN-5008399 (CLOSED) y OOLU9324944/RN-5008430 (YMS departed).",
    f"📍 DOCKS ACTUALIZADOS: OOCU8342103 → DOCK574, BSIU8440908 → DOCK566.",
    f"⚠️ DUPLICADO: RN-5008444 y RN-5008449 comparten containerNo=LabelKing07012026.",
    f"✅ CSGU6429436 confirmado EN YARDA DOCK45 (YMS GATE_CHECKED_IN).",
    f"✅ CAIU9453139 confirmado EN PROCESO (WMS IN_PROGRESS, TASK-5304239).",
    f"✅ DDDU5053860 cita Jul 2 18:00 confirmada WMS.",
]

feed['alerts'] = new_alerts + feed.get('alerts', [])

# Update guardrails
feed['guardrails'] = feed.get('guardrails', {})
feed['guardrails']['lastFullRun'] = ts
feed['guardrails']['lastWmsYmsAudit'] = ts

# Write
with open('public/container-feed.json', 'w') as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"\n✅ FEED ACTUALIZADO: {ts}")
print(f"   GREEN: {green_count}, YELLOW: {yellow_count}, RED: {red_count}, NORMAL: {normal_count}")
print(f"   Total activos: {len(rows)}")
print(f"   Excluidos: {len(excluded)}")
