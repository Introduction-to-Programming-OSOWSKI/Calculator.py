#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;
import datetime;

year = 2021
month = 1
day = 14

def test_code():
    assert main.calculate("add", 2, 2) == 4, "2 + 2 == 10 failed"
    assert main.calculate("add", 10, 2) == 12, "10 + 2 == 12 failed"

    assert main.calculate("subtract", 2, 2) == 0, "2 - 2 == 0 failed"
    assert main.calculate("subtract", 10, 5) == 5, "10 - 5 == 5 failed"
    
    assert main.calculate("multiply", 2, 3) == 6, "2 * 3 == 6 failed"
    assert main.calculate("multiply", 100, 5) == 500, "100 * 5 == 500 failed"
    
    assert main.calculate("divide", 5, 2) == 2.5, "5 / 2 == 2.5 failed"
    assert main.calculate("divide", 20, 2) == 10.0, "20 / 2 == 10.0 failed"

def test_late():
    assert datetime.datetime.now() < datetime.datetime(year, month, day + 1, 4, 0), "Submitted Late"
