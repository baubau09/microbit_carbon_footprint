steps = 0
days: List[number] = []

def on_gesture_shake():
    global steps
    steps += 1
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    days.append(steps)
    steps = 0

input.on_gesture(Gesture.SHAKE, on_gesture_shake)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)
