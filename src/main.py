from src.db import process_database
from src.rankings import process_rankings


def main():
    process_database()
    process_rankings()


if __name__ == "__main__":
    main()