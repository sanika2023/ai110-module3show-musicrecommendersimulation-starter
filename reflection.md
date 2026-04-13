# Reflection on Music Recommender Experiments

## Profile Comparisons

### Default Pop/Happy (genre=pop, mood=happy, energy=0.8) - Original vs Weight-Shifted
**Original (genre +2.0, mood +1.0, energy up to +2.0):** Top recommendations included "Sunrise City" (pop, happy, energy 0.82) with score ~4.96 (genre +2, mood +1, energy +1.96), followed by other pop/happy matches. This made sense because genre was the strongest weight, favoring pop songs.

**Weight-Shifted (genre +1.0, mood +1.0, energy up to +4.0):** Rankings flipped to energy-focused: "Storm Runner" (rock, intense, energy 0.91) scored 3.96 (energy closeness +3.96), "Electric Dreams" (electronic, excited, energy 0.88) at 3.92, ignoring genre/mood mismatches. This surprised me because doubling energy importance overwhelmed genre, showing how sensitive the system is to tuning—users prioritizing genre might get irrelevant recommendations.

### High-Energy Pop (genre=pop, mood=happy, energy=0.95) vs Chill Lofi (genre=electronic, mood=chill, energy=0.25)
High-Energy Pop would likely top with "Gym Hero" (pop, intense, energy 0.93) scoring high on genre match (+1.0) and energy closeness (~3.88), even though mood is intense vs happy—it's like recommending a pumped-up workout track for cheerful music, which could work if the user enjoys energetic vibes. Chill Lofi would shift to low-energy electronic/chill songs like "Spacewalk Thoughts" (ambient, chill, energy 0.28), scoring ~3.88 on energy, prioritizing mellow tracks over excitement mismatches. The difference highlights energy filter bubbles: high-energy profiles get intense songs regardless of mood, while low-energy ones get calm ones, potentially missing cross-genre gems.

### Deep Intense Rock (genre=rock, mood=intense, energy=0.90) vs Conflict Profile (genre=classical, mood=sad, energy=0.90)
Deep Intense Rock would favor "Storm Runner" (rock, intense, energy 0.91) with genre +1.0, mood +1.0, energy ~3.96, a perfect match. Conflict Profile (high energy with sad mood) might recommend "Raging Fire" (metal, angry, energy 0.95) scoring ~3.80 on energy alone, or "Moonlit Serenade" (classical, romantic, energy 0.20) if genre mattered more—but with current weights, energy dominates, so it picks high-energy mismatches. This makes sense because the system adds scores without considering contradictions, potentially recommending aggressive metal to someone wanting sad classical, which could feel off.

### Why "Gym Hero" Shows Up for Happy Pop Seekers
"Gym Hero" (pop, intense, energy 0.93) appears for happy pop profiles because genre match gives +1.0 (or +2.0 originally), and energy closeness adds significant points (~3.88 in shifted version), outweighing the mood mismatch (intense vs happy). It's like suggesting an upbeat gym anthem to someone who wants cheerful music—it might energize them and fit as "happy" in a broad sense, but it's not purely joyful. The system assumes genre is key, so it boosts pop tracks even if mood isn't exact, which is valid if users see intense pop as a subtype of happy music, but could be frustrating if they want only lighthearted tunes.</content>
<parameter name="filePath">c:\Users\sanik\OneDrive\Documents\Codepath\AI110\show_Music_Recommender\ai110-module3show-musicrecommendersimulation-starter\reflection.md