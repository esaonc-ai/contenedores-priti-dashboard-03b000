#!/usr/bin/env python3
"""Apply FFAU2426030 removal + CAAU7998380 alert + count updates."""
import json
from datetime import datetime

with open("public/container-feed.json", "r") as f:
    data = json.load(f)

now = "2026-07-09T03:15:00-07:00"
NOW_TS = now

# ── 1. PROMOTE CAAU7998380 to GREEN (as live had it) with alert note ──
for row in data["rows"]:
    if row.get("container") == "CAAU7998380":
        row["color"] = "green"
        row["status"] = "EN_YARDA"
        row["inYard"] = True
        row["note"] = (
            "🟢 EN YARDA. WMS inYardTime Jul 08 09:12. Evidencia YMS previa: "
            "ET-1119632 CHECK_IN + ET-1120155 YARD_CHECK FULL. "
            "⚠️ REVERIFICAR: YMS actual muestra 0 visitas para EQP-263541/EQP-264424. "
            "Evidencia previa ET-1119632/ET-1120155 no encontrada en corrida actual."
        )
        row["notes"] = row["note"]
        row["lastVerifiedAt"] = NOW_TS
        row["verificationSource"] = "WMS+YMS cross-check 03:15 PT — GREEN con alerta reverificación"
        row["greenEvidenceRule"] = {
            "reason": "YMS previa ET-1119632 CHECK_IN + ET-1120155 YARD_CHECK FULL + WMS inYardTime",
            "evidence": [
                "WMS inYard 07-08 09:12",
                "YMS previa ET-1119632 CHECK_IN",
                "YMS previa ET-1120155 YARD_CHECK FULL"
            ],
            "alert": "⚠️ YMS corrida actual: 0 visitas EQP-263541/EQP-264424. REVERIFICAR.",
            "promotedAt": NOW_TS
        }
        row.pop("falseGreenCorrected", None)
        break

# ── 2. REMOVE FFAU2426030 from active → move to excluded ──
ffau = None
for i, row in enumerate(data["rows"]):
    if row.get("container") == "FFAU2426030":
        ffau = data["rows"].pop(i)
        break

if ffau:
    excluded_entry = {
        "rn": "RN-5008480",
        "reason": (
            "WMS ambos tasks CLOSED. Recv TASK-5307691 CLOSED. "
            "Putaway TASK-5311289 CLOSED (Nanci Viviana Rosas 2026-07-06). "
            "Reportado VACÍO por Daniela 07/08. YMS Spot 565 TRAILER EMPTY. "
            "6 días en yarda."
        ),
        "recvTask": "TASK-5307691 CLOSED",
        "putTask": "TASK-5311289 CLOSED",
        "wasColor": "yellow",
        "wasStatus": "EN_PROCESO",
        "wasActive": True,
        "container": "FFAU2426030",
        "assignedTo": "Mateo Moreno",
        "removedAt": NOW_TS
    }
    data["excluded"].insert(0, excluded_entry)

# ── 3. UPDATE summary ──
data["summary"]["totalActive"] = 20
data["summary"]["totalExcluded"] = 27
data["summary"]["green"] = 1
data["summary"]["yellow"] = 5
data["summary"]["normal"] = 14
data["summary"]["excludedThisRun"] = 1
data["summary"]["promotedToGreenThisRun"] = 1
data["summary"]["notesUpdatedThisRun"] = 1

data["totalActive"] = 20
data["totalExcluded"] = 27

# ── 4. UPDATE message ──
data["message"] = (
    "FFAU2426030 REMOVIDO — ambos tasks CLOSED. "
    "20a (1g/5y/14n/0r). 27e. "
    "ALERTA: CAAU7998380 YMS sin visitas en corrida actual."
)

# ── 5. UPDATE lastUpdated ──
data["lastUpdated"] = NOW_TS

# ── 6. UPDATE alerts ──
data["alerts"] = [
    "✅ CORRECCIÓN 2026-07-09 03:15 PT: REMOVIDO FFAU2426030 (RN-5008480) — ambos tasks CLOSED (Recv TASK-5307691 + Putaway TASK-5311289). Reportado VACÍO 07/08. 20a (1g/5y/14n/0r). 27e.",
    "🔴 ALERTA ROLAS: CAAU7998380 (RN-5008646) — GREEN pero YMS actual muestra 0 visitas para EQP-263541/EQP-264424. Evidencia previa ET-1119632/ET-1120155 no encontrada en corrida actual. REVERIFICAR presencia física.",
    "🟢 CAAU7998380 (RN-5008646): EN YARDA (GREEN). WMS inYard 09:12 Jul 08. Evidencia YMS previa: ET-1119632 CHECK_IN + ET-1120155 YARD_CHECK FULL. ⚠️ ALERTA: reverificar en próxima corrida.",
    "🟡 ZCSU7781965 (RN-5008664): ANTI-ESTADO-VIEJO — DOCK41. TASK-5311621 IN_PROGRESS.",
    "⚠️ MRKU9388930 (RN-188088): YMS DOCK_CHECKED_OUT pero WMS receiving IN_PROGRESS.",
    "🔴 ALERTA ROLAS CRÍTICA: CSGU6429436 (RN-5008479) — CONTENEDOR FANTASMA en DOCK45.",
    "⚠️ TIIU6675897: Sin RN WMS. CORRECCIÓN de TIIU6671567. Drop Jul 09 12:00-14:00. PENDIENTE item setup 48-73-24Z-08997-01. Sin evidencia YMS.",
    "⚠️ TGSU5157375: Sin RN WMS. Anunciado ImportExport Jasmine 07/08 17:47 PT. Cita Jul 09 11:00-13:00. Sin evidencia YMS."
]

# ── 7. UPDATE _corrections ──
data["_corrections"] = {
    "alert": (
        "CORRECCIÓN Jul 9 03:15 PT: FFAU2426030 (RN-5008480) REMOVIDO — "
        "ambos tasks CLOSED. CAAU7998380 GREEN con alerta YMS. "
        "20a (1g/5y/14n/0r). 27e."
    ),
    "timestamp": NOW_TS,
    "ymsCheckNote": (
        "FFAU2426030: Recv TASK-5307691 CLOSED + Putaway TASK-5311289 CLOSED. "
        "CAAU7998380: YMS actual 0 visitas EQP-263541/EQP-264424 — REVERIFICAR."
    ),
    "removalsThisRun": [
        {
            "rn": "RN-5008480",
            "reason": "WMS ambos tasks CLOSED. Recv TASK-5307691 + Putaway TASK-5311289. Reportado VACÍO.",
            "container": "FFAU2426030"
        }
    ],
    "additionsThisRun": [],
    "demotionsThisRun": [],
    "promotionsThisRun": [
        {
            "rn": "RN-5008646",
            "reason": "YMS previa ET-1119632 CHECK_IN + ET-1120155 YARD_CHECK FULL + WMS inYard. ⚠️ ALERTA: YMS actual sin visitas.",
            "container": "CAAU7998380"
        }
    ],
    "notesUpdatedThisRun": ["CAAU7998380 alerta reverificación YMS", "FFAU2426030 removido"]
}

# ── 8. UPDATE guardrails ──
data["guardrails"]["closedRemovalRule"] = {
    "status": "ACTIVE",
    "removalNote": "Jul 9 03:15 PT: FFAU2426030 removed (both tasks CLOSED). 27 excluidos total.",
    "removalsThisRun": 1,
    "reactivationsThisRun": 0
}
data["guardrails"]["greenEvidenceRule"] = {
    "status": "ACTIVE",
    "promotionNote": (
        "Jul 9 03:15 PT: CAAU7998380 GREEN (YMS previa ET-1119632 + ET-1120155). "
        "⚠️ ALERTA: YMS actual 0 visitas. 1 green activo."
    ),
    "demotionsThisRun": 0,
    "promotionsThisRun": 1,
    "falseGreensDetected": 0
}
data["guardrails"]["antiEstadoViejo"] = {
    "status": "ACTIVE",
    "note": "Jul 9 03:15 PT: FFAU2426030 removido CLOSED. CAAU7998380 GREEN con alerta reverificación."
}

# ── 9. UPDATE verificationSource ──
data["verificationSource"] = (
    "WMS+YMS cross-check 03:15 PT — 1 removal (FFAU2426030 CLOSED) + 1 promotion (CAAU7998380 GREEN con alerta)"
)

# ── 10. Update TIIU6675897 and TGSU5157375 notes with YMS warning ──
for row in data["rows"]:
    if row.get("container") == "TIIU6675897":
        row["note"] = (
            "⚠️ PENDIENTE item setup 48-73-24Z-08997-01. UFB-128971. "
            "Sin RN en WMS. CORRECCIÓN: reemplaza a TIIU6671567 (excluido). "
            "Anunciado por ImportExport (Jasmine). Cita 07/09 12:00-14:00 Drop. "
            "Sin evidencia YMS."
        )
        row["notes"] = row["note"]
        row["lastVerifiedAt"] = NOW_TS
    elif row.get("container") == "TGSU5157375":
        row["note"] = (
            "⚠️ Anunciado ImportExport Jasmine 07/08 17:47 PT. "
            "Sin RN en WMS. PENDIENTE creación. Customer: GURUNANDA. "
            "Cita Jul 09 11:00-13:00. Sin evidencia YMS."
        )
        row["notes"] = row["note"]
        row["lastVerifiedAt"] = NOW_TS

# Write
with open("public/container-feed.json", "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# Verify
with open("public/container-feed.json", "r") as f:
    verified = json.load(f)

active = verified["rows"]
yellow_count = sum(1 for r in active if r.get("color") == "yellow")
green_count = sum(1 for r in active if r.get("color") == "green")
normal_count = sum(1 for r in active if r.get("color") == "normal")
red_count = sum(1 for r in active if r.get("color") == "red")
excluded_count = len(verified.get("excluded", []))

print(f"✅ Active: {len(active)} (g={green_count}, y={yellow_count}, n={normal_count}, r={red_count})")
print(f"✅ Excluded: {excluded_count}")
print(f"✅ lastUpdated: {verified['lastUpdated']}")
print(f"✅ message: {verified['message']}")
print(f"✅ FFAU2426030 in active? {'FFAU2426030' in [r.get('container','') for r in active]}")
print(f"✅ FFAU2426030 in excluded? {'FFAU2426030' in [e.get('container','') for e in verified.get('excluded',[])]}")
print(f"✅ CAAU7998380 color: {[r for r in active if r.get('container')=='CAAU7998380'][0].get('color') if any(r.get('container')=='CAAU7998380' for r in active) else 'NOT FOUND'}")
