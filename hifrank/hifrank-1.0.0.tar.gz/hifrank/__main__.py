# __main__.py
from datetime import datetime


def main():
    """Greet someone called Frank"""

    current_time = datetime.now().hour

    if current_time >= 6 and current_time < 12:
        print('Good morning Frank!')
    elif current_time >= 12 and current_time < 18:
        print('Good afternoon Frank!')
    elif current_time >= 18 and current_time < 24:
        print('Good evening Frank!')
    else:
        print('Go to bed Frank!')


if __name__ == "__main__":
    main()