import sys
import os
import traceback

import app

PATH = '/data/data/org.test.mafia'
logpath = os.path.join(os.environ.get('ANDROID_PRIVATE', PATH), 'crash.log')


def excepthook(exc_type, exc, tb):
    with open(logpath, 'w') as f:
        traceback.print_exception(exc_type, exc, tb, file=f)
    sys.__excepthook__(exc_type, exc, tb)


sys.excepthook = excepthook


if __name__ == "__main__":
    app.run()
