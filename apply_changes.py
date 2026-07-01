#!/usr/bin/env python3
"""
Apply changes to container-feed.json:
1. Remove RN-5008361 (CORRU0629026UNIS) → excluded
2. Add OOCU5501937 (RN-5008506) as PRE-ENTRY
3. Add CBHU7024789 (RN-5008507) as PRE-ENTRY
4. Fix RN-5008450: update container to BEAU5553433
5. Fix JTAU7362598 (RN-5008424): refresh verification
"""

import json
import copy
from datetime import datetime, timezone, timedelta

PST = timezone(timedelta(hours=-7))
now = datetime.now(PST)
timestamp = now.strftime('%Y-%m-%dT%H:%M:%S%z')
# Fix timezone format
timestamp = timestamp[:-2] + ':' + timestamp[-2:]

with open('public/container-feed.json', 'r') as f:
    feed = json.load(f)

print(f"Original: {feed['totalActive']} active, {feed['totalExcluded']} excluded")

changes = []

# ===== 1. REMOVE RN-5008361 (CORRU0629026UNIS) =====
removed_row = None
for i, r in enumerate(feed['rows']):
    if r.get('rn') == 'RN-5008361':
        removed_row = feed['rows'].pop(i)
        changes.append(f"REMOVED RN-5008361 / CORRU0629026UNIS")
        break

if removed_row:
    excluded_entry = {
        "container": removed_row.get("container", "CORRU0629026UNIS"),
        "rn": "RN-5008361",
        "rnStatus": removed_row.get("rnStatus", "IN_PROGRESS"),
        "reason": f"WMS closed audit {now.strftime('%b %d %H:%M')} PT: RN-5008361 receiving FORCE_CLOSED + putaway completed. Removido del activo por solicitud de Rufino.",
        "removedAt": timestamp,
        "removalSource": "WMS closed audit + Rufino request",
        "lastStatus": removed_row.get("status", ""),
        "lastVerifiedAt": timestamp,
        "verificationSource": "WMS closed audit + deploy request"
    }
    feed.setdefault('excludedContainers', []).insert(0, excluded_entry)
    feed['totalExcluded'] = feed.get('totalExcluded', 0) + 1

# ===== 2. ADD OOCU5501937 (RN-5008506) =====
new_rn_5008506 = {
    "container": "OOCU5501937",
    "rn": "RN-5008506",
    "rnStatus": "IMPORTED",
    "receipt": "RN-5008506",
    "dock": "—",
    "entry": "PRE-ENTRY · Nuevo RN Gurunanda · Pendiente cita/llegada",
    "inYard": False,
    "color": "normal",
    "appointmentTime": "Pendiente",
    "note": f"NUEVO {now.strftime('%b %d %H:%M')} PT: Agregado por solicitud de Rufino. RN-5008506 IMPORTED · OOCU5501937 · Gurunanda. Verificar WMS/YMS para cita y llegada.",
    "status": "📅 PRE-ENTRY — RN-5008506 IMPORTED · OOCU5501937 · Gurunanda · Pendiente verificación",
    "lastVerifiedAt": timestamp,
    "verificationSource": "Rufino request + deploy",
    "staleStateGuard": "OK_NO_ARRIVAL_EVIDENCE"
}
feed['rows'].append(new_rn_5008506)
changes.append(f"ADDED OOCU5501937 / RN-5008506 (PRE-ENTRY)")

# ===== 3. ADD CBHU7024789 (RN-5008507) =====
new_rn_5008507 = {
    "container": "CBHU7024789",
    "rn": "RN-5008507",
    "rnStatus": "IMPORTED",
    "receipt": "RN-5008507",
    "dock": "—",
    "entry": "PRE-ENTRY · Nuevo RN Gurunanda · Pendiente cita/llegada",
    "inYard": False,
    "color": "normal",
    "appointmentTime": "Pendiente",
    "note": f"NUEVO {now.strftime('%b %d %H:%M')} PT: Agregado por solicitud de Rufino. RN-5008507 IMPORTED · CBHU7024789 · Gurunanda. Verificar WMS/YMS para cita y llegada.",
    "status": "📅 PRE-ENTRY — RN-5008507 IMPORTED · CBHU7024789 · Gurunanda · Pendiente verificación",
    "lastVerifiedAt": timestamp,
    "verificationSource": "Rufino request + deploy",
    "staleStateGuard": "OK_NO_ARRIVAL_EVIDENCE"
}
feed['rows'].append(new_rn_5008507)
changes.append(f"ADDED CBHU7024789 / RN-5008507 (PRE-ENTRY)")

# ===== 4. FIX RN-5008450 — update container name =====
for r in feed['rows']:
    if r.get('rn') == 'RN-5008450':
        old_container = r.get('container', '')
        r['container'] = 'BEAU5553433 (LabelKing07012026, RN-5008450)'
        r['note'] = f"Corregido {now.strftime('%b %d %H:%M')} PT: container actualizado a BEAU5553433. WMS inYardTime Jul 1 18:36 + TASK-5305892 receiving IN_PROGRESS."
        r['lastVerifiedAt'] = timestamp
        r['verificationSource'] = 'WMS/YMS + deploy correction'
        changes.append(f"FIXED RN-5008450: container updated to BEAU5553433")

# ===== 5. FIX JTAU7362598 (RN-5008424) — refresh =====
for r in feed['rows']:
    if r.get('rn') == 'RN-5008424':
        r['lastVerifiedAt'] = timestamp
        r['verificationSource'] = 'WMS/YMS recheck + deploy'
        r['note'] = f"Revalidado {now.strftime('%b %d %H:%M')} PT: YMS DOCK_CHECKED_IN DOCK156. RN-5008424 IMPORTED activo. Sin receiveTask aún. AMERICAN CARRIERS."
        changes.append(f"FIXED JTAU7362598 / RN-5008424: re-verified")

# ===== Update metadata =====
feed['totalActive'] = len(feed['rows'])
feed['lastUpdated'] = timestamp
feed['message'] = f"Deploy {now.strftime('%b %d %H:%M')} PT: {', '.join(changes)}. Total: {feed['totalActive']} activos, {feed['totalExcluded']} excluidos."
feed['messageTimestamp'] = timestamp
feed['guardrails']['lastFullRun'] = timestamp
feed['guardrails']['lastClosedAudit'] = timestamp

# Update summary counts
green = sum(1 for r in feed['rows'] if r.get('color') == 'green')
yellow = sum(1 for r in feed['rows'] if r.get('color') == 'yellow')
normal = sum(1 for r in feed['rows'] if r.get('color') == 'normal')
red = sum(1 for r in feed['rows'] if r.get('color') == 'red')
feed['summary'] = {'green': green, 'yellow': yellow, 'normal': normal, 'red': red}

# Add alert for new additions
feed.setdefault('alerts', [])
feed['alerts'].insert(0, f"⚠️ RN-5008361 / CORRU0629026UNIS removido: receiving FORCE_CLOSED + putaway completado.")
feed['alerts'].insert(1, f"⚠️ NUEVOS: OOCU5501937 (RN-5008506) y CBHU7024789 (RN-5008507) agregados como PRE-ENTRY Gurunanda.")
feed['alerts'].insert(2, f"⚠️ RN-5008450 corregido: container BEAU5553433.")

with open('public/container-feed.json', 'w') as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"\n=== CAMBIOS APLICADOS ===")
for c in changes:
    print(f"  ✅ {c}")
print(f"\nUpdated: {feed['totalActive']} active, {feed['totalExcluded']} excluded")
print(f"lastUpdated: {feed['lastUpdated']}")
print(f"summary: {feed['summary']}")
