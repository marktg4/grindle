# Want to make an idle game about grinding levels
import time
starttime = time.time()
import random
from skills import skills, XP_LEVELS


# Set up functions

# Gain experience
def gain_xp(skill):
    base = skill.get('skill_base', 1)
    adder = skill.get('skill_adder', 0)
    multiplier = skill.get('skill_multiplier', 1)
    xp = round((base + adder) * multiplier, 1)
    skill['skill_xp'] += xp
    skill['skill_xp'] = round(skill['skill_xp'], 1)
    # print(F"Added {xp} experience to {skill.get('name', 'no name provided')}")
    return skill

# Check if skill has leveled up, and level it up if so, also apply xp bonuses?
def level_up(skill):
    current_level = skill['level']
    current_xp = skill['skill_xp']
    if current_level < 100:
        if current_xp >= XP_LEVELS[current_level]:
            skill['level'] += 1
            # print(F"{skill['name']} has reached level {skill['level']}")
            skill['skill_adder'] += 1
            # print(F"{skill['name']} will now receive an extra {skill['skill_adder']} xp")
            if skill['level'] % 5 == 0:
                skill['skill_multiplier'] += 0.1
                # print(F"{skill['name']} received an additive 10% experience bonus")
            return skill
    else:
        return skill

# Set speed of the game
def increase_speed(speed):
    speed = round(speed * 0.9, 4)
    return speed



# Set initial values

chosen_skill = skills[0]
speed = 1
total_level = len(skills)
# skill_adder = []
# skill_multiplier = []
# skill_base = []
# skill_xp = []
# for skill in SKILLS:
#     skill_adder.append(0)
#     skill_multiplier.append(1)
#     skill_base.append(1)
#     skill_xp.append(0)


# Game loop
while True:
    # Set chosen skill #####
    chosen_skill = skills[random.randint(0, len(skills)-1)]
    # chosen_skill = skills[0]
    # print(F"Chosen skill is {chosen_skill.get('name', 'no name provided')}")

    # Award XP
    # print(F"Current {chosen_skill} experience: {skill_xp[SKILLS.index(chosen_skill)]}")
    chosen_skill = gain_xp(chosen_skill)
    # print(F"New {chosen_skill.get('name', 'no name provided')} experience: {chosen_skill.get('skill_xp', 'no xp found')}")

    # Check if skill has leveled up
    chosen_skill = level_up(chosen_skill)

    # Check if total level is enough for a speed bonus
    level_check = 0
    for skill in skills:
        level_check += skill['level']
    if level_check > total_level:
        total_level = level_check
        if total_level % 5 == 0:
            speed = increase_speed(speed)
            # print(F'Total level is now {total_level}, game speed increased!')

    # Print a pretty table of data
    print(F"Total Level: {total_level} \t Game Speed: Every {speed} second(s)")
    print(F"Skill Breakdown:")
    for skill in skills:
        if len(skill['name']) < 7:
            print(F"\t{skill['name']} \t\t Level: {skill['level']} \t XP: {skill['skill_xp']}")
        else:
            print(F"\t{skill['name']} \t Level: {skill['level']} \t XP: {skill['skill_xp']}")

    # Remove the Time taken by code to execute
    time.sleep(speed)