import os


class StaticMapsConfig:
    MAPS_API_KEY = os.getenv("MAPS_API_KEY")


class KandinskyConfig:
    KANDINSKY_API_KEY = os.getenv("KANDINSKY_API_KEY")
    KANDINSKY_SECRET_KEY = os.getenv("KANDINSKY_SECRET_KEY")
