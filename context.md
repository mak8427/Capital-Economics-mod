# Pantalone_Economics mod context

## Overview

This is a Europa Universalis V mod focused on foreign corporate extraction, new religious content (Pantalonism), and a
scripted situation that tracks the rise of Pantalonism. It adds diplomacy relations, building types, production methods,
scripted effects, events, UI for a custom situation panel, and localization plus icons.

## Top-level layout

- `in_game/`: gameplay scripts (events, common data, GUI).
- `main_menu/`: localization, modifier definitions, and interface icons.
- `Mangiatoia.dds`, `pantalonism.dds`: icon assets at the root.
- `main.py`: sample PyCharm script (not used by the mod).

## Core mechanics

- Pantalonism religion: `in_game/common/religions/cap_econ_christian.txt` defines a new Christian-group religion with
  estate power and economic modifiers.
- Pantalone relations: scripted diplomacy relations for sending a Pantalone and granting extraction rights in
  `in_game/common/scripted_relations/cap_pantalone.txt` and
  `in_game/common/scripted_relations/cap_econ_extraction_rights.txt`.
- Rise of Pantalonism situation: `in_game/common/situations/CapEcon_pantalonism.txt` defines a global situation
  targeting one country, tracking Pantalonist population share and Mangiatoia pressure, and updating monthly.
- Situation UI: `in_game/gui/panels/situation/rise_of_pantalonism.gui` adds a custom panel showing target country,
  progress bars, and pie chart.
- Events and monthly pulse:
    - `in_game/common/on_action/cap_econ_country_monthly.txt` runs a monthly pulse for eligible countries, firing
      CapEcon events and estate income fixes.
    - `in_game/events/CapEcon_events.txt` and `in_game/events/religion/CapEcon_pantalonism.txt` add country events tied
      to the relations and religion.
    - `in_game/events/estate_income_fix.txt` adds hidden events that compensate estates for control shortfalls and
      manage estate gold.
- Scripted effects/triggers:
    - `in_game/common/scripted_effects/CapEcon_scripted_effects.txt` provides effects like converting pops to
      Pantalonism and destroying Mangiatoia buildings.
    - `in_game/common/scripted_triggers/CapEcon_triggers.txt` defines helper triggers for location rank checks.
- Buildings and production methods:
    - `in_game/common/building_types/CapEcon_foreign_extraction_buildings.txt` defines many foreign-owned extraction
      buildings gated by extraction rights.
    - `in_game/common/building_types/CapEcon_foreign_burgers_buildings.txt` adds corporate HQ buildings that boost caps
      and local effects.
    - `in_game/common/building_types/CaPEcon_foreign_uniques.txt` defines the Mangiatoia building (not player-buildable,
      tied to the situation).
    - `in_game/common/production_methods/CapEcon_foreign_extraction_methods.txt` provides maintenance/output methods for
      the corporate buildings.
- Caps and ranks:
    - `in_game/common/script_values/CapEcon_building_caps.txt` defines scripted caps for corporate extraction and HQ max
      levels.
    - `in_game/common/location_ranks/CapEcon_location_ranks.txt` replaces town/city rank modifiers and requirements.

## UI, localization, and icons

- Localization: `main_menu/localization/english/` includes text for buildings, events, diplomacy, modifiers, interfaces,
  and religions.
- Modifiers: `main_menu/common/modifier_type_definitions/CapEcon_modifier_types.txt`,
  `main_menu/common/modifier_icons/CapEcon_modifier_icons.txt`, and
  `main_menu/common/static_modifiers/CapEcon_static_modifiers.txt`.
- Icons: `main_menu/gfx/interface/icons/buildings/` and `main_menu/gfx/interface/icons/religion/` include DDS icons for
  corporate buildings and Pantalonism.

## Notes

- `in_game/common/script_values/CapEcon_scripted_values.txt` is currently empty (only a BOM).
- `main.py` appears to be a template file and not used by the mod scripts.

## Reference game files

There is a full base-game reference tree at `../GAME_FILES/` (relative to this mod root). It is useful for checking
vanilla definitions, GUI patterns, and localization.

Top-level structure in `../GAME_FILES/`:

- `in_game/`: base game scripting content (common data, events, GUI, map data, setup).
- `main_menu/`: base menu assets, GUI, localization, and modifier definitions.
- `mod/`: core game assets/config (fonts, gfx, gui, localization, settings, sound, etc.).
- `dlc/`: DLC content packs (shared + packs with gfx and localization).
- `loading_screen/`: loading screen assets and fonts.
