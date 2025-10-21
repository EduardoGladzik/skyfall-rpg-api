# Skyfall RPG API

This is an API designed to manage various elements for the Brazilian TTRPG, *Skyfall*. Initially, it will handle Abilities, Spells, and Descriptors.

---

## Core Concepts

* **Ability:** This is the main class representing general abilities within the game.
* **Spell:** This class **inherits from** Ability, adding specific properties relevant to magic.
* **Descriptor:** These function like "tags" used in the RPG system to convey specific information to the player. In this API, Descriptors will be used to link Abilities and Spells to Legacies, Classes, and Trails, which are planned for future implementation.

When the project is finished, you will be able to filter Abilities and Spells by name, PE cost, level, type, and many other options.

---

## Current Features

The system is currently capable of:

* **GET:** Fetching all 'Ability' and 'Spell' objects, with data returned from their respective serializers.
* **POST:** Creating 'Ability', 'Spell', and 'Descriptor' objects, correctly differentiating between them.
* **DELETE:** Deleting any object.

---

## Work in Progress (Broken Features)

The following functionalities are implemented but are not yet working correctly:

* **GET (by ID):** Fetching a single 'Ability', 'Spell', or 'Descriptor' object via its URL (e.g., `/habilidade:<name>`).
* **PUT:** Correctly updating 'Ability' and 'Spell' objects while differentiating between their types.

---

**Given that Skyfall's main audience is Brazilian, some user-facing strings in the project are written in Brazilian Portuguese.**