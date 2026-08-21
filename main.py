from ai.assembly import (
    create_engineering_mentor,
    create_engineering_vacancy,
)
from ai.cli.app import CLI


def main():
    agents = {
        "Engineering Mentor": create_engineering_mentor(),
        "Engineering Vacancy": create_engineering_vacancy(),
    }

    cli = CLI(agents)
    cli.run()


if __name__ == "__main__":
    main()
