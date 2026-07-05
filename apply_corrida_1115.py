#!/usr/bin/env python3
"""Corrida 2026-07-05 11:15 PT — MATU2656138 → EN YARDA + SMCU1114360 → excluded + 12 old → excluded"""
import json
import sys
from datetime import datetime, timezone, timedelta

now_pt = datetime.now(timezone(timedelta(hours=-7)))
NEW_TIME = now_pt.strftime('%Y-%m-%dT%H:%M:%S-07:00')
NEW_CORRIDA = now_pt.strftime('%Y-%m-%d %H:%M PT')

# Load live feed
with open("public/container-feed.json", "r") as f:
    feed = json.load(f)

print(f"Loaded feed: {len(feed['rows'])} rows, {len(feed.get('excludedContainers', feed.get('excluded', [])))} excluded")
print(f"Current lastUpdated: {feed.get('lastUpdated')}")

# ============================================================
# CHANGE #1: MATU2656138 — PRE-ENTRY → EN YARDA
# ============================================================
TARGET = "MATU2656138"
found_matu = False

for row in feed["rows"]:
    if TARGET in row.get("container", ""):
        found_matu = True
        print(f"\n🔧 MATU2656138 BEFORE: color={row.get('color')}, inYard={row.get('inYard')}")

        # Remove degradation/pre-entry fields
        for key in ["degradedAt", "degradedFrom", "degradedReason", "promotionReason",
                     "promotedAt", "downgradedAt", "downgradeReason", "antiFalseGreenRule",
                     "notesCleanupReason", "ymsStatus"]:
            row.pop(key, None)

        # SET EN YARDA
        row["color"] = "green"
        row["inYard"] = True
        row["et"] = "ET-1117774"
        row["dock"] = "PENDIENTE (sin spot/dock asignado en YMS)"
        row["spot"] = "—"
        row["entry"] = "En yarda · GATE_CHECKED_IN ✅ ET-1117774 Jul 2 20:11 PDT · DROP_OFF_DELIVERY · HAW TRUCKING / NATHAN HAO · Sin dock asignado · Sin receive task"
        row["status"] = "🟢 EN YARDA — RN-5008572 IMPORTED · MATU2656138 · GATE_CHECKED_IN ✅ ET-1117774 · Sin receive task · Sin ubicación asignada"
        row["alerta"] = "⚠️ Sin receive task. RN-5008572 existe pero sin tarea asignada. Sin dock/spot en YMS. HAW TRUCKING."
        row["note"] = "✅ CORRIDA 11:15 PT: PROMOVIDO PRE-ENTRY→EN YARDA. YMS ET-1117774 GATE_CHECKED_IN Jul 2 20:11 PDT (operador buenaguard). DROP_OFF_DELIVERY MATU2656138 FULL. Evidencia fotográfica: container, driver NATHAN HAO, vehicle 9G88837, USDOT 2894693. HAW TRUCKING INC. ⚠️ Sin dock/spot asignado (dropOffLocationId null). RN-5008572 IMPORTED pero SIN receive task. DO no está con UNIS (Rufino). PO# 8190/8107/8144."
        row["assignedTo"] = "Pendiente (sin task)"
        row["recvTask"] = "NINGUNO"
        row["receipt"] = "RN-5008572"
        row["rnStatus"] = "IMPORTED"
        row["rn"] = "RN-5008572"
        row["gateCheckIn"] = "2026-07-02T20:11:19-07:00"
        row["appointmentTime"] = "Jul 03 20:00 (APPT-6032807, vencida)"
        row["lastVerifiedAt"] = NEW_TIME
        row["verificationSource"] = "YMS ET-1117774 GATE_CHECKED_IN + WMS RN-5008572 — corrida 2026-07-05 11:15 PT"
        row["antiEstadoViejo"] = True
        row["staleStateGuard"] = f"ACTIVE {NEW_CORRIDA} — PROMOVIDO PRE-ENTRY→EN YARDA. YMS GATE_CHECKED_IN confirmado ET-1117774. ET-1117982 (anterior) era pre-checkin shell sin equipo. Corregido."
        row["promotionReason"] = "YMS ET-1117774 GATE_CHECKED_IN Jul 2 20:11 PDT + DROP_OFF_DELIVERY + evidencia fotográfica → EN YARDA Regla Rolas #3. ET-1117982 anterior era shell administrativo sin equipo."

        print(f"🔧 MATU2656138 AFTER:  color={row.get('color')}, inYard={row.get('inYard')}")
        print(f"   ET corregido: ET-1117982 → ET-1117774")
        break

if not found_matu:
    print(f"❌ ERROR: {TARGET} not found in rows!")
    sys.exit(1)

# ============================================================
# CHANGE #2: SMCU1114360 → excluded
# ============================================================
excluded = feed.get("excludedContainers", feed.get("excluded", []))
smcu_entry = {
    "container": "SMCU1114360",
    "rn": "RN-5008384",
    "reason": "Ambas tasks cerradas. Recv TASK-5303878 FORCE_CLOSED + Putaway TASK-5304043 CLOSED (completado Jun 30). Cita Jun 29.",
    "excludedAt": NEW_TIME,
    "excludedBy": "PritiAgent corrida 2026-07-05 11:15 PT — WMS verified both tasks closed"
}
excluded.append(smcu_entry)
if "excludedContainers" in feed:
    feed["excludedContainers"] = excluded
else:
    feed["excluded"] = excluded
print(f"\n✅ SMCU1114360 (RN-5008384) added to excluded. Total excluded: {len(excluded)}")

# ============================================================
# CHANGE #3: Add 12 old Phase 1/2 containers to excluded
# ============================================================
old_closed = [
    ("EITU8174300", "RN-5008303", "CLOSED Jun 25 — jlnieves"),
    ("CAAU5246296", "RN-5008296", "CLOSED Jun 24 — jlnieves"),
    ("DDDU5053448", "RN-5008297", "CLOSED Jun 25 — employee882504"),
    ("DDDU5053469", "RN-5008298", "CLOSED Jun 25 — employee882504"),
    ("CSNU8563588", "RN-5008300", "CLOSED Jun 26 — jlnieves"),
    ("BEAU6015134", "RN-5008320", "CLOSED Jun 26 — pedrofas39"),
    ("FCIU9601208", "RN-5008321", "CLOSED Jun 26 — employee882504"),
    ("FFAU6121609", "RN-5008322", "CLOSED Jun 26 — employee882504"),
    ("CAAU8362068", "RN-5008373", "CLOSED Jun 29 — jlnieves"),
    ("SEKU4670025", "RN-5008325", "CLOSED Jun 29 — jlnieves"),
    ("TCNU1243715", "RN-5008340", "CLOSED Jun 27 — jeespinoza"),
    ("TIIU7745643", "RN-5008341", "CLOSED Jun 27 — employee882504"),
]

added_old = 0
for container, rn, detail in old_closed:
    # Check if already in excluded
    already = False
    for exc in excluded:
        if container in str(exc.get("container", "")) or rn in str(exc.get("rn", "")):
            already = True
            break
    if not already:
        excluded.append({
            "container": container,
            "rn": rn,
            "reason": f"RN {detail}. Cita Jun 22-26 (Phase 1/2). WMS verified CLOSED — {NEW_CORRIDA}.",
            "excludedAt": NEW_TIME,
            "excludedBy": f"PritiAgent corrida {NEW_CORRIDA} — WMS confirmed CLOSED"
        })
        added_old += 1

if "excludedContainers" in feed:
    feed["excludedContainers"] = excluded
else:
    feed["excluded"] = excluded
print(f"✅ {added_old} old Phase 1/2 containers added to excluded. Total excluded: {len(excluded)}")

# ============================================================
# UPDATE COUNTS
# ============================================================
rows = feed["rows"]
en_yarda = sum(1 for r in rows if r.get("color") == "green")
en_proceso = sum(1 for r in rows if r.get("color") == "yellow")
degradados = sum(1 for r in rows if r.get("color") == "orange")
pre_entry = sum(1 for r in rows if r.get("color") == "normal")
transfer = sum(1 for r in rows if r.get("color") == "blue" or r.get("color") == "purple")

feed["enYarda"] = en_yarda
feed["enProceso"] = en_proceso
feed["degradados"] = degradados
feed["preEntry"] = pre_entry
feed["totalActive"] = len(rows)

print(f"\n📊 COUNTS: enYarda={en_yarda}, enProceso={en_proceso}, degradados={degradados}, preEntry={pre_entry}, transfer={transfer}, totalActive={len(rows)}")

# ============================================================
# UPDATE TOP-LEVEL FIELDS
# ============================================================
feed["lastUpdated"] = NEW_TIME
feed["lastVerificationRun"] = NEW_CORRIDA
feed["verifiedBy"] = f"PritiAgent — corrida {NEW_CORRIDA}"
feed["verificationSource"] = f"WMS+YMS+Outlook run {NEW_CORRIDA}"
feed["messageTimestamp"] = NEW_TIME
feed["message"] = (
    f"Corrida {NEW_CORRIDA} — 1 PROMOCIÓN PRE-ENTRY→🟢EN YARDA: MATU2656138 "
    f"(YMS GATE_CHECKED_IN ✅ ET-1117774). 1 agregado a excluidos: SMCU1114360 "
    f"(RN-5008384 ambas tasks cerradas). 12 históricos Phase 1/2 confirmados CLOSED y excluidos. "
    f"{en_yarda}🟢 EN YARDA, {en_proceso}🟡 EN PROCESO, {degradados}🟠 DEGRADADOS, "
    f"{pre_entry}📅 PRE-ENTRY, {transfer}📋 TRANSFER."
)

feed["summary"] = (
    f"Corrida {NEW_CORRIDA} — {len(rows)} activos: {en_yarda}🟢 EN YARDA, "
    f"{en_proceso}🟡 EN PROCESO, {degradados}🟠 DEGRADADOS, {pre_entry}📅 PRE-ENTRY, "
    f"{transfer}📋 TRANSFER. {len(excluded)} excluidos. "
    f"✅ MATU2656138 promovido a verde (YMS ET-1117774). "
    f"✅ SMCU1114360 + 12 históricos agregados a excluidos."
)

# ============================================================
# UPDATE ALERTS
# ============================================================
new_alerts = []

# Add promotion alert first
new_alerts.append(
    f"✅ CORRIDA {NEW_CORRIDA}: MATU2656138 promovido PRE-ENTRY→EN YARDA. "
    f"YMS ET-1117774 GATE_CHECKED_IN Jul 2 20:11 PDT (HAW TRUCKING/NATHAN HAO). "
    f"⚠️ Sin receive task, sin dock asignado."
)
new_alerts.append(
    f"✅ SMCU1114360 (RN-5008384) agregado a excluidos — ambas tasks cerradas Jun 30."
)
new_alerts.append(
    f"✅ 12 contenedores históricos Phase 1/2 (Jun 22-26) confirmados CLOSED en WMS y excluidos."
)

# Keep existing critical alerts
for alert in feed.get("alerts", []):
    if "MATU2656138" in alert:
        continue  # Replaced above
    if "SMCU1114360" in alert:
        continue
    new_alerts.append(alert)

feed["alerts"] = new_alerts

# ============================================================
# UPDATE GUARDRAILS
# ============================================================
feed["guardrails"]["entryListRule"] = (
    f"ACTIVE — Entry List o YMS físico requerido para EN YARDA (Regla Rolas #3). "
    f"{en_yarda} EN YARDA confirmados. MATU2656138 promovido por YMS GATE_CHECKED_IN. "
    f"{degradados} degradados por falta de evidencia física."
)
feed["guardrails"]["antiEstadoViejo"] = (
    f"ACTIVE — 1 promoción PRE-ENTRY→🟢 esta corrida: MATU2656138 (YMS ET-1117774 GATE_CHECKED_IN). "
    f"ET-1117982 corregido → ET-1117774."
)
feed["guardrails"]["staleStateGuard"] = (
    f"ACTIVE {NEW_CORRIDA} — MATU2656138 corregido: ET-1117982 (shell sin equipo) → ET-1117774 (GATE_CHECKED_IN real)."
)
feed["guardrails"]["closedRemovalRule"] = (
    f"ACTIVE — SMCU1114360 + 12 históricos agregados a excluidos tras verificar ambos tasks CLOSED."
)

# ============================================================
# UPDATE emailMonitor
# ============================================================
feed["emailMonitor"]["lastChecked"] = NEW_TIME
feed["emailMonitor"]["latestFindings"] = (
    f"Outlook corrida {NEW_CORRIDA}: 41 contenedores rastreados (Priti emails Jun 22-Jul 3). "
    f"MATU2656138 promovido a EN YARDA. SMCU1114360 + 12 históricos excluidos. "
    f"13 activos Jul 1-3 confirmados."
)

# ============================================================
# WRITE
# ============================================================
with open("public/container-feed.json", "w") as f:
    json.dump(feed, f, ensure_ascii=False, indent=2)

print(f"\n✅ Feed updated successfully!")
print(f"   Total rows: {len(feed['rows'])}")
print(f"   Total excluded: {len(excluded)}")
print(f"   lastUpdated: {feed['lastUpdated']}")
print(f"   enYarda: {feed['enYarda']}, enProceso: {feed['enProceso']}, degradados: {feed['degradados']}, preEntry: {feed['preEntry']}")
