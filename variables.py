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
ALLOWEDCHARS = "1234567890-+/*."
#Sizing
SMALL_FONT_SIZE = 20
MEDIUM_FONT_SIZE = 30
BIG_FONT_SIZE = 50
TEXT_MARGIN = 1
MINIMIUM_WIDTH = 100
#QSS

BUTTONSCOLOR = "#B6B6B6"
OPBUTTONSCOLOR = "grey"
BORDERRADIUS = ""
BUTTONFONTSIZE = '40px'


BUTTONSTYLESHEET = \
    f"font-size:{BUTTONFONTSIZE}; background:{BUTTONSCOLOR}; border-radius:{BORDERRADIUS}"
OPERATORBUTTONSTYLESHEET = \
    f"font-size:{BUTTONFONTSIZE}; background:{OPBUTTONSCOLOR}; border-radius:{BORDERRADIUS}"
EQUALSBUTTONSTYLESHEET = \
    f"font-size:{BUTTONFONTSIZE}; background: {OPBUTTONSCOLOR}; border-radius:{BORDERRADIUS}"
DELETEBUTTONSTYLESHEET = \
    f"font-size:{BUTTONFONTSIZE}; background: red; border-radius:{BORDERRADIUS}"