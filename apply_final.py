#!/usr/bin/env python3
"""CYCLE 05:07 PT Jul 1 — CLEAN apply. Key by (container, rn) for dedup."""
import json
from datetime import datetime, timezone, timedelta

now_pt = datetime.now(timezone(timedelta(hours=-7)))
ts = now_pt.strftime('%Y-%m-%dT%H:%M:%S-07:00')

with open('public/container-feed.json', 'r') as f:
    feed = json.load(f)

rows = feed.get('rows', [])

# ---- 1. Remove rows to delete ----
rows_to_remove = [
    ('BEAU5553433', 'SIN RN'),  # departed
]
rows = [r for r in rows if (r.get('container'), r.get('rn', r.get('receipt'))) not in rows_to_remove]
print(f"After removals: {len(rows)} rows")

# ---- 2. Remove DFSU7374979 from excluded ----
for key in ['excludedContainers', 'excluded']:
    feed[key] = [e for e in feed.get(key, []) if e.get('containerNo') != 'DFSU7374979']
print(f"DFSU7374979 removed from excluded. Excluded count: {len(feed.get('excludedContainers',[]))}")

# ---- 3. Add BEAU5553433 to excluded ----
bea_excl = {
    "containerNo": "BEAU5553433",
    "rn": None,
    "reason": "DEPARTED — YMS 05:07: PICK_UP_EMPTY 06-30 23:46. Chofer OOLU9324944 (ET-1116521) recogió vacío de DOCK98.",
    "excludedAt": ts
}
for key in ['excludedContainers', 'excluded']:
    feed[key].append(bea_excl)

# ---- 4. Add DFSU7374979 back to rows ----
dfsu = {
    "container": "DFSU7374979",
    "rn": "RN-5008310",
    "rnStatus": "IN_PROGRESS",
    "receipt": "RN-5008310",
    "dock": "DOCK61",
    "entry": "EN PROCESO — DOCK61 (REINSTATED 05:12 PT)",
    "inYard": True,
    "color": "yellow",
    "displayCategory": "yellow",
    "appointmentTime": "—",
    "note": "⚠️ REINSTATED 07/01 05:12 PT. Ciclo 04:55 lo excluyó por error. WMS: IN_PROGRESS, TASK-5303877 DOCK61, Caren Cubides. YMS: DOCK_CHECKED_IN DOCK61 Jun 29 15:17. ¡Activo!",
    "status": "EN PROCESO — DOCK61 (REINSTATED: WMS IN_PROGRESS + YMS DOCK_CHECKED_IN)",
    "statusText": "EN PROCESO — DOCK61 (REINSTATED: WMS IN_PROGRESS + YMS DOCK_CHECKED_IN)",
    "lastVerifiedAt": ts,
    "verificationSource": "WMS-cycle-0506 + YMS-cycle-0507 + cycle-20260701-0507",
    "staleStateGuard": True
}
rows.append(dfsu)

# ---- 5. Update existing rows ----
updates = {
    'OOLU9324944': {
        'dock': 'DOCK98',
        'note': '✅ YMS: ET-1116521 06-30 23:08, DROP_OFF_DELIVERY DOCK98. Chofer recogió BEAU5553433 vacío. Lleno se queda. WMS: RN-5008430 IMPORTED sin RT.',
        'status': 'EN YARDA — DOCK98 (YMS DROP_OFF_DELIVERY 06-30 23:08)',
        'statusText': 'EN YARDA — DOCK98 (YMS DROP_OFF_DELIVERY 06-30 23:08)',
        'lastVerifiedAt': ts,
        'verificationSource': 'YMS-cycle-0507 + WMS + cycle-20260701-0507',
    },
    'FFAU1548537': {
        'dock': 'DOCK44',
        'note': '✅ YMS: ET-1116141 06-30 10:22, DROP_OFF_DELIVERY DOCK44. Chofer recogió BSIU9381158 vacío. Lleno se queda. WMS: TASK-5304579 NEW, PEDRO AVILA.',
        'status': 'EN YARDA — DOCK44 (YMS DROP_OFF_DELIVERY 06-30 10:22)',
        'statusText': 'EN YARDA — DOCK44 (YMS DROP_OFF_DELIVERY 06-30 10:22)',
        'lastVerifiedAt': ts,
        'verificationSource': 'YMS-cycle-0507 + WMS + cycle-20260701-0507',
    },
    'OOCU8342103': {
        'dock': 'DOCK68',
        'note': 'WMS: IN_PROGRESS, RT CLOSED. YMS: DOCK_CHECKED_OUT DOCK68 06-30 18:40, RECV COMPLETADO. ⚠️ Sin PA task visible.',
        'lastVerifiedAt': ts,
        'verificationSource': 'WMS-cycle-0506 + YMS-cycle-0507 + cycle-20260701-0507',
    },
    'BSIU8440908': {
        'dock': 'DOCK62',
        'note': 'WMS: IN_PROGRESS, RT CLOSED. YMS: DOCK_CHECKED_OUT DOCK62 06-30 19:18, RECV COMPLETADO. ⚠️ Sin PA task visible.',
        'lastVerifiedAt': ts,
        'verificationSource': 'WMS-cycle-0506 + YMS-cycle-0507 + cycle-20260701-0507',
    },
    'EITU8162104': {
        'note': '🔴 8+d sin RN. Art (UNIS) pidió ASN Jun 24 — email SIN LEER. Sin ASN = sin RN. Priti preguntó 06/25, Rufino dijo "no ha llegado". ⚠️ ALERTA ROLAS: conseguir ASN o remover.',
        'lastVerifiedAt': ts,
        'verificationSource': 'WMS + Outlook-cycle-0507 + cycle-20260701-0507',
    },
    'JTAU7362582': {
        'note': '⚠️ YMS: DOBLE ET. DOCK60 (ET-1116418, RECV COMPLETADO, PEDRO AVILA) + DOCK166 (ET-1116387, GATE_CHECKED_IN, carrier "b", truck 9G48988). WMS: IN_PROGRESS.',
        'lastVerifiedAt': ts,
        'verificationSource': 'WMS + YMS-cycle-0507 + cycle-20260701-0507',
    },
    'JTAU7362598': {
        'note': '✅ YMS: ET-1116382 06-30 16:01, GATE_CHECKED_IN DOCK156, FULL, seal YMAQ364730. Driver KUN v (TWENTY TRANSP, 9G21216). Sin gate out. WMS: RN-5008424 IMPORTED.',
        'lastVerifiedAt': ts,
        'verificationSource': 'YMS-cycle-0507 + WMS + cycle-20260701-0507',
    },
    'CAIU9453139': {
        'note': '✅ YMS: ET-1116033 06-30 08:00, DOCK_CHECKED_IN DOCK2. WMS: IN_PROGRESS DOCK559, TASK-5304239, ccubides. ⚠️ Dock YMS(DOCK2) vs WMS(DOCK559).',
        'lastVerifiedAt': ts,
        'verificationSource': 'WMS-cycle-0506 + YMS-cycle-0507 + cycle-20260701-0507',
    },
}

for row in rows:
    c = row.get('container', '')
    if c in updates:
        row.update(updates[c])

# ---- 6. Recalculate ----
green = sum(1 for r in rows if r.get('displayCategory', r.get('color')) == 'green')
yellow = sum(1 for r in rows if r.get('displayCategory', r.get('color')) == 'yellow')
red = sum(1 for r in rows if r.get('displayCategory', r.get('color')) == 'red')
normal = sum(1 for r in rows if r.get('displayCategory', r.get('color')) == 'normal')
t_act = len(rows)
t_excl = len(feed.get('excludedContainers', []))

feed['rows'] = rows
feed['totalActive'] = t_act
feed['totalExcluded'] = t_excl

feed['summary'] = {
    "totalActive": t_act,
    "totalExcluded": t_excl,
    "byColor": {"green": green, "yellow": yellow, "red": red, "normal": normal},
    "alertasActivas": [
        {"level": "CRITICAL", "message": f"CICLO 05:07 PT Jul 1 — WMS+YMS+Outlook full cross-ref. {t_act} activos ({green}G/{yellow}Y/{red}R/{normal}N). {t_excl} excluidos."},
        {"level": "CRITICAL", "message": "🔴 DFSU7374979 REINSTATED: excluido por error en ciclo 04:55. WMS IN_PROGRESS + YMS DOCK_CHECKED_IN DOCK61. ¡Activo!"},
        {"level": "CRITICAL", "message": "RN-5006269 (MAWB): 121d en yarda DOCK566. Sin avance."},
        {"level": "CRITICAL", "message": "RN-183707 (ALNOR): 65d en yarda DOCK573. Sin avance."},
        {"level": "HIGH", "message": "🔴 EITU8162104: 8+d sin RN. Art pidió ASN Jun 24 — email SIN LEER."},
        {"level": "HIGH", "message": "⚠️ DOCK YMS vs WMS: OOCU8342103(68vs574) BSIU8440908(62vs566) CAIU9453139(2vs559)."},
        {"level": "HIGH", "message": "⚠️ SIN PA: OOCU8342103, BSIU8440908, TCNU4379515 — posiblemente ya completados."},
        {"level": "HIGH", "message": "RN-5008388 (Chapin): PA NEW 2d sin avance DOCK572."},
        {"level": "HIGH", "message": "CORRU RT FORCE_CLOSED (RN-5008361) — PA IN_PROGRESS. Anomalía."},
        {"level": "HIGH", "message": "JTAU7362582: DOBLE ET DOCK60(completado) + DOCK166(GATE_CHECKED_IN)."},
        {"level": "HIGH", "message": "BEAU5553433: DEPARTED. YMS PICK_UP_EMPTY 06-30 23:46. EXCLUIDO."},
        {"level": "INFO", "message": "7 citas HOY: DDDU5053860(10:00), JTAU7362561(11:00), CSGU6429436(13:30), DDDU5053432(16:00), LabelKing×3(17:00), ITL07012026(17:30), OOCU7355889(20:00)."},
        {"level": "INFO", "message": "Outlook 05:07: 2 UNREAD (Priti citas Jul 1-2 + Art ASN request EITU8162104)."},
        {"level": "INFO", "message": "YMS 05:07: 22 containers verificados. 5 en yarda, 11 sin rastro (aún no llegan)."},
    ]
}
feed['alerts'] = feed['summary']['alertasActivas']

# ---- 7. Metadata ----
feed['lastUpdated'] = ts
feed['message'] = f"CYCLE 05:07 PT Jul 1 — WMS+YMS+Outlook. {t_act} activos ({green}G/{yellow}Y/{red}R/{normal}N). DFSU7374979 REINSTATED. BEAU5553433 excluido."
feed['metadata'] = {
    "corridaInfo": f"Ciclo 05:07 PT Jul 1 · {t_act} activos · DFSU7374979 REINSTATED · WMS+YMS+Outlook",
    "feedLastUpdated": ts,
    "generatedAt": ts
}
feed['messageTimestamp'] = ts

# ---- 8. Save ----
with open('public/container-feed.json', 'w') as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"✅ CYCLE 05:07 PT Jul 1 — FINAL")
print(f"   Activos: {t_act} (G:{green} Y:{yellow} R:{red} N:{normal})")
print(f"   Excluidos: {t_excl}")
print(f"   DFSU7374979: REINSTATED ✅")
print(f"   BEAU5553433: EXCLUIDO ✅")
print(f"   Timestamp: {ts}")
