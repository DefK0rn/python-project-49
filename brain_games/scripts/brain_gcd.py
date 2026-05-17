from brain_games.engine import welcome_user
from brain_games.games.gcd import check_gcd


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    check_gcd(name)


if __name__ == "__main__":
    main()