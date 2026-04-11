from threading import Thread


def run_concurrent(func, *args, **kwargs):
    """Run a function in a separate thread to allow concurrent execution."""
    thread = Thread(target=func, args=args, kwargs=kwargs)
    thread.start()
    return thread

# Allows two functions to run at the same time (mainly used for sound)
