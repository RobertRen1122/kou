# prelim
on a laptop you only need to click two times:
1. date
2. book court
you will need to select the court number beforehand. if you select court 3, you still be at court 3 even when click the same date again.

# how to use
1. install all the necessary dependencies, main one is `pyautogui`
2. run `python coords.py` to confirm the coordinate of the data button (you will need to move your mouse to the location)
3. once confirmed, do `ctrl + c`
4. then move your mouse to the book court position that's going to show up later, once confirmed, do `ctrl + c` again
5. you should now see the terminal giving you the two pair of coordinates for select data and book court.
6. replace the `point1` and `point2` variables in `court.py`
7. set the target hour, minute, second in `court.py`
8. when it's close to booking court, run `python court.py` and make sure your terminal and webpage is on the same monitor, and that the mouse is already on the webpage. Also make sure the webpage looks EXACTLY the same as when you confirmed the coordinates
9. remember to kill the program after court booking