<!-- Maintainer Note:
- Purpose: context.md documents the mod architecture, ownership boundaries, and maintenance workflow for Pantalone_Economics.
- Reasoning: this file is the onboarding map for new maintainers so they can change mechanics safely without breaking cross-file links.
- Maintenance: update this file whenever a system is added, removed, renamed, or moved to a different script domain.
-->

# Pantalone_Economics Maintainer Context

## What this mod adds

Pantalone_Economics is a gameplay-heavy EU5 mod centered on four connected systems:

1. Pantalonism religion content and conversion pressure.
2. Corporate foreign extraction buildings and ownership logic.
3. International-company subject gameplay with custom government naming.
4. A Pantalonist international organization with custom law/parliament GUI.

The core design principle is: **economic expansion drives religious and political pressure, and those pressures feed back into state organization and subject behavior**.

## Repository layout

- `in_game/`: gameplay scripts (common definitions, event logic, and in-game GUI).
- `main_menu/`: localization, modifier metadata, and icon assets used by UI/game concepts.
- `docs/comment_coverage.md`: sidecar manifest proving every tracked file is documented.
- root `.dds` files: legacy/source texture assets kept for compatibility.

## System map by folder

### `in_game/common/`

- `advances/`: unlock gates for units/tech-driven content.
- `building_types/`: all custom corporate and Mangiatoia building definitions.
- `cabinet_actions/`: scripted population movement actions.
- `generic_actions/`: clickable/global action logic (including Pantalonism actions).
- `gods/`, `religions/`, `religious_aspects/`: religion package definitions.
- `government_reforms/`, `government_types/`: reform and government identity rules.
- `international_organizations/`, `laws/`, `parliament_types/`, `international_organization_payments/`: IO governance stack.
- `on_action/`: periodic hooks that trigger mod behavior.
- `prices/`, `script_values/`, `static_modifiers/`: balancing constants and computed values.
- `scripted_effects/`, `scripted_triggers/`, `scripted_relations/`: reusable script API.
- `situations/`: long-running state machine for Rise of Pantalonism.
- `subject_types/`: `international_company` lifecycle and behavior.
- `production_methods/`, `unit_types/`, `levies/`, `location_ranks/`: content support and scaling.

### `in_game/events/`

- `CapEcon_*_events.txt`: event chains for economy, politics, corporate behavior, and situation spikes.
- `CapEcon_situation_events.txt`: high-impact branch events tied to the situation progress model.

### `in_game/gui/`

- `panels/situation/rise_of_pantalonism.gui`: custom situation panel.
- `panels/organization/cap_econ_pantalonist_io.gui`: custom organization panel.

### `main_menu/common/`

- `modifier_type_definitions/`, `modifier_icons/`, `static_modifiers/`, `script_values/`: UI/meta definitions for presenting custom effects.

### `main_menu/gui/`

- Use uniquely named mod files such as `CapEcon_*.txt` or `CapEcon_*.gui` when extending shared GUI registries.
- Do **not** create mod files with the exact vanilla filename for global registries like `messagetypes.txt` unless you intentionally mean to override the whole file.
- In practice: custom message type additions belong in `main_menu/gui/CapEcon_messagetypes.txt`, not `main_menu/gui/messagetypes.txt`.

### `main_menu/localization/english/`

- One file family per domain: buildings, events, diplomacy, reforms, subjects, religion, interfaces, units, modifiers, etc.
- Rule: every scripted key added in `in_game/` must be localized here in the same change.

### `main_menu/gfx/interface/`

- `icons/buildings/`: building icons for all corporate and Mangiatoia assets.
- `icons/religion/`: religion icon assets.
- `advance/`: advance icon assets.

## Critical cross-file dependencies

- Building ids in `in_game/common/building_types/*.txt` must match:
  - production methods in `in_game/common/production_methods/*.txt`
  - localization keys in `main_menu/localization/english/CapEcon_buildings_l_english.yml`
  - icon filenames in `main_menu/gfx/interface/icons/buildings/`

- Subject/government behavior spans:
  - `in_game/common/subject_types/international_company.txt`
  - `in_game/common/government_types/CapEcon_company_government_type.txt`
  - `in_game/common/government_reforms/CapEcon_reforms.txt`
  - `main_menu/localization/english/CapEcon_government_names_l_english.yml`

- Situation logic spans:
  - `in_game/common/situations/CapEcon_pantalonism.txt`
  - `in_game/events/CapEcon_situation_events.txt`
  - `in_game/common/generic_actions/CapEcon_pantalonism_actions.txt`
  - `in_game/gui/panels/situation/rise_of_pantalonism.gui`

- IO law behavior spans:
  - `in_game/common/international_organizations/CapEcon_pantalonist_io.txt`
  - `in_game/common/laws/CapEcon_pantalonist_io_laws.txt`
  - `in_game/common/parliament_types/CapEcon_pantalonist_io_parliament_types.txt`
  - `in_game/gui/panels/organization/cap_econ_pantalonist_io.gui`

## Maintainer workflow

When changing mechanics, follow this order:

1. Update the source logic file (`in_game/common` or `in_game/events`).
2. Update dependent script references (effects, relations, scripted values, GUI bindings).
3. Update localization and icon references.
4. For GUI registry extensions, verify the mod file uses a unique prefixed filename instead of a vanilla exact-name override.
5. Update `docs/comment_coverage.md` if file set changed.
6. Re-run in-game error log checks (scope errors, undefined keys, missing localization).

## Commenting standard used in this repo

- Every text/script file contains a top `Maintainer Note` that explains purpose, reasoning, and maintenance constraints.
- Complex logic sections (loops, multi-branch scope logic, side-effect-heavy blocks) include inline comments to explain intent.
- Binary files (`.dds`) are documented through the sidecar manifest `docs/comment_coverage.md`.

## Reference vanilla tree

- Base reference content lives in `../GAME_FILES/`.
- Use it to confirm vanilla patterns for scope usage, subject behavior, law structure, and localization naming conventions.
