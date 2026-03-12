

# type annotaions are like hints to the programmer about the type of data that a variable or function parameter is expected to hold. They are not enforced by the Python interpreter, but they can help improve code readability and make it easier for developers to understand the intended use of variables and functions.

# It is similar typescript in javascript. It is a way to specify the type of data that a variable or function parameter is expected to hold. This can help improve code readability and make it easier for developers to understand the intended use of variables and functions.


# for "Any" type annotation, we can use the "typing" module in Python. The "Any" type annotation indicates that a variable or function parameter can be of any type. It is often used when the type of data is not known or when a function can accept multiple types of data.


from typing import Any


def sample_function(data: Any) -> None:
    print(f"The data is: {data}")


# GENERIC Types:

# type parameter in square brackets.

def process_items(items: list[str]):
    for item in items:
        print(item)


# we can also use multiple type parameters in a single function. For example, we can use a tuple to specify the types of multiple parameters.
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


# we can also use a dictionary to specify the types of keys and values in a dictionary. For example, we can use a dictionary to specify that the keys are strings and the values are floats.


def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


# Union Types:

# You can declare that a variable can be any of several types, for example, an int or a str.

# To define it you use the vertical bar (|) to separate both types. This means that item could be an int or a str.

def process_item(item: int | str):
    print(item)

# You can declare that a value could have a type, like str, but that it could also be None. This is useful for optional parameters in functions, where the parameter can be either a specific type or None if it is not provided.

# Using str | None instead of just str will let the editor help you detect errors where you could be assuming that a value is always a str, when it could actually be None too.


def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


# Classes as types

class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name
