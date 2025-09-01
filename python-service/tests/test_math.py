def test_addition_passes():
    assert 2 + 2 == 4  # PASS

def test_subtraction_fails_intentionally():
    assert 2 - 1 == 0  # FAIL on purpose (2-1 == 1)
