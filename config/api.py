from dataclasses import dataclass
import os


@dataclass
class StaticMapsConfig:
    MAPS_API_KEY: str = os.getenv("MAPS_API_KEY")


@dataclass
class KandinskyConfig:
    KANDINSKY_API_KEY: str = os.getenv("KANDINSKY_API_KEY")
    KANDINSKY_SECRET_KEY: str = os.getenv("KANDINSKY_SECRET_KEY")
