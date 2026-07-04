#!/usr/bin/env python3
"""
Corrida Jul 4 00:47 PT — Priti/Gurunanda Dashboard Update
Changes:
  1. RN-188094 REMOVED (recv FORCE_CLOSED + putaway CLOSED confirmed WMS fresh)
  2. RN-5008450 GREEN→NORMAL (no YMS evidence, Entry List No Data)
  3. RN-5006269 GREEN→NORMAL (no YMS evidence, Entry List No Data)
  4. RN-183707 GREEN→NORMAL (no YMS evidence, Entry List No Data)
  5. All rows re-verified with fresh timestamps
"""

import json
import sys
from datetime import datetime, timezone, timedelta

PST = timezone(timedelta(hours=-7))
NOW = datetime(2026, 7, 4, 0, 47, 0, tzinfo=PST)
NOW_STR = "2026-07-04T00:47:00-07:00"
VERIFICATION_SOURCE = "WMS+YMS+Outlook fresh Jul 4 00:47 PT"

with open("public/container-feed.json", "r") as f:
    data = json.load(f)

rows = data["rows"]
excluded = data["excluded"]

# --- CHANGE 1: Remove RN-188094 (recv FORCE_CLOSED + putaway CLOSED) ---
rn_188094 = None
for i, row in enumerate(rows):
    if row.get("rn") == "RN-188094":
        rn_188094 = rows.pop(i)
        break

if rn_188094:
    excluded.append({
        "rn": "RN-188094",
        "container": "GN07022026UNIS-1133 (53393)",
        "reason": "Ambos tasks cerrados (recv FORCE_CLOSED TASK-5307936 + putaway CLOSED TASK-5308246) — WMS fresh Jul 4 00:47 PT",
        "recvTask": "TASK-5307936 FORCE_CLOSED",
        "putTask": "TASK-5308246 CLOSED",
        "removedAt": NOW_STR,
        "wasActive": True
    })
    print("✓ RN-188094 removed → excluded (recv+putaway both closed)")

# --- CHANGE 2-4: Downgrade 3 greens → normal (no YMS evidence, Entry List No Data) ---
DOWNGRADE_RNS = {
    "RN-5008450": {
        "reason": "Sin evidencia YMS física (API bug) + Entry List 'No Data'. Rufino rule: green requiere YMS gate-in/drop full/spot o Entry List real result.",
        "alerta": "🚨 ALERTA ROLAS: Degradado GREEN→NORMAL — Sin evidencia YMS ni Entry List. Verificar físicamente DOCK45."
    },
    "RN-5006269": {
        "reason": "Sin evidencia YMS (API bug) + Entry List 'No Data'. 123+ días. Rufino rule: green requiere evidencia física confiable.",
        "alerta": "🚨 ALERTA ROLAS CRÍTICA: Degradado GREEN→NORMAL — 123+ días sin evidencia física YMS/Entry List. Verificar si existe en yarda."
    },
    "RN-183707": {
        "reason": "Sin evidencia YMS (API bug) + Entry List 'No Data'. 67+ días. Rufino rule: green requiere evidencia física confiable.",
        "alerta": "🚨 ALERTA ROLAS: Degradado GREEN→NORMAL — 67+ días sin evidencia física YMS/Entry List. Verificar si existe en yarda."
    }
}

for row in rows:
    rn = row.get("rn")
    if rn in DOWNGRADE_RNS:
        old_color = row["color"]
        row["color"] = "normal"
        row["inYard"] = False
        row["status"] = row.get("status", "").replace("🟢 EN YARDA", "📅 PRE-ENTRY")
        row["entry"] = row.get("entry", "").replace("En yarda", "PRE-ENTRY · Sin evidencia YMS")
        row["alerta"] = DOWNGRADE_RNS[rn]["alerta"]
        row["note"] = f"{DOWNGRADE_RNS[rn]['reason']} Corregido corrida Jul 4 00:47 PT."
        row["antiFalseGreenRule"] = "Entry List real result OR YMS gate-in/drop full/spot required for green — downgraded Jul 4 00:47 PT"
        row["downgradedAt"] = NOW_STR
        row["downgradeReason"] = DOWNGRADE_RNS[rn]["reason"]
        print(f"✓ {rn} ({row.get('container')}): {old_color} → normal (no YMS/Entry List evidence)")

# --- Update all rows with fresh verification ---
for row in rows:
    row["lastVerifiedAt"] = NOW_STR
    row["verificationSource"] = VERIFICATION_SOURCE
    row["staleStateGuard"] = True

# --- Update specific row notes with fresh data ---
for row in rows:
    rn = row.get("rn")
    
    if rn == "RN-5008447":  # DDDU5053860
        row["note"] = "YMS: gate-in Jul 2 20:53 SPOT675, gate-out 21:10 con DDDU5053432 (vacío). DOCK_CHECKED_IN Jul 3 15:41 → DOCK63. WMS: recv IN_PROGRESS TASK-5307692 Pedro Avila. Jonathan reporta EMPTY 07/03 21:38."
        row["entry"] = "En proceso · DOCK63 · Recv IN_PROGRESS TASK-5307692 · EMPTY (contenido descargado)"
        row["recvTask"] = "TASK-5307692 IN_PROGRESS"
        row["alerta"] = "⚠️ Recv IN_PROGRESS — contenedor ya vacío (Jonathan EMPTY 21:38). Verificar cierre de recibo."
    elif rn == "RN-5008481":  # TCKU6977609
        row["note"] = "YMS: gate-in Jul 2 21:03 SPOT775, gate-out 21:12 SIN EQUIPO (NO_EQUIPMENT). DOCK_CHECKED_IN Jul 3 15:36 → DOCK60. WMS: recv IN_PROGRESS TASK-5307690 Pedro Avila. Jonathan reporta EMPTY 07/03 21:38."
        row["recvTask"] = "TASK-5307690 IN_PROGRESS"
        row["alerta"] = "⚠️ Recv IN_PROGRESS — contenedor ya vacío. Chofer salió sin vacío Jul 2."
    elif rn == "RN-5008506":  # OOCU5501937
        row["note"] = "YMS: gate-in Jul 2 22:52 SPOT688, SIN gate-out. DOCK_CHECKED_IN Jul 3 15:33 → DOCK59. WMS: recv IN_PROGRESS TASK-5307688 Pedro Avila. Jonathan reporta EMPTY 07/03 21:38."
        row["recvTask"] = "TASK-5307688 IN_PROGRESS"
        row["alerta"] = "⚠️ Recv IN_PROGRESS — contenedor ya vacío. Sin gate-out registrado aún."
    elif rn == "RN-5008446":  # JTAU7362561
        row["note"] = "YMS: LIVE_DELIVERY DOCK65, DOCK_CHECKED_IN Jul 2 20:32. WMS: recv IN_PROGRESS TASK-5307533 Daniela Gonzalez. Jonathan reporta EMPTY 07/03 21:38."
        row["recvTask"] = "TASK-5307533 IN_PROGRESS"
        row["alerta"] = "⚠️ Recv IN_PROGRESS — contenedor ya vacío. LIVE_DELIVERY DOCK65."
    elif rn == "RN-188086":  # TGBU3785090
        row["note"] = "YMS: gate-in Jul 2 21:39 SPOT780, gate-out 21:52 con MRKU9748297 (vacío). WMS IMPORTED, TASK-5307685 NEW Caren Cubides, cita Jul 6. Entry List 'No Data' pero YMS confirma presencia física."
        row["lastVerifiedAt"] = NOW_STR
        row["alerta"] = "⚠️ YMS SPOT780 vs WMS DOCK104. Entry List sin datos pero YMS confirma drop-off físico Jul 2."
        row["antiFalseGreenRule"] = "YMS gate-in + SPOT780 + drop-off delivery confirma presencia física"
    elif rn == "RN-5008572":  # MATU2656138
        row["note"] = "YMS: GATE_CHECKED_IN Jul 2 20:11, SIN UBICACIÓN, SIN CUSTOMER en YMS. WMS IMPORTED RN-5008572, cita 20:00 vencida, sin receiving task. 36h+ esperando. Entry List 'No Data'."
        row["alerta"] = "🚨 CRÍTICA — 36h+ en yarda sin spot, sin receiving task. YMS confirma gate-in pero contenedor huérfano (sin customer ni RN en YMS)."
        row["antiFalseGreenRule"] = "YMS gate-in + equipment MATU2656138 confirma presencia física"
    elif rn == "RN-5008571":  # LabelKing07072026 PO8449
        row["note"] = "YMS: ET-1117707 PRE_ENTRY (cita original Jul 6). Llegada anticipada LIVE_DELIVERY DOCK38 WINDOW_CHECKED_IN Jul 3 10:14. WMS: TASK-5307907 NEW Caren Cubides. Entry List: ET-1118067 existe pero container=null."
        row["alerta"] = "⚠️ Llegó anticipado (cita Jul 6). Entry List container=null. Recv NEW."
        row["antiFalseGreenRule"] = "YMS LIVE_DELIVERY + WINDOW_CHECKED_IN DOCK38 confirma presencia física"
    elif rn == "RN-5008479":  # CSGU6429436
        row["note"] = "WMS: recv IN_PROGRESS TASK-5306174 Fatima Ponce DOCK68, 2d+. YMS no encontrado (API bug). Jonathan reportó EMPTY 07/02 pero WMS contradice. Entry List 'No Data'."
        row["alerta"] = "🚨 DISCREPANCIA 2d+: Recv IN_PROGRESS pero Jonathan reportó EMPTY 07/02. Entry List 'No Data'. Verificar físicamente DOCK68."
    elif rn == "RN-188084":  # GN07012026UNIS-1132
        row["note"] = "WMS: recv TASK-5307686 CLOSED (Fatima) + putaway TASK-5307890 IN_PROGRESS (Jorge Antonio Franco). 33 LPs pendientes. Entry List 'No Data'."
        row["recvTask"] = "TASK-5307686 CLOSED (Fatima)"
        row["putTask"] = "TASK-5307890 IN_PROGRESS (Jorge Antonio Franco)"
    elif rn == "RN-5008569":  # EITU9363654
        row["note"] = "WMS IMPORTED, cita doble 6:30AM+13:30 ambas vencidas Jul 3, no-show. YMS ET-1117697 PRE_ENTRY sin gate-in. Entry List 'No Data'."
    elif rn == "RN-5008570":  # TGBU8815453
        row["note"] = "WMS IMPORTED, cita doble 10AM+17:00 ambas vencidas Jul 3, no-show. YMS sin ET. Entry List 'No Data'."
    elif rn == "RN-5008507":  # CBHU7024789
        row["note"] = "WMS: inYard Jul 3 14:31, DOCK108, TASK-5307687 NEW Caren Cubides. YMS no encontrado (API bug). Entry List 'No Data'. Rufino rule: no green sin YMS/Entry List."
    elif rn == "RN-5008480":  # FFAU2426030
        row["note"] = "WMS: inYard Jul 3 14:31, DOCK128, TASK-5307691 NEW Caren Cubides. YMS no encontrado (API bug). Entry List 'No Data'. Rufino rule: no green sin YMS/Entry List."
    elif rn == "RN-5008483":  # CSNU6323633
        row["note"] = "WMS: inYard Jul 3 14:31, DOCK124, TASK-5307689 NEW Caren Cubides. YMS no encontrado (API bug). Entry List 'No Data'. Rufino rule: no green sin YMS/Entry List."
    elif rn == "RN-188044":  # GN07012026UNIS-1130
        row["note"] = "WMS: receiving IN_PROGRESS TASK-5306724 DOCK41 Caren Cubides. YMS: trailer 53693 DOCK_CHECKED_OUT 09:28 pero recibo sigue activo. Sin putaway."

# --- Recalculate summary ---
green = sum(1 for r in rows if r.get("color") == "green")
yellow = sum(1 for r in rows if r.get("color") == "yellow")
red = sum(1 for r in rows if r.get("color") == "red")
normal = sum(1 for r in rows if r.get("color") == "normal")

# --- Build alerts ---
alerts = [
    "ALERTA ROLAS CRÍTICA: MATU2656138/RN-5008572 — 36h+ en yarda SIN SPOT, SIN receiving task. Contenedor huérfano en YMS.",
    "ALERTA ROLAS: RN-188094 (GN07022026UNIS-1133) REMOVIDO — recv FORCE_CLOSED + putaway CLOSED.",
    "ALERTA ROLAS: 3 contenedores DEGRADADOS GREEN→NORMAL: RN-5008450, RN-5006269, RN-183707 — sin evidencia YMS ni Entry List.",
    "ALERTA ROLAS CRÍTICA: RN-5006269 — 123+ días sin recibir, posiblemente ya no está en yarda. Entry List 'No Data'.",
    "ALERTA ROLAS: RN-183707 — 67+ días sin recibir. Entry List 'No Data'.",
    "ALERTA ROLAS: CSGU6429436/RN-5008479 — DISCREPANCIA 2d+: recv IN_PROGRESS pero reportado EMPTY.",
    "ALERTA ROLAS: DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561 — EMPTY según Jonathan 07/03 21:38 pero recv IN_PROGRESS en WMS.",
    "ALERTA ROLAS: EITU9363654/RN-5008569 — DOBLE CITA VENCIDA Jul 3. No-show.",
    "ALERTA ROLAS: TGBU8815453/RN-5008570 — DOBLE CITA VENCIDA Jul 3. No-show.",
    "ALERTA ROLAS: CBHU7024789, FFAU2426030, CSNU6323633 — WMS muestra dock+tasks pero sin YMS/Entry List. Mantenidos PRE-ENTRY.",
    "ALERTA ROLAS: YMS API bug persiste — múltiples contenedores sin verificación YMS completa.",
    "ALERTA ROLAS: Live feed stale ~5h. Repo update requiere redeploy Coolify."
]

# --- Update data ---
data["lastUpdated"] = NOW_STR
data["totalActive"] = len(rows)
data["totalExcluded"] = len(excluded)
data["summary"] = {"green": green, "yellow": yellow, "red": red, "normal": normal}
data["message"] = f"Corrida Jul 4 00:47 PT — {len(rows)} activos ({green} green, {yellow} yellow, {normal} normal). REMOVIDO: RN-188094 (recv+putaway CLOSED). DEGRADADOS GREEN→NORMAL: RN-5008450, RN-5006269, RN-183707 (sin YMS/Entry List). Jonathan reporta 4 EMPTY: DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561."
data["alerts"] = alerts
data["messageTimestamp"] = NOW_STR
data["verificationSource"] = VERIFICATION_SOURCE
data["guardrails"]["staleStateGuard"] = f"ACTIVE — rows activos revalidados {NOW_STR}"
data["guardrails"]["lastStaleCheck"] = NOW_STR
data["guardrails"]["antiFalseGreenRule"] = "ACTIVE — 3 degradados green→normal (RN-5008450, RN-5006269, RN-183707) por falta de YMS/Entry List"
data["guardrails"]["antiFalseGreenDowngrades"] = 3
data["emailMonitor"]["lastChecked"] = NOW_STR
data["emailMonitor"]["alertas"] = [
    "Jonathan Heredia 07/03 21:38: EMPTY CONTAINERS — DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561 listos para pickup.",
    "Jonathan Heredia 07/03 21:46: 2nd Shift Receiving Progress — DDDU5053860, TCKU6977609, OOCU5501937, JTAU7362561 con recv PENDING.",
    "Priti Patel: MATU2656138 — DO not with UNIS. RN-5008572 creado pero sin ubicación.",
    "Nitin Singla: Transfers pendientes RN-187978, RN-188031, RN-188044 — todos ya procesados o excluded.",
    "Jerome Aranda: DN-3236621 LOADED, PO TO6331, 28 pallets, trailer 53176."
]

with open("public/container-feed.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"\n✅ Feed updated:")
print(f"   lastUpdated: {NOW_STR}")
print(f"   totalActive: {len(rows)} (green={green}, yellow={yellow}, red={red}, normal={normal})")
print(f"   totalExcluded: {len(excluded)}")
print(f"   alerts: {len(alerts)}")
