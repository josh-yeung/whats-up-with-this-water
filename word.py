import PySimpleGUI as sg
import copy
import random


# Insert code to generate a word here


def TextChar(value, key):
    return sg.Input(value, key=key, font='Courier 22', size=(1,1),  disabled_readonly_background_color='gray', border_width=1,  p=1, enable_events=True, disabled=True)

def main():
    words = ['OTTER', 'WHALE', 'SHARK', 'SQUID']

    num = random.randint(0,len(words))
    answer = words[num]
    layout = [[sg.Text('Wordle', font='_ 20')],
              [[TextChar('', (row, col)) for col in range(5)]for row in range(6)],
              [sg.B('Enter', bind_return_key=True)],
              [sg.Text('Or press enter', font='_ 10')]]

    window = sg.Window("Wordle", layout, finalize=True, element_justification='c')

    cur_row, correct = 0, False
    [window[(cur_row, col)].update(disabled=False) for col in range(5)]
    window.bind('<BackSpace>', '-BACKSPACE-')
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if isinstance(event, tuple):
            if len(values[event]):
                row, col = event
                char_input = values[event][-1]
                if not char_input.isalpha():                            # if not a character input, remove the input
                    window[event].update('')
                else:
                    window[event].update(char_input.upper()[0])         # convert to uppercase
                    if col < 4:
                        window[(row, col+1)].set_focus()                # Move to next position
        elif event == 'Enter' and cur_row < 5:
            guess = ''.join([values[(cur_row, j)] for j in range(5)])
            answer2 = copy.copy(answer)
            for i, letter in enumerate(guess):
                if letter == answer2[i]:
                    window[(cur_row, i)].update(background_color='green', text_color='white')
                    answer2 = answer2.replace(letter, '*')
                elif letter in answer2:
                    window[(cur_row, i)].update(background_color='#C9B359', text_color='white')
                    answer2 = answer2.replace(letter, '*')
                else:
                    window[(cur_row, i)].update(background_color='gray', text_color='white')
            if guess == answer:
                correct = True
                break
            cur_row += 1                                                # Move to the next row
            [window[(cur_row, col)].update(disabled=False) for col in range(5)]     # Enable inputs on next row
            window[(cur_row, 0)].set_focus()                            # Move to first position on row
        elif event == 'Enter' and cur_row == 5:
            correct = False
            break
        elif event == '-BACKSPACE-':
            current_focus = window.find_element_with_focus()
            current_key = current_focus.Key
            if isinstance(current_key, tuple):
                window[current_key].update('')
                if current_key[1] > 0:
                    window[(current_key[0], current_key[1]-1)].set_focus()
                    window[(current_key[0], current_key[1]-1)].update('')


    if correct:
        sg.popup('You win!')
    else:
        sg.popup(f'Sorry... the answer was {answer}')

    window.close()
