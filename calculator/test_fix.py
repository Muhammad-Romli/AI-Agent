from pkg.calculator import Calculator

def test_calculator():
    calc = Calculator()
    result = calc.evaluate("3 + 7 * 2")
    print(f"Result: {result}")
    assert result == 17.0, f"Expected 17.0, but got {result}"
    print("Test passed!")

if __name__ == "__main__":
    test_calculator()
