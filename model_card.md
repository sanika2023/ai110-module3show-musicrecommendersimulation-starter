# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**VibeFinder 1.0**

---

## 2. Intended Use  

This model suggests songs from a small catalog based on a user’s favorite genre, mood, and energy level. It is meant for classroom exploration and simple experiments, not for real music apps.

---

## 3. How the Model Works 

The recommender gives each song a score based on three things. It adds points when the song matches the user’s genre and mood. It also adds points when the song’s energy is close to the user’s desired energy. Songs with higher total scores are recommended first.

---

## 4. Data  

The dataset has 17 songs in `data/songs.csv`. It includes genres like pop, lofi, rock, electronic, classical, metal, and reggae. It also includes moods like happy, chill, intense, sad, and focused. The dataset is small and does not cover many styles or languages.

---

## 5. Strengths  

The system works well for clear taste profiles that match its limited catalog. It finds good results when the user wants a common genre and mood combination. It also makes the scoring easy to understand, so the recommendations are transparent.

---

## 6. Limitations and Bias 

The energy scoring mechanism creates filter bubbles for users with extreme energy preferences, as the absolute difference calculation strictly penalizes energy mismatches. For instance, a user who prefers very low-energy music (e.g., 0.2) will rarely see high-energy songs (e.g., 0.9), even if those songs perfectly match their favorite genre or mood, limiting their exposure to potentially enjoyable tracks. This bias was evident in the weight shift experiment, where doubling energy importance caused recommendations to prioritize energy closeness over genre matches, potentially unfair to users who value genre more. Additionally, the small dataset (17 songs) with uneven genre distribution—pop and lofi are overrepresented—means certain musical tastes are underserved, reinforcing biases towards popular or chill styles. Overall, the system's sensitivity to weight changes highlights how small algorithmic tweaks can amplify these inequities, making it less robust for diverse user preferences.

---

## 7. Evaluation  

I tested four real profile runs using the committed screenshots: High-Energy Pop, Chill Lofi, Deep Intense Rock, and Conflict Profile.

- **High-Energy Pop**: The top result was "Sunrise City" with score 4.74, followed by "Gym Hero" at 3.96. This shows the system still values pop genre and happy mood strongly even when the user wants higher energy.
- **Chill Lofi**: The top songs were "Spacewalk Thoughts" and "Library Rain," both chill mood tracks with low energy. This shows the model rewards a calm mood and low energy when those are requested.
- **Deep Intense Rock**: "Storm Runner" was the clear winner with matching genre, mood, and energy. This shows the system works well when all three preferences line up.
- **Conflict Profile**: The top recommendation was "Moonlit Serenade," a classical song with the right genre but wrong mood and low energy. This shows the model can struggle when user preferences contradict each other.

Overall, the model behaves well for simple, consistent tastes, but it can give misleading results for conflicting preferences.

---

## 8. Future Work  

- Add another score for mood strength, not just match or no match.
- Use more songs and more genres so the model is less biased.
- Add a way to balance genre, mood, and energy instead of always adding them the same way.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how much the recommendation results changed when I adjusted the scoring weights. A small change in how much the model cares about energy versus genre made very different songs appear at the top.

Using AI tools helped speed up the edits and gave me good wording for the model card and README. I had to double-check the actual outputs and screenshot data, because the tools can suggest reasoning that does not exactly match the committed results.

I was surprised that this simple algorithm still felt like a real recommender. Even with only genre, mood, and energy, the top songs changed in a way that matched different user moods.

If I extended this project, I would add more songs, use more features like tempo, and find a better balance between genre, mood, and energy.