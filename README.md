# Creating a custom dictionary in Python

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

> This exercise is extracted from the book [Python Object-Oriented Programming](https://www.amazon.es/Python-Object-Oriented-Programming-maintainable-object-oriented/dp/1801077266/ref=asc_df_1801077266/?tag=googshopes-21&linkCode=df0&hvadid=529772228567&hvpos=&hvnetw=g&hvrand=17210193121882028235&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9181140&hvtargid=pla-1286085671460&psc=1&mcid=a6e3b83f21283dadbc7c32fb85beaca3)

## Introduction

In Python, we can use different types of collections to store data. The most common ones are lists, tuples, sets, and dictionaries.

All these built-in collections implement the `Collection` protocol, which acts as an abstraction for the different types of collections.

The `Collection` at the same time depends on the `Container`, `Iterable`, and `Sized` protocols.

<details><summary>Container</summary>

- It defines the `__contains__` method, which is used to check if a collection contains a specific element.
- By implementing the `__contains__` method, a collection can be used in the `in`  and `not` operators.

</details>

<details><summary>Iterable</summary>

- It defines the `__iter__` method, which is used to iterate over the elements of a collection.
- By implementing the `__iter__` method, a collection can be used in a `for` loop.

</details>

<details><summary>Sized</summary>

- It defines the `__len__` method, which is used to get the number of elements in a collection.
- By implementing the `__len__` method, a collection can be used in the `len` function.

</details>

## Built-in dictionary

The class diagram of the built-in dictionary is shown below.

> [!IMPORTANT]
> In the [explanation of the commits section](#explanation) we will understand why this class hierarchy is important.

![MappingAbstractions](https://github.com/dimanu-py/python-custom-builtin/assets/61460617/50f03d55-3e57-4726-8bd1-dbbea22ba97e)

> [!NOTE]
> All these class definitions can be found inside _typing.pyi_ and _builtins.pyi_ files.

In Python, we can create a dictionary in two ways using the [overload decorator](https://levelup.gitconnected.com/overload-functions-in-python-d045375cff04):

1. Passing a sequence of key-value pairs to the `dict` constructor.
    
    ```python
    my_dict = dict({"a": 42, "b": 43, "c": 44})
    ```
2. Passing a list of tuples with key-value pairs to the `dict` constructor.

    ```python
    my_dict = dict([("a", 42), ("b", 43), ("c", 44)])
    ```

## Custom dictionary

We want to create a custom immutable dictionary. The goal is to be able to load our dictionary-like mapping once with
its keys and values, and then use it to map the keys to their values.

We want to end up with a type hint like this:

```python
BaseMapping = Mapping[Comparable, Any]
```

We are going to create a dictionary-like mapping from some key to an object of any type.

We've defined the key as `Comparable` because we want to be able to compare the keys and sort them in order.

<a name="explanation"></a>
### Code explanation

The commits of the main branch explain step by step how the process is done.

1. [Defining the `Comparable` protocol](https://github.com/dimanu-py/python-custom-builtin/commit/b628aeb0f8b05c9ec5e7106fb629d4ceeaafca48)
2. [Ho to use `@overload` decorator to allow different signatures](https://github.com/dimanu-py/python-custom-builtin/commit/3291739184e3aec22f2d416914a5c4e1f976c480)
3. [What means to inherit from `Sized`](https://github.com/dimanu-py/python-custom-builtin/commit/794d4bc9340521edc1fa5d45cf8087e85bd1ee7b)
4. [What means to inherit from `Iterable`](https://github.com/dimanu-py/python-custom-builtin/commit/aef85ece930a808fb33caf19a0eb05640b9c596c)
5. [What means to inherit from `Container`](https://github.com/dimanu-py/python-custom-builtin/commit/2a5267ac4038ff5c84e3482223d825da5253d2b2)
6. [What means to inherit from `Mapping`](https://github.com/dimanu-py/python-custom-builtin/commit/eb480e038cd3094509a603ad3e68f74c8ce3cdac)

### Visit my GitHub profile for more projects 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py)
