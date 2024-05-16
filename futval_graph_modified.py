###futval_graph.py
from graphics import *


def main():
    print("This program plots the growth of a 10 year investment.")

    # Get the principal and interest rate
    principal = float(input("Enter the initial principal: "))
    apr = float(input("Enter the annualised interest rate: "))

    # Create a graphics window with labels on the left edge
    win = GraphWin("Investment Growth Chart", 640, 480)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)

    Text(Point(-1, 0), "0.0K").draw(win)

    Text(Point(-1, 2500), "2.5K").draw(win)

    Text(Point(-1, 5000), "5.0K").draw(win)

    Text(Point(-1, 7500), "7.5K").draw(win)

    Text(Point(-1, 10000), "10.0K").draw(win)

    # Draw bar for initial principal
    # height = principal * 0.02

    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for each subsequent year
    for year in range(1, 11):
        # Calculate value for the next year
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year + 1, principal))

        # draw bar for this value
        # x11 = year * 25 + 40
        # height = principal * 0.02
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit")
    win.close


main()
