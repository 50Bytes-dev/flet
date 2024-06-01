from typing import TypeVar, Type, Any, Callable, Generic


T = TypeVar("T")
R = TypeVar("R")


class classproperty(Generic[T, R]):
    def __init__(self, func: Callable[[Type[T]], R]) -> None:
        self.func = func

    def __get__(self, obj: Any, cls: Type[T]) -> R:
        return self.func(cls)
