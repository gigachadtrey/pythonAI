import curses
import subprocess
import shlex  # Used for parsing shell commands with spaces

def main(stdscr):
  # Initialize color mode
  curses.start_color()

  # Define color pairs (foreground, background)
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)  # Default white on blue
  curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Highlighted black on white

  # Use the color pair as the default background
  stdscr.bkgd(' ', curses.color_pair(1))
  stdscr.clear()

  # Center text and button text
  h, w = stdscr.getmaxyx()
  text = "Launch AI?"
  yes_text = "[ Yes ]"
  no_text = "[  No  ]"

  text_x = w // 2 - len(text) // 2
  yes_x = w // 2 - len(yes_text) // 2 - 5
  no_x = w // 2 - len(no_text) // 2 + 5

  y = h // 2

  current_option = 0  # 0 = Yes, 1 = No

  while True:
    stdscr.clear()

    # Draw the main text
    stdscr.addstr(y, text_x, text, curses.color_pair(1))

    # Highlight the selected button
    if current_option == 0:
      stdscr.addstr(y + 2, yes_x, yes_text, curses.color_pair(2))
    else:
      stdscr.addstr(y + 2, yes_x, yes_text, curses.color_pair(1))

    if current_option == 1:
      stdscr.addstr(y + 2, no_x, no_text, curses.color_pair(2))
    else:
      stdscr.addstr(y + 2, no_x, no_text, curses.color_pair(1))

    stdscr.refresh()

    # Wait for user input
    key = stdscr.getch()

    # Navigate between options using left and right arrow keys
    if key == curses.KEY_LEFT:
      current_option = 0
    elif key == curses.KEY_RIGHT:
      current_option = 1
    elif key == ord('\n'):
      # Implement your button press actions here
      if current_option == 0:
        # Launch AI.py directly
        subprocess.run(["python", "AI.py"])
      else:
        print("No button pressed!")
        break

    # Clean up and exit
    curses.endwin()


if __name__ == "__main__":
  curses.wrapper(main)