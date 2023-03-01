filename = 'pi_million_digits.txt'

def main():
    with open(filename) as file:
        content = file.readlines()
    
    for line in content:
        line = line.strip()
    
    birthday = input("enter birthday in the format DDMMYY, i.e 012292 >")

    found = False
    for line in content:
        if birthday in line:
            found = True
            break
        else:
            continue

    if found:
        print("Your birthday appears in the first 1 million digits of pi!")
    else:
        print("tough luck! your birthday does not appear in the first 1 million digits...maybe the next 1 Million?")

if __name__ == '__main__':
    main()