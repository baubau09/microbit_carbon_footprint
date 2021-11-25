// Varibles
let steps = 0
let test = 0
let my_tree_record = 0
let STEP_PER_KM = 1390
let CO2_PER_KM = 0.083
let CO2_PER_TREE = 21
let CHALL_1 = 1
let CHALL_2 = 2
let CHALL_3 = 3
let CHALL_4 = 4
let CHALL_5 = 5
let CHALL_6 = 10
let CHALL_7 = 50
let CHALL_8 = 100
let days : number[] = []
let navigation = ["Press Logo to save your record at the end of each day", "Press A to view the trees saved in 30 days", "Press B to view completed challenges", "Press A and B together to show the record of me and my friends"]
// Modes
// on start
for (let option of navigation) {
    basic.showString(option)
}
// mode 1
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    steps += 1
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    
    days.push(steps)
    steps = 0
})
// mode 3
input.onPinPressed(TouchPin.P0, function on_pin_pressed_p0() {
    show_my_record()
})
// mode 4
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
radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    let our_record = receivedNumber + my_tree_record
    show_our_record(our_record)
})
// mode 5
input.onPinPressed(TouchPin.P2, function on_pin_pressed_p2() {
    show_completed_challenge()
})
// Functions
// functions for converting steps/km to the number of trees 
function convert_km_to_trees(kilometer: number): number {
    let total_co2 = kilometer * CO2_PER_KM
    let num_of_tree = CO2_PER_TREE / total_co2
    return num_of_tree
}

function convert_steps_to_trees(): number {
    let km = steps / STEP_PER_KM
    return convert_km_to_trees(km)
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

// functions for showing records and challenges
function show_my_record() {
    show_record(my_tree_record)
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
    if (my_tree_record >= CHALL_1) {
        led.plot(2, 4)
    }
    
    if (my_tree_record >= CHALL_2) {
        led.plot(1, 3)
    }
    
    if (my_tree_record >= CHALL_3) {
        led.plot(2, 3)
    }
    
    if (my_tree_record >= CHALL_4) {
        led.plot(3, 3)
    }
    
    if (my_tree_record >= CHALL_5) {
        i = 0
        while (i < num_of_led) {
            led.plot(i, 2)
            i += 1
        }
    }
    
    if (my_tree_record >= CHALL_6) {
        i = 0
        while (i < num_of_led) {
            led.plot(i, 1)
            i += 1
        }
    }
    
    if (my_tree_record >= CHALL_7) {
        led.plot(1, 0)
    }
    
    if (my_tree_record >= CHALL_8) {
        led.plot(3, 0)
    }
    
    basic.pause(3000)
    basic.clearScreen()
}

