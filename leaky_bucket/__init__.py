"""An implementation of the leaky bucket algorithm.
"""
from time import time
from threading import RLock

__all__ = ("LeakyBucket", )


class LeakyBucket(object):

    def __init__(self, capacity, leak_rate, is_lock=False):
        """
        :param capacity:  The total tokens in the bucket.
        :param leak_rate:  The rate in tokens/second that the bucket leaks
        """
        self._capacity = float(capacity)
        self._used_tokens = 0
        self._leak_rate = float(leak_rate)
        self._last_time = time()
        self._lock = RLock() if is_lock else None

    def get_used_tokens(self):
        if self._lock:
            with self._lock:
                return self._get_used_tokens()
        else:
            return self._get_used_tokens()

    def _get_used_tokens(self):
        now = time()
        delta = self._leak_rate * (now - self._last_time)
        self._used_tokens = max(0, self._used_tokens - delta)
        return self._used_tokens

    def _consume(self, tokens):
        if tokens + self._get_used_tokens() <= self._capacity:
            self._used_tokens += tokens
            self._last_time = time()
            return True
        return False

    def consume(self, tokens):
        if self._lock:
            with self._lock:
                return self._consume(tokens)
        else:
            return self._consume(tokens)
