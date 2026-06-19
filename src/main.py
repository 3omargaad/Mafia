from kivy.config import Config
from kivy.resources import resource_add_path
import app

if __name__ == "__main__":
    Config.write()
    resource_add_path("./")
    # Adds Global File Paths

    app.run()

# Runs main application
