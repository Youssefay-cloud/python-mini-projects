import random


def spin(symbols):
    return [random.choice(symbols) for _ in range(3)]


def check_win(result):
    return result[0] == result[1] == result[2]

def show_results(result):
    print(" | ".join(result))

def main():
    symbols = ["🕋", "🕌", "🗺️", "𓂀", "🏰", "🏛️"]
    names = {
        "🕋": "Kaaba - Makkah",
        "🕌": "Alaqsa Mosque",
        "🗺️": "the Nile river",
        "𓂀": "pyramids of giza",
        "🏰": "citadle of salaheldin",
        "🏛️": "Egyption museum - cairo",
    }

    counter = 0

    while True:
        print("you have three times to play")
        input("Please enter to spin the arabic landmark machine ")

        result = spin(symbols)
        show_results(result)
        if check_win(result):
            print(f"You discoverd 3 x {result[0]} {names.get(result[0])}")
            print("culture tour unlocked!")
            break
        else :
            print("try again to match the landmark")
        
        counter += 1

        if counter == 3:
            print("you used your 3 times")
            print("Have a nice day")
            break

if __name__ == "__main__":
    main()