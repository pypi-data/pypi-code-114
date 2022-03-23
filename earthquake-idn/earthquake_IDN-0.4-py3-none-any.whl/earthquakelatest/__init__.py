import requests
from bs4 import BeautifulSoup

description = "To get the latest earthquake in Indonesia from BMKG.go.id"

def extraction_data():
    """
    Date: 16 Maret 2022,
    Time: 11:06:43 WIB
    Magnitudo: 4.2
    Depth: 16 km
    Location: LS=7.90 - BT=107.04
    Epicenter: Pusat gempa berada di laut 109 km Tenggara Kota Sukabumi
    perceived: Dirasakan (Skala MMI): II Singajaya, II Cidaun, II Agrabinta, II Cidora
    :return:


    """
    try:
        content = requests.get("https://bmkg.go.id")
    except Exception:
        return None
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        date = result[0]
        time = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitude = None
        depth = None
        ls = None
        bt = None
        epicenter = None
        perceived = None

        for res in result:
            if i == 1:
                magnitude = res.text
            elif i == 2:
                depth = res.text
            elif i == 3:
                coordinate = res.text.split(' - ')
                ls = coordinate[0]
                bt = coordinate[1]
            elif i == 4:
                location = res.text
            elif i == 5:
                perceived = res.text
            i += 1


        result = dict()
        result["date"] = date
        result["time"] = time
        result["magnitude"] = magnitude
        result["depth"] = depth
        result["coordinate"] = {'ls': ls, 'bt': bt}
        result["location"] = location
        result["perceived"] = perceived

        return result
    else:
        return None

def display_data(result):
    if result is None:
        print("Can't find data latest earthquake")
        return
    print("Last Earthquake base on BMKG")
    print(f"Date: {result['date']}")
    print(f"Time: {result['time']}")
    print(f"Magnitude: {result['magnitude']}")
    print(f"Depth: {result['depth']}")
    print(f"Coordinate: LS = {result['coordinate']['ls']}, BT = {result['coordinate']['bt']}")
    print(f"Location: {result['location']}")
    print(f"Perceived: {result['perceived']}")

if __name__ == '__main__' :
    print(f'Description Package {description}')
    result = extraction_data()
    display_data(result)