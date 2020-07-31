#!/usr/bin/env python3
import time
import math
import random
from string_gen import *
from pynput import keyboard

final_list = []
time_scores = []
calc_time = []
level = 1
play = True

def main():
    if level == 1:
        dict = level_1
    elif level == 2:
        dict = level_2 
    elif level == 3:
        dict = level_3

    calc_time.append(time.perf_counter())
    global game_str
    game_str = random.choice(list(dict.values()))

    user_start = input('Enter S to start the game: ')
    if user_start == 'S':
        print('Welcome to Level ', level)
        print('Type out this string: {}'.format(game_str))
    
    def on_press(key):
        key_pressed = get_key_name(key)
        if key_pressed == 'Key.space':
            final_list.append(' ')
        elif key_pressed == 'Key.enter':
            count_errors(final_list)
        else:
            final_list.append(key_pressed)

    def count_errors(final_list):
        for val in final_list:
            if val == 'Key.backspace' or val == 'Key.shift':
                final_list.remove(val)

        final_answer = ''.join(final_list)
        if final_answer == game_str:
            print_results(final_answer)
        else:
            print(final_list)
            print('\nTry again. Type out this string: {}'.format(game_str))
            final_list.clear()

    def print_results(final_answer):
        calc_time.append(time.perf_counter())
        elapsed_time = calc_time[0] - calc_time[1]
        time_scores.append(elapsed_time)
        print('\nCongratulations! This is your output: ', final_answer)
        print(f'It took you {math.ceil(elapsed_time):.2f} seconds')
        next_round()
    
    with keyboard.Listener(
        on_press=on_press) as listener:
        listener.join()

def next_round():
    play_again = input('Would you like to advance to the next level? Type Y to continue or Q to quit: ')
    if play_again == 'Y':
        global level
        level = level + 1
        final_list.clear()
        main()
    elif play_again == 'Q':
        print('Thanks for playing!')
        exit()
    else:
        next_round()

def get_key_name(key):
    if isinstance(key, keyboard.KeyCode): 
        return key.char
    else:
        return str(key)


while play:
    main()