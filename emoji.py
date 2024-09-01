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


if sys.platform[0] == 'l':
    path = '/home/jan/git/Emoji'
if sys.platform[0] == 'w':
    path = "C:/Users/janbo/OneDrive/Documents/GitHub/Emoji"
os.chdir(path)
pdfmetrics.registerFont(TTFont('Segeo UI Emoji', 'segoe-ui-emoji.ttf'))
styles = getSampleStyleSheet()
emojiStyle = ParagraphStyle('emoji', parent=styles['Normal'], fontName = "Segeo UI Emoji", fontSize = 24)
emojiParagraph = Paragraph("hallo😎😛🙈🏈⚽", emojiStyle )
emojiname = "PDF/Emoji.pdf"
doc = SimpleDocTemplate(emojiname, pagesize=landscape(A4), rightMargin=5, leftMargin=5, topMargin=5, bottomMargin=5)
storypdf=[]
storypdf.append(emojiParagraph)
doc.build(storypdf)
key = input("Wait")