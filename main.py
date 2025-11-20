def slot(x: number):
    global round2
    if x <= 4:
        led.unplot(x, 2)
        for カウンター in range(5):
            led.plot(x, カウンター)
            basic.pause(100)
            music.play(music.tone_playable(831, music.beat(BeatFraction.SIXTEENTH)),
                music.PlaybackMode.IN_BACKGROUND)
            if input.button_is_pressed(Button.B):
                music.play(music.tone_playable(988, music.beat(BeatFraction.SIXTEENTH)),
                    music.PlaybackMode.IN_BACKGROUND)
                配列.append(カウンター)
                if x == 4:
                    if 配列 == [0, 1, 2, 3, 4] or 配列 == [4, 3, 2, 1, 0]:
                        atarisound2()
                        atariBlink(配列)
                        round2 = 0
                    elif 配列[0] == 配列[1] and (配列[2] == 配列[3] and (配列[3] == 配列[4] and 配列[4] == 配列[1])):
                        atarisound()
                        atariBlink(配列)
                        round2 = 0
                    else:
                        pass
                break
            else:
                led.unplot(x, カウンター)
            if カウンター == 4:
                カウンター = -1
            continue
def atarisound():
    music.play(music.tone_playable(659, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(740, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(740, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(831, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.IN_BACKGROUND)
    music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.IN_BACKGROUND)

def on_button_pressed_a():
    global caller, カウンター4, 配列, round2
    images.create_image("""
        . . . . .
        . . . . .
        # # # # #
        . . . . .
        . . . . .
        """).show_image(0)
    caller = 0
    カウンター4 = 0
    配列 = []
    round2 += 1
    if round2 == 100:
        led.plot(4, 0)
    else:
        slot(caller)
input.on_button_pressed(Button.A, on_button_pressed_a)

def atariBlink(y: List[number]):
    for カウンター2 in range(5):
        led.unplot(カウンター2, y[カウンター2])
    for index in range(8):
        for カウンター3 in range(5):
            led.toggle(カウンター3, y[カウンター3])
        basic.pause(200)

def on_button_pressed_b():
    global caller
    caller += 1
    slot(caller)
input.on_button_pressed(Button.B, on_button_pressed_b)

def atarisound2():
    music.play(music.tone_playable(659, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(659, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(740, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(740, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(740, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.IN_BACKGROUND)
    music.play(music.tone_playable(784, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(784, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(880, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(494, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(880, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.tone_playable(988, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.IN_BACKGROUND)
    music.play(music.tone_playable(1300, music.beat(BeatFraction.HALF)),
        music.PlaybackMode.IN_BACKGROUND)
カウンター4 = 0
caller = 0
round2 = 0
配列: List[number] = []
images.create_image("""
    . . . . .
    . . . . .
    # # # # #
    . . . . .
    . . . . .
    """).show_image(0)