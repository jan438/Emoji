import os
import sys
import unicodedata
from pathlib import Path
from datetime import datetime, date, timedelta
from ics import Calendar, Event
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER, A4, landscape, portrait
from reportlab.lib.units import inch
from reportlab.lib.colors import blue, green, black, red, pink, gray, brown, purple, orange, yellow, white
from reportlab.pdfbase import pdfmetrics  
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Image, Spacer, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER

def binairtostr(s, c):
    f = ""
    o = 4
    for i in range(c):
        f = f + s[o] + s[o+1]
        o = o + 4
    return f

def unicodetostr(code):
    u = code.encode("utf-8")
    s = str(u)
    f = binairtostr(s, len(u))
    print(s, f)
    return f

if sys.platform[0] == 'l':
    path = '/home/jan/git/Emoji'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Emoji"
os.chdir(path)
unicode1 = u"\u26BD"
f = unicodetostr(unicode1)
unicode2 = "\U0001F339"
f = unicodetostr(unicode2)
unicodeb = "\U0001F004"
unicode3 = "\U0001F38A"
unicodee = "\U0001F6C5"
print(unicode2, f)
nfn = "Ubuntu"
efn = 'Segeo UI Emoji'
pdfmetrics.registerFont(TTFont(efn, 'segoe-ui-emoji.ttf'))
pdfmetrics.registerFont(TTFont(nfn, 'Ubuntu-Regular.ttf'))
styles = getSampleStyleSheet()
normalStyle = ParagraphStyle('nrm', parent=styles['Normal'], fontName = nfn, fontSize = 24)
emojiStyle = ParagraphStyle('emo', parent=styles['Normal'], fontName = efn, fontSize = 24)
normalParagraph = Paragraph("hallo" + "<font name = " + nfn + ">" + "abc" + "</font>", normalStyle )
emojiParagraph1 = Paragraph("<font name = " + nfn + ">" + "hallo" + "</font>" + "😎😛🙈🏈" + unicode1 + unicode2 + unicodeb + unicode3 + unicodee + u"\xbc" +  u"\xbc\xbc" + u"\u2022" + "<font name = " + nfn + ">" + "hallo" + "</font>", emojiStyle )
emojiParagraph2 = Paragraph("<font name = " + nfn + ">" + "hallo" + "</font>" + "😎" + "<font name = " + nfn + ">" + "hallo" + "</font>", emojiStyle )
emojiname = "PDF/Emoji.pdf"
doc = SimpleDocTemplate(emojiname, pagesize=landscape(A4), rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)
storypdf=[]
storypdf.append(normalParagraph)
storypdf.append(Spacer(width=10, height=50))
storypdf.append(emojiParagraph1)
storypdf.append(Spacer(width=10, height=50))
storypdf.append(emojiParagraph2)
doc.build(storypdf)
key = input("Wait")