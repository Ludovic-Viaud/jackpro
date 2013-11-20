import pytest
import discret

def test_except():
    with pytest.raises(ValueError):
        discret.discret(0, mode='coucou')
    with pytest.raises(ValueError):
        discret.discret(0, mode='voila')
    with pytest.raises(ValueError):
        discret.discret(0, precision=3)
    with pytest.raises(ValueError):
        discret.discret(0, precision=6)
    with pytest.raises(ValueError):
        discret.discret(0, precision=7)
    with pytest.raises(ValueError):
        discret.discret(0, precision=9)
    discret.discret(0, precision=1)
    discret.discret(0, precision=2)
    discret.discret(0, precision=4)
    discret.discret(0, precision=5)
    discret.discret(0, precision=8)
    discret.discret(0, precision=10)
    discret.discret(0, mode='auto')
    discret.discret(0, mode='trunc')
    discret.discret(0, mode='-trunc')
    discret.discret(0, mode='floor')
    discret.discret(0, mode='ceil')

def test_auto():
    # ===== mode = 'auto' =====
    # ----- precision = 1 -----
    assert discret.discret(0.76, precision=1, mode='auto') == 1.0
    assert discret.discret(2.01, precision=1, mode='auto') == 2.0
    assert discret.discret(0, precision=1, mode='auto') == 0
    assert discret.discret(-5.31, precision=1, mode='auto') == -5
    assert discret.discret(-6.81, precision=1, mode='auto') == -7
    # ----- precision = 2 -----
    assert discret.discret(0.76, precision=2, mode='auto') == 1.0
    assert discret.discret(2.01, precision=2, mode='auto') == 2.0
    assert discret.discret(0, precision=2, mode='auto') == 0
    assert discret.discret(-5.31, precision=2, mode='auto') == -5.5
    assert discret.discret(-6.81, precision=2, mode='auto') == -7
    # ----- precision = 4 -----
    assert discret.discret(0.76, precision=4, mode='auto') == 0.75
    assert discret.discret(2.01, precision=4, mode='auto') == 2.0
    assert discret.discret(0, precision=4, mode='auto') == 0
    assert discret.discret(-5.31, precision=4, mode='auto') == -5.25
    assert discret.discret(-6.91, precision=4, mode='auto') == -7

def test_trunc():
    # ===== mode = 'trunc' =====
    # ----- precision = 1 -----
    assert discret.discret(0.76, precision=1, mode='trunc') == 0
    assert discret.discret(2.01, precision=1, mode='trunc') == 2.0
    assert discret.discret(0, precision=1, mode='trunc') == 0
    assert discret.discret(-5.31, precision=1, mode='trunc') == -5
    assert discret.discret(-6.81, precision=1, mode='trunc') == -6
    # ----- precision = 2 -----
    assert discret.discret(0.76, precision=2, mode='trunc') == 0.5
    assert discret.discret(2.01, precision=2, mode='trunc') == 2.0
    assert discret.discret(0, precision=2, mode='trunc') == 0
    assert discret.discret(-5.31, precision=2, mode='trunc') == -5
    assert discret.discret(-6.81, precision=2, mode='trunc') == -6.5
    # ----- precision = 4 -----
    assert discret.discret(0.76, precision=4, mode='trunc') == 0.75
    assert discret.discret(2.01, precision=4, mode='trunc') == 2.0
    assert discret.discret(0, precision=4, mode='trunc') == 0
    assert discret.discret(-5.31, precision=4, mode='trunc') == -5.25
    assert discret.discret(-6.91, precision=4, mode='trunc') == -6.75

def test_rtrunc():
    # ===== mode = '-trunc' =====
    # ----- precision = 1 -----
    assert discret.discret(0.76, precision=1, mode='-trunc') == 1
    assert discret.discret(2.01, precision=1, mode='-trunc') == 3
    assert discret.discret(0, precision=1, mode='-trunc') == 0
    assert discret.discret(-5.31, precision=1, mode='-trunc') == -6
    assert discret.discret(-6.81, precision=1, mode='-trunc') == -7
    # ----- precision = 2 -----
    assert discret.discret(0.76, precision=2, mode='-trunc') == 1
    assert discret.discret(2.01, precision=2, mode='-trunc') == 2.5
    assert discret.discret(0, precision=2, mode='-trunc') == 0
    assert discret.discret(-5.31, precision=2, mode='-trunc') == -5.5
    assert discret.discret(-6.81, precision=2, mode='-trunc') == -7
    # ----- precision = 4 -----
    assert discret.discret(0.76, precision=4, mode='-trunc') == 1
    assert discret.discret(2.01, precision=4, mode='-trunc') == 2.25
    assert discret.discret(0, precision=4, mode='-trunc') == 0
    assert discret.discret(-5.31, precision=4, mode='-trunc') == -5.5
    assert discret.discret(-6.91, precision=4, mode='-trunc') == -7

def test_floor():
    # ===== mode = 'floor' =====
    # ----- precision = 1 -----
    assert discret.discret(0.76, precision=1, mode='floor') == 0
    assert discret.discret(2.01, precision=1, mode='floor') == 2
    assert discret.discret(0, precision=1, mode='floor') == 0
    assert discret.discret(-5.31, precision=1, mode='floor') == -6
    assert discret.discret(-6.81, precision=1, mode='floor') == -7
    # ----- precision = 2 -----
    assert discret.discret(0.76, precision=2, mode='floor') == 0.5
    assert discret.discret(2.01, precision=2, mode='floor') == 2
    assert discret.discret(0, precision=2, mode='floor') == 0
    assert discret.discret(-5.31, precision=2, mode='floor') == -5.5
    assert discret.discret(-6.81, precision=2, mode='floor') == -7
    # ----- precision = 4 -----
    assert discret.discret(0.76, precision=4, mode='floor') == 0.75
    assert discret.discret(2.01, precision=4, mode='floor') == 2
    assert discret.discret(0, precision=4, mode='floor') == 0
    assert discret.discret(-5.31, precision=4, mode='floor') == -5.5
    assert discret.discret(-6.91, precision=4, mode='floor') == -7

def test_ceil():
    # ===== mode = 'ceil' =====
    # ----- precision = 1 -----
    assert discret.discret(0.76, precision=1, mode='ceil') == 1
    assert discret.discret(2.01, precision=1, mode='ceil') == 3
    assert discret.discret(0, precision=1, mode='ceil') == 0
    assert discret.discret(-5.31, precision=1, mode='ceil') == -5
    assert discret.discret(-6.81, precision=1, mode='ceil') == -6
    # ----- precision = 2 -----
    assert discret.discret(0.76, precision=2, mode='ceil') == 1
    assert discret.discret(2.01, precision=2, mode='ceil') == 2.5
    assert discret.discret(0, precision=2, mode='ceil') == 0
    assert discret.discret(-5.31, precision=2, mode='ceil') == -5
    assert discret.discret(-6.81, precision=2, mode='ceil') == -6.5
    # ----- precision = 4 -----
    assert discret.discret(0.76, precision=4, mode='ceil') == 1
    assert discret.discret(2.01, precision=4, mode='ceil') == 2.25
    assert discret.discret(0, precision=4, mode='ceil') == 0
    assert discret.discret(-5.31, precision=4, mode='ceil') == -5.25
    assert discret.discret(-6.91, precision=4, mode='ceil') == -6.75