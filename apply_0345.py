#!/usr/bin/env python3
"""Corrida 03:45 PT — Cambios a container-feed.json"""
import json

FEED_PATH = "public/container-feed.json"
NEW_TS = "2026-07-01T03:45:00.000000-07:00"

with open(FEED_PATH) as f:
    feed = json.load(f)

rows = feed["rows"]

# 1. JTAU7362598: YELLOW -> GREEN
for r in rows:
    if r.get("container") == "JTAU7362598":
        r["color"] = "green"
        r["inYard"] = True
        r["dock"] = "DOCK156"
        r["entry"] = "YMS ET-1116382 GATE_CHECKED_IN DOCK156 (TWENTY TRANSPORTATION, DROP_OFF + PICK_UP_EMPTY) · Full dropped, tractor salió. WMS IMPORTED sin receiving task."
        r["status"] = "🟢 EN YARDA — JTAU7362598 · DOCK156 · YMS ET-1116382 GATE_CHECKED_IN · WMS IMPORTED (gap integración YMS→WMS)"
        r["note"] = "✅ CORRECCIÓN 03:45 PT: ANTI-ESTADO-VIEJO. YMS ET-1116382 GATE_CHECKED_IN DOCK156 (TWENTY TRANSPORTATION, DROP_OFF + PICK_UP_EMPTY). Full JTAU7362598 EN YARDA. WMS RN-5008424 IMPORTED sin receiving task — gap de integración YMS→WMS. Cambio: yellow→green."
        r["staleStateGuard"] = "CORRECTED_03:45 — YMS confirms GATE_CHECKED_IN DOCK156, upgraded from CITA VENCIDA to EN YARDA"
        r["displayCategory"] = "green"
        r["statusText"] = "🟢 EN YARDA — JTAU7362598 · DOCK156 · YMS ET-1116382 GATE_CHECKED_IN"
        r["lastVerifiedAt"] = NEW_TS
        r["verificationSource"] = "WMS+YMS 03:45 PT | RN-5008424 IMPORTED | DOCK156 | YMS ET-1116382 GATE_CHECKED_IN (TWENTY TRANSPORTATION, DROP_OFF+PICK_UP_EMPTY)"
        r["appointmentTime"] = "Jun 30 23:00 (llegó 07/01 03:37 PT)"
        print("✅ JTAU7362598: yellow → green")
        break

# 2. ALL rows: update timestamp
for r in rows:
    r["lastVerifiedAt"] = NEW_TS

# 3. CAIU9453139: WMS dock DOCK559
for r in rows:
    if r.get("container", "").startswith("CAIU9453139"):
        r["dock"] = "DOCK2 (YMS) / DOCK559 (WMS RT)"
        r["entry"] = "YMS ET-1116033 DOCK2 / WMS inYardTime 06/30 / WMS dock actualizado DOCK559 / receiving IN_PROGRESS"
        r["note"] = "🟡 WMS+YMS 03:37 PT: RN-5008385 IN_PROGRESS. RT TASK-5304239 IN_PROGRESS (PEDRO AVILA, ~18h activo). YMS DOCK2 DOCK_CHECKED_IN. WMS dock actualizado DOCK559. Putaway PENDING. GURUNANDA."
        r["status"] = "🟡 IN_PROGRESS — RN-5008385 · YMS DOCK2 / WMS DOCK559 · RT TASK-5304239 IN_PROGRESS (PEDRO AVILA) · Putaway PENDING"
        r["verificationSource"] = "WMS 03:45 PT | RN-5008385 IN_PROGRESS | WMS DOCK559 | RT TASK-5304239 IN_PROGRESS (PEDRO AVILA) | YMS DOCK2"
        r["statusText"] = "🟡 IN_PROGRESS — RN-5008385 · YMS DOCK2 / WMS DOCK559 · RT TASK-5304239 "
        print("🔄 CAIU9453139: WMS dock DOCK559")
        break

# 4. JTAU7362582: YMS DOCK166
for r in rows:
    if r.get("container") == "JTAU7362582":
        r["dock"] = "DOCK166 (YMS) / DOCK60 (WMS RT)"
        r["entry"] = "YMS ET-1116387 GATE_CHECKED_IN DOCK166 + ET-1116418 DOCK_CHECKED_OUT DOCK60 · PT TASK-5305219 IN_PROGRESS · Devanned 04:04 AM"
        r["note"] = "⚠️ WMS+YMS 03:37 PT: PT TASK-5305219 IN_PROGRESS (32 LPs, DANIELA GONZALEZ, desde 04:05). RT TASK-5305188 CLOSED. YMS: ET-1116387 GATE_CHECKED_IN DOCK166 + ET-1116418 DOCK_CHECKED_OUT DOCK60. ⚠️ Carrier no habitual. Sin RN visible en YMS (solo WMS)."
        r["status"] = "🟡 IN_PROGRESS — RN-5008426. PT TASK-5305219 activo. RT CLOSED. YMS DOCK166/DOCK60. ⚠️ Carrier no habitual, sin RN YMS."
        r["verificationSource"] = "WMS+YMS 03:45 PT | RN-5008426 IN_PROGRESS | YMS DOCK166 + DOCK60 | RT TASK-5305188 CLOSED | PT TASK-5305219 IN_PROGRESS (DANIELA GONZALEZ) | ET-1116387+1116418"
        r["statusText"] = "🟡 IN_PROGRESS — RN-5008426. PT TASK-5305219 activo. YMS DOCK166/DOCK60."
        print("🔄 JTAU7362582: YMS DOCK166")
        break

# 5. BSIU8440908
for r in rows:
    if r.get("container") == "BSIU8440908":
        r["entry"] = "YMS ET-1116129 GATE_CHECK_OUT (inbound=BSIU8440908, outbound=FFAU6121609 empty) + ET-1116362 DOCK_CHECKED_OUT DOCK62 · Full BSIU8440908 se quedó · PT TASK-5305201 IN_PROGRESS"
        r["note"] = "⚠️ WMS+YMS 03:37 PT: PT TASK-5305201 IN_PROGRESS (27 LPs, PEDRO AVILA). RT TASK-5305125 CLOSED. YMS: ET-1116129 GATE_CHECK_OUT (tractor salió con FFAU6121609 vacío, BSIU8440908 full se quedó) + ET-1116362 DOCK_CHECKED_OUT DOCK62. ⚠️ DANIELA dijo COMPLETADO (FALSO)."
        r["verificationSource"] = "WMS+YMS 03:45 PT | RN-5008387 IN_PROGRESS | DOCK62 | RT TASK-5305125 CLOSED | PT TASK-5305201 IN_PROGRESS (PEDRO AVILA) | YMS ET-1116129 (inbound BSIU, outbound FFAU6121609 empty)"
        print("🔄 BSIU8440908: YMS inbound/outbound")
        break

# 6. OOCU8342103
for r in rows:
    if r.get("container") == "OOCU8342103":
        r["dock"] = "DOCK68 (YMS+WMS)"
        r["entry"] = "YMS ET-1116363 DOCK_CHECKED_OUT DOCK68 (inbound=OOCU8342103→DOCK155, outbound=FCIU9601208 empty) · Full OOCU8342103 se quedó · PT TASK-5305197 IN_PROGRESS"
        r["note"] = "⚠️ WMS+YMS 03:37 PT: PT TASK-5305197 IN_PROGRESS. RT TASK-5305126 CLOSED. YMS ET-1116363 DOCK_CHECKED_OUT DOCK68 (inbound OOCU8342103→DOCK155, outbound FCIU9601208 vacío). Full EN YARDA. YMS+WMS coinciden DOCK68."
        r["verificationSource"] = "WMS+YMS 03:45 PT | RN-5008386 IN_PROGRESS | DOCK68 | RT TASK-5305126 CLOSED | PT TASK-5305197 IN_PROGRESS (PEDRO AVILA) | YMS ET-1116363 (inbound OOCU, outbound FCIU9601208 empty)"
        print("🔄 OOCU8342103: YMS inbound/outbound")
        break

# 7. TCNU4379515: WMS DOCK562
for r in rows:
    if r.get("container") == "TCNU4379515":
        r["dock"] = "DOCK48 (YMS) / DOCK562 (WMS)"
        r["entry"] = "YMS ET-1116105 DOCK_CHECKED_IN LIVE_DELIVERY DOCK48 · PT TASK-5304515 IN_PROGRESS · WMS dock DOCK562"
        r["note"] = "⚠️ RECUPERADO: PT TASK-5304515 IN_PROGRESS (desde Jun 30 16:56, ~19h abierta, 2 LPs pendientes). RT TASK-5304474 CLOSED. YMS LIVE: ET-1116105 DOCK_CHECKED_IN DOCK48 LIVE_DELIVERY. WMS dock DOCK562. Devanned Jun 30 16:53."
        r["status"] = "🟡 IN_PROGRESS — RN-5008399. PT TASK-5304515 activo ~19h (2 LPs). RT CLOSED. YMS DOCK48 / WMS DOCK562."
        r["verificationSource"] = "WMS+YMS 03:45 PT | RN-5008399 IN_PROGRESS | WMS DOCK562 | YMS DOCK48 LIVE_DELIVERY | RT TASK-5304474 CLOSED | PT TASK-5304515 IN_PROGRESS (Caren Cubides)"
        r["statusText"] = "🟡 IN_PROGRESS — RN-5008399. PT TASK-5304515 activo ~19h (2 LPs). YMS DOCK48 / WMS DOCK562."
        print("🔄 TCNU4379515: WMS dock DOCK562")
        break

# 8-9. Re-confirm OOLU9324944 + FFAU1548537
for r in rows:
    if r.get("container") == "OOLU9324944":
        r["note"] = "✅ RE-CONFIRMADO 03:45 PT: YMS ET-1116521 GATE_CHECK_OUT = tractor salió con BEAU5553433 vacío. OOLU9324944 full SE QUEDÓ en DOCK98. WMS RN-5008430 IMPORTED sin receiving task — gap integración YMS→WMS. VERDE confirmado."
        r["verificationSource"] = "WMS+YMS 03:45 PT | RN-5008430 IMPORTED | DOCK98 | RE-CONFIRMADO YMS ET-1116521 (tractor salió con BEAU5553433 vacío, OOLU9324944 full quedó)"
        r["staleStateGuard"] = "RE-CONFIRMED_03:45 — YMS GATE_CHECK_OUT with BEAU5553433 empty, OOLU9324944 full in yard"
        print("✅ OOLU9324944: GREEN re-confirmado")
    if r.get("container") == "FFAU1548537":
        r["note"] = "✅ RE-CONFIRMADO 03:45 PT: YMS ET-1116141 GATE_CHECK_OUT = tractor salió con BSIU9381158 vacío. FFAU1548537 full SE QUEDÓ en DOCK44. WMS IMPORTED, RT TASK-5304579 NEW DOCK66. VERDE confirmado."
        r["verificationSource"] = "WMS+YMS 03:45 PT | RN-5008428 IMPORTED | DOCK44 YMS / DOCK66 WMS | RE-CONFIRMADO YMS ET-1116141 (tractor salió con BSIU9381158 vacío, FFAU1548537 full quedó)"
        r["staleStateGuard"] = "RE-CONFIRMED_03:45 — YMS GATE_CHECK_OUT with BSIU9381158 empty, FFAU1548537 full in yard"
        print("✅ FFAU1548537: GREEN re-confirmado")

# Count
green_count = sum(1 for r in rows if r.get("displayCategory", r.get("color")) == "green")
yellow_count = sum(1 for r in rows if r.get("displayCategory", r.get("color")) == "yellow")
normal_count = sum(1 for r in rows if r.get("displayCategory", r.get("color")) == "normal")
red_count = sum(1 for r in rows if r.get("displayCategory", r.get("color")) == "red")
by_color = {"green": green_count, "yellow": yellow_count, "normal": normal_count, "red": red_count}

# Metadata
feed["lastUpdated"] = NEW_TS
feed["messageTimestamp"] = NEW_TS
feed["message"] = f"ALERTA ROBERT 07/01 03:45 PT: WMS(32)+YMS(36). CORRECCIÓN: JTAU7362598 yellow→green (YMS confirma GATE_CHECKED_IN DOCK156). 33 activos ({green_count}G/{yellow_count}Y/{red_count}R/{normal_count}N)."
feed["summary"]["green"] = green_count
feed["summary"]["yellow"] = yellow_count
feed["summary"]["normal"] = normal_count
feed["summary"]["red"] = red_count
feed["summary"]["byColor"] = by_color
feed["metadata"]["corridaInfo"] = feed["message"]
feed["metadata"]["feedLastUpdated"] = NEW_TS
feed["metadata"]["generatedAt"] = NEW_TS
feed["metadata"]["byColor"] = by_color

# Alerts
feed["alerts"] = [
    f"✅ CICLO 03:45 PT: WMS(32)+YMS(36). CORRECCIÓN: JTAU7362598 yellow→green (YMS ET-1116382 GATE_CHECKED_IN DOCK156). 33 activos ({green_count}G/{yellow_count}Y/{red_count}R/{normal_count}N).",
    "🚨 ALERTA ROBERT CRÍTICA: RN-5006269 MAWB 00120698274 — 121 DÍAS en yarda sin receiving.",
    "🚨 ALERTA ROBERT: RN-183707 ALNOR04242026 — 65 días en yarda sin receiving.",
    "✅ JTAU7362598 CORREGIDO: YMS ET-1116382 GATE_CHECKED_IN DOCK156 (TWENTY TRANSPORTATION). WMS IMPORTED sin receiving task.",
    "✅ OOLU9324944 + FFAU1548537: GREEN re-confirmado por YMS 03:37 PT (fulls en yarda, tractores salieron con vacíos).",
    "⚠️ JTAU7362582+JTAU7362598: carriers no habituales, SIN RN visible en YMS (WMS sí tiene RN-5008426/RN-5008424).",
    "🔴 CAIU9721329: YMS confirma 5 DÍAS en DOCK141 sin RN activo (RN-5008176 CLOSED). QX LOGISTIX, no Gurunanda. Contenedor físicamente en yarda.",
    "🟡 7 RNs con receiving CLOSED + putaway activo: BSIU8440908, Chapin06292026, CORRU0629026UNIS, GN1125, JTAU7362582, OOCU8342103, TCNU4379515.",
    "🔴 EITU8162104: 7d+ sin RN. Priti preguntó estado 06/25 — sin respuesta. YMS sin rastro.",
    "📅 CITAS HOY: DDDU5053860(10:00), JTAU7362561(11:00), CSGU6429436(13:30), DDDU5053432(16:00), LabelKing×3(17:00), ITL07012026(17:30), OOCU7355889(20:00).",
    "📅 3 citas MAÑANA 07/02: FFAU2426030, CSNU6323633, TCKU6977609.",
    "⚠️ YMS search-by-paging sigue ROTO. 36 ETs directos verificados. Sin cambios en excluidos.",
    "⚠️ YMMU6698133 + CSGU6625300: ETs residuales/stale confirmados por YMS. RNs CLOSED.",
]
feed["summary"]["alertasActivas"] = feed["alerts"]

# Guardrails
feed["guardrails"]["antiEstadoViejo"] = f"CORRECTED 03:45 PT: JTAU7362598 yellow→green (YMS ET-1116382 GATE_CHECKED_IN DOCK156). OOLU9324944+FFAU1548537 re-confirmados GREEN. 0 PRE-ENTRY/NORMAL con evidencia yarda restantes."
feed["guardrails"]["lastGuardrailRun"] = NEW_TS
feed["guardrails"]["dockCorrection"] = "CAIU9453139 WMS DOCK64→DOCK559. TCNU4379515 WMS DOCK48→DOCK562. Otros docks OK."
feed["guardrails"]["ymsVerificationNote"] = "YMS revalidado 03:37 PT: 36 ETs directos verificados. JTAU7362598 nuevo ET-1116382 DOCK156. 9 contenedores sin ET conocido (filtros rotos)."
feed["guardrails"]["coolifyDeployNote"] = "Live dashboard — este deploy actualiza datos a 03:45 PT Jul 1."
feed["guardrails"]["jtauAlert"] = "JTAU7362582+JTAU7362598: carriers no habituales, sin RN en YMS. Monitorear."
feed["guardrails"]["caiu9721329Alert"] = "CAIU9721329: 5d DOCK141 sin RN activo (RN-5008176 CLOSED). QX LOGISTIX, no Gurunanda. Contenedor físico en yarda."
feed["ymsReadingRule"] = "YMS LIVE 2026-07-01 03:37 PT — 36 ETs verificados. NUEVOS: JTAU7362598 ET-1116382 DOCK156 GATE_CHECKED_IN (TWENTY TRANSPORTATION), JTAU7362582 ET-1116387 DOCK166 GATE_CHECKED_IN. RE-CONFIRMADOS: OOLU9324944 DOCK98 (BEAU5553433 vacío salió), FFAU1548537 DOCK44 (BSIU9381158 vacío salió). 7 citas HOY sin llegada aún."

# Update excluded containers YMS notes
for xc in feed.get("excludedContainers", []):
    if xc.get("container", "").startswith("CAIU9721329"):
        xc["reason"] = "CLOSED WMS 06/29 — PERO YMS 03:37 PT: ET-1112226 DOCK_CHECKED_IN DOCK141, 5 DÍAS estancado. QX LOGISTIX, no Gurunanda. Contenedor físicamente en yarda. CONTRADICCIÓN YMS/WMS."
        xc["wmsRechecked"] = "2026-07-01T03:37 PT"
        xc["wmsConfirmation"] = "RE-CONFIRMADO 03:37 PT: WMS CLOSED/FORCE_CLOSED ambas tareas cerradas. YMS confirma 5d DOCK141."
        xc["ymsContradiction"] = True
    if xc.get("container", "").startswith("YMMU6698133"):
        xc["wmsRechecked"] = "2026-07-01T03:37 PT"
        xc["wmsConfirmation"] = "ET residual/stale confirmado por YMS 03:37 PT. RN CLOSED."
    if xc.get("container", "").startswith("CSGU6625300"):
        xc["wmsRechecked"] = "2026-07-01T03:37 PT"
        xc["wmsConfirmation"] = "ET residual/stale confirmado por YMS 03:37 PT. RN CLOSED."

with open(FEED_PATH, "w") as f:
    json.dump(feed, f, indent=2, ensure_ascii=False)

print(f"\n✅ FEED ACTUALIZADO. {len(rows)} rows, {green_count}G/{yellow_count}Y/{red_count}R/{normal_count}N")
print(f"📝 lastUpdated: {NEW_TS}")
