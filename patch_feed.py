#!/usr/bin/env python3
"""Patch container-feed.json with corrections from 29-Jun-2026 monitoring cycle."""
import json
from datetime import datetime, timezone, timedelta

# Load current feed
with open('public/container-feed.json', 'r') as f:
    feed = json.load(f)

# --- CORRECTIONS TO ROWS ---
row_corrections = {
    'BEAU5553433 (RN-5008342)': {
        'displayCategory': 'yellow',
        'color': 'yellow',
        'statusText': 'EN PROCESO (contradicción)',
        'note': '⚠️ CONTRADICCIÓN: WMS RN-5008342 IN_PROGRESS (devanning 29-Jun 17:15) vs YMS DOCK_CHECKED_OUT 29-Jun 10:15. Revisar.',
        'status': '🟡 CONTRADICCIÓN YMS/WMS — WMS dice en DOCK, YMS dice checkout.'
    },
    'DFSU7374979 (RN-5008310)': {
        'displayCategory': 'yellow',
        'color': 'yellow',
        'statusText': 'EN YARDA (contradicción)',
        'note': '⚠️ CONTRADICCIÓN: WMS RN-5008310 IMPORTED (en yarda desde 27-Jun, 2.5 días) vs YMS GATE_CHECK_OUT 26-Jun. ~103K unidades esperando.',
        'status': '🟡 CONTRADICCIÓN YMS/WMS — WMS dice en yarda SPOT772, YMS dice checkout.'
    },
    'SMCU1114360 (RN-5008384)': {
        'displayCategory': 'yellow',
        'color': 'yellow',
        'statusText': 'SALIÓ DE YARDA (contradicción)',
        'note': '⚠️ CONTRADICCIÓN: YMS GATE_CHECK_OUT 29-Jun 09:52 vs RN-5008384 IMPORTED en WMS. ¿Salió o sigue? Revisar.',
        'status': '🟡 CONTRADICCIÓN — YMS checkout 09:52 hoy, pero RN sigue IMPORTED en WMS.'
    },
    'MATU2596614 (RN-5008382)': {
        'note': '📅 PRE-ENTRY — RN-5008382 IMPORTED. Cita 29-Jun 14:00. Sin rastro YMS aún.',
        'status': '📅 PRE-ENTRY — RN-5008382 IMPORTED. Cita hoy 14:00. Sin rastro aún.'
    },
    'MATU2610055 (RN-5008383)': {
        'note': '📅 PRE-ENTRY — RN-5008383 IMPORTED. Cita 29-Jun 14:00. Sin rastro YMS aún.',
        'status': '📅 PRE-ENTRY — RN-5008383 IMPORTED. Cita hoy 14:00. Sin rastro aún.'
    },
}

for row in feed.get('rows', []):
    container_key = row.get('container', '')
    if container_key in row_corrections:
        for k, v in row_corrections[container_key].items():
            row[k] = v

# --- UPDATE SUMMARY ---
rows = feed.get('rows', [])
green = sum(1 for r in rows if r.get('displayCategory', r.get('color')) == 'green')
yellow = sum(1 for r in rows if r.get('displayCategory', r.get('color')) == 'yellow')
red = sum(1 for r in rows if r.get('displayCategory', r.get('color')) == 'red')
normal = sum(1 for r in rows if r.get('displayCategory', r.get('color')) == 'normal')
in_yard = sum(1 for r in rows if r.get('inYard'))
sin_rn = sum(1 for r in rows if not r.get('receipt') and not r.get('rn'))
pre_entry = sum(1 for r in rows if 'PRE-ENTRY' in str(r.get('statusText', '')) or 'PRE-ENTRY' in str(r.get('status', '')))

feed['summary'] = {
    'green': green,
    'yellow': yellow,
    'red': red,
    'normal': normal,
    'visible': green + yellow + red + normal,
    'enYardaProceso': in_yard,
    'sinRn': sin_rn,
    'preEntry': pre_entry,
    'excluded': len(feed.get('excludedContainers', [])),
    'totalVisible': green + yellow + red + normal,
}

# --- UPDATE ALERTAS ROLAS ---
now_pt = datetime.now(timezone(timedelta(hours=-7)))
timestamp_str = now_pt.strftime('%Y-%m-%dT%H:%M:%S-07:00')

alertas = [
    "🚨 ALERTA ROLAS: BEAU5553433 — Contradicción YMS vs WMS. YMS DOCK_CHECKED_OUT (10:15) pero WMS IN_PROGRESS (devanning 17:15). Revisar urgente.",
    "🚨 ALERTA ROLAS: DFSU7374979 — Contradicción YMS vs WMS. YMS GATE_CHECK_OUT (26-Jun) pero WMS IMPORTED en yarda SPOT772 (2.5 días). ~103K u esperando.",
    "🚨 ALERTA ROLAS: SMCU1114360 — YMS GATE_CHECK_OUT hoy 09:52 pero RN-5008384 sigue IMPORTED en WMS. ¿Salió realmente?",
    "⚠️ ALERTA ROLAS: FFAU6121609 — 4+ días en DOCK64 sin checkout. RN-5008322 CLOSED 26-Jun pero contenedor sigue DOCK_CHECKED_IN en YMS.",
    "⚠️ ALERTA ROLAS: CAAU8362068 — RN-5008373 CLOSED (29-Jun 15:56) pero YMS muestra GATE_CHECKED_IN SPOT772.",
    "⚠️ ALERTA ROLAS: BSIU9381158 — RN-5008324 CLOSED (26-Jun 20:31) pero YMS muestra GATE_CHECKED_IN SPOT761.",
    "⚠️ ALERTA ROLAS: RN-187767 (53162) — Cita era 07:00 AM, llegó a yarda 19:20. 12h de retraso. Aún sin receiving.",
    "⚠️ ALERTA ROLAS: 6 contenedores del 29-30 Jun sin ET en YMS: CAIU9453139, MATU2596614, MATU2610055, OOCU8342103, BSIU8440908 (todos PRE-ENTRY).",
    "⚠️ ALERTA ROLAS: RN-5008310 (DFSU7374979) — 2.5 días en yarda sin receiving task iniciado.",
    "ℹ️ INFO ROLAS: EITU8162104 sigue SIN RN ni rastro YMS. Priti preguntó estado el 25-Jun. Sin resolver."
]

feed['alertasRolas'] = alertas
feed['lastUpdated'] = timestamp_str
feed['message'] = f"Monitor Priti 29-Jun-2026 13:47 PT — {green} verde, {yellow} amarillo, {red} rojo, {normal} normal. {len(alertas)} alertas activas. {len(feed.get('excludedContainers', []))} excluidos."

# Save
with open('public/container-feed.json', 'w') as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"✅ Feed actualizado: {timestamp_str}")
print(f"   Verdes: {green}, Amarillos: {yellow}, Rojos: {red}, Normal: {normal}")
print(f"   Alertas: {len(alertas)}, Excluidos: {len(feed.get('excludedContainers', []))}")
print(f"   Total visible: {green + yellow + red + normal}")
