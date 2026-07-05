# CORRIDA REPORT — Jul 4 19:15 PT
## Agente Priti Contenedores en Yarda para Rufino

---

### 📊 RESUMEN

| Métrica | Valor |
|----------|-------|
| **Hora corrida** | Jul 4 19:15 PT |
| **Activos totales** | **26** (6🟢 + 7🟡 + 13📅) |
| **Nuevos agregados** | 1 (EITU8162104) |
| **Removidos** | 0 |
| **Entry List confirmados** | 5 (CSGU6429436, DDDU5053860, TCKU6977609, OOCU5501937, TGBU3785090) |
| **YMS gate-in confirmados** | 6 (+ MATU2656138) |
| **Falsos green corregidos** | 0 nuevos (3 ya corregidos en corridas anteriores) |
| **Excluidos totales** | 26 |

---

### 🔍 REVISIÓN COMPLETA

#### Outlook
- ✅ 2 correos NO LEÍDOS de Priti: MATU2656138 (cita Jul 3) y OOCU7355889 — ambos ya procesados
- ✅ 4 correos Jonathan Heredia (Jul 4 04:46): Receiving Progress + Empty Containers 07/03
- ✅ 14 contenedores de listas "EMPTY" verificados WMS — TODOS CLOSED/FORCE_CLOSED
- ✅ EITU8162104 detectado en correo Priti Jun 25 — SIN RN en WMS → AGREGADO a PRE-ENTRY

#### WMS (Entry List + Tasks)
- 5/26 contenedores con Entry List CONFIRMED (containerNOs reales)
- 3/26 Entry List NO DATA pero con trailer (no container)
- 18/26 Entry List NO DATA (sin evidencia física)
- 8 receiving tasks NEW, 7 IN_PROGRESS, 0 CLOSED (nuevos)
- 0 nuevos con ambos tasks cerrados → 0 removidos esta corrida

#### YMS
- 6/26 con gate-in + matching equipment confirmado
- 2/26 con evidencia débil (N/A fields o LIVE_DELIVERY completed)
- 18/26 sin evidencia YMS (search-by-paging no filtra)

---

### 🟢 EN YARDA (6) — Verificación Rufino Rule

| Contenedor | Entry List | YMS Gate-in | Rufino Rule | Estado |
|-----------|-----------|-------------|-------------|--------|
| **TGBU3785090** | ✅ YES | ✅ TGBU3785090 | PASSA | 🟢 GREEN |
| **MATU2656138** | ❌ NO DATA | ✅ MATU2656130 | PASSA (YMS) | 🟢 GREEN ⚠️ SIN SPOT |
| **LabelKing PO8423** | ❌ NO DATA | ❌ LIVE_DELIVERY done | Excepción LIVE | 🟢 GREEN ⚠️ |
| **MAWB 00120698274** | ❌ NO DATA | ❌ No record | Historical 124d | 🟢 GREEN 🚨 |
| **ALNOR04242026** | ❌ NO DATA | ❌ No record | Historical 68d | 🟢 GREEN 🚨 |
| **LabelKing PO8449** | ❌ NO DATA | ⚠️ All N/A | Débil | 🟢 GREEN ⚠️ |

---

### 🟡 EN PROCESO (7)

| Contenedor | Recv Task | Putaway | Entry List | YMS Equip |
|-----------|----------|---------|-----------|----------|
| JTAU7362561 | IN_PROGRESS | — | ❌ | ❌ |
| CSGU6429436 | IN_PROGRESS | — | ✅ | ✅ |
| GN07012026UNIS-1130 | IN_PROGRESS | — | ❌ | ❌ |
| DDDU5053860 | IN_PROGRESS | — | ✅ | ✅ |
| TCKU6977609 | IN_PROGRESS | — | ✅ | ✅ |
| OOCU5501937 | IN_PROGRESS | — | ✅ | ✅ |
| GN07012026UNIS-1132 | CLOSED | IN_PROGRESS | ❌ | ❌ |

---

### 📅 PRE-ENTRY (13, incl. nuevo EITU8162104)
- 11 contenedores con RN IMPORTED sin evidencia física
- 3 falsos green mantenidos en PRE-ENTRY (CBHU7024789, FFAU2426030, CSNU6323633)
- 1 TRANSFER (DN-3236621)
- 1 NUEVO sin RN (EITU8162104)

---

### 🚨 ALERTAS ROLAS

1. **🚨 CRÍTICA: Dashboard/feed live STALE** — El feed en vivo (https://contenedores-priti-dashboard-03b000.coolify.item.pub/container-feed.json) muestra lastUpdated 2026-07-04T10:17:00-07:00 (~9h stale). Los cambios están en GitHub (main + master) pero Coolify NO ha desplegado. Posiblemente mismo problema de "no available server" reportado Jul 2-3.

2. **🚨 CRÍTICA: MATU2656138** — 44h+ en yarda SIN SPOT. YMS gate-in Jul 2 20:11 confirmado pero sin ubicación. Cita Jul 3 VENCIDA.

3. **🚨 CRÍTICA: RN-5006269 (124d) + RN-183707 (68d)** — Posiblemente abandonados. Sin evidencia YMS/Entry List.

4. **🚨 CSGU6429436** — Recv IN_PROGRESS 3d+. Jonathan reportó EMPTY 07/02. Entry List CONFIRMED. Verificar DOCK68 físicamente.

5. **⚠️ JTAU7362561** — Entry List NO DATA, YMS sin equipment. LIVE_DELIVERY sin evidencia física.

6. **⚠️ LabelKing PO8423** — LIVE_DELIVERY completado (trailer salió Jul 1). Recv NEW 3d sin iniciar.

7. **⚠️ EITU8162104** — NUEVO. Correo Priti Jun 25, SIN RN en WMS.

8. **⚠️ LabelKing PO8449** — YMS WINDOW_CHECKED_IN con todos los campos N/A.

---

### 📦 REPO STATUS
- ✅ `main` branch: commit 7a23dfc (3 commits ahead of live)
- ✅ `master` branch: synced with main
- ✅ `container-feed.json` actualizado correctamente con 26 rows
- ❌ Live feed sigue stale (10:17 PT) — Coolify no despliega

---

### 🔧 PENDIENTE
- Coolify deployment necesita intervención manual o esperar recuperación
- Verificar físicamente DOCK68 (CSGU6429436)
- Asignar spot a MATU2656138
- Investigar EITU8162104 (sin RN)
