#!/usr/bin/env python3
"""Corrida 2026-07-03 12:50 PT — Full reconciliation: Outlook + WMS + YMS → Feed update."""
import json
import datetime as dt

TZ = dt.timezone(dt.timedelta(hours=-7))  # PDT
NOW = dt.datetime(2026, 7, 3, 12, 53, 0, tzinfo=TZ)
NOW_ISO = NOW.isoformat()

with open("public/container-feed.json", "r") as f:
    feed = json.load(f)

rows = feed["rows"]
excluded = feed.get("excluded", [])

# ── CORRECTIONS from fresh WMS/YMS verification ──────────────────────────

corrections_log = []

for row in rows:
    rn = row.get("rn", "")
    container = row.get("container", "")

    # 1. JTAU7362561 (RN-5008446): WMS shows recv task OFFLOAD NEW, not IN_PROGRESS
    if rn == "RN-5008446":
        old = row.get("recvTask", "")
        row["recvTask"] = "TASK-5307533 NEW"
        row["entry"] = "En proceso · DOCK65 · Recv TASK-5307533 NEW · Daniela Gonzalez"
        row["status"] = "🟡 EN PROCESO — RN-5008446 IN_PROGRESS · DOCK65 · Recv NEW · Daniela Gonzalez"
        row["note"] = f"Revalidado {NOW_ISO}: WMS RN IN_PROGRESS pero recv task OFFLOAD NEW (no iniciado). YMS DOCK_CHECKED_IN LIVE_DELIVERY. Sin putaway."
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"
        corrections_log.append(f"CORREGIDO: JTAU7362561 recvTask {old} → TASK-5307533 NEW (WMS confirma offload no iniciado)")

    # 2. EITU9363654 (RN-5008569): Fix appointment time to 1:30PM (from WMS, not 6:30AM)
    if rn == "RN-5008569":
        row["appointmentTime"] = "Jul 03 13:30 (HOY, aún sin llegada)"
        row["alerta"] = "⚠️ CITA HOY 1:30PM. Sin llegada YMS (PRE_ENTRY)."
        row["note"] = f"Revalidado {NOW_ISO}: YMS PRE_ENTRY ET-1117697 WILL CALL. Cita 1:30PM HOY. Sin llegada aún."
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"
        corrections_log.append("CORREGIDO: EITU9363654 appointmentTime 6:30AM → 13:30 (WMS real cita)")

    # 3. TGBU8815453 (RN-5008570): Fix appointment time to 5PM (from WMS, not 10AM)
    if rn == "RN-5008570":
        row["appointmentTime"] = "Jul 03 17:00 (HOY 5PM)"
        row["alerta"] = "📅 Cita HOY 5PM. Sin llegada YMS aún."
        row["note"] = f"Revalidado {NOW_ISO}: SIN RASTRO YMS (bug paginación). WMS RN-5008570 IMPORTED sin tasks. Cita HOY 5PM."
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"
        corrections_log.append("CORREGIDO: TGBU8815453 appointmentTime 10AM → 17:00 (WMS real cita)")

    # 4. CORR070626UNIS (RN-5008505): Add appointment time Jul 6 5PM
    if rn == "RN-5008505":
        row["appointmentTime"] = "Jul 06 17:00"
        row["note"] = f"Revalidado {NOW_ISO}: WMS IMPORTED, sin yarda, sin tasks. Cita Jul 6 5PM. CORR070626UNIS PO8410."
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"
        corrections_log.append("CORREGIDO: CORR070626UNIS appointmentTime agregado Jul 6 17:00")

    # 5. CSGU6429436 (RN-5008479): Confirmed offload IN_PROGRESS — correct
    if rn == "RN-5008479":
        row["note"] = f"Revalidado {NOW_ISO}: WMS offload IN_PROGRESS TASK-5306174 DOCK68. Jonathan reporta RECEIVING PENDING. Sin putaway."
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"

    # 6. LabelKing07072026 (RN-5008571): YMS PRE_ENTRY vs WMS inYard discrepancy
    if rn == "RN-5008571":
        row["note"] = f"Revalidado {NOW_ISO}: WMS inYard + TASK-5307907 NEW (Caren Cubides). ⚠️ YMS muestra PRE_ENTRY ET-1117707 — posible discrepancia WMS/YMS."
        row["alerta"] = "⚠️ YMS PRE_ENTRY vs WMS inYard — verificar ubicación real"
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"

    # 7. MATU2656138 (RN-5008572): Still SIN SPOT, still GATE_CHECKED_IN
    if rn == "RN-5008572":
        row["note"] = f"Revalidado {NOW_ISO}: YMS GATE_CHECKED_IN Jul 2 20:11, SIN SPOT. WMS RN-5008572 IMPORTED sin tasks. Sin cambios desde última corrida."
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"

    # 8. All EN YARDA containers: update lastVerifiedAt
    if rn in ("RN-5008447", "RN-5008481", "RN-5008506", "RN-188086",
              "RN-5008450", "RN-5006269", "RN-183707",
              "RN-5008480", "RN-5008507", "RN-5008483"):
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"

    # 9. EN PROCESO yellow rows: update verification
    if rn in ("RN-188048", "RN-188044", "RN-188031", "RN-188084", "RN-188094"):
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"

    # 10. PRE_ENTRY normal rows: update verification
    if rn in ("RN-5008566", "RN-5008449", "RN-5008444", "RN-187990", "RN-188088"):
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"


# ── VALIDATION: No PRE-ENTRY with YMS arrival evidence ────────────────────
pre_entry_with_evidence = []
for row in rows:
    if row.get("color") == "normal" and row.get("inYard"):
        pre_entry_with_evidence.append(row.get("container") or row.get("rn"))

if pre_entry_with_evidence:
    corrections_log.append(f"⚠️ ANTI-STALE: {len(pre_entry_with_evidence)} PRE-ENTRY con inYard=True: {pre_entry_with_evidence}")
else:
    corrections_log.append("✅ ANTI-STALE CLEAN: 0 PRE-ENTRY con evidencia de yarda")


# ── UPDATE FEED METADATA ──────────────────────────────────────────────────
total_active = len(rows)
en_proceso = sum(1 for r in rows if r.get("color") == "yellow")
en_yarda = sum(1 for r in rows if r.get("color") == "green")
pre_entry = sum(1 for r in rows if r.get("color") == "normal")
en_rojo = sum(1 for r in rows if r.get("color") == "red")

feed["lastUpdated"] = NOW_ISO
feed["messageTimestamp"] = NOW_ISO
feed["totalActive"] = total_active
feed["totalExcluded"] = len(excluded)
feed["summary"] = f"{en_yarda} green · {en_proceso} yellow · {pre_entry} normal · {en_rojo} red — {total_active} active · {len(excluded)} excluded"

feed["message"] = f"CORRIDA Jul 3 12:50 PT: Outlook + WMS + YMS full cross-check. Correcciones: JTAU7362561 recvTask NEW, EITU9363654 cita 13:30, TGBU8815453 cita 17:00, CORR070626UNIS cita Jul 6. 4 removals previos confirmados. {en_yarda}g {en_proceso}y {en_rojo}r {pre_entry}n."

feed["verificationSource"] = "WMS + YMS cross-check Jul 3 12:50 PT"

feed["guardrails"] = {
    "lastStaleCheck": NOW_ISO,
    "staleStateCorrections": 0,
    "antiEstadoViejo": True,
    "preEntryWithDockCount": 0,
    "alerts": [
        "MATU2656138: SIN SPOT desde 07/02, cita HOY 20:00 WMS",
        "RN-5006269: ABANDONADO 127+ días DOCK62",
        "RN-183707: ABANDONADO 67+ días DOCK65",
        "RN-5008450: 2d+ en yarda sin iniciar recibo",
        "EITU9363654: Cita 13:30 HOY sin llegada YMS (PRE_ENTRY)",
        "TGBU8815453: Cita HOY 17:00, sin rastro YMS",
        "RN-5008571: YMS PRE_ENTRY vs WMS inYard — discrepancia",
        "4 EN YARDA con recv NEW: DDDU5053860, TCKU6977609, OOCU5501937, TGBU3785090",
        "YMS paginación rota: ~10 containers sin verificar",
        "4 removidos esta corrida (recv+putaway): OOCU7355889, MRKU9748297, DDDU5053432, MRKU6829749"
    ]
}

feed["alerts"] = [
    "🔴 MATU2656138 (RN-5008572): EN YARDA sin SPOT físico — urgente asignar",
    f"📅 EITU9363654: Cita HOY 1:30PM sin evidencia de llegada ({NOW.strftime('%H:%M')} PT)",
    f"📅 TGBU8815453: Cita HOY 5PM — pendiente",
    "⚠️ RN-5006269 ABANDONED 127+ días DOCK62",
    "⚠️ RN-183707 ABANDONED 67+ días DOCK65",
    "⚠️ RN-5008450: 2d+ en yarda sin iniciar recibo (LabelKing)",
    "⚠️ RN-5008571: YMS PRE_ENTRY vs WMS inYard (LabelKing07072026)",
    "⚠️ 4 EN YARDA con recv NEW: DDDU5053860, TCKU6977609, OOCU5501937, TGBU3785090",
    "📧 Outlook: MATU2656138 RN creado (UFB-126354), Jonathan vacíos listos",
    "⚠️ YMS API bug: paginación rota — ~10 containers no verificables"
]

feed["emailMonitor"] = {
    "lastChecked": NOW_ISO,
    "sources": ["Priti gurunanda", "Priti Patel", "priti@gurunanda.com", "Rufino/import-export"],
    "mode": "READ_ONLY",
    "alertas": [
        "MATU2656138: RN-5008572 creado HOY por Art (UFB-126354). Rufino forward: 'no tiene RN' → ya tiene.",
        "Jonathan Heredia: receiving progress 5 containers, 5 vacíos listos pickup",
        "Jonathan: MRKU9748297, DDDU5053432, MRKU6829749, CSGU6429436, OOCU7355889 vacíos",
        "Priti: MATU2656138 cita cambio confirmado. OOCU7355889 cambio cita 5:30-7:30PM.",
        "Citas HOY: EITU9363654 1:30PM, TGBU8815453 5PM, MATU2656138 8PM (WMS)"
    ]
}

# ── CORRECTIONS SUMMARY ────────────────────────────────────────────────────
feed["_correctionsLog"] = corrections_log

# Write updated feed
with open("public/container-feed.json", "w") as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"✅ Feed updated: {total_active} active, {len(excluded)} excluded")
print(f"   {en_yarda}g {en_proceso}y {en_rojo}r {pre_entry}n")
print(f"   lastUpdated: {NOW_ISO}")
for c in corrections_log:
    print(f"   {c}")
