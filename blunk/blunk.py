from multiprocessing.pool import ThreadPool
from threading import Lock
from typing import Callable

_receivers_mutex = Lock()

_receivers = {}


def send(channel: str, **kwargs):
    _receivers_mutex.acquire()

    if channel not in _receivers:
        raise RuntimeError(f'No receivers register for channel {channel}.')

    try:
        def run_receiver(receiver):
            receiver(**kwargs)

        with ThreadPool(5) as pool:
            pool.map(run_receiver, _receivers.get(channel, []))

    finally:
        _receivers_mutex.release()


def register(channel: str, handler: Callable):
    _receivers_mutex.acquire()
    try:
        _receivers.setdefault(channel, []).append(handler)
    finally:
        _receivers_mutex.release()


def unregister_for_channel(channel: str, handler: Callable):
    _receivers_mutex.acquire()
    try:
        _receivers.get('channel').remove(handler)
    finally:
        _receivers_mutex.release()


def unregister_for_handler(handler: Callable):
    _receivers_mutex.acquire()
    try:
        for k, v in _receivers.items():
            if handler in v:
                v.remove(handler)
    finally:
        _receivers_mutex.release()
