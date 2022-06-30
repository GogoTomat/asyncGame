import time
import curses


def draw(canvas):
    row, column = (5, 20)
    canvas.addstr(row, column, '*', curses.A_BOLD)
    canvas.refresh()
    time.sleep(20)


if __name__ == '__main__':
    curses.update_lines_cols()
    curses.wrapper(draw)