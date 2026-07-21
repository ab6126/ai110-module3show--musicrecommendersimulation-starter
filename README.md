# 🎵 Music Recommender Simulation

## Project Summary

This project builds a simple content-based music recommendation system. Each song has features such as genre, mood, energy, valence, and danceability. The recommender compares these features with a user's taste profile and assigns each song a score. Songs with the highest scores are recommended to the user. This project demonstrates how recommendation systems can use data and scoring rules to personalize suggestions.

---

## How The System Works

Explain your design in plain language.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.
This recommender uses a content-based filtering approach. Instead of comparing users with one another, it compares each song's features with the user's preferences.

### Song Features

Each song contains:

- Genre
- Mood
- Energy
- Valence
- Danceability

### User Profile

The user profile stores:

- Favorite genre
- Favorite mood
- Target energy
- Target valence
- Target danceability

### Scoring Rule

Each song starts with a score of 0.

- Genre match = +2 points
- Mood match = +1 point
- Energy similarity = up to +2 points
- Valence similarity = up to +1 point
- Danceability similarity = up to +1 point

The songs are then sorted from the highest score to the lowest score. The recommender returns the top five songs with the highest scores.

### Recommendation Process

1. Load all songs from `data/songs.csv`.
2. Create a user profile with preferred genre, mood, energy, valence, and danceability.
3. Compare every song with the user profile.
4. Calculate a score for each song.
5. Sort the songs from highest score to lowest score.
6. Return the top five songs.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

   ```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** _(optional)_: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

## This recommender uses a small song catalog, so its recommendations are limited. It only considers a few song features and does not understand lyrics, language, artist popularity, or a user's listening history. The scoring weights may also favor some features too strongly. For example, a genre match may receive a high score even when the song's mood or energy is not a good match. Because the dataset is small and manually created, it may not represent all genres, artists, or user preferences fairly.

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this
