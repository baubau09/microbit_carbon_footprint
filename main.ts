let steps = 0
let test = 0
let tree_record = 0
let STEP_PER_KM = 1390
let CO2_PER_KM = 0.083
let CO2_PER_TREE = 21
let days : number[] = []
let navigation = ["Press Logo to save your record at the end of each day", "Press A to view the trees saved in 30 days", "Press B to view completed challenges", "Press A and B together to show the record of me and my friends"]
basic.forever(function on_forever() {
    
    for (let option of navigation) {
        basic.showString(option)
    }
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    steps += 1
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    
    days.push(steps)
    steps = 0
})
function convert_steps() {
    
}

function convert_km_to_trees(kilometer: number): number {
    let total_co2 = kilometer * CO2_PER_KM
    let num_of_tree = CO2_PER_TREE / total_co2
    return num_of_tree
}

function convert_steps_to_trees(): number {
    let km = steps / STEP_PER_KM
    return convert_km_to_trees(km)
}

function show_my_record() {
    music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.Once)
    basic.showLeds(`
                . . # . .
                . # # # .
                . # # # .
                # # # # #
                . . # . .
    `)
    basic.pause(1000)
    basic.showNumber(tree_record)
    basic.pause(2000)
    basic.clearScreen()
}

