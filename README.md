# AI Game Recommender

An AI-based game recommendation system that recommends a game to a user based on their game-playing history and preferences.

## Overview

The goal of this project is to build a model that can analyze a user's gameplay history, identify patterns in their game preferences, and recommend a game that best fits those preferences.

Given a user's history of games they have played, the system compares that history against a collection of available games and produces a ranked set of recommendations.

The initial project scope will be limited to a few game store platforms so that the dataset remains manageable while still providing enough games and metadata for meaningful recommendations.

## Problem Statement

Given a user's gameplay history, the model should describe the user's preferences and identify games that are a good fit for those preferences.

For example, if a user has played:

* Counter-Strike 2
* Rainbow Six Siege
* Valorant

with relatively high playtime, the system might identify preferences for competitive, multiplayer FPS games and recommend another game with similar characteristics.

## System Overview

```text
User Gameplay History
        |
        v
+-----------------------+
| Feature Representation|
+-----------------------+
        |
        v
+-----------------------+
| Preference / Embedding |
|       Model            |
+-----------------------+
        |
        v
Compare Against Game Corpus
        |
        v
+-----------------------+
| Recommendation Scores |
+-----------------------+
        |
        v
Rank Games
        |
        v
Top Recommendations
```

## Input

The primary input is the user's game-playing history.

Potential game attributes include:

* Playtime
* Genre
* Platform
* Tags
* Release year
* Price
* Single-player / multiplayer
* Number of downloads
* Installed / uninstalled status

The system may also incorporate additional attributes as the project develops.

## Representation

Many of the game's attributes are categorical rather than numerical. These attributes need to be converted into numerical representations before they can be compared by the model.

Potential representations include:

* Encoded categorical features
* Numerical game metadata
* Vector embeddings
* Other feature representations explored during experimentation

The project will investigate which representation produces useful similarity between a user's gameplay history and candidate games.

## Recommendation Model

The basic recommendation process is:

1. Collect the user's gameplay history.
2. Represent the user's history as a feature vector or embedding.
3. Represent each candidate game using the same or a compatible representation.
4. Compare the user's history against each candidate game.
5. Assign a recommendation/similarity score to each game.
6. Rank the candidate games.
7. Return the highest-ranking recommendations.

## Dataset

The project will use two main sources of information:

### User Data

Information about the user's own gameplay history, such as:

* Games played
* Playtime
* Potentially other information available from the user's game history

### Game Corpus

A collection of games from selected game store platforms containing information such as:

* Genre
* Tags
* Platform
* Price
* Release year
* Download count
* Multiplayer information

The project will initially focus on a limited number of game store platforms to keep the scope manageable.

## Evaluation

The project will evaluate recommendation quality using accuracy, precision, and recall.

A recommendation can be considered correct when its similarity to the expected result exceeds a defined threshold.

### Accuracy

The proportion of recommendations that are considered correct compared with the user's expected results.

### Precision

For recommendations made for a particular game or preference, the proportion that are considered correct.

### Recall

For the games or preferences expected by the user, the proportion that the recommendation system successfully identifies.

The exact evaluation procedure and similarity threshold will be established as the project develops.

## Error Analysis

Error analysis will examine cases where the system's recommendations differ from the expected results.

The analysis will consider:

* Overall recommendation performance
* Whether individual recommendations meet the similarity threshold
* Whether an expected game or preference was successfully identified
* How changes to the input history affect the recommendations

## Experiments

One planned experiment is to remove a game from the user's gameplay history and observe how the recommendations change.

For example:

```text
Original History:
Game A
Game B
Game C

          |
      Remove Game C
          |

Modified History:
Game A
Game B
```

The expectation is that changing the query should potentially change the resulting recommendations. The magnitude of that change may depend on how much information was contained in the original history.

Experiments will record the exact query, corpus, model/tool, and top results where applicable.

## Project Milestones

* [ ] Gather initial training/data samples
* [ ] Build the initial prototype
* [ ] Gather additional data for tuning
* [ ] Implement evaluation metrics
* [ ] Perform controlled experiments
* [ ] Analyze errors
* [ ] Improve the recommendation system

## Project Status

This project is currently in the design and prototyping stage.

The representation, embedding method, similarity function, and final recommendation model are still being investigated.

## Team

* Daniel
* Edward
* Olivier
