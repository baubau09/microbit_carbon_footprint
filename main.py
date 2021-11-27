#Varibles
radio.set_group(1)
days = 0
current_steps = 0
my_steps_record = 0
my_tree_record = 0
KM_PER_STEP = 1390
CO2_PER_KM = 83
CO2_PER_TREE = 21000
CHALL_1 = 1
CHALL_2 = 2
CHALL_3 = 3
CHALL_4 = 4
CHALL_5 = 5
CHALL_6 = 10
CHALL_7 = 25
CHALL_8 = 50
YEAR = 365

#on start
show_intro()
if my_steps_record == 0 :
    show_menu()

#Modes
#mode 1
# Hello Katie, I modified both two functions below, 
# I put music and icons and change only Variables name.
# I believe the algorithm is the same as yours.
# This is just an example, so if you don't like it, feel free to modify 
# or delete it! Please delete my comments. Thank you. 
def on_gesture_shake():
    global current_steps
    current_steps += 1
    basic.show_icon(IconNames.EIGTH_NOTE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global my_steps_record
    global my_tree_record
    global current_steps
    basic.show_icon(IconNames.YES)
    my_steps_record += current_steps
    current_steps = 0
    my_tree_record = convert_steps_to_trees(my_steps_record)
    basic.clear_screen()
    
    #if a year has passed, reset data
    if days == YEAR :
        my_steps_record = 0
        my_tree_record = 0
        days = 0
    else:
        days += 1    
        
    basic.clear_screen()
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
    global my_tree_record
    our_record = receivedNumber + my_tree_record
    show_our_record(our_record)
radio.on_received_number(on_received_number)

#mode 5
def on_pin_pressed_p2():
    show_completed_challenge()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)

#Functions
#basic functions 
def play_effect_sound_dingdong():
    music.play_tone(523, music.beat(BeatFraction.QUARTER))
    music.play_tone(659, music.beat(BeatFraction.QUARTER))

def play_effect_sound_the_end():
    music.play_tone(262, music.beat(BeatFraction.HALF))
    music.play_tone(330, music.beat(BeatFraction.HALF))
    music.play_tone(392, music.beat(BeatFraction.HALF))

def congrats_completed_all_challenges():
    basic.show_icon(IconNames.HEART)
    pause(100)
    basic.clear_screen()
    pause(100)

def reset_all_data():
    global my_steps_record
    global my_tree_record
    my_steps_record = 0
    my_tree_record = 0

#functions for converting steps/km to the number of trees
def convert_km_to_steps(kilometer):
    num_of_steps = kilometer * KM_PER_STEP
    return num_of_steps
    
def convert_steps_to_trees(num_of_steps):
    km = num_of_steps / KM_PER_STEP
    return convert_km_to_trees(Math.round(km))

def convert_km_to_trees(kilometer):
    total_co2 = kilometer * CO2_PER_KM
    num_of_tree = 0
    if total_co2 >= CO2_PER_TREE :
        num_of_tree = total_co2 / CO2_PER_TREE
    return Math.round(num_of_tree)

#functions for showing intro, menu, records and challenges
def show_intro():
    music.start_melody(music.built_in_melody(Melodies.CHASE),
            MelodyOptions.FOREVER_IN_BACKGROUND)
    basic.show_string("Save Earth!")
    music.stop_all_sounds()
    basic.show_icon(IconNames.HAPPY)
    basic.clear_screen()

def show_menu():
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_string("p0")
    basic.show_leds("""
                    . . # . .
                    . # # # .
                    . # # # .
                    # # # # #
                    . . # . .
                    """)
    basic.clear_screen()
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    basic.show_string("p0")
    basic.show_leds("""
                    . . # . .
                    . # # # .
                    . # # # .
                    # # # # #
                    . . # . .
                    """)
    basic.clear_screen()
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    basic.show_string("p0")
    basic.show_leds("""
                    . . # . .
                    . # # # .
                    . # # # .
                    # # # # #
                    . . # . .
                    """)
    basic.clear_screen()
    music.play_tone(349, music.beat(BeatFraction.WHOLE))
    basic.show_string("p1")
    basic.show_leds("""
                    . . . . .
                    . # . # .
                    # # # # #
                    . # . # .
                    # . # . #
                    """)
    basic.show_leds("""
                    . . # . .
                    . # # # .
                    . # # # .
                    # # # # #
                    . . # . .
                    """)
    basic.clear_screen()
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    basic.show_string("p2")
    basic.show_leds("""
                    . # . # .
                    # . # . #
                    # . . . #
                    . # . # .
                    . . # . .
                    """)
    basic.clear_screen()
    play_effect_sound_the_end()
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.show_icon(IconNames.TARGET)
    basic.show_icon(IconNames.DIAMOND)
    basic.clear_screen()

def show_my_record():
    show_record(my_tree_record)

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
    basic.show_leds("""
                    . # . # .
                    # . # . #
                    # . . . #
                    . # . # .
                    . . # . .
                    """)
    pause(500)
    basic.clear_screen()
    if my_tree_record >= CHALL_1:
        led.plot(2, 4)
    pause(500)
    if my_tree_record >= CHALL_2:
        led.plot(1, 3)
    pause(500)
    if my_tree_record >= CHALL_3:
        led.plot(2, 3)
    pause(500)
    if my_tree_record >= CHALL_4:
        led.plot(3, 3)
    pause(500)
    if my_tree_record >= CHALL_5:
        i = 0
        while i < num_of_led:
            led.plot(i, 2)
            i += 1
    pause(500)
    if my_tree_record >= CHALL_6:
        i = 0
        while i < num_of_led:
            led.plot(i, 1)
            i += 1
    pause(500)
    if my_tree_record >= CHALL_7:
        led.plot(1, 0)
    pause(500)
    if my_tree_record >= CHALL_8:
        led.plot(3, 0)
        pause(500)
        congrats_completed_all_challenges()
        congrats_completed_all_challenges()
        congrats_completed_all_challenges()
        reset_all_data()
    basic.clear_screen()
