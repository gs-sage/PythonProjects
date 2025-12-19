# Static method
"""Methods that don't use the self parameter and work at class level"""

class Student:
    @staticmethod # decorator
    def hello():
        print("hello")

"""Decorators allow us to wrap another function in order to extend the behavior of the wrapped function
without permanently modifying it."""