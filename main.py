steps = 0
test = 0
days: List[number] = []
navigation: List[string] = [
    'Press Logo to save your record at the end of each day',
    'Press A to view the trees saved in 30 days',
    'Press B to view completed challenges',
    'Press A and B together to show the record of me and my friends'
]

for option in navigation:
    basic.show_string(option)

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

def convert_steps():
    global steps

