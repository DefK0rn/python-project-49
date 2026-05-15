from brain_games.engine import welcome_user
from brain_games.games.calc import check_calc


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    check_calc(name)


if __name__ == "__main__":
    main()