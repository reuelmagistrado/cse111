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
    assert compute_unita_electricity(textBox, textBox1) == 66.0


textBox2 = Entry(root)
textBox2.insert(0, "1763.0")
textBox3 = Entry(root)
textBox3.insert(0, "1799.0")


def test_compute_unitb_electricity():
    assert compute_unitb_electricity(textBox2, textBox3) == 36.0


textBox4 = Entry(root)
textBox4.insert(0, "2364.0")
textBox5 = Entry(root)
textBox5.insert(0, "2547.0")


def test_compute_unitc_electricity():
    assert compute_unitc_electricity(textBox4, textBox5) == 183.0


textBox6 = Entry(root)
textBox6.insert(0, "10152.0")
textBox7 = Entry(root)
textBox7.insert(0, "10519.0")


def test_compute_unitd_electricity():
    assert compute_unitd_electricity(textBox6, textBox7) == 367.0


textBox8 = Entry(root)
textBox8.insert(0, "6042.0")
textBox9 = Entry(root)
textBox9.insert(0, "6232.0")


def test_compute_unite_electricity():
    assert compute_unite_electricity(textBox8, textBox9) == 190.0


textBox10 = Entry(root)
textBox10.insert(0, "1352.0")
textBox11 = Entry(root)
textBox11.insert(0, "1410.0")


def test_compute_unitf_electricity():
    assert compute_unitf_electricity(textBox10, textBox11) == 58.0


# WATER

textBox12 = Entry(root)
textBox12.insert(0, "73.0")
textBox13 = Entry(root)
textBox13.insert(0, "76.0")


def test_compute_unita_water():
    assert compute_unita_water(textBox12, textBox13) == 3.0


textBox14 = Entry(root)
textBox14.insert(0, "44.0")
textBox15 = Entry(root)
textBox15.insert(0, "46.0")


def test_compute_unitb_water():
    assert compute_unitb_water(textBox14, textBox15) == 2.0


textBox16 = Entry(root)
textBox16.insert(0, "63.0")
textBox17 = Entry(root)
textBox17.insert(0, "68.0")


def test_compute_unitc_water():
    assert compute_unitc_water(textBox16, textBox17) == 5.0


textBox18 = Entry(root)
textBox18.insert(0, "118.0")
textBox19 = Entry(root)
textBox19.insert(0, "121.0")


def test_compute_unitd_water():
    assert compute_unitd_water(textBox18, textBox19) == 3.0


textBox20 = Entry(root)
textBox20.insert(0, "125.0")
textBox21 = Entry(root)
textBox21.insert(0, "128.0")


def test_compute_unite_water():
    assert compute_unite_water(textBox20, textBox21) == 3.0


textBox22 = Entry(root)
textBox22.insert(0, "107.0")
textBox23 = Entry(root)
textBox23.insert(0, "111.0")


def test_compute_unitf_water():
    assert compute_unitf_water(textBox22, textBox23) == 4.0


# Call the main function that is part of pytest so
# that the computer will execute the test functions
# in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
