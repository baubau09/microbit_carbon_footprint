steps = 0
test = 0
tree_record = 0
STEP_PER_KM = 1390
CO2_PER_KM = 0.083
CO2_PER_TREE = 21
days: List[number] = []
navigation: List[string] = [
    'Press Logo to save your record at the end of each day',
    'Press A to view the trees saved in 30 days',
    'Press B to view completed challenges',
    'Press A and B together to show the record of me and my friends'
]

def on_forever():
    global navigation
    for option in navigation:
        basic.show_string(option)
basic.forever(on_forever)

def on_gesture_shake():
    global steps
    steps += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global days
    global steps
    days.append(steps)
    steps = 0

input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def convert_steps():
    global steps

def convert_km_to_trees(kilometer: number):
    total_co2 = kilometer * CO2_PER_KM
    num_of_tree = CO2_PER_TREE / total_co2
    return num_of_tree

def convert_steps_to_trees():
    km = steps / STEP_PER_KM
    return convert_km_to_trees(km)

def show_my_record():
    music.start_melody(music.built_in_melody(Melodies.RINGTONE), MelodyOptions.ONCE)
    basic.show_leds("""
                . . # . .
                . # # # .
                . # # # .
                # # # # #
                . . # . .
    """)
    basic.pause(1000)
    basic.show_number(tree_record)
    basic.pause(2000)
    basic.clear_screen()




