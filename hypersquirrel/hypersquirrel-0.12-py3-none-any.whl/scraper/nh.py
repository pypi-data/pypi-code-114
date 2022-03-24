from commmons import html_from_url, get_host_url


def scrape(url):
    tree = html_from_url(url)

    def get_thumbnailurl(vid):
        imgs = tree.xpath("//img[contains(@class,'thumb')]")
        for img in imgs:
            datasrc = img.attrib.get("data-src")
            if datasrc and vid in datasrc:
                return datasrc
        return None

    li_elements = tree.xpath("//li[contains(@class,'videoblock')]")
    for li in li_elements:
        vkey = li.attrib.get("data-video-vkey")
        vid = li.attrib.get("data-video-id")
        if vkey:
            href = f"view_video.php?viewkey={vkey}"
            for a in li.xpath(f"//a[@href='/{href}']"):
                title = a.attrib.get("title")
                if title:
                    file = {
                        "fileid": vkey,
                        "sourceurl": f"{get_host_url(url)}/{href}",
                        "filename": title.strip()
                    }

                    thumbnailurl = get_thumbnailurl(vid)
                    if thumbnailurl:
                        file["thumbnailurl"] = thumbnailurl

                    yield file
                    break
