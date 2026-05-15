from brain_games.even import check_even, welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    check_even(name)


if __name__ == "__main__":
    main()