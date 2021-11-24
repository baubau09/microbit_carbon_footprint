let steps = 0
let days : number[] = []
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    steps += 1
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    
    
    days.push(steps)
    steps = 0
})
