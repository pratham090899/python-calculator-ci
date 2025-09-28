import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from calculator import addition

def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
