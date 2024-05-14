import curses
from curses import wrapper
import time
import random

TARGET_TEXT = [
    "First Text",
    "Second Text",
    "Third Text",
    "Fourth Text"
]

def load_text():
    with open("SpeedTyping.txt", "r") as file:
        lines = file.readlines()
        return random.choice(lines).strip()
    
def choose_target():
    return random.choice(TARGET_TEXT)

def display_text(stdscr, target, typed, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM : {wpm}", curses.color_pair(3))
        
    for  i, char in enumerate(typed):
        color = curses.color_pair(1)
        if target[i] != char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)

    stdscr.refresh()

def typing_test(stdscr):
    target_text = choose_target()
        
    typed_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        elapsed_time = max(time.time() - start_time, 1)
        wpm = round(len(typed_text) / (elapsed_time / 60) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, typed_text, wpm)
        stdscr.refresh()

        if "".join(typed_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\x7f", "\b") and len(typed_text) > 0:
            typed_text.pop()
        elif len(target_text) > len(typed_text):
            typed_text.append(key)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress Any Key To Start...")
    stdscr.refresh()
    stdscr.getkey()

    run = True
    while run:
        typing_test(stdscr)

        stdscr.addstr(2, 0, "Congrats! You Completed the Test! Press 'Y' to Play Again or Press Any Key to Exit...")
        key = stdscr.getkey()
        
        if ord(key) == 121 or ord(key) == 89:
            continue
        else:
            break

wrapper(main)