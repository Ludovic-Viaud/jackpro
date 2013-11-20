import pytest
import sabot

@pytest.fixture
def newSabot():
    return sabot.Sabot()

def test_init(newSabot):
    assert len(newSabot._data) == 6*52
    assert newSabot._cutcard == 52
    for x in range(2, 12):
        if x == 10:
            assert newSabot._data.count(x) == 4*4*6
        else:
            assert newSabot._data.count(x) == 4*6
    assert newSabot._current == 6*52 - 1
    assert newSabot.cutcarded() == False
    assert newSabot.decksOut() == 0.0

def test_en_action(newSabot):
    assert newSabot.draw() == newSabot._data[-1]
    assert newSabot._current == 6*52 - 1 - 1
    assert newSabot.draw() == newSabot._data[-2]
    assert newSabot._current == 6*52 - 1 - 2
    for x in range(50):  # @UnusedVariable
        newSabot.draw()
    assert newSabot.decksOut() == 1.0
    assert newSabot.decksRem() == 5.0
    assert newSabot.cutcarded() == False
    for x in range(52):  # @UnusedVariable
        newSabot.draw()
    assert newSabot.decksOut() == 2.0
    assert newSabot.decksRem() == 4.0
    assert newSabot.cutcarded() == False
    for x in range(200):  # @UnusedVariable
        newSabot.draw()
    assert newSabot.cutcarded() == True

def test_shuffle(newSabot):
    test_en_action(newSabot)
    assert newSabot._current == 7
    newSabot.shuffle()
    assert newSabot._current == 6*52-1
    test_en_action(newSabot)
    assert newSabot._current == 7
