# Skyfall RPG API Structure

This is an API designed to manage all sorts of things for the Skyfall RPG. Initially, i will only create an 'Ability' class, but in the future, there will be equipment, items, spells, and everything else.

The structure of the 'Ability' will look something like this:

## Ability Class
### Attributes of an Ability
*Note: Initially it were meant to be a 'skyfall spells api', but i found out mid way that spells are considered abilities in the system. The attributes marked with an 'X' before it will be inherited by the 'Spells' class when i create it.*

- **`Fonte`**: (String) For now, all will be from the `'Livro Básico'`, but in the future, it will be important to differentiate the sources.
- **`Execução`**: (Enum) The type of action required to use the ability.
  - `Ação`
  - `Ação Bônus`
  - `Reação`
  - `Ação Livre`
  - `Mains de uma ação`
- **`Nome`**: (String) The name of the ability.
x **`Tipo`**: (Enum) The functional category of a spell.
  - `Controle`
  - `Ofensivo`
  - `Utilitário`
x **`Camada`**: (Enum) The power level of a spell.
  - `Truque`
  - `Superficial`
  - `Rasa`
  - `Profunda`
- **`Custo`**: (String) The resource cost to use the ability. May contain a `'Repetível'` marker.
  - **`Descritores`**: (Array of Strings) Keywords or tags associated with the ability (e.g., `'Ígneo'`, `'Magia'`, `'Ataque'`)
- **`Descrição`**: (String) The general, narrative description of the ability.
- **`Propriedades`**: (Object) Mechanical details of how the ability functions.
  - **`Alcance`**: (Enum) The range and area of effect.
    - `Cone` / `Cilíndro` / `Cubo` / `Esfera` / `Linha` / `Toque` / `Pessoal`
  - **`Alvo`**: (String) Specifies the target(s) of the ability (e.g., `'1 criatura'`, `'um ponto que você pode ver'`).
  - **`Duração`**: (Enum) How long the ability's effects last.
    - `Instântaneo` / `Concentração`
  x **`Componentes`**: (Array of Strings) The components required to use a spell.
    - `Verbal (V)`
    - `Somático (S)`
    - `Material (M)`
  - **`Ataque`**: (String, Nullable) The formula or type of attack roll. This field only appears if `Descritores` include `'Ataque'`.
  - **`Gatilho`**: (String, Nullable) The specific condition that allows this ability to be used. This field only appears if `Execução` is `'Reação'`.
- **`Efeitos`**: (Object) Describes the results of using the ability.
  - **`Acerto`**: (String, Nullable) The effect on a successful attack. This field only appears if `Descritores` include `'Ataque'`.
  - **`Erro`**: (String, Nullable) The effect on a failed attack. This field also only appears if `Descritores` include `'Ataque'`.
  - **`Efeito`**: (String) The primary, guaranteed effect of the ability.
  - **`Especial`**: (String, Nullable) Any additional or special effects not covered above.
- **`Modificadores`**: (Array of Objects) A list of optional ways to alter the ability, often by increasing its cost.
  - **`Custo`**: (String) The additional cost for applying this modification.
  - **`Tipo`**: (Enum) The nature of the modification.
    - `Muda` / `Adiciona` / `Remove` / `Amplificar`
  - **`Descrição`**: (String) A description of what this modification does.

---
*The structure is in pt-br because the majority of customers of Skyfall are brazilian.*