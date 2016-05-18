"""An implementation of the leaky bucket algorithm.
"""
from time import time

__all__ = ("LeakyBucket", )


class LeakyBucket(object):

    def __init__(self, capacity, fill_rate, is_lock=False):
        """
        :param capacity:  The total tokens in the bucket.
        :param fill_rate:  The rate in tokens/second that the bucket will be refilled
        """
        self._capacity = float(capacity)
        self._cur_tokens = 0
        self._fill_rate = float(fill_rate)
        self._is_lock = is_lock
        self._last_time = time()

    def get_cur_tokens(self):
        now = time()
        delta = self._fill_rate * (now - self._last_time)
        self._cur_tokens = max(0, self._cur_tokens + delta)
        return self._cur_tokens

    def _consume(self, tokens):
        if tokens <= self.get_cur_tokens():
            self._cur_tokens += tokens
            return True
        return False

    def consume(self, tokens):
        return self._consume(tokens)
