#!/usr/bin/env python3
"""Ciclo 03:43 PT Jul 1 — Cross-reference WMS+YMS+Outlook → update feed"""
import json
import sys
from datetime import datetime, timezone, timedelta

PST = timezone(timedelta(hours=-7))
NOW = datetime(2026, 7, 1, 3, 43, 0, tzinfo=PST)
NOW_ISO = NOW.isoformat()

with open("public/container-feed.json", "r") as f:
    feed = json.load(f)

rows = feed["rows"]
excluded = feed.get("excludedContainers", [])

# ─── Helper ───
def find_row(container_id):
    for r in rows:
        if container_id in r.get("container", ""):
            return r
    return None

def find_excluded(container_id):
    for e in excluded:
        if container_id in e.get("container", ""):
            return e
    return None

def update_row(r, updates):
    r.update(updates)
    r["lastVerifiedAt"] = NOW_ISO
    if "verificationSource" in updates:
        r["verificationSource"] = updates["verificationSource"]
    else:
        r["verificationSource"] = f"WMS+YMS cross-ref 03:43 PT | {r.get('rn','?')}"

# ─── 1. DFSU7374979 (RN-5008310): RE-INTEGRATE from excluded ───
dsfu = find_excluded("DFSU7374979")
if dsfu:
    excluded.remove(dsfu)
    print(f"REMOVED from excluded: {dsfu['container']}")

new_row = {
    "container": "DFSU7374979",
    "rn": "RN-5008310",
    "rnStatus": "IN_PROGRESS",
    "receipt": "RN-5008310",
    "dock": "DOCK61",
    "entry": "WMS IN_PROGRESS DOCK61 · RT FORCE_CLOSED + PA CLOSED · ⚠️ EDGE CASE",
    "inYard": True,
    "color": "yellow",
    "appointmentTime": "Jun 23 (original)",
    "note": "⚠️ ALERTA ROLAS: Re-integrado desde excluidos. Nitin reportó IN_PROGRESS 06/30. WMS 03:40 PT confirma: receipt IN_PROGRESS, RT TASK-5303877 FORCE_CLOSED, PA TASK-5304501 CLOSED. Ambos tasks terminales pero receipt sigue IN_PROGRESS. Edge case — monitorear próximo ciclo.",
    "status": "🟡 EDGE CASE — RN-5008310 · DOCK61 · RT+PA cerrados · Receipt IN_PROGRESS · Re-integrado 03:43 PT",
    "lastVerifiedAt": NOW_ISO,
    "verificationSource": "WMS 03:40 PT | RN-5008310 IN_PROGRESS DOCK61 · RT FORCE_CLOSED · PA CLOSED · ⚠️ EDGE CASE re-integrado",
    "staleStateGuard": "REINTEGRATED_EDGE_CASE",
    "displayCategory": "yellow",
    "statusText": "🟡 EDGE CASE — RN-5008310 · DOCK61 · RT+PA cerrados · Receipt IN_PROGRESS"
}
rows.append(new_row)
print("ADDED: DFSU7374979 (RN-5008310) as YELLOW edge case")

# ─── 2. FOUR YELLOW → NORMAL: no yarda evidence, no active tasks ───
yellow_to_normal = [
    ("FUS06292026UNIS-57", "RN-187878", "Cita vencida 06/30 20:00 · WMS IMPORTED sin inYard ni RT · Sin evidencia llegada"),
    ("FUS06302026UNIS-58", "RN-187991", "Cita vencida 06/30 07:00 · WMS IMPORTED sin inYard ni RT · Sin evidencia llegada"),
    ("GN06302026UNIS-1127 (tráiler 53166)", "RN-187979", "Cita vencida 06/30 07:00 · WMS IMPORTED sin inYard ni RT · Sin evidencia llegada"),
    ("GN06302026UNIS-1128 (tráiler 53541)", "RN-187983", "Cita vencida 06/30 07:00 · WMS IMPORTED sin inYard ni RT · Sin evidencia llegada"),
]

for container_id, rn, reason in yellow_to_normal:
    row = find_row(container_id)
    if row:
        row["color"] = "normal"
        row["inYard"] = False
        row["displayCategory"] = "normal"
        row["statusText"] = f"📅 PRE-ENTRY — {rn} IMPORTED · Sin llegada · {reason[:50]}..."
        row["status"] = f"📅 PRE-ENTRY — {rn} IMPORTED · Sin llegada · Reclasificado 03:43 PT"
        row["note"] = f"🔄 RECLASIFICADO 03:43 PT: {reason}. YMS sin rastro. ANTI-ESTADO-VIEJO: sin evidencia de yarda → NORMAL."
        row["staleStateGuard"] = "RECLASSIFIED_YELLOW_TO_NORMAL"
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = f"WMS+YMS 03:43 PT | {rn} IMPORTED · Sin inYard · Sin RT · YMS sin rastro · Reclasificado yellow→normal"
        print(f"  YELLOW→NORMAL: {container_id} ({rn}) — {reason}")

# ─── 3. Update OOLU9324944 note (empty picked up) ───
oolu = find_row("OOLU9324944")
if oolu:
    oolu["note"] = oolu.get("note","") + " | 🆕 03:43 PT: YMS confirma GATE_CHECK_OUT vacío OOLU9324944 (PICK_UP_EMPTY con BEAU5553433 06/30 23:46). Lleno ya devanned en DOCK98. Ciclo físico completado. WMS sigue IMPORTED sin tasks — posible cierre pendiente."
    oolu["entry"] = "YMS ET-1116521: lleno DOCK98 devanned → vacío GATE_CHECK_OUT 06/30 23:46 · WMS RN-5008430 IMPORTED sin tasks"
    oolu["lastVerifiedAt"] = NOW_ISO
    oolu["verificationSource"] = "WMS+YMS 03:43 PT | WMS: RN-5008430 IMPORTED sin tasks · YMS: GATE_CHECK_OUT vacío 06/30 23:46 · Ciclo físico completado"
    print("  UPDATED: OOLU9324944 — empty GATE_CHECK_OUT confirmed")

# ─── 4. Update CAIU9453139 dock (YMS confirms DOCK2, WMS DOCK64) ───
caiu = find_row("CAIU9453139")
if caiu:
    caiu["dock"] = "DOCK2 (YMS) / DOCK64 (WMS RT)"
    caiu["note"] = caiu.get("note","") + " | 🆕 03:43 PT: YMS re-confirma DOCK2 DOCK_CHECKED_IN 12h+. WMS RT sigue DOCK64."
    caiu["lastVerifiedAt"] = NOW_ISO
    caiu["verificationSource"] = "WMS+YMS 03:43 PT | RN-5008385 IN_PROGRESS · YMS DOCK2 DOCK_CHECKED_IN · WMS DOCK64 RT IN_PROGRESS"
    print("  UPDATED: CAIU9453139 dock confirmed")

# ─── 5. Update TCNU4379515 note ───
tcn = find_row("TCNU4379515")
if tcn:
    tcn["note"] = tcn.get("note","") + " | 🆕 03:43 PT: YMS confirma DOCK48 DOCK_CHECKED_IN (LIVE_DELIVERY). DOCK_CHECKED_OUT breve 09:53→DOCK_CHECKED_IN 09:54."
    tcn["lastVerifiedAt"] = NOW_ISO
    tcn["verificationSource"] = "WMS+YMS 03:43 PT | RN-5008399 IN_PROGRESS DOCK48 · YMS DOCK_CHECKED_IN · LIVE_DELIVERY"
    print("  UPDATED: TCNU4379515 note")

# ─── 6. Update JTAU7362598 note (YMS PRE_ENTRY still active) ───
jtau = find_row("JTAU7362598")
if jtau:
    jtau["note"] = "⚠️ Cita vencida 06/30 23:00 — 15h+. WMS: IMPORTED APPT-6032434 sin dock ni tasks. 🆕 YMS 03:13 PT: ET-1116609 PRE_ENTRY detectado por cámara lane 11 — posible llegada temprana SIN equipo confirmado. Requiere verificación manual. | 🆕 03:43 PT: YMS PRE_ENTRY persiste. Sin gate check-in."
    jtau["entry"] = "YMS ET-1116609 PRE_ENTRY (cámara 03:13) · Sin gate check-in · WMS IMPORTED sin RT"
    jtau["lastVerifiedAt"] = NOW_ISO
    jtau["verificationSource"] = "WMS+YMS 03:43 PT | RN-5008424 IMPORTED · YMS ET-1116609 PRE_ENTRY · Sin gate check-in"
    print("  UPDATED: JTAU7362598 note")

# ─── 7. Update FFAU1548537 note ───
ffau = find_row("FFAU1548537")
if ffau:
    ffau["note"] = ffau.get("note","") + " | 🆕 03:43 PT: YMS GATE_CHECK_OUT confirmado — vacío FFAU1548537 recogido con BSIU9381158. Lleno se quedó en DOCK44. WMS inYardTime Jun 30 17:23, recv TASK-5304579 NEW DOCK66."
    ffau["lastVerifiedAt"] = NOW_ISO
    ffau["verificationSource"] = "WMS+YMS 03:43 PT | RN-5008428 IMPORTED DOCK66 · YMS GATE_CHECK_OUT vacío DOCK44 · Lleno en yarda"
    print("  UPDATED: FFAU1548537 note")

# ─── 8. Update BSIU8440908 / OOCU8342103 / JTAU7362582 with YMS confirmation ───
for cid in ["BSIU8440908", "OOCU8342103", "JTAU7362582"]:
    row = find_row(cid)
    if row:
        row["note"] = row.get("note","") + f" | 🆕 03:43 PT: YMS DOCK_CHECKED_OUT confirmado. Putaway sigue IN_PROGRESS en WMS."
        row["lastVerifiedAt"] = NOW_ISO

# ─── 9. Update all normal rows (citas HOY check) ───
citas_hoy = ["DDDU5053860", "JTAU7362561", "CSGU6429436", "DDDU5053432", "OOCU7355889"]
for cid in citas_hoy:
    row = find_row(cid)
    if row:
        row["lastVerifiedAt"] = NOW_ISO
        row["verificationSource"] = row.get("verificationSource","") + f" | YMS 03:43 PT: sin llegada aún"

# LabelKing rows
for cid in ["RN-5008444", "RN-5008449", "RN-5008450"]:
    row = find_row(cid)
    if row:
        row["lastVerifiedAt"] = NOW_ISO

# ─── 10. Update excluded list for DFSU7374979 ───
# Already removed above. Add a recovery note.
excluded.append({
    "container": "DFSU7374979",
    "rn": "RN-5008310",
    "reason": "⚠️ RE-INTEGRADO AL ACTIVO 07/01 03:43 PT: receipt IN_PROGRESS con RT+PA cerrados. Edge case detectado por Nitin 06/30. Re-integrado como YELLOW para monitoreo.",
    "recoveryNote": "Re-integrado 03:43 PT. RT FORCE_CLOSED + PA CLOSED pero receipt IN_PROGRESS. Monitorear."
})

# ─── 11. Update summary and metadata ───
green_count = sum(1 for r in rows if r.get("color") == "green")
yellow_count = sum(1 for r in rows if r.get("color") == "yellow")
normal_count = sum(1 for r in rows if r.get("color") == "normal")
red_count = sum(1 for r in rows if r.get("color") == "red")
total = len(rows)

feed["lastUpdated"] = NOW_ISO
feed["totalActive"] = total
feed["totalExcluded"] = len(excluded)
feed["summary"] = {
    "green": green_count,
    "yellow": yellow_count,
    "normal": normal_count,
    "red": red_count,
    "totalActive": total,
    "totalExcluded": len(excluded),
    "byColor": {
        "green": green_count,
        "yellow": yellow_count,
        "normal": normal_count,
        "red": red_count
    },
    "alertasActivas": [
        f"✅ CICLO 03:43 PT: WMS(33)+YMS(8) revalidados. {total} rows ({green_count}G/{yellow_count}Y/{red_count}R/{normal_count}N). Anti-estado-viejo: CLEAN.",
        "🚨 ALERTA ROLAS: DFSU7374979 (RN-5008310) RE-INTEGRADO — receipt IN_PROGRESS pero RT+PA cerrados. Edge case.",
        "🚨 ALERTA ROLAS CRÍTICA: RN-5006269 MAWB — 121 DÍAS en yarda. UOM config bloqueo.",
        "🚨 ALERTA ROLAS: RN-183707 ALNOR — 65 días en yarda sin receiving.",
        "🚨 ALERTA ROLAS: RN-5008361 CORRU — RT FORCE_CLOSED (over items), PT activo. Posible inconsistencia.",
        "⚠️ OOLU9324944: YMS vacío GATE_CHECK_OUT. WMS IMPORTED sin tasks. Ciclo físico completado, WMS pendiente cierre.",
        "🔴 EITU8162104: 8d sin RN. Priti preguntó 06/25.",
        "📅 CITAS HOY (7): DDDU5053860(10:00), JTAU7362561(11:00), CSGU6429436(13:30), DDDU5053432(16:00), LabelKing×3(17:00), ITL07012026(17:30), OOCU7355889(20:00).",
        "🔄 4 transfers UNIS reclasificados YELLOW→NORMAL: sin evidencia yarda. Anti-estado-viejo aplicado."
    ]
}
feed["alerts"] = feed["summary"]["alertasActivas"]
feed["message"] = f"ALERTA ROLAS 07/01 03:43 PT: CICLO COMPLETO. WMS(33)+YMS(8) cross-ref. DFSU7374979 re-integrado. 4 transfers→NORMAL. Anti-estado-viejo CLEAN."
feed["messageTimestamp"] = NOW_ISO
feed["metadata"]["corridaInfo"] = feed["message"]
feed["metadata"]["feedLastUpdated"] = NOW_ISO
feed["metadata"]["generatedAt"] = NOW_ISO
feed["metadata"]["totalActive"] = total
feed["metadata"]["totalExcluded"] = len(excluded)
feed["metadata"]["byColor"] = {"green": green_count, "yellow": yellow_count, "normal": normal_count, "red": red_count}

feed["guardrails"]["antiEstadoViejo"] = "CLEAN — 03:43 PT: 33 RNs WMS + 8 ETs YMS cross-ref. 4 transfers reclasificados Y→N (sin evidencia yarda). 0 PRE-ENTRY/NORMAL con evidencia yarda."
feed["guardrails"]["lastGuardrailRun"] = NOW_ISO
feed["guardrails"]["wmsCycleNote"] = "33 RNs revalidados 03:40 PT. 0 CLOSED. DFSU7374979 edge case detectado (RT+PA cerrados, receipt IN_PROGRESS). 4 transfers sin RT reclasificados."
feed["guardrails"]["ymsCycleNote"] = "8 ETs revalidados 03:43 PT. CAIU9453139 DOCK2 12h+. TCNU4379515 DOCK48 LIVE_DELIVERY. OOLU9324944 vacío GATE_CHECK_OUT. JTAU7362598 PRE_ENTRY. 5 citas HOY sin llegada."
feed["guardrails"]["reintegrationNote"] = "DFSU7374979 (RN-5008310) re-integrado 03:43 PT desde excluidos. Nitin reportó IN_PROGRESS. RT+PA cerrados pero receipt activo."

feed["ymsReadingRule"] = "YMS LIVE 2026-07-01 03:43 PT — 8 ETs verificados: CAIU9453139(DOCK2 DOCK_CHECKED_IN), TCNU4379515(DOCK48 DOCK_CHECKED_IN LIVE_DELIVERY), OOLU9324944(GATE_CHECK_OUT vacío), FFAU1548537(GATE_CHECK_OUT vacío, lleno se quedó), OOCU8342103/BSIU8440908/JTAU7362582(DOCK_CHECKED_OUT, PT activo), JTAU7362598(PRE_ENTRY). 5 citas HOY sin llegada aún."

feed["emailMonitor"]["lastChecked"] = NOW_ISO
feed["emailMonitor"]["alertas"] = [
    "📧 0 correos nuevos de Priti desde 03:10 PT.",
    "📧 Nitin (06/30) reportó DFSU7374979 IN_PROGRESS — RE-INTEGRADO al activo.",
    "📅 7 citas HOY 07/01: DDDU5053860(10:00), JTAU7362561(11:00), CSGU6429436(13:30), DDDU5053432(16:00), LabelKing×3(17:00), ITL07012026(17:30), OOCU7355889(20:00)",
    "📅 3 citas MAÑANA 07/02: FFAU2426030, CSNU6323633, TCKU6977609"
]

# ─── 12. Write ───
with open("public/container-feed.json", "w") as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"\n✅ FEED UPDATED: {total} rows ({green_count}G/{yellow_count}Y/{red_count}R/{normal_count}N)")
print(f"   Excluded: {len(excluded)}")
print(f"   Timestamp: {NOW_ISO}")
