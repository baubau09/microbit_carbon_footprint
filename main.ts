let steps = 0
let test = 0
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

