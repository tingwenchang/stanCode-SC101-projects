"""
File: babygraphics.py
Name: Tingwen
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1900.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1910.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1920.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1930.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1940.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1950.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1960.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1970.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1980.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-1990.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-2000.txt',
    '/Users/wenny/Desktop/SC101/SC101_Assignment4/data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    # total width divided the number of years, then times the order of the x location

    x_coordinate = GRAPH_MARGIN_SIZE+int(((width-2*GRAPH_MARGIN_SIZE) / len(YEARS)) * int(year_index))
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, (CANVAS_WIDTH - GRAPH_MARGIN_SIZE), GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE),
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), width=LINE_WIDTH)
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), GRAPH_MARGIN_SIZE - 20,
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE + 20, width=LINE_WIDTH)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX,
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, anchor=tkinter.NW, text=YEARS[i])


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    x = int((CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE) / 12)
    y = (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE)/1000
    y_out = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE

    for i in range(len(lookup_names)):
        name = lookup_names[i]
        print(10)
        for j in range(len(YEARS)-1):
            year = YEARS[j]
            if str(year) in name_data[name]:
                rank = int(name_data[name][str(year)])
                print(6)
            else:
                rank = 1001
                print(7)

            next_year = YEARS[j+1]
            if str(next_year) in name_data[name]:
                next_rank = int(name_data[name][str(next_year)])
                print(8)
            else:
                next_rank = 1001
                print(9)

            if rank > 1000 and next_rank < 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + x * j, y_out,
                                   GRAPH_MARGIN_SIZE + x * (j+1), GRAPH_MARGIN_SIZE + y * next_rank,
                                   width=LINE_WIDTH, fill=COLORS[i % 4])
                canvas.create_text(GRAPH_MARGIN_SIZE + x * j + TEXT_DX, y_out,
                                   text=name+' *', fill=COLORS[i % 4], anchor=tkinter.SW)
                print(1)
            elif rank < 1000 and next_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + x * j, GRAPH_MARGIN_SIZE + y * rank,
                                   GRAPH_MARGIN_SIZE + x * (j+1), y_out, width=LINE_WIDTH, fill=COLORS[i % 4])
                canvas.create_text(GRAPH_MARGIN_SIZE + x * j + TEXT_DX, GRAPH_MARGIN_SIZE + y * rank,
                                   text=name+" "+str(rank), fill=COLORS[i % 4], anchor=tkinter.SW)
                print(2)
            elif rank > 1000 and next_rank > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + x * j, y_out,
                                   GRAPH_MARGIN_SIZE + x * (j+1), y_out, width=LINE_WIDTH, fill=COLORS[i % 4])
                canvas.create_text(GRAPH_MARGIN_SIZE + x * j + TEXT_DX, y_out,
                                   text=name+' *', fill=COLORS[i % 4], anchor=tkinter.SW)
                print(3)
            else:
                canvas.create_line(GRAPH_MARGIN_SIZE + x * j, GRAPH_MARGIN_SIZE + y * rank,
                                   GRAPH_MARGIN_SIZE + x * (j+1), GRAPH_MARGIN_SIZE + y * next_rank,
                                   fill=COLORS[i % 4], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + x * j + TEXT_DX, GRAPH_MARGIN_SIZE + y * rank,
                                   text=name+" "+str(rank), fill=COLORS[i % 4], anchor=tkinter.SW)
                print(4)

            if j+1 == len(YEARS)-1:
                if next_rank > 1000:
                    canvas.create_text(GRAPH_MARGIN_SIZE + x * (j+1) + TEXT_DX, y_out, text=name + ' *',
                               fill=COLORS[i % 4], anchor=tkinter.SW)
                    print(5)
                else:
                    canvas.create_text(GRAPH_MARGIN_SIZE + x * (j+1) + TEXT_DX, GRAPH_MARGIN_SIZE + y * next_rank,
                        text=name+" "+str(next_rank), fill=COLORS[i % 4], anchor=tkinter.SW)
                    print(6)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
