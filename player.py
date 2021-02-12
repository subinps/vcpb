import os
import threading
from queue import Queue
from mpv import MPV
from helpers import run

mpv = MPV()
queue = Queue()
currently_playing = {}

    while True:
        # Blocks until there is an item in the queue, so there won't be a lot of hardware usage
        item = queue.get()
        # Add the current playing item to a different variable, as Queue.queue will not show
        currently_playing = item
        log = None  # Group "Now Playing" message to be deleted if sent

        if "on_start" in item:  # Avoid KeyError
            if item["on_start"]:  # Make sure it is not None
                # True quote to make sure the users understands which song
                run(item["on_start"], quote=True)

        if "log" in item:
            if item["log"]:
                caption = item["log"]["kwargs"]["caption"]
                caption = caption.format(
                    item["url"],
                    item["title"],
                    item["duration"],
                )  # Edit the caption and add the video title (with a link to it) and it's duration
                log = run(item["log"], caption=caption)

        mpv.play(item["file"])
        mpv.wait_for_playback()

        if "on_end" in item:
            if item["on_end"]:
                run(item["on_end"], quote=True)

        if log:  # As said below, if the "Now Playing" message was sent, delete it
            log.delete()

        queue.task_done()


threading.Thread(target=worker, daemon=True).start()


def play(
    file,
    title,
    duration,
    url,
    log=None,
    on_start=None,
    on_end=None,
):
    queue.put(
        {
            "file": file,
            "on_start": on_start,
            "on_end": on_end,
            "title": title,
            "url": url,
            "log": log,
            "duration": duration,
        }
    )


def is_currently_playing() -> bool:
    return mpv.filename
