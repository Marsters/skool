chocBars = 2
people = 3
SQUARES_PER_BAR = 7
wholeBarsEach = chocBars // people
chocSquares = chocBars % people * SQUARES_PER_BAR
pricePerBar = 4
print("Whole chocolates bars each: ", wholeBarsEach)
print("Extra squares each: ", chocSquares // people)
print("Squares left over: ", chocSquares % people)
print("Cost per person: ", round(pricePerBar * chocBars / people, 2))
