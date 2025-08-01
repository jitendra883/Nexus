# 1. Import the random module
import random

# 2. Create subjects, actions, and places
subjects = [
    "Jitendra Singh",
    "Virat Kohli",
    "A Bangla Cat",
    "A Group of Lions",
    "PM Modi",
    "Auto Rickshaw Driver from Bihar",
    "Chota Bacha"
]

actions = [
    "launches",
    "cancels",
    "declares war on",
    "eats",
    "celebrates",
    "dances with",
    "orders"
]

places_or_things = [
    "at Red Fort",
    "at India Gate",
    "in Kolkata local train",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL T20 match",
    "a plate of Rasgulla"
]

# 3. Start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"\nBREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n "+ headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower()
    if user_input == "no":
        print("\nThanks for using the Fake News Headline Generator. Have a fun day!")
        break
