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

def bytetostr(byte):
    hexchars = [[] for _ in range(16)]
    hexchars[0] = "0"
    hexchars[1] = "1"
    hexchars[2] = "2"
    hexchars[3] = "3"
    hexchars[4] = "4"
    hexchars[5] = "5"
    hexchars[6] = "6"
    hexchars[7] = "7"
    hexchars[8] = "8"
    hexchars[9] = "9"
    hexchars[10] = "A"
    hexchars[11] = "B"
    hexchars[12] = "C"
    hexchars[13] = "D"
    hexchars[14] = "E"
    hexchars[15] = "F"


    print(byte)

def unicodetostr(code):
    u = code.encode("utf-8")
    for i in range(len(u)):
        bytetostr(u[i])
    print(code, len(code), u, len(u))

if sys.platform[0] == 'l':
    path = '/home/jan/git/Emoji'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Emoji"
os.chdir(path)
unicode1 = u"\u26BD"
unicodetostr(unicode1)
unicode2 = "\U0001F339"
unicodetostr(unicode2)
nfn = "Ubuntu"
efn = 'Segeo UI Emoji'
pdfmetrics.registerFont(TTFont(efn, 'segoe-ui-emoji.ttf'))
pdfmetrics.registerFont(TTFont(nfn, 'Ubuntu-Regular.ttf'))
styles = getSampleStyleSheet()
normalStyle = ParagraphStyle('nrm', parent=styles['Normal'], fontName = nfn, fontSize = 24)
emojiStyle = ParagraphStyle('emo', parent=styles['Normal'], fontName = efn, fontSize = 24)
normalParagraph = Paragraph("hallo" + "<font name = " + nfn + ">" + "abc" + "</font>", normalStyle )
emojiParagraph = Paragraph("<font name = " + nfn + ">" + "hallo" + "</font>" + "😎😛🙈🏈" + unicode1 + unicode2 + u"\xbc" +  u"\xbc\xbc" + u"\u2022" + "<font name = " + nfn + ">" + "hallo" + "</font>", emojiStyle )
emojiname = "PDF/Emoji.pdf"
doc = SimpleDocTemplate(emojiname, pagesize=landscape(A4), rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)
storypdf=[]
storypdf.append(normalParagraph)
storypdf.append(Spacer(width=10, height=50))
storypdf.append(emojiParagraph)
doc.build(storypdf)
key = input("Wait")