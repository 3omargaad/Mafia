import threading


def run_concurrent(func, *args, **kwargs):
    """Run a function in a separate thread to allow concurrent execution."""
    thread = threading.Thread(target=func, args=args, kwargs=kwargs)
    thread.start()
    return thread
