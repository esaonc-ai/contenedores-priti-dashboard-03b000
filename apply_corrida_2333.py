#!/usr/bin/env python3
"""
Update Priti Container Feed — Corrida Jul 3 23:33 PT
Base: repo feed (22:14 PT, 27 active) + fresh WMS/YMS cross-check
"""
import json
from datetime import datetime, timezone, timedelta

pdt = timezone(timedelta(hours=-7))
now = datetime.now(pdt)
timestamp = now.strftime("%Y-%m-%dT%H:%M:%S-07:00")
print(f"🕐 Corrida: {timestamp}")

# Load repo feed (more recent than live)
with open("/home/user/workspace/repo/public/container-feed.json") as f:
    feed = json.load(f)

rows = feed["rows"]
print(f"Base: {len(rows)} rows from repo (22:14 PT)")

# Build lookup by RN
by_rn = {}
for r in rows:
    rn = r.get("rn", "")
    if rn:
        by_rn[rn] = r

def update_row(r, **kwargs):
    for k, v in kwargs.items():
        r[k] = v
    r["lastVerifiedAt"] = timestamp
    r["verificationSource"] = "WMS + YMS cross-check corrida Jul 3 23:33 PT"
    r["staleStateGuard"] = True
    r["antiEstadoViejo"] = True

changes_applied = []

# ═══════════════════════════════════════════════════
# GREEN → YELLOW: No YMS physical evidence
# (Entry List rule: dock+task NEW ≠ physical proof)
# ═══════════════════════════════════════════════════

green_degradations = [
    ("RN-5008450", "LabelKing07012026 / PO8423", "DOCK45", "TASK-5305892",
     "3 días en yarda sin recibir. Sin evidencia YMS (API limitation). WMS: inYard Jul 1, DOCK45, TASK-5305892 NEW, Jerome Aranda.",
     "⚠️ 3 DÍAS EN YARDA sin recibir. Sin evidencia YMS. Entry List pendiente.",
     "Jerome Aranda"),

    ("RN-5006269", "MAWB 00120698274", "DOCK62", "TASK-5207670",
     "123+ DÍAS EN YARDA. Sin evidencia YMS. WMS: DOCK62, TASK-5207670 NEW. ABANDONADO. 'New UOM setup needed'.",
     "🚨 CRÍTICO: 123+ DÍAS ABANDONADO. Sin evidencia YMS. Requiere acción urgente.",
     "Caren Cubides"),

    ("RN-183707", "ALNOR04242026", "DOCK65", "TASK-5252949",
     "67+ DÍAS EN YARDA. Sin evidencia YMS. WMS: DOCK65, TASK-5252949 NEW. Trailer 53132A. 'Live Unload'. ABANDONADO.",
     "🚨 67+ DÍAS ABANDONADO. Sin evidencia YMS. Entry List pendiente.",
     "Caren Cubides"),

    ("RN-5008571", "LabelKing07072026 PO8449", "DOCK38", "TASK-5307907",
     "YMS solo PRE_ENTRY (sin gate-in físico). WMS: inYard Jul 3, DOCK38, TASK-5307907 NEW. WINDOW_CHECKED_IN Jul 3 10:14. Llegó anticipado (cita Jul 6). Entry List pendiente.",
     "⚠️ Llegó anticipado (cita Jul 6). Sin gate-in YMS. Entry List pendiente.",
     "Caren Cubides"),
]

for rn_id, container, dock, task_id, note, alerta, assignee in green_degradations:
    if rn_id in by_rn:
        r = by_rn[rn_id]
        update_row(r,
            color="yellow",
            status=f"🟡 EN YARDA (sin recepción) — {rn_id} IMPORTED · {dock} · {task_id} NEW",
            entry=f"En yarda · {dock} · Recv {task_id} NEW · {assignee}",
            inYard=True, dock=dock,
            note=f"⚠️ DEGRADADO green→yellow (regla Entry List): {note}",
            alerta=alerta,
            recvTask=f"{task_id} NEW", putTask="—", rnStatus="IMPORTED",
            assignedTo=assignee,
            degradationReason="Sin evidencia YMS/Entry List física (regla Entry List).",
            degradedAt=timestamp,
        )
        changes_applied.append(f"GREEN→YELLOW: {container} ({rn_id})")

# ═══════════════════════════════════════════════════
# UPDATE GREEN (keep green, YMS confirmed)
# ═══════════════════════════════════════════════════

# TGBU3785090 — YMS confirms physical presence
if "RN-188086" in by_rn:
    r = by_rn["RN-188086"]
    update_row(r,
        dock="SPOT780 (YMS) / DOCK104 (WMS)",
        note="✅ YMS CONFIRMA: ET-1117817 Gate Check-in Jul 2 21:39, DROP_OFF_DELIVERY FULL TGBU3785090, SPOT780. Gate Check-out Jul 2 21:52 con vacío MRKU9748297. WMS: IMPORTED, DOCK104, TASK-5307685 NEW, cita Jul 6. EN YARDA confirmado por YMS físico.",
        entry="En yarda · SPOT780 (YMS) / DOCK104 (WMS) · Recv TASK-5307685 NEW · Caren Cubides",
        alerta="⚠️ En yarda (SPOT780 YMS) pero WMS cita Jul 6. Recv task NEW sin iniciar. Llegó anticipado 4 días.",
        recvTask="TASK-5307685 NEW", rnStatus="IMPORTED",
        assignedTo="Caren Cubides", et="ET-1117817",
        appointmentTime="Jul 06 15:00",
    )
    changes_applied.append("UPDATED: TGBU3785090 (RN-188086) — YMS confirmed")

# MATU2656138 — RN-5008572 confirmed
if "RN-5008572" in by_rn:
    r = by_rn["RN-5008572"]
    update_row(r,
        note="⚠️ YMS: GATE_CHECKED_IN Jul 2 20:11, DROP_OFF_DELIVERY FULL SIZE_40, SIN SPOT. WMS: RN-5008572 SÍ EXISTE Gurunanda (Rufino estaba equivocado). IMPORTED, PO# 8190,8107,8144. SIN receiving task. Cita Jul 3 20:00 VENCIDA. Carrier: HAW TRUCKING.",
        alerta="🚨 CRÍTICA: 24h+ en yarda SIN spot, SIN receiving task. Cita vencida. RN-5008572 confirmado Gurunanda.",
        entry="En yarda · SIN SPOT · IMPORTED · Sin receiving task · Cita vencida",
        dock="SIN SPOT (YMS GATE_CHECKED_IN)", et="ET-1117774",
        appointmentTime="Jul 03 20:00 (VENCIDA)",
        receipt="RN-5008572", rnStatus="IMPORTED",
    )
    changes_applied.append("UPDATED: MATU2656138 (RN-5008572) — RN confirmed, Rufino corrected")

# ═══════════════════════════════════════════════════
# UPDATE YELLOW with fresh WMS/YMS data
# ═══════════════════════════════════════════════════

# DDDU5053860
if "RN-5008447" in by_rn:
    r = by_rn["RN-5008447"]
    update_row(r,
        dock="DOCK63",
        note="YMS: SPOT675→DOCK_CHECKED_IN Jul 3 15:41. WMS: recv IN_PROGRESS TASK-5307692, Pedro Avila, inició Jul 3 22:41. Jonathan reporta EMPTY 07/03. Recv+Putaway PENDING.",
        alerta="⚠️ Recv IN_PROGRESS. Jonathan reporta EMPTY 07/03. NO REMOVER hasta recv+putaway CLOSED.",
        entry="En proceso · DOCK63 · Recv IN_PROGRESS TASK-5307692 · Pedro Avila · Inició 22:41 PT",
        recvTask="TASK-5307692 IN_PROGRESS", assignedTo="Pedro Avila",
    )
    changes_applied.append("UPDATED: DDDU5053860 (RN-5008447)")

# TCKU6977609
if "RN-5008481" in by_rn:
    r = by_rn["RN-5008481"]
    update_row(r,
        dock="DOCK60",
        note="YMS: SPOT775→DOCK_CHECKED_IN Jul 3 15:36. Gate Check-out sin equipment (driver sin contenedor). WMS: recv IN_PROGRESS TASK-5307690, Pedro Avila, inició Jul 3 22:36. Jonathan reporta EMPTY 07/03.",
        entry="En proceso · DOCK60 · Recv IN_PROGRESS TASK-5307690 · Pedro Avila · Inició 22:36 PT",
        recvTask="TASK-5307690 IN_PROGRESS", assignedTo="Pedro Avila",
    )
    changes_applied.append("UPDATED: TCKU6977609 (RN-5008481)")

# OOCU5501937
if "RN-5008506" in by_rn:
    r = by_rn["RN-5008506"]
    update_row(r,
        dock="DOCK59",
        note="YMS: SPOT688→DOCK_CHECKED_IN Jul 3 15:33. Sin Gate Check-out. WMS: recv IN_PROGRESS TASK-5307688, Pedro Avila, inició Jul 3 22:33. Jonathan reporta EMPTY 07/03.",
        entry="En proceso · DOCK59 · Recv IN_PROGRESS TASK-5307688 · Pedro Avila · Inició 22:33 PT",
        recvTask="TASK-5307688 IN_PROGRESS", assignedTo="Pedro Avila",
    )
    changes_applied.append("UPDATED: OOCU5501937 (RN-5008506)")

# JTAU7362561
if "RN-5008446" in by_rn:
    r = by_rn["RN-5008446"]
    update_row(r,
        note="YMS LIVE_DELIVERY DOCK_CHECKED_IN DOCK65. WMS recv IN_PROGRESS TASK-5307533, Pedro Avila. Jonathan reporta EMPTY 07/03. Recv+Putaway PENDING.",
        alerta="⚠️ LIVE_DELIVERY DOCK65 — recv IN_PROGRESS. Jonathan reporta EMPTY 07/03. NO REMOVER hasta recv+putaway CLOSED.",
        entry="En proceso · DOCK65 · Recv IN_PROGRESS TASK-5307533 · Pedro Avila",
        recvTask="TASK-5307533 IN_PROGRESS", assignedTo="Pedro Avila",
    )
    changes_applied.append("UPDATED: JTAU7362561 (RN-5008446)")

# CSGU6429436
if "RN-5008479" in by_rn:
    r = by_rn["RN-5008479"]
    update_row(r,
        note="⚠️ DISCREPANCIA: WMS recv IN_PROGRESS TASK-5306174, Fatima Ponce, DOCK68, 2d+. Jonathan reportó EMPTY 07/02. YMS sin datos. Verificar físicamente DOCK68.",
        alerta="🚨 DISCREPANCIA: Recv IN_PROGRESS 2d+ pero Jonathan reportó EMPTY 07/02. Verificar DOCK68 físicamente.",
        assignedTo="Fatima Ponce",
    )
    changes_applied.append("UPDATED: CSGU6429436 (RN-5008479)")

# GN1132 (RN-188084) — recv CLOSED, putaway IN_PROGRESS
if "RN-188084" in by_rn:
    r = by_rn["RN-188084"]
    update_row(r,
        note="Recv TASK-5307686 CLOSED (Jul 3 17:03 PT). Putaway TASK-5307890 IN_PROGRESS, 33 LPs pendientes. Jorge Antonio Franco. MANTENER ACTIVO.",
        recvTask="TASK-5307686 CLOSED", putTask="TASK-5307890 IN_PROGRESS",
    )
    changes_applied.append("UPDATED: GN1132 (RN-188084)")

# GN1133 (RN-188094) — recv FORCE_CLOSED, putaway IN_PROGRESS
if "RN-188094" in by_rn:
    r = by_rn["RN-188094"]
    update_row(r,
        note="Recv TASK-5307936 FORCE_CLOSED (Jul 3 21:25 PT, EXCEPTION: different lot#). Putaway TASK-5308246 IN_PROGRESS. Anthony Vazquez. MANTENER ACTIVO.",
        recvTask="TASK-5307936 FORCE_CLOSED", putTask="TASK-5308246 IN_PROGRESS",
    )
    changes_applied.append("UPDATED: GN1133 (RN-188094)")

# RN-188048 — keep YELLOW, recv FORCE_CLOSED, putaway uncertain
if "RN-188048" in by_rn:
    r = by_rn["RN-188048"]
    update_row(r,
        note="⚠️ Recv TASK-5306832 FORCE_CLOSED (exception: short item). Devanned Jul 3 14:39. Dock check-out completado. Putaway no detectable vía API separada — posiblemente cerrado con FORCE_CLOSE. MANTENER ACTIVO por precaución. Verificar cierre definitivo.",
        alerta="⚠️ Recv FORCE_CLOSED (short item). Putaway no confirmable vía API. Verificar cierre definitivo.",
        recvTask="TASK-5306832 FORCE_CLOSED (short item)",
        putTask="⚠️ No detectable (posiblemente cerrado)",
    )
    changes_applied.append("UPDATED: RN-188048 — kept YELLOW, putaway uncertain")

# ═══════════════════════════════════════════════════
# UPDATE NORMAL rows
# ═══════════════════════════════════════════════════

# CBHU7024789, FFAU2426030, CSNU6323633 — keep NORMAL
for rn_id, container, dock_wms, task_id in [
    ("RN-5008507", "CBHU7024789", "DOCK108", "TASK-5307687"),
    ("RN-5008480", "FFAU2426030", "DOCK128", "TASK-5307691"),
    ("RN-5008483", "CSNU6323633", "DOCK124", "TASK-5307689"),
]:
    if rn_id in by_rn:
        r = by_rn[rn_id]
        update_row(r,
            note=f"⚠️ WMS: IMPORTED, {dock_wms}, {task_id} NEW, inYard Jul 3 14:31. YMS: SIN DATOS. NO verde: dock+task NEW sin YMS/Entry List. Cita vencida.",
            alerta=f"⚠️ Cita vencida. Dock {dock_wms} + task NEW SIN YMS/Entry List. Mantener PRE-ENTRY.",
            dock=f"{dock_wms} (WMS, sin YMS)",
            recvTask=f"{task_id} NEW", putTask="—",
        )
        changes_applied.append(f"UPDATED: {container} ({rn_id}) — NORMAL")

# EITU9363654, TGBU8815453
for rn_id, note_text, alerta_text in [
    ("RN-5008569", "YMS: PRE_ENTRY ET-1117697. WMS: IMPORTED, sin receiving task. DOBLE CITA VENCIDA Jul 3. No-show. WILL CALL.", "🚨 DOBLE CITA VENCIDA Jul 3. No-show."),
    ("RN-5008570", "YMS: SIN DATOS. WMS: IMPORTED, sin receiving task. DOBLE CITA VENCIDA Jul 3. No-show.", "🚨 DOBLE CITA VENCIDA Jul 3. No-show."),
]:
    if rn_id in by_rn:
        r = by_rn[rn_id]
        update_row(r, note=note_text, alerta=alerta_text)
        changes_applied.append(f"UPDATED: {rn_id}")

# TEMU8901490, CORR070626UNIS
for rn_id, note_text in [
    ("RN-5008566", "YMS: SIN DATOS. WMS: IMPORTED, sin receiving task. Cita Jul 7 16:00. OK."),
    ("RN-5008505", "WMS: IMPORTED, sin receiving task. Cita Jul 6 17:00. PO 8410. OK."),
]:
    if rn_id in by_rn:
        r = by_rn[rn_id]
        update_row(r, note=note_text)
        changes_applied.append(f"UPDATED: {rn_id}")

# DN-3236621
for r in rows:
    if r.get("container", "").startswith("DN-3236621"):
        update_row(r,
            note="WMS: LOADED. Trailer 53176. TO6331 → Fusion Transportation, Fontana. 28 pallets, 3 items. Firmado Jul 3 19:17. Carrier: UNKN.",
        )
        changes_applied.append("UPDATED: DN-3236621 (Trailer 53176)")
        break

# ═══════════════════════════════════════════════════
# COUNTS & METADATA
# ═══════════════════════════════════════════════════

green = sum(1 for r in rows if r.get("color") == "green")
yellow = sum(1 for r in rows if r.get("color") == "yellow")
red = sum(1 for r in rows if r.get("color") == "red")
normal = sum(1 for r in rows if r.get("color") == "normal")

feed["totalActive"] = len(rows)
feed["lastUpdated"] = timestamp
feed["summary"] = {
    "green": green, "yellow": yellow, "red": red, "normal": normal,
    "totalActive": len(rows),
    "totalExcluded": feed.get("totalExcluded", 25),
}
feed["guardrails"] = {
    "antiStaleState": True,
    "entryListRule": True,
    "closedRemovalRule": True,
    "rnPrimaryKey": True,
    "preserveAssignments": True,
    "ymsReadingRule": True,
    "schedule": "15 min · America/Los_Angeles",
    "lastStaleCheck": timestamp,
    "staleFound": 4, "staleFixed": 4,
    "alerts": [
        "MATU2656138/RN-5008572: 24h+ en yarda SIN spot, SIN task. Cita vencida. RN confirmado Gurunanda (Rufino corregido).",
        "CSGU6429436/RN-5008479: DISCREPANCIA recv IN_PROGRESS vs EMPTY reportado Jonathan.",
        "RN-5006269: 123+ DÍAS ABANDONADO en yarda. Sin evidencia YMS.",
        "RN-183707: 67+ DÍAS ABANDONADO en yarda. Sin evidencia YMS.",
        "EITU9363654/TGBU8815453: DOBLE CITA VENCIDA no-show.",
        "4 degradados green→yellow por regla Entry List (sin YMS físico).",
        "3 NORMAL con dock+task NEW sin YMS/Entry List (CBHU, FFAU, CSNU).",
        "RN-188048: Recv FORCE_CLOSED, putaway no confirmable. Mantener en observación.",
        "YMS API limitación: solo 50 de 118K registros accesibles.",
        "4 containers Jonathan reporta EMPTY 07/03: NO REMOVER hasta recv+putaway CLOSED.",
    ],
}

# Write
outpath = "/home/user/workspace/repo/public/container-feed.json"
with open(outpath, "w") as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"\n✅ Feed actualizado: {outpath}")
print(f"   totalActive: {len(rows)} | green: {green} | yellow: {yellow} | red: {red} | normal: {normal}")
print(f"   excluded: {feed.get('totalExcluded', '?')}")
print(f"\n📊 {len(changes_applied)} CAMBIOS:")
for c in changes_applied:
    print(f"   • {c}")
print(f"\n🚨 ALERTAS:")
for a in feed["guardrails"]["alerts"]:
    print(f"   • {a}")
