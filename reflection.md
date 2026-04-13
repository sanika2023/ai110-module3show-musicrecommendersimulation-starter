# Reflection on Music Recommender Experiments

## Profile Comparisons

### High-Energy Pop vs Chill Lofi
The High-Energy Pop screenshot actually showed "Sunrise City" at the top with score 4.74, followed by "Gym Hero" at 3.96. That means the recommender still preferred a pop song that matched both genre and happy mood, even though the profile wanted higher energy. This makes sense because the system gives a lot of weight to matching genre and mood, so a slightly lower-energy pop song can beat a perfect-energy song with the wrong mood.

For Chill Lofi, the top results were "Spacewalk Thoughts" and "Library Rain," both chill mood songs with low energy. This was expected: the model rewarded mood match and energy closeness while avoiding high-energy pop tracks. In other words, Chill Lofi behaved like a calm listener who is willing to accept genre mismatch so long as the song feels mellow.

### Deep Intense Rock vs Conflict Profile
The Deep Intense Rock screenshot showed "Storm Runner" as the clear winner with genre match, mood match, and very close energy. That confirmed the system works well when genre, mood, and energy all agree.

The Conflict Profile screenshot was especially revealing. The top song was "Moonlit Serenade," a classical track with the right genre but wrong mood and low energy. It scored higher than sad high-energy matches like "Heartbreak Blues" because genre match was stronger than the other signals. That shows the system can be “tricked” by contradictory preferences: if the user wants sad and high-energy classical, the recommender may still choose a low-energy classical song just because the genre is correct.

### What Changed and Why It Makes Sense
- **High-Energy Pop**: The recommendation stayed within pop because pop genre match is a strong signal, even though the energy preference was high. So the system acts like it thinks “happy pop” is more important than “just high-energy.”
- **Chill Lofi**: The system shifted to mellow mood matches, which is good for a chill listener. It shows mood can override genre when the energy preference is low.
- **Deep Intense Rock**: When all three signals align, the output is very stable. That means the model is good at clear, unambiguous tastes.
- **Conflict Profile**: The model struggled because it could not balance two opposing desires. This makes sense given the current math: it simply adds scores, so a strong genre match can outweigh a mismatched energy or mood.

### Explaining to a Non-Programmer
If you ask for “Happy Pop,” the system often recommends songs like "Gym Hero" because it sees pop as the most important part of your taste. Even if "Gym Hero" feels more intense than you asked for, the model thinks you still want pop music first. This is why a workout-style pop song can show up for someone asking for cheerful pop: the recommender is treating genre similarity as the biggest clue to what you like.