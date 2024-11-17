from pathlib import Path

__all__ = [
    "ICONDIR",
    "SMALL_FONT_SIZE",
    "MEDIUM_FONT_SIZE",
    "BIG_FONT_SIZE",
    "TEXT_MARGIN",
    "MINIMIUM_WIDTH"
]

ICONDIR = str(Path(__file__).parent / "assets/images/calculatoricon.ico")

#Sizing
SMALL_FONT_SIZE = 20
MEDIUM_FONT_SIZE = 30
BIG_FONT_SIZE = 50
TEXT_MARGIN = 4
MINIMIUM_WIDTH = 200