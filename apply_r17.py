#!/usr/bin/env python3
"""R17 LLEGADAS YMS — 08/04 20:05 PT: 37 revisados uno por uno (Container→Trailer→equipment-entry/activity, ET apoyo).
0 LLEGADAS nuevas. Metadata-only update + alerts. Preserves all 48 rows verbatim."""
import json, hashlib, sys

TS = "2026-08-04T20:05:00-07:00"
TS_UTC = "2026-08-05T03:05:00+00:00"
RUN = "R17 LLEGADAS YMS"

path_root = "container-feed.json"
path_pub = "public/container-feed.json"

def load(p):
    with open(p, "r", encoding="utf-8") as f:
        return json.load(f), hashlib.md5(open(p, "rb").read()).hexdigest()

feed, h0 = load(path_root)
pub, h0p = load(path_pub)
assert h0 == h0p, "root vs public feed diverge"
assert feed.get("lastUpdated") == "2026-08-04T18:40:00-07:00", f"feed changed since read: {feed.get('lastUpdated')}"

rows = feed["rows"]
print("ROWS BEFORE:", len(rows))
containers_before = [r.get("container") for r in rows]
assert len(rows) == 48, "expected 48 rows"

# ---- 1. top-level metadata (message, lastUpdated, updatedBy, verificationSource) ----
feed["message"] = (
    "R17 LLEGADAS YMS — 2026-08-04T20:05:00-07:00. 37 revisados uno por uno "
    "(Container → Trailer, equipment-entry/activity completos, ET apoyo). 0 LLEGADAS nuevas. "
    "5 con llegada histórica ya fuera (CSNU7382630, GCXU5097405, TCNU4365281, TEMU9327290, YMMU6638670 — "
    "inYard=false, OUT_OF_YARD/COMPLETED, sin reingreso). 32 sin evidencia física (azul). "
    "48 activos (37 azul/11 amarillo)."
)
feed["lastUpdated"] = TS
feed["updatedBy"] = "RUTINA LIGERA LLEGADAS YMS — 08/04 20:05 PT (Agente Priti)"
feed["verificationSource"] = (
    "R17 LLEGADAS YMS 08/04 20:05 PT — 37 contenedores revisados en YMS/Window "
    "(Container → Trailer, equipment-entry/history + equipment-activity, ET como apoyo): 0 llegadas nuevas. "
    "5 con llegada histórica ya fuera (CSNU7382630, TCNU4365281, TEMU9327290, GCXU5097405, YMMU6638670 — "
    "inYard=false, OUT_OF_YARD/COMPLETED, gate-out del contenedor, sin reingreso). "
    "32 sin rastro físico (ni Container ni Trailer; cero equipment-entry/activity): "
    "se conserva En yarda=No / azul / PRE_ENTRY. Sin cambios de fila en este ciclo."
)
feed["summary"] = {
    "red": 0, "green": 0, "blue": 37, "yellow": 11, "normal": 0,
    "totalActive": 48, "totalExcluded": 11, "addedThisRun": 0, "excludedThisRun": 0, "orderChanged": False,
}
feed["guardrails"]["orderCheck"]["appliedBy"] = "R17 - LLEGADAS YMS (Agente Priti)"
feed["guardrails"]["orderCheck"]["appliedAt"] = TS
feed["guardrails"]["orderCheck"]["snapshotMatch"] = True
feed["guardrails"]["orderCheck"]["orderChanged"] = False
feed["guardrails"]["lastYmsArrivalScan"] = TS_UTC

# ---- 2. alerts: prepend R17 entry, refresh ROLAS live-stale entry in place ----
new_run_alert = (
    "🟦 R17 LLEGADAS YMS — 2026-08-04T20:05:00-07:00: 0 llegadas nuevas. 37 revisados uno por uno "
    "(Container → Trailer, equipment-entry/activity, ET apoyo). 5 con llegada histórica ya fuera "
    "(CSNU7382630, TCNU4365281, TEMU9327290, GCXU5097405, YMMU6638670 — inYard=false, sin reingreso). "
    "32 sin evidencia física (azul). 48 activos (37 azul/11 amarillo). Sin cambios de fila."
)
rolas_alert = (
    "🚨 ALERTA ROLAS — Feed live STALE: https://contenedores-priti-dashboard-03b000.coolify.item.pub/container-feed.json "
    "sirve lastUpdated 2026-08-02T05:27:00-07:00 (repo main @ R17 08/04 20:05 PT). Coolify sin auto-deploy "
    "(recurrente desde Jul; requiere Force Redeploy manual). CERT TLS *.coolify.item.pub RENOVADO (válido "
    "05/08/2026–03/11/2026) — ya no bloquea HTTPS. Faltan en live: 9 llegadas R8/R9, metadatos R10-R16 y "
    "llegada R16 CSNU7908411. Dashboard live muestra 47 azul/1 amarillo vs repo 37 azul/11 amarillo. "
    "Requiere Force Redeploy manual en Coolify. Verificado 08/04 20:05 PT."
)

# remove previous ROLAS live-stale entries to avoid unbounded duplicates (keep history compact)
feed["alerts"] = [a for a in feed["alerts"] if not a.startswith("🚨 ALERTA ROLAS — Feed live STALE")]
feed["alerts"].insert(0, new_run_alert)
feed["alerts"].insert(1, rolas_alert)

# ---- 3. verify rows untouched ----
assert len(feed["rows"]) == 48
containers_after = [r.get("container") for r in feed["rows"]]
assert containers_before == containers_after, "row order changed!"
# deep-compare rows content
import copy
rows_snapshot = copy.deepcopy(rows)

for p in (path_root, path_pub):
    with open(p, "w", encoding="utf-8") as f:
        json.dump(feed, f, ensure_ascii=False, indent=2)
        f.write("\n")

# re-read and validate
for p in (path_root, path_pub):
    with open(p, "r", encoding="utf-8") as f:
        d = json.load(f)
    assert d["rows"] == rows_snapshot, f"rows changed in {p}"
    assert len(d["rows"]) == 48
    assert d["lastUpdated"] == TS
print("ROWS AFTER:", len(feed["rows"]))
print("ALERTS:", len(feed["alerts"]))
print("OK — feed updated (metadata only, rows preserved).")
