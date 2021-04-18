def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
    music.play_tone(440, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    music.play_tone(330, music.beat(BeatFraction.WHOLE))
    basic.show_icon(IconNames.HOUSE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play_tone(523, music.beat(BeatFraction.WHOLE))
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.B, on_button_pressed_b)
