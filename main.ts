let steps = 0
let days : number[] = []
function on_gesture_shake() {
    
    steps += 1
}

input.onGesture(Gesture.Shake, on_gesture_shake)
input.onGesture(Gesture.Shake, on_gesture_shake)
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    let steps: number;
    days.push(steps)
    steps = 0
})
