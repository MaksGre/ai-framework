from ai.assembly import create_engineering_mentor
from ai.cli.app import CLI


def main():
    mentor = create_engineering_mentor()
    cli = CLI(mentor)
    cli.run()


if __name__ == "__main__":
    main()
