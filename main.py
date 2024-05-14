# ===================== Task 1 ===================== 
import mood_responses
from random import choice


moods = ["happy", "sad", "excited", "tired"]
mood = choice(moods)

print(mood_responses.mood_fn(mood))


# ===================== Task 2 ===================== 
import text_utils

rev_str = text_utils.reverse_string('hello world')
print(rev_str)

cap_str = text_utils.capitalize_string("capitalize this text")
print(cap_str)