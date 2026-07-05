#!/usr/bin/env python3
"""Apply MATU2656138 DEGRADADO→EN YARDA promotion to the container feed."""
import json
import sys

# Load the live feed (which is more current than repo version)
with open("public/container-feed.json", "r") as f:
    feed = json.load(f)

TARGET_CONTAINER = "MATU2656138"
NEW_TIME = "2026-07-05T04:50:00-07:00"
NEW_CORRIDA = "2026-07-05 04:50 PT"

# Find and update MATU2656138
found = False
for row in feed["rows"]:
    if TARGET_CONTAINER in row.get("container", ""):
        found = True
        print(f"BEFORE: color={row.get('color')}, status={row.get('status')[:80]}...")

        # === UPDATE ALL FIELDS ===
        row["color"] = "green"
        row["inYard"] = True
        row["status"] = "🟢 EN YARDA — Entry List ✅ ET-1117774 · Gate Check-In confirmado · Sin receiving task · RN-5008572"
        row["entry"] = "En yarda · Entry List ✅ ET-1117774 · Gate Check-In NATHAN HAO/HAW TRUCKING · Sin receiving task · RN-5008572"
        row["dock"] = "PENDIENTE (sin dock asignado)"
        row["note"] = "✅ PROMOVIDO DEGRADADO→EN YARDA Jul 5 04:50 PT. WMS Entry List ET-1117774 confirmado (NATHAN HAO, HAW TRUCKING INC, DROP_OFF_DELIVERY). YMS GATE_CHECKED_IN Jul 2 20:11 PT, sin check-out. RN-5008572 existe en WMS pero sin receiving task. DO no está con UNIS (Rufino). Sin dock asignado. PO# 8190/8107/8144."
        row["alerta"] = "⚠️ Sin receiving task. RN-5008572 existe pero DO no está con UNIS (Rufino). Sin dock asignado."
        row["ymsStatus"] = "GATE_CHECKED_IN Jul 2 20:11 PT (ET-1117774, NATHAN HAO, HAW TRUCKING INC, DROP_OFF_DELIVERY). Entry List ✅ confirmado. Sin check-out."
        row["assignedTo"] = "Pendiente (sin receiving task)"
        row["recvTask"] = "NINGUNO"
        row["lastVerifiedAt"] = NEW_TIME
        row["verificationSource"] = "WMS Entry List ET-1117774 + YMS GATE_CHECKED_IN — 2026-07-05 04:50 PT"
        row["staleStateGuard"] = "ACTIVE 2026-07-05 04:50 PT — PROMOVIDO DEGRADADO→EN YARDA. Entry List ✅ ET-1117774 (NATHAN HAO, HAW TRUCKING). YMS gate-in confirmado. Sin receiving task."
        row["promotionReason"] = "Entry List ✅ ET-1117774 confirmado WMS (NATHAN HAO, HAW TRUCKING, DROP_OFF_DELIVERY) + YMS GATE_CHECKED_IN Jul 2 20:11 PT → EN YARDA según Regla Rolas #3."

        # Remove degradation-related fields
        for key in ["degradedAt", "degradedFrom", "degradedReason", "notesCleanupReason", "antiFalseGreenRule", "downgradedAt", "downgradeReason"]:
            row.pop(key, None)

        print(f"AFTER:  color={row.get('color')}, status={row.get('status')[:80]}...")
        break

if not found:
    print(f"ERROR: {TARGET_CONTAINER} not found in rows!")
    sys.exit(1)

# === UPDATE COUNTS ===
en_yarda_count = sum(1 for r in feed["rows"] if r.get("color") == "green")
en_proceso_count = sum(1 for r in feed["rows"] if r.get("color") == "yellow")
degradados_count = sum(1 for r in feed["rows"] if r.get("color") == "orange")
pre_entry_count = sum(1 for r in feed["rows"] if r.get("color") == "normal")

feed["enYarda"] = en_yarda_count
feed["enProceso"] = en_proceso_count
feed["degradados"] = degradados_count
feed["preEntry"] = pre_entry_count

print(f"\nCOUNTS: enYarda={en_yarda_count}, enProceso={en_proceso_count}, degradados={degradados_count}, preEntry={pre_entry_count}")

# === UPDATE TOP-LEVEL FIELDS ===
feed["lastUpdated"] = NEW_TIME
feed["lastVerificationRun"] = "2026-07-05 04:50 PT"
feed["verifiedBy"] = "PritiAgent — corrida 2026-07-05 04:50 PT"
feed["verificationSource"] = "WMS+YMS+Outlook run 2026-07-05 04:50 PT"
feed["messageTimestamp"] = NEW_TIME
feed["message"] = f"Corrida Jul 05 04:50 PT — 1 PROMOCIÓN orange→verde: MATU2656138 (Entry List ✅ ET-1117774 + YMS GATE_CHECKED_IN). {en_yarda_count}🟢 EN YARDA, {en_proceso_count}🟡 EN PROCESO, {degradados_count}🟠 DEGRADADOS, {pre_entry_count}📅 PRE-ENTRY, 1📋 TRANSFER."
feed["summary"] = f"Corrida Jul 05 04:50 PT — 25 activos: {en_yarda_count}🟢 EN YARDA, {en_proceso_count}🟡 EN PROCESO, {degradados_count}🟠 DEGRADADOS, {pre_entry_count-1}📅 PRE-ENTRY, 1📋 TRANSFER. 26 excluidos. ✅ 1 promovido a verde (MATU2656138)."

# === UPDATE ALERTS ===
new_alerts = []
for alert in feed.get("alerts", []):
    if "MATU2656138" in alert and ("degrad" in alert.lower() or "orange" in alert.lower()):
        # Replace degradation alert with promotion alert
        new_alerts.append("✅ PROMOCIÓN: MATU2656138 → EN YARDA. Entry List ✅ ET-1117774 (NATHAN HAO, HAW TRUCKING, DROP_OFF_DELIVERY) + YMS GATE_CHECKED_IN Jul 2 20:11. Sin receiving task. Regla Rolas #3 cumplida.")
    elif "MATU2656138" in alert:
        # Skip old MATU alerts
        continue
    else:
        new_alerts.append(alert)

# Add fresh alert about this promotion
new_alerts.insert(0, f"🔧 CORRIDA Jul 05 04:50 PT: 1 PROMOCIÓN orange→verde: MATU2656138 (Entry List ✅ ET-1117774). {en_yarda_count}🟢 EN YARDA, {degradados_count}🟠 DEGRADADOS.")

feed["alerts"] = new_alerts

# === UPDATE GUARDRAILS ===
feed["guardrails"]["entryListRule"] = f"ACTIVE — Entry List o YMS físico requerido para EN YARDA (Regla Rufino #3). {en_yarda_count} promovidos por Entry List ✅. {degradados_count} degradados por Entry List NO DATA."
feed["guardrails"]["antiEstadoViejo"] = f"ACTIVE — 1 promoción orange→verde esta corrida (MATU2656138 Entry List ✅)."
feed["guardrails"]["staleStateGuard"] = "ACTIVE 2026-07-05 04:50 PT — 1 promovido (MATU2656138 Entry List ✅)."
feed["guardrails"]["ymsReadingRule"] = "ACTIVE (gate check-out ≠ full departure). MATU2656138 promovido a verde: YMS gate-in + Entry List ✅ confirmados."

# === UPDATE emailMonitor ===
feed["emailMonitor"]["lastChecked"] = NEW_TIME
feed["emailMonitor"]["latestFindings"] = "Outlook corrida 04:50 PT: MATU2656138 promovido DEGRADADO→EN YARDA por Entry List ✅ ET-1117774 (NATHAN HAO, HAW TRUCKING)."

# === WRITE ===
with open("public/container-feed.json", "w") as f:
    json.dump(feed, f, ensure_ascii=False, indent=2)

print("\n✅ Feed updated successfully!")
print(f"   Total rows: {len(feed['rows'])}")
print(f"   lastUpdated: {feed['lastUpdated']}")
print(f"   enYarda: {feed['enYarda']}, degradados: {feed['degradados']}")
