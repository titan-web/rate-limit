"""An implementation of the token bucket algorithm.
"""
from time import time


class TokenBucket(object):

    def __init__(self, capacity, fill_rate, is_lock=False):
        """
        :param capacity:  The total tokens in the bucket.
        :param fill_rate:  The rate in tokens/second that the bucket will be refilled
        """
        self._capacity = float(capacity)
        self._tokens = float(capacity)
        self._fill_rate = float(fill_rate)
        self._init_time = time()
        self._is_lock = is_lock

    @property
    def tokens(self):
        if self._tokens < self._capacity:
            now = time()
            delta = self._fill_rate * (now - self._init_time)
            self._tokens = min(self._capacity, self._tokens + delta)
            self._init_time = now
        return self._capacity

    def can_consume(self, tokens):
        if tokens <= self.tokens:
            self._tokens -= tokens
            return True
        return False
