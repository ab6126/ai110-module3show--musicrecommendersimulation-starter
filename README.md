# 🎵 Music Recommender Simulation

# Project Summary

This project builds a simple content-based music recommendation system. Each song has features such as genre, mood, and energy. The recommender compares these features with a user's taste profile and assigns each song a score. Songs with the highest scores are recommended to the user. This project demonstrates how recommendation systems use data and scoring rules to personalize suggestions.

---

# How The System Works

This recommender uses a content-based filtering approach. Instead of comparing the behavior of different users, it compares each song's features with the current user's preferences.

## Song Features

Each song contains the following information:

- ID
- Title
- Artist
- Genre
- Mood
- Energy
- Tempo in beats per minute
- Valence
- Danceability
- Acousticness

The recommender currently uses these features for scoring:

- Genre
- Mood
- Energy

Additional features such as valence and danceability could be added in future versions.

---

## User Profile

The recommender compares each song with a user's preferences.

Example user profile:

- Favorite genre: pop
- Favorite mood: happy
- Target energy: 0.80

```python
user_prefs = {
    "genre": "pop",
    "mood": "happy",
    "energy": 0.80
}
```

This profile allows the recommender to distinguish between different types of music. For example, an intense rock song may have high energy but will not match the user's preferred genre. A chill lofi song may have the right energy but not the preferred mood. Using several features gives the recommender more information than using genre alone.

---

## Algorithm Recipe

Every song begins with a score of 0.

1. Add **2.0 points** if the song's genre matches the user's preferred genre.
2. Add **1.0 point** if the song's mood matches the user's preferred mood.
3. Add up to **2.0 points** based on how closely the song's energy matches the user's preferred energy.
4. Save the song's final score and the reasons it received those points.
5. Sort all songs from highest score to lowest score.
6. Return the top five songs.

---

## Numerical Similarity

For the energy feature, similarity is calculated as:

```python
energy_score = 2 - abs(song_energy - target_energy) * 2
```

For example, if the user's target energy is **0.80** and a song's energy is **0.75**, then:

```text
Energy score = 2 - |0.75 - 0.80| × 2
             = 1.90
```

---

## Example Score

Suppose a song has:

- Genre: pop
- Mood: happy
- Energy: 0.75

The score becomes:

- Genre match: +2.00
- Mood match: +1.00
- Energy similarity: +1.90

Final score:

```text
2.00 + 1.00 + 1.90 = 4.90
```

Each song is scored individually. After every song receives a score, the recommender sorts the songs from highest to lowest score and returns the top recommendations.

---

## Recommendation Process

```text
User Preferences
        ↓
Load songs from data/songs.csv
        ↓
Compare each song with the user profile
        ↓
Calculate score and explanation
        ↓
Repeat for every song
        ↓
Sort songs by score
        ↓
Return the top five recommendations
```

---

## Potential Bias in the Design

The recommender gives genre the highest weight (2.0 points). Because of this, songs from the preferred genre may rank above songs from other genres even if they have a better mood or energy match. Since the dataset is relatively small, recommendations may not represent every music preference equally.

---

# Getting Started

## Setup

1. Create a virtual environment (optional):

```bash
python -m venv .venv
```

2. Activate it.

Mac/Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the recommender:

```bash
python -m src.main
```

---

## Running Tests

```bash
python -m pytest
```

---

# Sample Recommendation Output

Example output for the **High-Energy Pop** profile:

```text
+------------------------+---------+------------------------------------------------------------------------+
| Song                   | Score   | Reasons                                                                |
+------------------------+---------+------------------------------------------------------------------------+
| Sunrise City           | 4.96    | genre match (+2.00), mood match (+1.00), energy similarity (+1.96)     |
| Gym Hero               | 3.74    | genre match (+2.00), energy similarity (+1.74)                         |
| Rooftop Lights         | 2.92    | mood match (+1.00), energy similarity (+1.92)                          |
| Weekend Lights         | 2.76    | mood match (+1.00), energy similarity (+1.76)                          |
| Night Drive Loop       | 1.90    | energy similarity (+1.90)                                              |
+------------------------+---------+------------------------------------------------------------------------+
```

---

# Experiments You Tried

I tested the recommender using three different user profiles:

- High-Energy Pop
- Chill Lofi
- Intense Rock

## High-Energy Pop

```text
Sunrise City - Score: 4.96
Gym Hero - Score: 3.74
Rooftop Lights - Score: 2.92
Weekend Lights - Score: 2.76
Night Drive Loop - Score: 1.90
```

`Sunrise City` ranked first because it matched the user's preferred genre, mood, and energy.

## Chill Lofi

```text
Library Rain - Score: 5.00
Midnight Coding - Score: 4.86
Focus Flow - Score: 3.90
Spacewalk Thoughts - Score: 2.86
Coffee Shop Stories - Score: 1.96
```

`Library Rain` ranked first because it matched the lofi genre, chill mood, and target energy.

## Intense Rock

```text
Storm Runner - Score: 4.98
Gym Hero - Score: 2.94
Electric Pulse - Score: 1.98
Weekend Lights - Score: 1.96
Fast Lane - Score: 1.92
```

`Storm Runner` ranked first because it matched the rock genre, intense mood, and high-energy preference.

The recommendations changed clearly across the three profiles, showing that the recommender responds appropriately to different user preferences.

---

# Limitations and Risks

The recommender uses a relatively small song catalog, so recommendations are limited. It only considers genre, mood, and energy. It does not consider lyrics, artist popularity, release year, or listening history.

Because the dataset is manually created, it may not represent every music genre or user preference fairly. Musical taste is also dynamic, but the recommender assumes users have fixed preferences.

---

# Reflection

See the completed **Model Card** for a detailed discussion of the recommender's design, evaluation, strengths, limitations, future improvements, and personal reflection.

**Model Card:** `model_card.md`

---

# Optional Extension: Visual Summary Table

I completed the **Visual Summary Table** challenge by improving the command-line output. Recommendations are displayed in a formatted ASCII table showing:

- Song title
- Recommendation score
- Explanation of the score

I implemented this using Python string formatting without external libraries. I tested the feature with the High-Energy Pop, Chill Lofi, and Intense Rock user profiles, and all automated tests continued to pass successfully.
