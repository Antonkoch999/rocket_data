"""This module contains custom decorators."""

import django.db
import time
import functools


def query_debugger(func):
    """Required to test the number of database queries."""
    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        django.db.reset_queries()

        start_queries = len(django.db.connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(django.db.connection.queries)

        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func
