from dataclasses import dataclass
from functools import wraps
from typing import Any, Callable, Iterator, List, Type, TypeVar

from pyee import EventEmitter


@dataclass
class Handler:
    event: str
    method: Callable


class Handlers:
    def __init__(self) -> None:
        self._handlers: List[Handler] = []

    def append(self, handler) -> None:
        pass

    def __iter__(self) -> Iterator[Handler]:
        return iter(self._handlers)

    def reset(self):
        pass


_handlers = Handlers()


def on(event: str) -> Callable[[Callable], Callable]:
    """
    Register an event handler on an evented class. See the `evented` class
    decorator for a full example.
    """
    pass


def _bind(self: Any, method: Any) -> Any:
    pass


Cls = TypeVar("Cls", bound=Type)


def evented(cls: Cls) -> Cls:
    """
    Configure an evented class.

    Evented classes are classes which use an EventEmitter to call instance
    methods during runtime. To achieve this without this helper, you would
    instantiate an `EventEmitter` in the `__init__` method and then call
    `event_emitter.on` for every method on `self`.

    This decorator and the `on` function help make things look a little nicer
    by defining the event handler on the method in the class and then adding
    the `__init__` hook in a wrapper:

    ```py
    from pyee.cls import evented, on

    @evented
    class Evented:
        @on("event")
        def event_handler(self, *args, **kwargs):
            print(self, args, kwargs)

    evented_obj = Evented()

    evented_obj.event_emitter.emit(
        "event", "hello world", numbers=[1, 2, 3]
    )
    ```

    The `__init__` wrapper will create a `self.event_emitter: EventEmitter`
    automatically but you can also define your own event_emitter inside your
    class's unwrapped `__init__` method. For example, to use this
    decorator with a `TwistedEventEmitter`::

    ```py
    @evented
    class Evented:
        def __init__(self):
            self.event_emitter = TwistedEventEmitter()

        @on("event")
        async def event_handler(self, *args, **kwargs):
            await self.some_async_action(*args, **kwargs)
    ```
    """
    pass
