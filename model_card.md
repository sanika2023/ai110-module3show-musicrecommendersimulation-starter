# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works 

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

The energy scoring mechanism creates filter bubbles for users with extreme energy preferences, as the absolute difference calculation strictly penalizes energy mismatches. For instance, a user who prefers very low-energy music (e.g., 0.2) will rarely see high-energy songs (e.g., 0.9), even if those songs perfectly match their favorite genre or mood, limiting their exposure to potentially enjoyable tracks. This bias was evident in the weight shift experiment, where doubling energy importance caused recommendations to prioritize energy closeness over genre matches, potentially unfair to users who value genre more. Additionally, the small dataset (17 songs) with uneven genre distribution—pop and lofi are overrepresented—means certain musical tastes are underserved, reinforcing biases towards popular or chill styles. Overall, the system's sensitivity to weight changes highlights how small algorithmic tweaks can amplify these inequities, making it less robust for diverse user preferences.

## 7. Evaluation  

I tested several user profiles to see how the recommender handles different preferences. The default profile (pop, happy, energy 0.8) recommended pop and happy songs with close energy, like "Sunrise City." After the weight shift experiment (doubling energy importance, halving genre), the same profile suddenly favored energy-matched songs over genre matches, with "Storm Runner" (rock, intense, energy 0.91) topping the list despite no genre or mood alignment. This surprised me because it showed how sensitive the system is to scoring weights—small changes can flip recommendations from genre-focused to energy-focused, potentially making it feel unpredictable or biased.

I also evaluated hypothetical profiles like High-Energy Pop (pop, happy, 0.95), which would boost intense pop tracks; Chill Lofi (electronic, chill, 0.25), favoring mellow electronic songs; Deep Intense Rock (rock, intense, 0.90), pulling up aggressive rock; and a Conflict Profile (classical, sad, 0.90), which might struggle with contradictions. Comparisons are detailed in `reflection.md`. Overall, the tests revealed that the system works well for straightforward preferences but creates filter bubbles for extremes, as seen in the energy dominance after tuning.

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
