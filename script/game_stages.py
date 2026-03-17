from host import wait
import audio
import concurrency


def intro():
    concurrency.run_concurrent(audio.play_audio, audio.WELCOME)
    wait(5)
    concurrency.run_concurrent(audio.play_audio, audio.INTRO)
    wait(5)
