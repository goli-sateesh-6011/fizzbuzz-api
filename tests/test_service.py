from app.service import generate_fizzbuzz

# test case 1
def test_generate_fizzbuzz():
    result = generate_fizzbuzz(
        int1=3,
        int2=5,
        limit=15,
        str1="Fizz",
        str2="Buzz",
    )

    expected = [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]

    assert result == expected

# Test case 2
def test_generate_fizzbuzz_no_replacements():
    result = generate_fizzbuzz(
        int1=100,
        int2=200,
        limit=5,
        str1="Fizz",
        str2="Buzz"
    )

    assert result == [
        "1",
        "2",
        "3",
        "4",
        "5",
    ]

# Test case 3
def test_generate_fizzbuzz_all_replacements():
    result = generate_fizzbuzz(
        int1=1,
        int2=2,
        limit=3,
        str1="A",
        str2="B",
    )

    assert result == [
        "A",
        "AB",
        "A"
    ]

# Test Case 4 
def test_generate_fizzbuzz_limit_one():
    result = generate_fizzbuzz(
        int1=2,
        int2=3,
        limit=1,
        str1="Fizz",
        str2="Buzz",
    )

    assert result == ["1"]