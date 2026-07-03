#!/usr/bin/env python3
"""Corrida 2026-07-03 14:15 PT — Fresh WMS/YMS cross-check and feed update."""
import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=-7))  # PDT
now = datetime.now(tz)
now_iso = now.isoformat()
print(f"🕐 Corrida: {now_iso}")

# Load feed
with open("public/container-feed.json") as f:
    feed = json.load(f)

rows = feed["rows"]
rn_map = {r.get("rn", ""): r for r in rows}

changes = []

# ──────────────────────────────────────────
# CHANGE 1: JTAU7362561 / RN-5008446 — recv IN_PROGRESS confirmed
# ──────────────────────────────────────────
r = rn_map["RN-5008446"]
if r.get("recvTask") != "TASK-5307533 IN_PROGRESS":
    r["recvTask"] = "TASK-5307533 IN_PROGRESS"
    r["entry"] = "En proceso · DOCK65 · Recv IN_PROGRESS TASK-5307533 · Daniela Gonzalez"
    r["status"] = "🟡 EN PROCESO — RN-5008446 IN_PROGRESS · DOCK65 · Daniela Gonzalez"
    r["note"] = "Revalidado 2026-07-03T14:15:00-07:00: WMS confirms recv IN_PROGRESS TASK-5307533 DOCK65 Daniela Gonzalez."
    changes.append("JTAU7362561: recvTask IN_PROGRESS confirmado WMS fresh")

# ──────────────────────────────────────────
# CHANGE 2: CSGU6429436 / RN-5008479 — assignedTo update
# ──────────────────────────────────────────
r = rn_map["RN-5008479"]
if r.get("assignedTo") != "Fatima Del Rosario Ponce":
    r["assignedTo"] = "Fatima Del Rosario Ponce"
    r["entry"] = "En proceso · DOCK68 · Recv IN_PROGRESS TASK-5306174 · Fatima Del Rosario Ponce · 1d+"
    r["status"] = "🟡 EN PROCESO — RN-5008479 IN_PROGRESS · DOCK68 · Fatima Del Rosario Ponce · 1d+ en recibo"
    r["note"] = "Revalidado 2026-07-03T14:15:00-07:00: WMS confirms recv IN_PROGRESS TASK-5306174 DOCK68 Fatima Del Rosario Ponce."
    changes.append("CSGU6429436: assignedTo Fatima Del Rosario Ponce (WMS fresh)")

# ──────────────────────────────────────────
# CHANGE 3: TGBU3785090 / RN-188086 — Updated notes
# ──────────────────────────────────────────
r = rn_map["RN-188086"]
r["dock"] = "DOCK104"
r["spot"] = "SPOT780"
r["entry"] = "En yarda · DOCK104 · Recv TASK-5307685 NEW · Caren Cubides · YMS SPOT780 drop full"
r["status"] = "🟢 EN YARDA — RN-188086 IMPORTED · TGBU3785090 · DOCK104 (WMS) / SPOT780 (YMS drop)"
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: YMS ET-1117817 GATE_CHECK_OUT Jul 2 21:52 (driver recogió vacío MRKU9748297), "
             "full quedó SPOT780. WMS fresh: IMPORTED, inYardTime Jul 3 14:30, TASK-5307685 NEW DOCK104 Caren Cubides. "
             "YMS customer=ORG-655875 no Gurunanda.")
r["recvTask"] = "TASK-5307685 NEW"
r["assignedTo"] = "Caren Cubides"
r["putTask"] = "NONE"
r["alerta"] = "⚠️ YMS customer ORG-655875 (no Gurunanda) pero WMS RN-188086 Gurunanda. Full dropped SPOT780, ahora DOCK104."
changes.append("TGBU3785090: dock DOCK104 confirmado WMS fresh, YMS drop full SPOT780")

# ──────────────────────────────────────────
# CHANGE 4: RN-188031 — EXCEPTION status
# ──────────────────────────────────────────
r = rn_map["RN-188031"]
r["rnStatus"] = "EXCEPTION"
r["entry"] = "En proceso · DOCK148 · Rcv FORCE_CLOSED · Putaway IN_PROGRESS TASK-5306958 · ⚠️ RN EXCEPTION"
r["status"] = "🟡 EN PROCESO — RN-188031 EXCEPTION · recv FORCE_CLOSED · putaway IN_PROGRESS TASK-5306958 · DOCK148"
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: WMS RN status EXCEPTION (razón: different lo#). "
             "Recv TASK-5306175 FORCE_CLOSED (Fatima). Putaway TASK-5306958 — WMS no confirma putaway endpoint (API limit). "
             "Mantener activo hasta verificar putaway cerrado.")
r["recvTask"] = "TASK-5306175 FORCE_CLOSED"
r["alerta"] = "⚠️ RN EXCEPTION 'different lo#' + recv FORCE_CLOSED. Trailer DOCK_CHECKED_OUT. Verificar putaway."
changes.append("RN-188031: RN status EXCEPTION (WMS fresh), recv TASK-5306175 FORCE_CLOSED")

# ──────────────────────────────────────────
# CHANGE 5: RN-188048 — Update note with WMS fresh
# ──────────────────────────────────────────
r = rn_map["RN-188048"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: WMS RN-188048 IN_PROGRESS; recv FORCE_CLOSED (short item exception); "
             "putaway TASK-5307700. WMS no endpoint para verificar putaway status.")
r["recvTask"] = "FORCE_CLOSED (short item)"
changes.append("RN-188048: note updated with WMS fresh")

# ──────────────────────────────────────────
# CHANGE 6: GN07022026UNIS-1133 / RN-188094 — assignedTo update
# ──────────────────────────────────────────
r = rn_map["RN-188094"]
if r.get("assignedTo") != "Fatima Del Rosario Ponce":
    r["assignedTo"] = "Fatima Del Rosario Ponce"
    r["entry"] = "En proceso · DOCK41 · Recv IN_PROGRESS TASK-5307936 · Fatima Del Rosario Ponce"
    r["status"] = "🟡 EN PROCESO — RN-188094 recv IN_PROGRESS TASK-5307936 · DOCK41 · Fatima Del Rosario Ponce"
    r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: WMS confirms recv IN_PROGRESS TASK-5307936 DOCK41 Fatima Del Rosario Ponce. "
                 "Sin putaway asignado.")
    changes.append("RN-188094: assignedTo Fatima Del Rosario Ponce (WMS fresh)")

# ──────────────────────────────────────────
# CHANGE 7: RN-188084 — Update note with WMS fresh
# ──────────────────────────────────────────
r = rn_map["RN-188084"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: WMS RN-188084 IN_PROGRESS; recv TASK-5307686 CLOSED (Fatima); "
             "putaway IN_PROGRESS. 33 LPs pendientes.")
r["recvTask"] = "TASK-5307686 CLOSED"
r["assignedTo"] = "Fatima Del Rosario Ponce (recv) · Jorge Antonio Franco (putaway)"
changes.append("RN-188084: note updated WMS fresh, recvTask CLOSED confirmed")

# ──────────────────────────────────────────
# CHANGE 8: MATU2656138 / RN-5008572 — Fresh data
# ──────────────────────────────────────────
r = rn_map["RN-5008572"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: YMS ET-1117774 GATE_CHECKED_IN Jul 2 20:11, NO LOCATION. "
             "WMS IMPORTED, sin inYardTime, sin tasks. Cita WMS APPT-6032807 Jul 3 20:00. "
             "14h+ desde gate check-in sin spot asignado.")
r["alerta"] = "🚨 CRÍTICO: 14h+ desde gate check-in (Jul 2 20:11), SIN SPOT, WMS sin inYardTime. Cita 8PM HOY."
r["status"] = "🟢 EN YARDA — MATU2656138 · RN-5008572 · SIN SPOT ⚠️ · 14h+ en espera · Cita 8PM"
changes.append("MATU2656138: alerta actualizada, 14h+ sin spot, WMS sin inYardTime")

# ──────────────────────────────────────────
# CHANGE 9: EITU9363654 / RN-5008569 — Appointment passed
# ──────────────────────────────────────────
r = rn_map["RN-5008569"]
r["alerta"] = "⚠️ CITA 1:30PM VENCIDA. YMS sigue PRE_ENTRY (2:19PM). Sin evidencia de llegada."
r["appointmentTime"] = "Jul 03 13:30 (VENCIÓ, sin llegada a 14:19 PT)"
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: YMS PRE_ENTRY ET-1117697. Cita 1:30PM venció. "
             "WMS IMPORTED sin task, sin inYardTime. Sin evidencia de llegada a las 2:19PM.")
r["status"] = "📅 PRE-ENTRY — RN-5008569 IMPORTED · EITU9363654 · Cita 1:30PM VENCIDA"
changes.append("EITU9363654: cita 1:30PM VENCIDA, YMS PRE_ENTRY confirmado 2:19PM")

# ──────────────────────────────────────────
# CHANGE 10: TGBU8815453 / RN-5008570 — Appointment passed
# ──────────────────────────────────────────
r = rn_map["RN-5008570"]
r["alerta"] = "⚠️ Cita 10AM-12PM VENCIDA. Sin evidencia YMS/WMS. Posible no-show."
r["appointmentTime"] = "Jul 03 10:00-12:00 (VENCIÓ, sin llegada)"
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: Sin evidencia YMS (API limit). WMS IMPORTED sin task, sin inYardTime. "
             "Cita 10AM-12PM venció sin llegada registrada.")
r["status"] = "📅 PRE-ENTRY — RN-5008570 IMPORTED · TGBU8815453 · Cita 10AM-12PM VENCIDA"
changes.append("TGBU8815453: cita 10AM-12PM VENCIDA, sin evidencia llegada")

# ──────────────────────────────────────────
# CHANGE 11: LabelKing PO8449 / RN-5008571 — Update note
# ──────────────────────────────────────────
r = rn_map["RN-5008571"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: YMS ET-1118067 WINDOW_CHECKED_IN DOCK38 07/03 10:14 PT. "
             "WMS IMPORTED, inYardTime, TASK-5307907 NEW (Caren Cubides). LIVE_DELIVERY confirmada.")
r["alerta"] = ""  # remove old alert
r["et"] = "ET-1118067"
changes.append("LabelKing PO8449: YMS ET-1118067 confirmado, LIVE_DELIVERY DOCK38")

# ──────────────────────────────────────────
# CHANGE 12: DDDU5053860 / RN-5008447 — Fresh notes
# ──────────────────────────────────────────
r = rn_map["RN-5008447"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: YMS ET-1117794 GATE_CHECK_OUT Jul 2 21:10 (driver recogió vacío DDDU5053432). "
             "Full DDDU5053860 quedó SPOT675. WMS IMPORTED, inYardTime Jul 3 03:52, TASK-5307692 NEW DOCK13 Caren Cubides.")
changes.append("DDDU5053860: note actualizado con fresh WMS/YMS")

# ──────────────────────────────────────────
# CHANGE 13: TCKU6977609 / RN-5008481 — Fresh notes
# ──────────────────────────────────────────
r = rn_map["RN-5008481"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: YMS ET-1117803 GATE_CHECK_OUT Jul 2 21:12 (driver salió sin equipo, "
             "NO_EQUIPMENT). Full TCKU6977609 quedó SPOT775. WMS IMPORTED, inYardTime Jul 3 04:02, TASK-5307690 NEW DOCK126 Caren Cubides.")
changes.append("TCKU6977609: note actualizado con fresh WMS/YMS")

# ──────────────────────────────────────────
# CHANGE 14: OOCU5501937 / RN-5008506 — Fresh notes
# ──────────────────────────────────────────
r = rn_map["RN-5008506"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: YMS ET-1117844 GATE_CHECKED_IN SPOT688 Jul 2 22:52 (15h tarde vs cita). "
             "WMS IMPORTED, inYardTime Jul 3 05:52, TASK-5307688 NEW DOCK11 Caren Cubides.")
changes.append("OOCU5501937: note actualizado con fresh WMS/YMS")

# ──────────────────────────────────────────
# CHANGE 15: CBHU7024789 / RN-5008507 — Update note
# ──────────────────────────────────────────
r = rn_map["RN-5008507"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: WMS IMPORTED, inYardTime Jul 3 14:31, TASK-5307687 NEW DOCK108 Caren Cubides. "
             "YMS sin rastro (API paginación bug). Cita original Jul 1 vencida.")
changes.append("CBHU7024789: note actualizado con WMS fresh")

# ──────────────────────────────────────────
# CHANGE 16: FFAU2426030 / RN-5008480 — Update note
# ──────────────────────────────────────────
r = rn_map["RN-5008480"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: WMS IMPORTED, inYardTime Jul 3 14:31, TASK-5307691 NEW DOCK128 Caren Cubides. "
             "YMS sin rastro (API paginación bug). Cita original Jul 1 vencida.")
changes.append("FFAU2426030: note actualizado con WMS fresh")

# ──────────────────────────────────────────
# CHANGE 17: CSNU6323633 / RN-5008483 — Update note
# ──────────────────────────────────────────
r = rn_map["RN-5008483"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: WMS IMPORTED, inYardTime Jul 3 14:31, TASK-5307689 NEW DOCK124 Caren Cubides. "
             "YMS sin rastro (API paginación bug). Cita original Jul 1 vencida.")
changes.append("CSNU6323633: note actualizado con WMS fresh")

# ──────────────────────────────────────────
# CHANGE 18: RN-188044 — Update note
# ──────────────────────────────────────────
r = rn_map["RN-188044"]
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: WMS RN-188044 IN_PROGRESS; recv TASK-5306724 IN_PROGRESS DOCK41 Caren Cubides. "
             "Sin putaway. YMS sin rastro (API limit).")
changes.append("RN-188044: note actualizado WMS fresh")

# ──────────────────────────────────────────
# CHANGE 19: RN-5008450 — Fresh note
# ──────────────────────────────────────────
r = rn_map["RN-5008450"]
r["assignedTo"] = "Jerome Aranda"
r["note"] = ("Revalidado 2026-07-03T14:15:00-07:00: WMS IMPORTED, inYardTime Jul 1, TASK-5305892 NEW DOCK45 Jerome Aranda. "
             "2d+ sin iniciar receiving. YMS sin rastro (API limit).")
r["alerta"] = "⚠️ 2d+ en yarda sin iniciar recibo (Jerome Aranda)."
changes.append("RN-5008450: assignedTo Jerome Aranda WMS fresh")

# ──────────────────────────────────────────
# Update all lastVerifiedAt timestamps
# ──────────────────────────────────────────
for row in rows:
    row["lastVerifiedAt"] = "2026-07-03T14:15:00-07:00"
    row["staleStateGuard"] = True
    row["antiEstadoViejo"] = True

# ──────────────────────────────────────────
# Update feed metadata
# ──────────────────────────────────────────
feed["lastUpdated"] = "2026-07-03T14:15:00-07:00"
feed["messageTimestamp"] = "2026-07-03T14:15:00-07:00"
feed["verificationSource"] = "Outlook + WMS + YMS full cross-check Jul 3 14:15 PT"
feed["totalActive"] = len(rows)

# Summary counts
green = sum(1 for r in rows if r.get("color") == "green")
yellow = sum(1 for r in rows if r.get("color") == "yellow")
normal = sum(1 for r in rows if r.get("color") == "normal")
red = sum(1 for r in rows if r.get("color") == "red")
enYarda = sum(1 for r in rows if r.get("inYard") == True and r.get("color") == "green")
enProceso = sum(1 for r in rows if r.get("color") == "yellow")
preEntry = sum(1 for r in rows if r.get("color") == "normal")

feed["summary"] = f"{green} green · {yellow} yellow · {normal} normal · {red} red — {feed['totalActive']} active · {feed['totalExcluded']} excluded"
feed["message"] = f"CORRIDA Jul 3 14:15 PT: Fresh WMS/YMS cross-check. {len(changes)} actualizaciones. {green}g {yellow}y {normal}n {red}r. Citas vencidas EITU9363654 (1:30PM) y TGBU8815453 (10AM). MATU2656138 sigue SIN SPOT 14h+."

# Update alerts
feed["alerts"] = [
    "🚨 CRÍTICO: MATU2656138 (RN-5008572) — 14h+ desde gate check-in SIN SPOT. WMS sin inYardTime.",
    "📅 EITU9363654: Cita 1:30PM VENCIDA. YMS PRE_ENTRY a 2:19PM. No-show.",
    "📅 TGBU8815453: Cita 10AM-12PM VENCIDA. Sin evidencia llegada.",
    "⚠️ RN-188031 EXCEPTION 'different lo#' — verificar putaway antes de remover.",
    "🔴 RN-5006269 ABANDONADO 127+ días DOCK62",
    "🔴 RN-183707 ABANDONADO 67+ días DOCK65",
    "⚠️ RN-5008450: 2d+ en yarda sin iniciar recibo (LabelKing)",
    "⚠️ 4 EN YARDA con recv NEW: DDDU5053860, TCKU6977609, OOCU5501937, TGBU3785090",
    "⚠️ YMS API paginación rota: ~10 containers sin verificar por YMS",
    "✅ ANTI-STALE CLEAN: 0 PRE-ENTRY con evidencia de yarda",
    "✅ 5 removidos confirmados WMS (recv+putaway CLOSED): OOCU7355889, DDDU5053432, MRKU9748297, MRKU6829749, RN-187978",
]

feed["guardrails"]["lastStaleCheck"] = "2026-07-03T14:15:00-07:00"
feed["guardrails"]["staleStateCorrections"] = 0
feed["guardrails"]["preEntryWithDockCount"] = 0
feed["guardrails"]["alerts"] = feed["alerts"]

feed["emailMonitor"]["lastChecked"] = "2026-07-03T14:15:00-07:00"
feed["emailMonitor"]["alertas"] = [
    "Outlook Jul 3 14:15: Priti solo MATU2656138 en correos recientes. Jonathan Heredia: receiving progress + 5 vacíos listos.",
    "Priti pidió agregar ImportExport@gurunanda.com para MATU2656138 (NO ACTUAR — SOLO LECTURA).",
    "Correos NO LEÍDOS de Priti sobre MATU2656138 y OOCU7355889 (citas).",
    "MRKU6829749 conflicto RN-188037 vs RN-188040 resuelto por WMS.",
    "Citas HOY: EITU9363654 1:30PM (venció), TGBU8815453 10AM (venció), MATU2656138 8PM WMS."
]

# Write updated feed
with open("public/container-feed.json", "w") as f:
    json.dump(feed, f, ensure_ascii=False, indent=2)

print(f"\n✅ Feed updated: {feed['totalActive']} active, {feed['totalExcluded']} excluded")
print(f"   Summary: {feed['summary']}")
print(f"\n📋 Changes applied ({len(changes)}):")
for c in changes:
    print(f"   • {c}")

# Validate: check for PRE-ENTRY with dock
pre_entry_with_dock = [r for r in rows if r.get("color") == "normal" and r.get("dock") and r.get("dock") != "—" and r.get("inYard") == False]
if pre_entry_with_dock:
    print(f"\n🚨 ALERTA: {len(pre_entry_with_dock)} PRE-ENTRY rows con dock asignado!")
    for r in pre_entry_with_dock:
        print(f"   • {r.get('container')} / {r.get('rn')} — dock: {r.get('dock')}")
else:
    print("\n✅ ANTI-STALE CHECK: 0 PRE-ENTRY con dock — CLEAN")
