# Business logic
def generate_fizzbuzz(
    int1: int,
    int2: int,
    limit: int,
    str1: str,
    str2: str,
) -> list[str]:
    result = []

    for number in range(1, limit + 1):

        if number % int1 == 0 and number % int2 == 0:
            result.append(str1 + str2)

        elif number % int1 == 0:
            result.append(str1)

        elif number % int2 == 0:
            result.append(str2)

        else:
            result.append(str(number))
        
    return result

