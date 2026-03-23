src/
    kivy_gui/
        app.kv              | Main file to load all screens
        common.kv           | Common widget attributes across screens
        game.kv             | Holds game screen ui
        login.kv            | Holds login screen ui
        player.kv           | Holds player screen ui
        role.kv             | Holds role screen ui
        setup.kv            | Holds setup screen ui

    main.py                 | Runs the main program
    app.py                  | Sets up the application
    background.py           | Creates the background gradient
    screens.py              | Manages functionality of screens
    assets.py               | Stores the paths to assets
    audio.py                | Functionality for running audio
    game_setup.py           | Defines game object
    player.py               | Defines player object
    narrative.py            | Stores in game text
    concurrency.py          | Allows for threading