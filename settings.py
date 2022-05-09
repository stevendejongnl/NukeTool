from dataclasses import dataclass


@dataclass(frozen=True)
class WindowSettings:
    title: str = 'Nuke Tool'
    width: int = 1280
    height: int = 720
