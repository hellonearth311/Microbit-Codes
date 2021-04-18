input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Heart)
    music.playTone(440, music.beat(BeatFraction.Whole))
})
input.onButtonPressed(Button.AB, function () {
    music.playTone(330, music.beat(BeatFraction.Whole))
    basic.showIcon(IconNames.House)
})
input.onButtonPressed(Button.B, function () {
    music.playTone(523, music.beat(BeatFraction.Whole))
    basic.showIcon(IconNames.Happy)
})
