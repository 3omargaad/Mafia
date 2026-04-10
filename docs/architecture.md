assets/
    audio/
        player_names/
            ...

        preset/
            uk/
                detective_sleep.ogg
                detective.ogg
                discuss.ogg
                doctor_sleep.ogg
                doctor.ogg
                execution.ogg
                fortunately.ogg
                game_continues.ogg
                game_over.ogg
                intro.ogg
                mafia_sleep.ogg
                mafia.ogg
                morning.ogg
                night.ogg
                reveal.ogg
                unfortunately.ogg
                vote.ogg
                welcome.ogg

    fonts/
        PressStart2P-Regular.ttf
        RobotoSlab-Medium.ttf
        Rye-Regular.ttf

    images/
        ...

bin/
    accents.py

src/
    gui/
        kivy_gui/
            app.kv              | Main file to load all Screens
            common.kv           | Common widget attributes across Screens
            end.kv              | Kivy code for End Screen UI
            game.kv             | Kivy code for Game Screen UI
            login.kv            | Kivy code for Login Screen UI
            player.kv           | Kivy code for Player Screen UI
            role.kv             | Kivy code for Role Screen UI
            setup.kv            | Kivy code for Setup Screen UI

        python_gui/
            game_screen.py          | Python code for Game Screen Object
            login_screen.py         | Python code for Login Screen Object
            player_screen.py        | Python code for Player Screen Object
            role_screen.py          | Python code for Role Screen Object
            setup_screen.py         | Python code for Setup Screen Object
            end_screen.py           | Python code for End Screen Object

    main.py                 | Runs the main program
    app.py                  | Sets up the application
    background.py           | Creates the background gradient
    screens.py              | Manages functionality of screens
    assets.py               | Stores the paths to assets
    audio.py                | Functionality for running audio
    game_setup.py           | Defines game object
    player.py               | Defines player object
    narrative.py            | Stores core in game text
    concurrency.py          | Allows for threading
    roles.py                | Assigns roles randomly
    ui_control.py           | Main module for controllling ui changes
