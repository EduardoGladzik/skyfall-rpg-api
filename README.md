# Skyfall RPG API

This is an API designed to consult various elements of the Brazilian TTRPG, *Skyfall*. Initially, it will handle only Abilities, Spells, and Descriptors.

---

## Core Concepts

* **Ability:** This is the main class representing general abilities within the game.
* **Spell:** This class **inherits from** Ability, adding specific properties relevant to magic.
* **Descriptor:** These function like "tags" used in the RPG system to convey specific information to the player. In this API, Descriptors will be used to link Abilities and Spells to Legacies, Classes, and Trails, which are planned for future implementation.

When the project is finished, you will be able to filter Abilities and Spells by name, PE cost, level, type, and many other options.

---

## Current Features

The system is currently capable of:

* **GET:** Fetching all 'Ability', 'Spell' and 'Descriptor' objects, with data returned from their respective serializers.
* **GET (by NAME):** Fetching a single 'Ability', 'Spell', or 'Descriptor' object via its URL (`api/object:<name>`).

---

## Testing purposes functionalities

The following functionalities are implemented only for testing purposes and will be soon removed:
* **PUT:** Correctly updating 'Ability' and 'Spell' objects while differentiating between their types.
* **POST:** Creating 'Ability', 'Spell', and 'Descriptor' objects, correctly differentiating between them.
* **DELETE:** Deleting any object.

---

**Given that Skyfall's main audience is Brazilian, some user-facing strings in the project are written in Brazilian Portuguese.**