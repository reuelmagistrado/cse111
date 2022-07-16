from calc import *
from tkinter import *
import pytest
root = Tk()
root.geometry("200x100")
  
textBox = Entry(root)
textBox.insert(0, "683.0")

textBox1 = Entry(root)
textBox1.insert(0, "749.0")

def test_compute_unita_electricity():
    assert compute_unita_electricity(textBox, textBox1)  == 66.0


textBox2 = Entry(root)
textBox2.insert(0, "1763.0")

textBox3 = Entry(root)
textBox3.insert(0, "1799.0")

def test_compute_unita_electricity():
    assert compute_unita_electricity(textBox2, textBox3)  == 66.0
















pytest.main(["-v", "--tb=line", "-rN", __file__])