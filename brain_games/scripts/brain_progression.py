from brain_games.engine import welcome_user
from brain_games.games.progression import check_progression


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    check_progression(name)


if __name__ == "__main__":
    main()