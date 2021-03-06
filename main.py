# Variables
radio.set_group(1)
days = 1
km_input = 0
current_steps = 0
my_steps_record = 0
my_tree_record = 0
KM_PER_STEP = 1390 #O n average, there are 1390 steps in a kilometer
CO2_PER_KM = 83 # A small motorbike's CO2 emission is approximately 83g
CO2_PER_TREE = 21000 # A tree can absorb 21000g of CO2
YEAR = 365

# Variables for challenges
# Each challenge refers to a specific number of trees.
CHALL_1 = 1
CHALL_2 = 2
CHALL_3 = 3
CHALL_4 = 4
CHALL_5 = 5
CHALL_6 = 10
CHALL_7 = 25
CHALL_8 = 50


### INSTRUCTIONS ###
# Press logo to save current steps records
# Press pin 0 to show my tree records
# Press pin 1 to show me and my friends records
# Press pin 2 to show my completed challenges
# A and B buttons are used to manually enter the KM travelled
#   Press A to decrease km by 1
#   Press B to increase km by 1
#   Press A and B together to save km record

### RESET DATA ###
# Data will be automatically reset
# 1) if a year has passed
# 2) if a user completed all challenges


# On start
show_intro()
if my_steps_record == 0 :
    show_menu()

### MODES ###
# mode 1: Save steps data to convert and store trees data
# Gesture detection to count current steps
def on_gesture_shake():
    global current_steps
    current_steps += 1
    basic.show_icon(IconNames.EIGTH_NOTE)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global days
    global YEAR

    save_my_data(True)
    #if a year has passed, reset data
    if days >= YEAR :
        reset_all_data()
    else:
        days += 1
        
    basic.clear_screen()
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

# mode 2: User manually input kilometer travelled in case they use Public transportation

# Press A to decrease km by 1
def on_button_pressed_a():
    global km_input

    if km_input == 0:
        basic.show_icon(IconNames.No)
        pause(500)
        basic.clear_screen()
    else:
        km_input -= 1
        basic.show_number(km_input)
    
input.on_button_pressed(Button.A, on_button_pressed_a)

# Press B to increase km by 1
def on_button_pressed_b():
    global km_input
    
    km_input += 1
    basic.show_number(km_input)
    
input.on_button_pressed(Button.B, on_button_pressed_b)

# Press A and B together to save km record
def on_button_pressed_ab():
    save_my_data(False)
input.on_button_pressed(Button.AB, on_button_pressed_ab)


# mode 3: Show accumulated tree records
def on_pin_pressed_p0():
    show_my_record()
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)


# mode 4: Friends mode

# 4.1 Send my tree record to my friend's microbit
def on_pin_pressed_p1():
    radio.set_group(1)
    radio.send_number(my_tree_record) # Send my record to my friend's microbit
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


# 4.2 Calculate the total tree records of me and my friend
def on_received_number(receivedNumber):
    global my_tree_record

    our_record = receivedNumber + my_tree_record
    show_our_record(our_record)
radio.on_received_number(on_received_number)

# mode 5: Show my completed challenges
def on_pin_pressed_p2():
    show_completed_challenge()
input.on_pin_pressed(TouchPin.P2, on_pin_pressed_p2)


### UTILITY FUCTIONS ###

# Save Data
def save_my_data(is_logo_pressed):
    global my_steps_record
    global my_tree_record
    global current_steps
    global km_input

    # Play effect sound to notify a microbit is attempting to save data
    music.start_melody(music.built_in_melody(Melodies.BA_DING), MelodyOptions.ONCE)
    basic.show_icon(IconNames.YES) # A checked icon is shown
    
    if is_logo_pressed:
        # Convert steps to trees then save to records
        my_steps_record += current_steps # Add current steps to the records
        current_steps = 0 # Reset current steps
    else:
        # Convert km to trees then save to records
        my_steps_record += convert_km_to_steps(km_input) # Add current km to the records
        km_input = 0 # Reset km input

    my_tree_record = convert_steps_to_trees(my_steps_record)
    basic.clear_screen()

# Reset data
def reset_all_data():
    # Play effect sound to notify a microbit is attempting to reset data
    # and reset data.
    global my_steps_record
    global my_tree_record
    global days

    my_steps_record = 0
    my_tree_record = 0
    days = 0
    basic.clear_screen()

# Functions for converting steps/km to the number of trees
def convert_km_to_steps(kilometer):
    # This function converts the number of km to the number of steps
    # and returns the number of steps

    num_of_steps = kilometer * KM_PER_STEP
    return num_of_steps
    
def convert_steps_to_trees(num_of_steps):
    # This function converts the number of steps to the number of trees
    # and returns number of trees by calling 'convert_km_to_trees' function

    km = num_of_steps / KM_PER_STEP
    return convert_km_to_trees(Math.round(km))

def convert_km_to_trees(kilometer):
    # This function converts the number of km to the number of trees
    # and returns number of trees

    total_co2 = kilometer * CO2_PER_KM
    num_of_tree = 0
    if total_co2 >= CO2_PER_TREE :
        num_of_tree = total_co2 / CO2_PER_TREE
    return Math.round(num_of_tree)

# Functions for showing intro and menu
def show_intro():
    music.start_melody(music.built_in_melody(Melodies.CHASE),
            MelodyOptions.FOREVER_IN_BACKGROUND)
    basic.show_string("Hi")
    music.stop_all_sounds()
    basic.show_icon(IconNames.HAPPY)
    basic.clear_screen()

def show_menu():
    # Play 'Do' and show button and a representative icon for mode 1
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
    basic.show_string("shake")
    basic.show_icon(IconNames.EIGTH_NOTE)
    basic.clear_screen()
    pause(500)
    basic.show_icon(IconNames.YES)
    pause(1000)
    basic.show_leds("""
                    . . . . .
                    . # # # .
                    # # . # #
                    # . . . #
                    . # # # .
                    """)
    pause(1000)
    basic.clear_screen()

    # Play 'Re' and show button and a representative icon for mode 2
    music.play_tone(294, music.beat(BeatFraction.WHOLE))
    basic.show_string("KM")
    basic.clear_screen()
    pause(500)
    basic.show_string("A")
    basic.show_arrow(ArrowNames.NORTH)
    pause(500)
    basic.show_string("B")
    basic.show_arrow(ArrowNames.SOUTH)
    pause(500)
    basic.show_icon(IconNames.YES)
    pause(1000)
    basic.clear_screen()
    basic.show_string("A + B")
    pause(1000)
    basic.clear_screen()

    # Play 'Mi' and show button and a representative icon for mode 3
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

    # Play 'Fa' and show button and representative icons for mode 4
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

    # Play 'Sol' and show button and a representative icon for mode 5
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

# Functions for showing my accumulated saved trees record
# and me and my friend's accumulated saved trees record
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
    basic.clear_screen()
    basic.show_number(record)
    basic.pause(2000)
    basic.clear_screen()

# Functions for showing completed challenge by my records
def show_completed_challenge():
    num_of_led = 5

    # Play representative music and an icon for the introduction
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

    # Turn on led lights if users completed assigned challenges.
    if my_tree_record < CHALL_1:
        basic.show_leds("""
                            . # . # .
                            # . # . #
                            # . . . #
                            . # . # .
                            . . # . .
                            """)
        pause(500)
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
        reset_all_data()
    basic.clear_screen()