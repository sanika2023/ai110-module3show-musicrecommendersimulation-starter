from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv
import os

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
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
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        """Return the top k song recommendations for the given user."""
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        """Explain why a specific song was recommended for the user."""
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Converts numerical fields to float/int for computation.
    Required by src/main.py
    """
    songs = []
    
    # Handle relative path (from project root)
    if not os.path.isabs(csv_path):
        csv_path = os.path.join(os.path.dirname(__file__), '..', csv_path)
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numerical fields to appropriate types
                song = {
                    'id': int(row['id']),
                    'title': row['title'],
                    'artist': row['artist'],
                    'genre': row['genre'],
                    'mood': row['mood'],
                    'energy': float(row['energy']),
                    'tempo_bpm': float(row['tempo_bpm']),
                    'valence': float(row['valence']),
                    'danceability': float(row['danceability']),
                    'acousticness': float(row['acousticness'])
                }
                songs.append(song)
        
        print(f"Successfully loaded {len(songs)} songs from {csv_path}")
        return songs
    
    except FileNotFoundError:
        print(f"Error: Could not find file at {csv_path}")
        return []
    except ValueError as e:
        print(f"Error converting numerical values: {e}")
        return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons: List[str] = []

    # Genre is a moderate signal.
    if song.get('genre') == user_prefs.get('genre'):
        score += 1.0
        reasons.append('genre match (+1.0)')
    else:
        reasons.append('genre mismatch (+0.0)')

    # Mood is important but secondary.
    if song.get('mood') == user_prefs.get('mood'):
        score += 1.0
        reasons.append('mood match (+1.0)')
    else:
        reasons.append('mood mismatch (+0.0)')

    # Energy is a graded similarity score.
    user_energy = float(user_prefs.get('energy', 0.0))
    song_energy = float(song.get('energy', 0.0))
    energy_diff = abs(song_energy - user_energy)
    energy_score = max(0.0, 4.0 * (1.0 - energy_diff))
    score += energy_score
    reasons.append(f'energy closeness (+{energy_score:.2f})')

    return score, reasons


def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = [
        (song, score, '; '.join(reasons))
        for song in songs
        for score, reasons in [score_song(user_prefs, song)]
    ]

    ranked_songs = sorted(scored_songs, key=lambda item: item[1], reverse=True)
    return ranked_songs[:k]
