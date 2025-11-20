function slot (x: number) {
    if (x <= 4) {
        led.unplot(x, 2)
        for (let カウンター = 0; カウンター <= 4; カウンター++) {
            led.plot(x, カウンター)
            basic.pause(100)
            music.play(music.tonePlayable(831, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
            if (input.buttonIsPressed(Button.B)) {
                music.play(music.tonePlayable(988, music.beat(BeatFraction.Sixteenth)), music.PlaybackMode.InBackground)
                配列.push(カウンター)
                if (x == 4) {
                    if (配列 == [
                    0,
                    1,
                    2,
                    3,
                    4
                    ] || 配列 == [
                    4,
                    3,
                    2,
                    1,
                    0
                    ]) {
                        atarisound2()
                        atariBlink(配列)
                        round = 0
                    } else if (配列[0] == 配列[1] && (配列[2] == 配列[3] && (配列[3] == 配列[4] && 配列[4] == 配列[1]))) {
                        atarisound()
                        atariBlink(配列)
                        round = 0
                    } else {
                    	
                    }
                }
                break;
            } else {
                led.unplot(x, カウンター)
            }
            if (カウンター == 4) {
                カウンター = -1
            }
            continue;
        }
    }
}
function atarisound () {
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(494, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(740, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(494, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(740, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(831, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
    music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.InBackground)
}
input.onButtonPressed(Button.A, function () {
    images.createImage(`
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        `).showImage(0)
    caller = 0
    カウンター = 0
    配列 = []
    round += 1
    if (round == 100) {
        led.plot(4, 0)
    } else {
        slot(caller)
    }
})
function atariBlink (y: number[]) {
    for (let カウンター = 0; カウンター <= 4; カウンター++) {
        led.unplot(カウンター, y[カウンター])
    }
    for (let index = 0; index < 8; index++) {
        for (let カウンター = 0; カウンター <= 4; カウンター++) {
            led.toggle(カウンター, y[カウンター])
        }
        basic.pause(200)
    }
}
input.onButtonPressed(Button.B, function () {
    caller += 1
    slot(caller)
})
function atarisound2 () {
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(494, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(659, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(740, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(494, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(740, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(740, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    music.play(music.tonePlayable(784, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(494, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(784, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(880, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(494, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(880, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    music.play(music.tonePlayable(988, music.beat(BeatFraction.Quarter)), music.PlaybackMode.InBackground)
    music.play(music.tonePlayable(1300, music.beat(BeatFraction.Half)), music.PlaybackMode.InBackground)
}
let カウンター = 0
let caller = 0
let round = 0
let 配列: number[] = []
images.createImage(`
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    `).showImage(0)
