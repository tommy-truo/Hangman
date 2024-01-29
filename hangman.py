import os
from random import randint


def clear_console():
    os.system('cls')


def options_menu():
    options_menu_print()
    options_menu_select()

def options_menu_print():
    print("What gamemode would you like to play?")
    print("1. Random word")
    print("2. Custom word")
    print("3. Quit program")

def options_menu_select():
    selected = input("\n(Please enter number)\n>>>")

    while selected not in ['1', '2', '3']:
        clear_console()
        print("That is not a valid option. Please enter a number to select an option.\n")
        options_menu_print()
        selected = input("\n(Please enter number)\n>>>")

    if selected == '1':
        random_word()
    
    elif selected == '2':
        custom_word()

    elif selected == '3':
        clear_console()
        print("Thank you for playing hangman!")


def print_hangman_image(mistakes):
    hangman_images = ['''
     -----
     |   |
         |
         |
         |
         |
    ----------''', '''
     -----
     |   |
     0   |
         |
         |
         |
    ----------''', '''
     -----
     |   |
     0   |
     |   |
         |
         |
    ----------''', '''
     -----
     |   |
     0   |
    /|   |
         |
         |
    ----------''', '''
     -----
     |   |
     0   |
    /|\  |
         |
         |
    ----------''', '''
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    ----------''', '''
     -----
     |   |
     0   |
    /|\  |
    / \  |
         |
    ----------''']

    print(hangman_images[mistakes])



def print_word_progress(word, correct_letters):
    word_progress = ""

    for char in word:
        if char in correct_letters:
            word_progress = word_progress + char + " "
        else:
            word_progress = word_progress + "_ "

    print(word_progress)


def print_all_guessed(all_guessed):
    all_previous_guesses = "\nAll previous guesses: "
    for char in all_guessed:
        all_previous_guesses = all_previous_guesses + char + " "

    print(all_previous_guesses)


def find_unique_chars(word):
    unique_chars = []

    for char in word:
        if char not in unique_chars:
            unique_chars.append(char)

    return unique_chars


def random_word():
    word_bank = "about, above, abuse, accept, accident, accuse, across, activist, actor, administration, admit, adult, advertise, advise, affect, afraid, after, again, against, agency, aggression, agree, agriculture, force, airplane, airport, album, alcohol, alive, almost, alone, along, already, although, always, ambassador, amend, ammunition, among, amount, anarchy, ancestor, ancient, anger, animal, anniversary, announce, another, answer, apologize, appeal, appear, appoint, approve, archeology, argue, around, arrest, arrive, artillery, assist, astronaut, astronomy, asylum, atmosphere, attach, attack, attempt, attend, attention, automobile, autumn, available, average, avoid, awake, award, balance, balloon, ballot, barrier, battle, beauty, because, become, before, begin, behavior, behind, believe, belong, below, betray, better, between, biology, black, blame, bleed, blind, block, blood, border, borrow, bottle, bottom, boycott, brain, brave, bread, break, breathe, bridge, brief, bright, bring, broadcast, brother, brown, budget, build, building, bullet, burst, business, cabinet, camera, campaign, cancel, cancer, candidate, capital, capture, career, careful, carry, catch, cause, ceasefire, celebrate, center, century, ceremony, chairman, champion, chance, change, charge, chase, cheat, cheer, chemicals, chemistry, chief, child, children, choose, circle, citizen, civilian, civil, rights, claim, clash, class, clean, clear, clergy, climate, climb, clock, close, cloth, clothes, cloud, coalition, coast, coffee, collapse, collect, college, colony, color, combine, command, comment, committee, common, communicate, community, company, compare, compete, complete, complex, compromise, computer, concern, condemn, condition, conference, confirm, conflict, congratulate, Congress, connect, conservative, consider, constitution, contact, contain, container, continent, continue, control, convention, cooperate, correct, corruption, cotton, count, country, court, cover, crash, create, creature, credit, crime, criminal, crisis, criticize, crops, cross, crowd, crush, culture, curfew, current, custom, customs, damage, dance, danger, daughter, debate, decide, declare, decrease, defeat, defend, deficit, define, degree, delay, delegate, demand, democracy, demonstrate, denounce, depend, deplore, deploy, depression, describe, desert, design, desire, destroy, detail, detain, develop, device, dictator, different, difficult, dinner, diplomat, direct, direction, disappear, disarm, disaster, discover, discrimination, discuss, disease, dismiss, dispute, dissident, distance, divide, doctor, document, dollar, donate, double, dream, drink, drive, drown, during, early, earth, earthquake, ecology, economy, education, effect, effort, either, elect, electricity, embassy, embryo, emergency, emotion, employ, empty, enemy, energy, enforce, engine, engineer, enjoy, enough, enter, environment, equal, equipment, escape, especially, establish, estimate, ethnic, evaporate, event, every, evidence, exact, examine, example, excellent, except, exchange, excuse, execute, exercise, exile, exist, expand, expect, expel, experience, experiment, expert, explain, explode, explore, export, express, extend, extra, extraordinary, extreme, extremist, factory, false, family, famous, father, favorite, federal, female, fence, fertile, field, fierce, fight, final, financial, finish, fireworks, first, float, flood, floor, flower, fluid, follow, force, foreign, forest, forget, forgive, former, forward, freedom, freeze, fresh, friend, frighten, front, fruit, funeral, future, gather, general, generation, genocide, gentle, glass, goods, govern, government, grain, grass, great, green, grind, ground, group, guarantee, guard, guerrilla, guide, guilty, happen, happy, harvest, headquarters, health, heavy, helicopter, hijack, history, holiday, honest, honor, horrible, horse, hospital, hostage, hostile, hotel, house, however, human, humor, hunger, hurry, husband, identify, ignore, illegal, imagine, immediate, immigrant, import, important, improve, incident, incite, include, increase, independent, individual, industry, infect, inflation, influence, inform, information, inject, injure, innocent, insane, insect, inspect, instead, instrument, insult, intelligence, intelligent, intense, interest, interfere, international, Internet, intervene, invade, invent, invest, investigate, invite, involve, island, issue, jewel, joint, judge, justice, kidnap, knife, knowledge, labor, laboratory, language, large, laugh, launch, learn, leave, legal, legislature, letter, level, liberal, light, lightning, limit, liquid, listen, literature, little, local, lonely, loyal, machine, magazine, major, majority, manufacture, march, market, marry, material, mathematics, matter, mayor, measure, media, medicine, member, memorial, memory, mental, message, metal, method, microscope, middle, militant, military, militia, mineral, minister, minor, minority, minute, missile, missing, mistake, model, moderate, modern, money, month, moral, morning, mother, motion, mountain, mourn, movement, movie, murder, music, mystery, narrow, nation, native, natural, nature, necessary, negotiate, neighbor, neither, neutral, never, night, noise, nominate, normal, north, nothing, nowhere, nuclear, number, object, observe, occupy, ocean, offensive, offer, office, officer, official, often, operate, opinion, oppose, opposite, oppress, orbit, order, organize, other, overthrow, paint, paper, parachute, parade, pardon, parent, parliament, partner, party, passenger, passport, patient, peace, people, percent, perfect, perform, period, permanent, permit, person, persuade, physical, physics, picture, piece, pilot, place, planet, plant, plastic, please, plenty, point, poison, police, policy, politics, pollute, popular, population, position, possess, possible, postpone, poverty, power, praise, predict, pregnant, present, president, press, pressure, prevent, price, prison, private, prize, probably, problem, process, produce, profession, professor, profit, program, progress, project, promise, propaganda, property, propose, protect, protest, prove, provide, public, publication, publish, punish, purchase, purpose, quality, question, quick, quiet, radar, radiation, radio, railroad, raise, reach, react, ready, realistic, reason, reasonable, rebel, receive, recent, recession, recognize, record, recover, reduce, reform, refugee, refuse, register, regret, reject, relations, release, religion, remain, remains, remember, remove, repair, repeat, report, represent, repress, request, require, rescue, research, resign, resist, resolution, resource, respect, responsible, restaurant, restrain, restrict, result, retire, return, revolt, right, river, rocket, rough, round, rubber, rural, sabotage, sacrifice, sailor, satellite, satisfy, school, science, search, season, second, secret, security, seeking, seize, Senate, sense, sentence, separate, series, serious, serve, service, settle, several, severe, shake, shape, share, sharp, sheep, shell, shelter, shine, shock, shoot, short, should, shout, shrink, sickness, signal, silence, silver, similar, simple, since, single, sister, situation, skeleton, skill, slave, sleep, slide, small, smash, smell, smoke, smooth, social, soldier, solid, solve, sound, south, space, speak, special, speech, speed, spend, spill, spirit, split, sport, spread, spring, square, stand, start, starve, state, station, statue, steal, steam, steel, stick, still, stone, store, storm, story, stove, straight, strange, street, stretch, strike, strong, structure, struggle, study, stupid, subject, submarine, substance, substitute, subversion, succeed, sudden, suffer, sugar, suggest, suicide, summer, supervise, supply, support, suppose, suppress, surface, surplus, surprise, surrender, surround, survive, suspect, suspend, swallow, swear, sweet, sympathy, system, target, taste, teach, technical, technology, telephone, telescope, television, temperature, temporary, tense, terrible, territory, terror, terrorist, thank, theater, theory, there, these, thick, thing, think, third, threaten, through, throw, tired, today, together, tomorrow, tonight, torture, total, touch, toward, trade, tradition, traffic, tragic, train, transport, transportation, travel, treason, treasure, treat, treatment, treaty, trial, tribe, trick, troops, trouble, truce, truck, trust, under, understand, unite, universe, university, unless, until, urgent, usual, vacation, vaccine, valley, value, vegetable, vehicle, version, victim, victory, video, village, violate, violence, visit, voice, volcano, volunteer, wages, waste, watch, water, wealth, weapon, weather, weigh, welcome, wheat, wheel, where, whether, which, while, white, whole, willing, window, winter, withdraw, without, witness, woman, wonder, wonderful, world, worry, worse, worth, wound, wreck, wreckage, write, wrong, yellow, yesterday, young"
    word_list = word_bank.split(", ")
    index = randint(1, len(word_list))
    answer = word_list[index]
    game(answer)



def custom_word():
    clear_console()
    answer = input("Enter the word to be guessed\n\n>>>")
    game(answer)


def print_game_info(mistakes, answer, correct_guesses, all_guessed):
    clear_console()
    print_hangman_image(mistakes)
    print_word_progress(answer, correct_guesses)
    print_all_guessed(all_guessed)




def game(answer):
    mistakes = 0
    correct_guesses = []
    unique_chars = find_unique_chars(answer)
    all_guessed = []

    while True:
        print_game_info(mistakes, answer, correct_guesses, all_guessed)

        if mistakes == 6:
            print("\nOh no! Game over!")
            print("The correct answer was: " + answer)
            break
        elif len(correct_guesses) == len(unique_chars):
            print("\nYou won!")
            break
        else:
            char_guessed = guess(all_guessed, mistakes, answer, correct_guesses)
            all_guessed.append(char_guessed)
            if char_guessed in unique_chars:
                correct_guesses.append(char_guessed)
            else:
                mistakes += 1


def guess(all_guessed, mistakes, answer, correct_guesses):
    char_guessed = input("\nGuess a letter:\n>>>")

    while (len(char_guessed) > 1) or (char_guessed in all_guessed):
        print_game_info(mistakes, answer, correct_guesses, all_guessed)
        if len(char_guessed) > 1:
            print("\n\nONLY GUESS ONE LETTER!")
        elif char_guessed in all_guessed:
            print("\n\nYOU ALREADY GUESSED THIS LETTER!")
        char_guessed = input("\nGuess a letter:\n\n>>>")

    return char_guessed


def main():
    clear_console()
    print("Welcome to hangman!\n")
    options_menu()

if __name__ == '__main__':
    main()
