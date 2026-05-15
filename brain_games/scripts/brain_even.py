from brain_games.engine import welcome_user
from brain_games.games.even import check_even


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    check_even(name)


if __name__ == "__main__":
    main()