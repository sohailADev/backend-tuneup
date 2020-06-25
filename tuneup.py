#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = "sohailadev"

import cProfile
import pstats
import functools
import timeit
from collections import Counter


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        profile = cProfile.Profile()
        profile.enable()
        value = func(*args, **kwargs)
        profile.disable()
        get_stats_obj = pstats.Stats(profile).strip_dirs(
        ).sort_stats('cumulative').print_stats()
        return value

    return wrapper_timer


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Returns True if title is within movies list."""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    counter = Counter(movies)
    duplicates = []
    for key, Value in counter.items():
        if Value > 1:
            duplicates.append(key)

    return duplicates


def timeit_helper():
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(stmt="find_duplicate_movies ('moveies.txt') ",setup=" __main__ import find_duplicate_movies")
    result = min(t.repeat(repeat=7, number=5)) / 5
    print("Best time across 7 rep of 5 runs per/rep " + str(result) + " sec")


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()
