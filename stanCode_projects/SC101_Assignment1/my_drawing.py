"""
File:
Name: Ting Wen
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: My Favorite Cartoon
    Guess what! My favorite cartoon is Spongebob~~~~ When I feel exhausted after everyday classes, I watch Spongebob
    to relax and lol. I like to see those characters do dumb dumb thing, because it's really cute!!
    """
    window = GWindow(width=800, height=450)
    background_p = GRect(400, 450, x=0, y=0)
    window.add(background_p)
    background_p.filled = True
    background_p.fill_color = 'pink'
    background_p.color = 'pink'
    eyes_p = GOval(120, 200, x=70, y=160)
    window.add(eyes_p)
    eyes_p.filled = True
    eyes_p.fill_color = 'white'
    eyes_p1 = GOval(120, 200, x=190, y=160)
    window.add(eyes_p1)
    eyes_p1.filled = True
    eyes_p1.fill_color = 'white'
    eyes_p2 = GOval(30, 30, x=145, y=250)
    window.add(eyes_p2)
    eyes_p2.filled = True
    eyes_p3 = GOval(30, 30, x=205, y=250)
    window.add(eyes_p3)
    eyes_p3.filled = True
    eyebrow = GPolygon()
    eyebrow.add_vertex((130, 80))
    eyebrow.add_vertex((150, 100))
    eyebrow.add_vertex((50, 200))
    eyebrow.add_vertex((30, 180))
    window.add(eyebrow)
    eyebrow.filled = True
    eyebrow1 = GPolygon()
    eyebrow1.add_vertex((250, 80))
    eyebrow1.add_vertex((230, 100))
    eyebrow1.add_vertex((330, 200))
    eyebrow1.add_vertex((350, 180))
    window.add(eyebrow1)
    eyebrow1.filled = True
    background_s = GRect(400, 450, x=400, y=0)
    window.add(background_s)
    background_s.filled = True
    background_s.fill_color = 'yellow'
    background_s.color = 'yellow'
    eyelash = GPolygon()
    eyelash.add_vertex((463, 120))
    eyelash.add_vertex((445, 130))
    eyelash.add_vertex((495, 200))
    window.add(eyelash)
    eyelash.filled = True
    eyelash1 = GPolygon()
    eyelash1.add_vertex((505, 110))
    eyelash1.add_vertex((523, 110))
    eyelash1.add_vertex((518, 200))
    window.add(eyelash1)
    eyelash1.filled = True
    eyelash2 = GPolygon()
    eyelash2.add_vertex((580, 130))
    eyelash2.add_vertex((565, 120))
    eyelash2.add_vertex((535, 200))
    window.add(eyelash2)
    eyelash2.filled = True
    eyelash3 = GPolygon()
    eyelash3.add_vertex((630, 120))
    eyelash3.add_vertex((615, 130))
    eyelash3.add_vertex((655, 200))
    window.add(eyelash3)
    eyelash3.filled = True
    eyelash4 = GPolygon()
    eyelash4.add_vertex((670, 110))
    eyelash4.add_vertex((689, 110))
    eyelash4.add_vertex((678, 200))
    window.add(eyelash4)
    eyelash4.filled = True
    eyelash5 = GPolygon()
    eyelash5.add_vertex((745, 135))
    eyelash5.add_vertex((730, 125))
    eyelash5.add_vertex((695, 200))
    window.add(eyelash5)
    eyelash5.filled = True
    eyes_s = GOval(150, 150, x=450, y=170)
    window.add(eyes_s)
    eyes_s.filled = True
    eyes_s.fill_color = 'white'
    eyes_s1 = GOval(150, 150, x=600, y=170)
    window.add(eyes_s1)
    eyes_s1.filled = True
    eyes_s1.fill_color = 'white'
    eyes_s2 = GOval(50, 50, x=500, y=220)
    window.add(eyes_s2)
    eyes_s2.filled = True
    eyes_s2.fill_color = 'skyblue'
    eyes_s2.color = 'skyblue'
    eyes_s3 = GOval(50, 50, x=650, y=220)
    window.add(eyes_s3)
    eyes_s3.filled = True
    eyes_s3.fill_color = 'skyblue'
    eyes_s3.color = 'skyblue'
    eyes_s4 = GOval(20, 20, x=515, y=235)
    window.add(eyes_s4)
    eyes_s4.filled = True
    eyes_s5 = GOval(20, 20, x=665, y=235)
    window.add(eyes_s5)
    eyes_s5.filled = True
    nose = GOval(50, 62, x=575, y=285)
    window.add(nose)
    nose.filled = True
    nose.fill_color = 'yellow'


if __name__ == '__main__':
    main()
