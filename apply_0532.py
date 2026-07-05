#!/usr/bin/env python3
"""
apply_0532.py — Corrida Jul 05 05:32 PT
- Update lastVerifiedAt + verificationSource on all 25 active rows
- Update staleStateGuard on all active rows  
- Update 7 excluded items with re-verified reason (Jonathan Heredia emails + WMS CLOSED)
- Update feed timestamps
- NO state changes — all 25 active rows confirmed correct
"""

import json
import re
from datetime import datetime, timezone, timedelta

PACIFIC = timezone(timedelta(hours=-7))

# --- Load feed ---
with open("public/container-feed.json", "r") as f:
    feed = json.load(f)

NEW_VERIFIED_AT = "2026-07-05T05:32:00-07:00"
NEW_VERIFICATION_SOURCE = "WMS+Outlook Jul 05 05:05 PT"
NEW_LAST_UPDATED = "2026-07-05T05:32:00-07:00"
NEW_LAST_VERIFICATION_RUN = "2026-07-05 05:32 PT"

# ============================================================
# 1. UPDATE ALL 25 ACTIVE ROWS
# ============================================================
for row in feed["rows"]:
    row["lastVerifiedAt"] = NEW_VERIFIED_AT
    row["verificationSource"] = NEW_VERIFICATION_SOURCE
    
    # Update staleStateGuard — replace old timestamps with new
    old_guard = row.get("staleStateGuard", "")
    # Replace "04:35 PT" with "05:32 PT" and update the date part
    new_guard = old_guard.replace("04:35 PT", "05:32 PT")
    new_guard = new_guard.replace("2026-07-05 04:35", "2026-07-05 05:32")
    new_guard = new_guard.replace("04:25 PT", "05:05 PT")  # verification source ref
    # Also replace any "WMS+Outlook+YMS run 2026-07-05 04:25 PT" inside staleStateGuard
    new_guard = re.sub(r"WMS.*run 2026-07-05 04:\d\d PT", "WMS+Outlook Jul 05 05:05 PT re-verified", new_guard)
    row["staleStateGuard"] = new_guard

# ============================================================
# 2. UPDATE 7 EXCLUDED ITEMS (re-confirmed from Jonathan Heredia emails)
# ============================================================
excluded_updates = {
    "RN-188040": {
        "container": "MRKU9748297 (PO6368a Alnor)",
        "reason": "Both receiving+putaway tasks closed in WMS (Jul 05 05:05 PT re-confirmed — Jonathan Heredia). Recv TASK-5306833 FORCE_CLOSED + Putaway TASK-5307517 CLOSED.",
        "putTask": "TASK-5307517 CLOSED",
        "recvTask": "TASK-5306833 FORCE_CLOSED",
        "removedAt": "2026-07-05T05:05:00-07:00"
    },
    "RN-5008448": {
        "container": "DDDU5053432",
        "reason": "Both receiving+putaway tasks closed in WMS (Jul 05 05:05 PT re-confirmed — Jonathan Heredia). Recv TASK-5306835 CLOSED + Putaway TASK-5307532 CLOSED. RN CLOSED. YMS: vacio recogido Jul 2.",
        "putTask": "TASK-5307532 CLOSED",
        "recvTask": "TASK-5306835 CLOSED",
        "removedAt": "2026-07-05T05:05:00-07:00"
    },
    "RN-5008445": {
        "container": "OOCU7355889",
        "reason": "Both receiving+putaway tasks closed in WMS (Jul 05 05:05 PT re-confirmed — Jonathan Heredia). Recv TASK-5307534 CLOSED (Fatima) + Putaway TASK-5307737 CLOSED (jlnieves). RN CLOSED.",
        "putTask": "TASK-5307737 CLOSED",
        "recvTask": "TASK-5307534 CLOSED",
        "removedAt": "2026-07-05T05:05:00-07:00"
    },
    "RN-188048": {
        "container": "GN07012026UNIS-1131 (53166)",
        "reason": "Both receiving+putaway tasks closed in WMS (Jul 05 05:05 PT re-confirmed — Jonathan Heredia). Recv TASK-5306832 FORCE_CLOSED + Putaway TASK-5307700 CLOSED. DOCK10.",
        "putTask": "TASK-5307700 CLOSED",
        "recvTask": "TASK-5306832 FORCE_CLOSED",
        "removedAt": "2026-07-05T05:05:00-07:00"
    },
    "RN-188094": {
        "container": "GN07022026UNIS-1133 (53393)",
        "reason": "Both receiving+putaway tasks closed in WMS (Jul 05 05:05 PT re-confirmed — Jonathan Heredia). Recv TASK-5307936 FORCE_CLOSED + Putaway TASK-5308246 CLOSED. DOCK41.",
        "putTask": "TASK-5308246 CLOSED",
        "recvTask": "TASK-5307936 FORCE_CLOSED",
        "removedAt": "2026-07-05T05:05:00-07:00"
    },
    "RN-187978": {
        "container": "GN06302026UNIS-1126 (53180)",
        "reason": "Both receiving+putaway tasks closed in WMS (Jul 05 05:05 PT re-confirmed — Jonathan Heredia). Recv TASK-5304933 CLOSED + Putaway TASK-5305439 CLOSED. DOCK1.",
        "putTask": "TASK-5305439 CLOSED",
        "recvTask": "TASK-5304933 CLOSED",
        "removedAt": "2026-07-05T05:05:00-07:00"
    },
    "RN-188031": {
        "container": "GN06302026UNIS-1129 (53169)",
        "reason": "Both receiving+putaway tasks closed in WMS (Jul 05 05:05 PT re-confirmed — Jonathan Heredia). Recv TASK-5306175 FORCE_CLOSED + Putaway TASK-5306958 CLOSED. RN EXCEPTION. DOCK148.",
        "putTask": "TASK-5306958 CLOSED",
        "recvTask": "TASK-5306175 FORCE_CLOSED",
        "removedAt": "2026-07-05T05:05:00-07:00"
    }
}

for item in feed["excluded"]:
    rn = item.get("rn", "")
    if rn in excluded_updates:
        update = excluded_updates[rn]
        item["reason"] = update["reason"]
        if update.get("putTask"):
            item["putTask"] = update["putTask"]
        if update.get("recvTask"):
            item["recvTask"] = update["recvTask"]
        item["removedAt"] = update["removedAt"]
        if update.get("container"):
            item["container"] = update["container"]

# ============================================================
# 3. UPDATE FEED-LEVEL FIELDS
# ============================================================
feed["lastUpdated"] = NEW_LAST_UPDATED
feed["lastVerificationRun"] = NEW_LAST_VERIFICATION_RUN
feed["verificationSource"] = NEW_VERIFICATION_SOURCE
feed["verifiedBy"] = "PritiAgent — corrida completa 2026-07-05 05:05 PT"
feed["messageTimestamp"] = "2026-07-05T05:05:00-07:00"

# Update message
feed["message"] = ("Corrida Jul 05 05:05 PT — 25 activos confirmados sin cambios. "
                   "7 excluidos re-confirmados (Jonathan Heredia + WMS CLOSED). "
                   "Anti-estado-viejo validado: 0 PRE-ENTRY con evidencia física. "
                   "RN-188084 putaway IN_PROGRESS — NO se remueve.")

# Update summary
feed["summary"] = ("Corrida Jul 05 05:05 PT — 25 activos: 6🟢 EN YARDA, 7🟡 EN PROCESO, "
                   "3🟠 DEGRADADOS, 8📅 PRE-ENTRY, 1📋 TRANSFER. "
                   "26 excluidos (7 re-confirmados Jonathan Heredia). "
                   "0 cambios de estado. AntiEstadoViejo ✅.")

# Update alerts
feed["alerts"] = [
    "🔧 CORRIDA Jul 05 05:05 PT: 25 activos confirmados sin cambios de estado. 7 excluidos re-confirmados (Jonathan Heredia + WMS). AntiEstadoViejo validado ✅.",
    "📋 7 EXCLUIDOS RE-CONFIRMADOS: MRKU9748297, DDDU5053432, OOCU7355889, GN07012026UNIS-1131, GN07022026UNIS-1133, GN06302026UNIS-1126, GN06302026UNIS-1129 — ambos tasks cerrados en WMS (Jonathan Heredia).",
    "⚠️ 5 no-shows con cita vencida: EITU9363654, TGBU8815453, LabelKing PO7937, LabelKing PO8357, ITL07012026.",
    "🚨 RN-5006269 (MAWB 00120698274): 125d+ estancado. Entry List NO DATA. Evaluar cierre con Rufino.",
    "🚨 RN-183707 (ALNOR04242026): 69d+ estancado. 2 RNs. Entry List NO DATA. Evaluar cierre con Rufino.",
    "⚠️ CSGU6429436: 3.5d+ en recibo IN_PROGRESS DOCK68. Jonathan reportó EMPTY. WMS contradice.",
    "⚠️ DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561: Jonathan reportó EMPTY 07/03-07/04 pero WMS recv IN_PROGRESS.",
    "⚠️ MATU2656138 (RN-5008572): Degradado. YMS gate-in sin ubicación + Entry List NO DATA + Rufino dice 'no RN'.",
    "✅ RN-188084 (GN07012026UNIS-1132): Putaway TASK-5307890 IN_PROGRESS (31 LPs). NO se remueve.",
    "✅ Anti-estado-viejo validado: 8 PRE-ENTRY confirmados sin receiving task ni evidencia física en WMS/YMS. Correcto.",
    "📊 6🟢 EN YARDA (Entry List/YMS ✅), 7🟡 EN PROCESO, 3🟠 DEGRADADOS, 8📅 PRE-ENTRY, 1📋 TRANSFER."
]

# Update emailMonitor
feed["emailMonitor"]["lastChecked"] = "2026-07-05T05:05:00-07:00"
feed["emailMonitor"]["latestFindings"] = ("Outlook corrida 05:05 PT: Jonathan Heredia emails re-confirmed 7 containers CLOSED in WMS. "
                                          "25 activos sin cambios. Anti-estado-viejo: 8 PRE-ENTRY validados sin evidencia física.")

# Update guardrails
feed["guardrails"]["staleStateGuard"] = "ACTIVE 2026-07-05 05:32 PT — 25 activos re-verificados. 7 excluidos re-confirmados. AntiEstadoViejo validado."
feed["guardrails"]["antiEstadoViejo"] = "ACTIVE — 0 cambios de estado. 8 PRE-ENTRY sin receiving task confirmado. Regla #8 cumplida."
feed["guardrails"]["closedRemovalRule"] = "ACTIVE — 26 excluidos (recv+putaway ambos cerrados). 7 re-confirmados esta corrida (Jonathan Heredia)."

# Update emailMonitor
feed["emailMonitor"]["lastChecked"] = "2026-07-05T05:05:00-07:00"

# Write updated feed
with open("public/container-feed.json", "w") as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

# --- Verify ---
with open("public/container-feed.json", "r") as f:
    verified = json.load(f)

print(f"✅ Feed updated successfully!")
print(f"   Active rows: {len(verified['rows'])}")
print(f"   Excluded:    {len(verified['excluded'])}")
print(f"   lastUpdated: {verified['lastUpdated']}")
print(f"   verificationSource: {verified['verificationSource']}")

# Check all rows have new timestamp
all_updated = all(r.get("lastVerifiedAt") == NEW_VERIFIED_AT for r in verified["rows"])
print(f"   All rows lastVerifiedAt updated: {all_updated}")

# Count recvTask statuses
from collections import Counter
statuses = Counter(r.get("recvTask", "NONE") for r in verified["rows"])
print(f"   RecvTask distribution: {dict(statuses)}")

# Check the 7 excluded items
updated_excluded = 0
for item in verified["excluded"]:
    rn = item.get("rn", "")
    if rn in excluded_updates:
        updated_excluded += 1
        print(f"   ✅ Excluded {rn}: {item.get('reason','')[:80]}...")
print(f"   Total excluded items updated: {updated_excluded}/7")
