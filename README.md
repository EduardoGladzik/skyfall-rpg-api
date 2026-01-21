# Skyfall RPG API

This API is designed to query various elements of the Brazilian TTRPG, *Skyfall*. Initially, it will handle only Abilities, Spells, and Descriptors.

---

## Core Concepts

* **BaseAbility:** Base class for abilities and spells; it contains all the basic properties of an ability.
* **Abilities:** Currently, this class inherits directly from BaseAbility without additional properties.
* **Spells:** Inherits from BaseAbility, adding specific properties relevant to magic mechanics.
* **Descriptors:** These function as "tags" used within the RPG system to convey specific information to the player.
* **Modifications:** Add-ons for abilities and spells that modify specific properties.
* **ModificationTypes:** Represents the specific types associated with a modification (a single modification can have multiple types).

--- 

## Current Project State

* **Backend:** Currently fully functional, with the database being populated.
* **Frontend:** Currently under development.

*Once the project is finished, you will be able to filter Abilities and Spells by name, PE cost, level, type, and many other options.*

---

## Future Implementations
- Classes
- Legacies
- Paths