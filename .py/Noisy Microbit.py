def on_logo_touched():
    basic.show_number(randint(0, 100))
    basic.show_icon(IconNames.HEART)
    music.play_melody("C5 A B G A F G E ", 500)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)
