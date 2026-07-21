import csv
from dataclasses import dataclass
from typing import Dict, List, Tuple


@dataclass
class Song:
    """Represent a song and its musical attributes."""

    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float


@dataclass
class UserProfile:
    """Represent a user's musical preferences."""

    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool


class Recommender:
    """Score and rank Song objects for a UserProfile."""

    def __init__(self, songs: List[Song]):
        self.songs = songs

    def _score(self, user: UserProfile, song: Song) -> float:
        """Calculate the compatibility score for one song."""

        score = 0.0

        if song.genre.lower() == user.favorite_genre.lower():
            score += 2.0

        if song.mood.lower() == user.favorite_mood.lower():
            score += 1.0

        energy_similarity = max(
            0.0,
            1.0 - abs(song.energy - user.target_energy),
        )
        score += energy_similarity * 2.0

        if user.likes_acoustic:
            score += song.acousticness
        else:
            score += 1.0 - song.acousticness

        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k songs sorted from highest to lowest score."""

        ranked_songs = sorted(
            self.songs,
            key=lambda song: self._score(user, song),
            reverse=True,
        )

        return ranked_songs[:k]

    def explain_recommendation(
        self,
        user: UserProfile,
        song: Song,
    ) -> str:
        """Explain why a song matches a user's preferences."""

        reasons = []

        if song.genre.lower() == user.favorite_genre.lower():
            reasons.append("genre match")

        if song.mood.lower() == user.favorite_mood.lower():
            reasons.append("mood match")

        energy_difference = abs(song.energy - user.target_energy)

        if energy_difference <= 0.10:
            reasons.append("very close energy level")
        elif energy_difference <= 0.25:
            reasons.append("similar energy level")

        if user.likes_acoustic and song.acousticness >= 0.5:
            reasons.append("strong acoustic sound")
        elif not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append("low acousticness")

        if not reasons:
            reasons.append("overall feature similarity")

        return ", ".join(reasons)


def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numerical fields."""

    songs = []

    with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            song = {
                "id": int(row["id"]),
                "title": row["title"],
                "artist": row["artist"],
                "genre": row["genre"],
                "mood": row["mood"],
                "energy": float(row["energy"]),
                "tempo_bpm": float(row["tempo_bpm"]),
                "valence": float(row["valence"]),
                "danceability": float(row["danceability"]),
                "acousticness": float(row["acousticness"]),
            }

            songs.append(song)

    return songs


def score_song(
    user_prefs: Dict,
    song: Dict,
) -> Tuple[float, List[str]]:
    """Score one song and return its score and explanation reasons."""

    score = 0.0
    reasons = []

    preferred_genre = user_prefs.get("genre", "").lower()
    preferred_mood = user_prefs.get("mood", "").lower()
    target_energy = float(user_prefs.get("energy", 0.5))

    if song["genre"].lower() == preferred_genre:
        score += 2.0
        reasons.append("genre match (+2.00)")

    if song["mood"].lower() == preferred_mood:
        score += 1.0
        reasons.append("mood match (+1.00)")

    energy_similarity = max(
        0.0,
        1.0 - abs(song["energy"] - target_energy),
    )
    energy_points = energy_similarity * 2.0
    score += energy_points
    reasons.append(f"energy similarity (+{energy_points:.2f})")

    # These preferences are optional because main.py currently provides
    # only genre, mood, and energy.
    if "valence" in user_prefs:
        valence_similarity = max(
            0.0,
            1.0 - abs(song["valence"] - float(user_prefs["valence"])),
        )
        score += valence_similarity
        reasons.append(
            f"valence similarity (+{valence_similarity:.2f})"
        )

    if "danceability" in user_prefs:
        danceability_similarity = max(
            0.0,
            1.0
            - abs(
                song["danceability"]
                - float(user_prefs["danceability"])
            ),
        )
        score += danceability_similarity
        reasons.append(
            f"danceability similarity (+{danceability_similarity:.2f})"
        )

    return score, reasons


def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
) -> List[Tuple[Dict, float, str]]:
    """Score all songs and return the top k ranked recommendations."""

    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    ranked_songs = sorted(
        scored_songs,
        key=lambda item: item[1],
        reverse=True,
    )

    return ranked_songs[:k]
