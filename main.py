def on_forever():
    pass
basic.forever(on_forever)
def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
