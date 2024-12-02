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
SMALL_FONT_SIZE = 15
MEDIUM_FONT_SIZE = 30
BIG_FONT_SIZE = 45
TEXT_MARGIN = 4
MINIMIUM_WIDTH = 100
MAXIMUM_WIDHT = 300
MAXIMUM_HEIGHT = 60
#QSS

BUTTONSCOLOR = "#B6B6B6"
OPBUTTONSCOLOR = "grey"
BORDERRADIUS = ""
BUTTONFONTSIZE = '40px'
BUTTONFONTS = "Roboto Condensed"

BUTTONSTYLESHEET = \
    f"""font-size:{BUTTONFONTSIZE};
      background:{BUTTONSCOLOR}; border-radius:{BORDERRADIUS};"""
OPERATORBUTTONSTYLESHEET = \
    f"""font-size:{BUTTONFONTSIZE};
      background:{OPBUTTONSCOLOR}; border-radius:{BORDERRADIUS}"""
EQUALSBUTTONSTYLESHEET = \
    f"""font-size:{BUTTONFONTSIZE};
      background: black; border-radius:{BORDERRADIUS}; color: white"""
DELETEBUTTONSTYLESHEET = \
    f"""font-size:{BUTTONFONTSIZE};
      background: red; border-radius:{BORDERRADIUS}"""
BACKBUTTONSTYLESHEET = \
    f"""font-size:{BUTTONFONTSIZE};
      background: grey; border-radius:{BORDERRADIUS}; color: black"""