from host import wait
import audio
import assets
import concurrency


def intro():
    concurrency.run_concurrent(audio.play_audio, assets.WELCOME)
    wait(5)
    concurrency.run_concurrent(audio.play_audio, assets.INTRO)
    wait(5)
