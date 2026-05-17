from brain_games.engine import welcome_user
from brain_games.games.prime import check_prime


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    check_prime(name)


if __name__ == "__main__":
    main()