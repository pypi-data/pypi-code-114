from commmons import html_from_url, get_host_url


def _get_img(card):
    imgs = card.xpath(".//img")
    return imgs[0] if imgs else None


def scrape_v2ph(url):
    root = html_from_url(url)

    for a in root.xpath("//a[@class='media-cover']"):
        img = _get_img(a)
        if img is None:
            continue

        yield {
            "fileid": "v2ph" + a.attrib["href"].split("/")[-1].split(".")[0].split("?")[0],
            "filename": img.attrib["alt"],
            "sourceurl": "vpr://" + get_host_url(url) + a.attrib["href"],
            "thumbnailurl": img.attrib["data-src"]
        }
