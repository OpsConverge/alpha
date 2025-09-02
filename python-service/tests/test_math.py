"""Test cases for basic math operations with mixed pass/fail results."""

def test_addition_works():
    """Test that addition works correctly."""
    assert 2 + 3 == 5
    assert -1 + 1 == 0
    assert -2 + -3 == -5

def test_subtraction_works():
    """Test that subtraction works correctly."""
    assert 5 - 3 == 2
    assert 3 - 5 == -2
    assert 0 - 0 == 0

def test_subtraction_fails_intentionally():
    """This test will fail intentionally for testing purposes."""
    assert 2 - 1 == 0  # Expected: 0, Actual: 1

def test_multiplication_works():
    """Test that multiplication works correctly."""
    assert 3 * 4 == 12
    assert 0 * 5 == 0
    assert -2 * 3 == -6

def test_multiplication_fails_intentionally():
    """This test will fail intentionally for testing purposes."""
    assert 3 * 4 == 10  # Expected: 10, Actual: 12

def test_division_works():
    """Test that division works correctly."""
    assert 6 / 2 == 3.0
    assert 5 / 2 == 2.5
    assert -6 / 2 == -3.0

def test_division_fails_intentionally():
    """This test will fail intentionally for testing purposes."""
    assert 6 / 2 == 4.0  # Expected: 4.0, Actual: 3.0
