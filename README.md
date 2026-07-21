# 🎵 Music Recommender Simulation

## Project Summary

This project builds a simple content-based music recommendation system. Each song has features such as genre, mood, energy, valence, and danceability. The recommender compares these features with a user's taste profile and assigns each song a score. Songs with the highest scores are recommended to the user. This project demonstrates how recommendation systems use data and scoring rules to personalize suggestions.

---

## How The System Works

This recommender uses a content-based filtering approach. Instead of comparing the behavior of different users, it compares each song's features with the current user's preferences.

### Song Features

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

The first version of the scoring system will primarily use:

- Genre
- Mood
- Energy
- Valence
- Danceability

### User Profile

The recommender will compare the songs with this example taste profile:

- Favorite genre: pop
- Favorite mood: happy
- Target energy: 0.80
- Target valence: 0.85
- Target danceability: 0.75

The user profile will be represented as a dictionary:

```python
user_prefs = {
    "favorite_genre": "pop",
    "favorite_mood": "happy",
    "target_energy": 0.80,
    "target_valence": 0.85,
    "target_danceability": 0.75
}
```

This profile can distinguish between different kinds of music. For example, an intense rock song may have high energy, but it will not match the user's favorite genre or mood. A chill lofi song may also fail to match the user's pop and happy preferences. Using several features gives the recommender more information than using genre alone.

### Algorithm Recipe

Every song begins with a score of 0.

1. Add 2.0 points if the song's genre matches the user's favorite genre.
2. Add 1.0 point if the song's mood matches the user's favorite mood.
3. Add up to 2.0 points based on how closely the song's energy matches the user's target energy.
4. Add up to 1.0 point based on how closely the song's valence matches the user's target valence.
5. Add up to 1.0 point based on how closely the song's danceability matches the user's target danceability.
6. Save the song's final score and the reasons it received those points.
7. Sort all songs from highest score to lowest score.
8. Return the top five songs.

### Numerical Similarity

For numerical features, similarity is calculated using this formula:

```python
similarity = 1 - abs(song_value - target_value)
```

For example, if the user's target energy is `0.80` and a song's energy is `0.75`, the similarity is:

```text
1 - |0.75 - 0.80| = 0.95
```

Because energy has a weight of 2.0, the song earns:

```text
0.95 × 2.0 = 1.90 energy points
```

### Example Score

Suppose a song has these features:

- Genre: pop
- Mood: happy
- Energy: 0.75
- Valence: 0.80
- Danceability: 0.70

Using the example user profile, the song receives:

- Genre match: `+2.00`
- Mood match: `+1.00`
- Energy similarity: `+1.90`
- Valence similarity: `+0.95`
- Danceability similarity: `+0.95`

The final score is:

```text
2.00 + 1.00 + 1.90 + 0.95 + 0.95 = 6.80
```

The scoring rule evaluates one individual song and produces a numeric score. The ranking rule evaluates all songs, sorts them by score, and selects the top results. Both rules are necessary because scoring a song does not automatically determine which songs should be recommended first.

### Recommendation Process

```text
User preferences
        ↓
Load songs from data/songs.csv
        ↓
Compare one song with the user profile
        ↓
Calculate its score and reasons
        ↓
Repeat for every song
        ↓
Sort songs from highest score to lowest score
        ↓
Return the top five recommendations
```

### Potential Bias in the Design

This recommender may over-prioritize genre because genre receives 2.0 points. A song from another genre might closely match the user's mood, energy, valence, and danceability but still rank below a genre match. The feature weights may need to be adjusted after testing the recommendations.

---

## Getting Started

### Setup

1. Create a virtual environment. This is optional but recommended.

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment.

   On Mac or Linux:

   ```bash
   source .venv/bin/activate
   ```

   On Windows:

   ```bash
   .venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python -m src.main
   ```

### Running Tests

Run the tests with:

```bash
pytest
```

Additional tests can be added to `tests/test_recommender.py`.

---

## Sample Recommendation Output

This section will be completed after the recommender has been implemented and run.

```text
User profile: Not tested yet

Recommendations:
1. To be added after implementation
2. To be added after implementation
3. To be added after implementation
```

**Screenshot or video:** Optional

---

## Experiments You Tried

This section will be completed after the recommender is implemented. Planned experiments include:

- Changing the genre weight from 2.0 to 0.5
- Comparing results with and without valence
- Comparing results for pop, rock, and lofi user profiles
- Testing different target energy values

---

## Limitations and Risks

This recommender uses a small song catalog, so its recommendations are limited. It only considers a few song features and does not understand lyrics, language, artist popularity, or a user's listening history. The scoring weights may also favor some features too strongly. For example, a genre match may receive a high score even when the song's mood or energy is not a good match.

Because the dataset is small and manually created, it may not represent all genres, artists, cultures, or user preferences fairly. The system also assumes that a person's preferences can be represented by fixed target values, even though musical taste may change depending on activity, location, or mood.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

This section will be completed after the implementation and testing phases. The final reflection will explain what I learned about how recommendation systems turn data into predictions and where bias or unfairness may appear.
