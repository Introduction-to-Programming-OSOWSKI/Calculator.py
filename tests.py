#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 1
day = 14

def test_code():
    assert main.calculate("add", 2, 2) == 4
    assert main.calculate("add", 10, 2) == 12

    assert main.calculate("subtract", 2, 2) == 0
    assert main.calculate("subtract", 10, 5) == 5
    
    assert main.calculate("multiply", 2, 3) == 6
    assert main.calculate("multiply", 100, 5) == 500
    
    assert main.calculate("divide", 5, 2) == 2.5
    assert main.calculate("divide", 20, 2) == 10.0

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
