import random

Genre = ["Fantasy", "Sci-Fi", "Adventure", "Horror"]
Setting = ["Medieval", "Futuristic", "Apocalyptic", "Underwater"]
Story_plot = ["Rescue the Princess", "Save the World from Destruction", "Uncover a Conspiracy", "Survive a Zombie Apocalypse"]
Characters = ["Warrior", "Wizard", "Alien", "Detective"]
Enemy = ["Dragon", "Robot", "Zombie", "Vampire"]
Objective = ["Collect Artifacts", "Defeat the Villain", "Solve Puzzles", "Escape from a Dangerous Situation"]
Mechanics = ["Turn-based Combat", "Open World Exploration", "Puzzle-solving", "Stealth"]
Theme = ["Courage", "Exploration", "Mystery", "Survival"]
Location = ["Ancient Temple", "Space Station", "Haunted House", "Lost City"]
Twist = ["Betrayal by a Companion", "Time Travel", "Discovering a Hidden Identity", "Parallel Universes"]
Rules = ["No Magic Allowed", "Limited Resources", "Time Limit", "No Violence"]

def generate_game_idea():
    game_idea = (
      "Genre:" +  random.choice(Genre) + " \n" +
      "\nSetting: " + random.choice(Setting) + " \n" +
      "\nStory Plot: " + random.choice(Story_plot) + "\n " +
      "\nObjective: " + random.choice(Objective) + "\n " +
      "\nMechanics: " + random.choice(Mechanics) + " \n" +
      "\nTwist: " + random.choice(Twist) + "\n " +
      "\nCharacters: " +  random.choice(Characters) + " \n" +
      "\nEnemy: " + random.choice(Enemy) + "\n " +
      "\nLocation: " + random.choice(Location) + "\n " +
      "\nTheme: " +  random.choice(Theme)
    )
    return game_idea
