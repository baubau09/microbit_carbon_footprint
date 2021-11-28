//  RMIT University Vietnam
//  Course: COSC2500 Introduction to Computer Systems
//  Semester: 2021C
//  Assessment 2 - Microbit Project
// # Student: Tran Phuong Anh (s3914138)
// # Student: Lee Gain (s3878170)
//  Project description: To encourage people to reduce their carbon footprint by walking or using public transportation
//  Created date: 27/11/2021
//  Last modified date: 03/12/2021
//  Variables
radio.setGroup(1)
let days = 0
let current_steps = 0
let my_steps_record = 0
let my_tree_record = 0
let KM_PER_STEP = 1390
let CO2_PER_KM = 83
let CO2_PER_TREE = 21000
let CHALL_1 = 1
let CHALL_2 = 2
let CHALL_3 = 3
let CHALL_4 = 4
let CHALL_5 = 5
let CHALL_6 = 10
let CHALL_7 = 25
let CHALL_8 = 50
let YEAR = 365
// ## INSTRUCTIONS ###
//  Press logo to save current steps records
//  Press pin 0 to show my tree records 
//  Press pin 1 to show me and my friends records
//  Press pin 2 to show my completed challenges
//  On start
show_intro()
if (my_steps_record == 0) {
    show_menu()
}

//  Gesture detection to count current steps
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    current_steps += 1
    basic.showIcon(IconNames.EigthNote)
})
// ## MODES ###
//  mode 1: Save steps data to convert and store trees data
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    
    
    
    basic.showIcon(IconNames.Yes)
    //  A checked icon is shown
    my_steps_record += current_steps
    //  Add current steps to the records
    current_steps = 0
    //  Reset current steps
    //  Convert steps to trees then save to records
    my_tree_record = convert_steps_to_trees(my_steps_record)
    basic.clearScreen()
    // if a year has passed, reset data
    if (days == YEAR) {
        my_steps_record = 0
        my_tree_record = 0
        days = 0
    } else {
        days += 1
    }
    
    basic.clearScreen()
})
//  mode 3: Show accumulated tree records
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    show_my_record()
})
//  mode 4: Friends mode 
//  4.1 Send my tree record to my friend's microbit
input.onPinPressed(TouchPin.P1, function on_pin_pressed_p1() {
    radio.setGroup(1)
    radio.sendNumber(my_tree_record)
    basic.showLeds(`
                    . . . . .
                    # # # # #
                    # # . # #
                    # . # . #
                    # # # # #
                    `)
    basic.pause(2000)
    basic.clearScreen()
})
//  4.2 Calculate the total tree records of me and my friend 
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    
    let our_record = receivedNumber + my_tree_record
    show_our_record(our_record)
})
//  mode 5: Show my completed challenges
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    show_completed_challenge()
})
// ## UTILITY FUCTIONS ###
//  Sound and image effects
function play_effect_sound_dingdong() {
    music.playTone(523, music.beat(BeatFraction.Quarter))
    music.playTone(659, music.beat(BeatFraction.Quarter))
}

function play_effect_sound_the_end() {
    music.playTone(262, music.beat(BeatFraction.Half))
    music.playTone(330, music.beat(BeatFraction.Half))
    music.playTone(392, music.beat(BeatFraction.Half))
}

function congrats_completed_all_challenges() {
    basic.showIcon(IconNames.Heart)
    pause(100)
    basic.clearScreen()
    pause(100)
}

//  Reset data
function reset_all_data() {
    
    
    my_steps_record = 0
    my_tree_record = 0
}

//  Functions for converting steps/km to the number of trees
function convert_km_to_steps(kilometer: number): number {
    let num_of_steps = kilometer * KM_PER_STEP
    return num_of_steps
}

function convert_steps_to_trees(num_of_steps: number): number {
    let km = num_of_steps / KM_PER_STEP
    return convert_km_to_trees(Math.round(km))
}

function convert_km_to_trees(kilometer: number): number {
    let total_co2 = kilometer * CO2_PER_KM
    let num_of_tree = 0
    if (total_co2 >= CO2_PER_TREE) {
        num_of_tree = total_co2 / CO2_PER_TREE
    }
    
    return Math.round(num_of_tree)
}

//  Functions for showing intro, menu, records and challenges
function show_intro() {
    music.startMelody(music.builtInMelody(Melodies.Chase), MelodyOptions.ForeverInBackground)
    basic.showString("Save Earth!")
    music.stopAllSounds()
    basic.showIcon(IconNames.Happy)
    basic.clearScreen()
}

function show_menu() {
    music.playTone(262, music.beat(BeatFraction.Whole))
    basic.showString("p0")
    basic.showLeds(`
                    . . # . .
                    . # # # .
                    . # # # .
                    # # # # #
                    . . # . .
                    `)
    basic.clearScreen()
    music.playTone(294, music.beat(BeatFraction.Whole))
    basic.showString("p0")
    basic.showLeds(`
                    . . # . .
                    . # # # .
                    . # # # .
                    # # # # #
                    . . # . .
                    `)
    basic.clearScreen()
    music.playTone(330, music.beat(BeatFraction.Whole))
    basic.showString("p0")
    basic.showLeds(`
                    . . # . .
                    . # # # .
                    . # # # .
                    # # # # #
                    . . # . .
                    `)
    basic.clearScreen()
    music.playTone(349, music.beat(BeatFraction.Whole))
    basic.showString("p1")
    basic.showLeds(`
                    . . . . .
                    . # . # .
                    # # # # #
                    . # . # .
                    # . # . #
                    `)
    basic.showLeds(`
                    . . # . .
                    . # # # .
                    . # # # .
                    # # # # #
                    . . # . .
                    `)
    basic.clearScreen()
    music.playTone(392, music.beat(BeatFraction.Whole))
    basic.showString("p2")
    basic.showLeds(`
                    . # . # .
                    # . # . #
                    # . . . #
                    . # . # .
                    . . # . .
                    `)
    basic.clearScreen()
    play_effect_sound_the_end()
    basic.showIcon(IconNames.SmallDiamond)
    basic.showIcon(IconNames.Target)
    basic.showIcon(IconNames.Diamond)
    basic.clearScreen()
}

function show_my_record() {
    show_record(my_tree_record)
}

function show_our_record(our_record: number) {
    basic.showLeds(`
                    . . . . .
                    . # . # .
                    # # # # #
                    . # . # .
                    # . # . #
                    `)
    basic.pause(1000)
    show_record(our_record)
}

function show_record(record: number) {
    music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.Once)
    basic.showLeds(`
                    . . # . .
                    . # # # .
                    . # # # .
                    # # # # #
                    . . # . .
                    `)
    basic.pause(1000)
    basic.showNumber(record)
    basic.pause(2000)
    basic.clearScreen()
}

function show_completed_challenge() {
    let i: number;
    let num_of_led = 5
    music.startMelody(music.builtInMelody(Melodies.PowerUp), MelodyOptions.Once)
    basic.showLeds(`
                    . # . # .
                    # . # . #
                    # . . . #
                    . # . # .
                    . . # . .
                    `)
    pause(500)
    basic.clearScreen()
    if (my_tree_record >= CHALL_1) {
        led.plot(2, 4)
    }
    
    pause(500)
    if (my_tree_record >= CHALL_2) {
        led.plot(1, 3)
    }
    
    pause(500)
    if (my_tree_record >= CHALL_3) {
        led.plot(2, 3)
    }
    
    pause(500)
    if (my_tree_record >= CHALL_4) {
        led.plot(3, 3)
    }
    
    pause(500)
    if (my_tree_record >= CHALL_5) {
        i = 0
        while (i < num_of_led) {
            led.plot(i, 2)
            i += 1
        }
    }
    
    pause(500)
    if (my_tree_record >= CHALL_6) {
        i = 0
        while (i < num_of_led) {
            led.plot(i, 1)
            i += 1
        }
    }
    
    pause(500)
    if (my_tree_record >= CHALL_7) {
        led.plot(1, 0)
    }
    
    pause(500)
    if (my_tree_record >= CHALL_8) {
        led.plot(3, 0)
        pause(500)
        congrats_completed_all_challenges()
        congrats_completed_all_challenges()
        congrats_completed_all_challenges()
        reset_all_data()
    }
    
    basic.clearScreen()
}

