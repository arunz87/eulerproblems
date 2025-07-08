# EULER PROBLEM 001
# Problem Statement:
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
# 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


def multiples(of: int, upto: int) -> range:
    return range(of, upto, of)


def select(n: int) -> bool:
    # This function checks if a number is a multiple of 3 or 5
    return n % 3 == 0 or n % 5 == 0


def euler001_1(limit: int) -> int:
    # This function calculates the sum of all multiples of 3 or 5 below a given limit
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)


def euler001_2(limit: int) -> int:
    # This function calculates the sum of all multiples of 3 or 5 below a given limit
    return (
        sum(multiples(3, limit)) + sum(multiples(5, limit)) - sum(multiples(15, limit))
    )


def euler001_3(limit: int) -> int:
    # This function calculates the sum of all multiples of 3 or 5 below a given limit
    return sum(set(multiples(3, limit)) | set(multiples(5, limit)))


def euler001_4(limit: int) -> int:
    # This function calculates the sum of all multiples of 3 or 5 below a given limit
    return sum(filter(select, range(1, limit)))


def euler001_5(limit: int) -> int:
    # This function calculates the sum of all multiples of 3 or 5 below a given limit
    return sum([n for n in range(1, limit) if select(n)])


if __name__ == "__main__":
    # using range to iterate through numbers below the limit
    # and checking if they are multiples of 3 or 5
    print("Using range to iterate through numbers:")
    print(euler001_1(1000))
    # Output: 233168
    print("Using multiples function to generate ranges:")
    print(euler001_2(1000))
    # Output: 233168
    print("Using set union to combine multiples:")
    print(euler001_3(1000))
    # Output: 233168
    print("Using filter to select multiples:")
    print(euler001_4(1000))
    # Output: 233168
    print("List comprehension version:")
    print(euler001_5(1000))
    # Output: 233168
    # All four functions should return the same result
    assert (
        euler001_1(1000)
        == euler001_2(1000)
        == euler001_3(1000)
        == euler001_4(1000)
        == euler001_5(1000)
        == 233168
    )
    print("All tests passed!")
# This code defines three different functions to solve the same problem
# of finding the sum of all multiples of 3 or 5 below a given limit.
