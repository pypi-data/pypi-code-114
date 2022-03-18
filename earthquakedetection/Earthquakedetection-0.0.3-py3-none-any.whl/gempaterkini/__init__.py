from bs4 import BeautifulSoup
import requests


def ekstraksi_data():
    """
    waktu: 11 maret 2022, 18:49:52 WIB
    Magnitude: 4.0
    Kedalaman: 10 km
    Lokasi: LS=4.06 BT=133.51
    Pusat Gempa: Pusat gempa berada di darat 98 Km Barat Daya Kaimana
    Dirasakan (Skala MMI): II Kaimana
    :return:
    """
    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 1
        waktu = None
        magnitude = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None

        for res in result:
            if i == 1:
                waktu = res.text
            elif i == 2:
                magnitude = res.text
            elif i == 3:
                kedalaman = res.text
            elif i == 4:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 5:
                lokasi = res.text
            elif i == 6:
                dirasakan = res.text
            i = i + 1

        hasil = dict()
        hasil['waktu'] = waktu
        hasil['magnitude'] = magnitude
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt': bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print("tidak bisa menemukan dat gempa terkini")
        return

    print('gempa terakhir berdasarkan BMKG')
    print(f"waktu {result['waktu']}")
    print(f"Magnitude {result['magnitude']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"koordinat LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"lokasi {result['lokasi']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    result = ekstraksi_data()
    tampilkan_data(result)
