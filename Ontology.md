# Game Recommendation Ontology

## Purpose

This document defines the primary concepts, entities, attributes, and relationships used by the AI Game Recommender project.

The ontology describes what the recommendation system is reasoning about. It is intentionally separate from the implementation so that the underlying concepts remain consistent even if the representation or recommendation model changes.

---

## Core Concepts

### User

A person whose gameplay history is used to generate recommendations.

A user has:

* A gameplay history
* Preferences inferred from that history
* Potentially explicit preferences
* Recommended games

---

### Game

A game that may either appear in the user's gameplay history or be considered as a recommendation.

A game may have:

* Title
* Genre
* Tags
* Platform
* Release year
* Price
* Multiplayer status
* Download count
* Installation status

---

### Gameplay History

A collection of games and information describing the user's interaction with those games.

Gameplay history may include:

* Game played
* Playtime
* Installation status
* Other available information about the user's interaction with the game

Gameplay history is the primary source of information used to infer a user's preferences.

---

### Game Preference

A characteristic of games that appears to be relevant to a user's choices.

Potential preference dimensions include:

* Genre
* Tags
* Platform
* Playtime patterns
* Price
* Multiplayer preference
* Other game attributes

Preferences may be inferred from the user's gameplay history rather than explicitly provided by the user.

---

### Game Corpus

The collection of candidate games against which a user's gameplay history is compared.

The corpus is expected to contain game metadata from a limited number of game store platforms.

---

### Feature

A measurable or representable property of a game or gameplay history.

Examples include:

```text
price = 19.99
playtime = 250 hours
genre = FPS
platform = PC
multiplayer = true
```

Categorical features may need to be encoded into numerical representations before being used by the recommendation model.

---

### Representation

A numerical representation of a game, gameplay history, or preference.

Possible representations include:

* Encoded categorical features
* Feature vectors
* Embeddings

The project will investigate which representation best captures useful relationships between games.

---

### Recommendation

A candidate game selected because its representation has a high degree of similarity to the representation of the user's gameplay history.

Recommendations are generated from the candidate game corpus.

---

### Recommendation Score

A numerical value representing the model's assessment of how closely a candidate game matches the user's represented preferences.

Games can be ranked according to their recommendation scores.

---

The recommendation process can be represented as:

```text
User
 |
 | gameplay history
 v
Gameplay History
 |
 | represented as
 v
User Representation
 |
 | compared with
 v
Game Representations
 |
 | produces
 v
Similarity / Recommendation Scores
 |
 | ranked into
 v
Recommendations
```

The candidate games can then be sorted according to their scores.

---

## Game Attributes

| Attribute           | Description                               | Type                       |
| ------------------- | ----------------------------------------- | -------------------------- |
| Title               | Name of the game                          | Text                       |
| Playtime            | Amount of time played                     | Numerical                  |
| Genre               | Game genre                                | Categorical                |
| Platform            | Platform the game is available on         | Categorical                |
| Tags                | Descriptive tags associated with the game | Categorical / Multi-valued |
| Release Year        | Year the game was released                | Numerical                  |
| Price               | Game price                                | Numerical                  |
| Multiplayer         | Whether the game supports multiplayer     | Boolean / Categorical      |
| Download Count      | Number of downloads                       | Numerical                  |
| Installation Status | Whether the game is installed             | Boolean / Categorical      |

---

## User-Level Information

The recommendation system primarily derives user preferences from gameplay history.

For example:

```text
User History
├── Counter-Strike 2
│   └── High playtime
├── Rainbow Six Siege
│   └── High playtime
└── Valorant
    └── High playtime
```

This history may produce a representation containing stronger associations with characteristics such as:

```text
Competitive
FPS
Multiplayer
PC
```

These inferred characteristics can then be compared with candidate games.

---

### Query

The user's complete game-playing history.

### Corpus

The collection of games available in the selected game store dataset, including relevant metadata such as:

* Price
* Tags
* Genre
* Download count
* Platform

### Model

The project will investigate vector representations and similarity methods.

### Results

The top results are the games with the highest calculated recommendation scores.

