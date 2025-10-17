# Skyfall RPG API Structure

This is an API designed to manage all sorts of things for the Skyfall RPG. Initially, i will only create an 'Ability' class, but in the future, there will be equipment, items, spells, and everything else.

The structure of the 'Ability' will look something like this:

## Ability Class
### Attributes of an Ability
*Note: Initially it were meant to be a 'skyfall spells api', but i found out mid way that spells are considered abilities in the system. The attributes marked with an 'X' before it will be inherited by the 'Spells' class when i create it.*

- **`Fonte`**: (String) For now, all will be from the `'Livro Básico'`, but in the future, it will be important to differentiate the sources.
- **`Execution`**: (Enum) The type of action required to use the ability.
  - `Action`
  - `Bonus Action`
  - `Reaction`
  - `Free Action`
  - `More than one action`
- **`Name`**: (String) The name of the ability.
x **`Type`**: (Enum) The functional category of a spell.
  - `Control`
  - `Offensive`
  - `Utility`
x **`Tier`**: (Enum) The power level of a spell.
  - `Cantrip`
  - `Superficial`
  - `Shallow`
  - `Deep`
- **`Cost`**: (String) The resource cost to use the ability. May contain a `'repeatable'` marker.
- **`Descriptors`**: (Array of Strings) Keywords or tags associated with the ability (e.g., `'Fire'`, `'Teleportation'`, `'Attack'`).
- **`Description`**: (String) The general, narrative description of the ability.
- **`Properties`**: (Object) Mechanical details of how the ability functions.
  - **`Range`**: (Enum) The range and area of effect.
    - `Cone` / `Cylinder` / `Cube` / `Sphere` / `Line` / `Touch` / `Self`
  - **`Target`**: (String) Specifies the target(s) of the ability (e.g., `'1 creature'`, `'a point you can see'`).
  - **`Duration`**: (Enum) How long the ability's effects last.
    - `Instantaneous` / `Concentration`
  x **`Components`**: (Array of Strings) The components required to use a spell.
    - `Verbal (V)`
    - `Somatic (S)`
    - `Material (M)`
  - **`Attack`**: (String, Nullable) The formula or type of attack roll. This field only appears if `Descriptors` include `'Attack'`.
  - **`Trigger`**: (String, Nullable) The specific condition that allows this ability to be used. This field only appears if `Execution` is `'Reaction'`.
- **`Effects`**: (Object) Describes the results of using the ability.
  - **`OnHit`**: (String, Nullable) The effect on a successful attack. This field only appears if `Descriptors` include `'Attack'`.
  - **`OnMiss`**: (String, Nullable) The effect on a failed attack. This field also only appears if `Descriptors` include `'Attack'`.
  - **`Effect`**: (String) The primary, guaranteed effect of the ability.
  - **`Special`**: (String, Nullable) Any additional or special effects not covered above.
- **`Modifications`**: (Array of Objects) A list of optional ways to alter the ability, often by increasing its cost.
  - **`Cost`**: (String) The additional cost for applying this modification.
  - **`Type`**: (Enum) The nature of the modification.
    - `Change` / `Add` / `Remove` / `Amplify`
  - **`Description`**: (String) A description of what this modification does.

---
*This structure is based on the Brazilian TTRPG Skyfall.*