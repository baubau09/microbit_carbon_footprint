#Varibles
steps = 0
test = 0
my_tree_record = 0
STEP_PER_KM = 1390
CO2_PER_KM = 0.083
CO2_PER_TREE = 21
CHALL_1 = 1
CHALL_2 = 2
CHALL_3 = 3
CHALL_4 = 4
CHALL_5 = 5
CHALL_6 = 10
CHALL_7 = 50
CHALL_8 = 100
days: List[number] = []
navigation: List[string] = [
    'Press Logo to save your record at the end of each day',
    'Press A to view the trees saved in 30 days',
    'Press B to view completed challenges',
    'Press A and B together to show the record of me and my friends'
]

#Modes
#on start
for option in navigation:
    basic.show_string(option)

#mode 1
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

#mode 3
def on_pin_pressed_p0():
    show_my_record()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

#mode 4
def on_pin_pressed_p1():
    radio.set_group(1)
    radio.send_number(my_tree_record)
    basic.show_leds("""
                . . . . .
                # # # # #
                # # . # #
                # . # . #
                # # # # #
    """)
    basic.pause(2000)
    basic.clear_screen()
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)

def on_received_number(receivedNumber):
    our_record = receivedNumber + my_tree_record
    show_our_record(our_record)
radio.on_received_number(on_received_number)

#mode 5
def on_pin_pressed_p2():
    show_completed_challenge()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

#Functions
#functions for converting steps/km to the number of trees 
def convert_km_to_trees(kilometer: number):
    total_co2 = kilometer * CO2_PER_KM
    num_of_tree = CO2_PER_TREE / total_co2
    return num_of_tree

def convert_steps_to_trees():
    km = steps / STEP_PER_KM
    return convert_km_to_trees(km)

def show_our_record(our_record):
    basic.show_leds("""
                . . . . .
                . # . # .
                # # # # #
                . # . # .
                # . # . #
        """)
    basic.pause(1000)
    show_record(our_record)

#functions for showing records and challenges
def show_my_record():
    show_record(my_tree_record)

def show_record(record):
    music.start_melody(music.built_in_melody(Melodies.RINGTONE), MelodyOptions.ONCE)
    basic.show_leds("""
                . . # . .
                . # # # .
                . # # # .
                # # # # #
                . . # . .
    """)
    basic.pause(1000)
    basic.show_number(record)
    basic.pause(2000)
    basic.clear_screen()

def show_completed_challenge():
    num_of_led = 5
    music.start_melody(music.built_in_melody(Melodies.POWER_UP), MelodyOptions.ONCE)
    if my_tree_record >= CHALL_1:
        led.plot(2, 4)
    if my_tree_record >= CHALL_2:
        led.plot(1, 3)
    if my_tree_record >= CHALL_3:
        led.plot(2, 3)
    if my_tree_record >= CHALL_4:
        led.plot(3, 3)
    if my_tree_record >= CHALL_5:
        i = 0
        while i < num_of_led:
            led.plot(i, 2)
            i += 1
    if my_tree_record >= CHALL_6:
        i = 0
        while i < num_of_led:
            led.plot(i, 1)
            i += 1
    if my_tree_record >= CHALL_7:
        led.plot(1, 0)
    if my_tree_record >= CHALL_8:
        led.plot(3, 0)
    basic.pause(3000)
    basic.clear_screen()
