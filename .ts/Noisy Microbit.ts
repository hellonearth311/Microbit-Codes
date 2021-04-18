input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    basic.showNumber(randint(0, 100))
    basic.showIcon(IconNames.Heart)
    music.playMelody("C5 A B G A F G E ", 500)
})
