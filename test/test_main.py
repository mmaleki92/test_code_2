import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from main import greet

def test_greet():
    assert greet("World") == "Hello, World!"

def test_greet3():
    assert greet("World") == "Hello, World!"

def test_greet2():
    assert greet("World") == "Hello, World!"

def test_greet1():
    assert greet("World") == "Hello, World!"