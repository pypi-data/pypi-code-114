from commmons import html_from_url, get_host_url


def scrape(url):
    tree = html_from_url(url)
    host_url = get_host_url(url)

    divs = tree.xpath("//div[contains(@class, 'video-item')]")
    for div in divs:
        if "data-id" not in div.attrib:
            continue

        dataid = div.attrib["data-id"]
        atags = div.xpath("./a")

        if not atags:
            continue

        imgs = div.xpath("./a/picture/img")
        if not imgs:
            continue

        atag = atags[0]
        img = imgs[0]

        yield {
            "fileid": "sb" + dataid,
            "sourceurl": host_url + atag.attrib["href"],
            "filename": img.attrib["alt"],
            "thumbnailurl": img.attrib["data-src"]
        }
