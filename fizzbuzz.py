def fizzer(upper: int) -> list:
    """Does some fizzbuzz action"""
    result: list[str] = []
    for n in range(1,upper):
        out = ""
        if (n % 3) == 0:
            out = out + 'Fizz'
        if (n % 5) == 0:
            out = out + 'Buzz'
        if out == "":
            out = str(n)

        result.append(out)

    return result

def main():
    """Python3 FizzBuzz"""
    upper_bound = input("Upper bound? > ")
    upper_bound = int(upper_bound)
    result = fizzer(upper_bound)

    with open('fizzbuzz_results.txt',mode='w+t') as file:
        for line in result:
            file.write(line)
            file.write("\n")

if __name__ == '__main__':
    main()