import requests


def get():
    r = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

    val = r['Valute']['USD']['Value']

    print('Курс доллара:', val, 'Рублей')

    if val > 100:
        print('ПОМОГИТЕ!!!')
