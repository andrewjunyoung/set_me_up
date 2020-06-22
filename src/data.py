from dataclasses import dataclass


@dataclass
class Step:
    fn: Callable
    gui: bool = False

    def exec(self) -> None:
        if self.gui:
            self.fn()

