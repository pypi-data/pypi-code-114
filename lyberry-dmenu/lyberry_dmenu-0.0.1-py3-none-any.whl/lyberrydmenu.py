import lyberry_api

# This will first try to use a dmenu wrapper library, which you can get off of PyPI as simply dmenu.
# If that is not installed it will make a class that emulates part of the library.
try:
    import dmenu
except:
    import subprocess

    class dmenu:
        def show(self, items: list, lines: int = 0, prompt: str = ""):
            items_str = ""
            for item in items:
                items_str += f"{item}\n"
            return (
                subprocess.check_output(
                    ["dmenu", "-l", str(lines), "-p", prompt], input=items_str.encode()
                )
                .decode()
                .rstrip()
            )

    dmenu = dmenu()


class LyBerry_Dmenu:
    def __init__(self):
        self.lbry = lyberry_api.LBRY_Api()

    def repl(self):
        commands = ["search", "following"]
        selected = dmenu.show(commands, lines=len(commands), prompt="Command to run:")

        if selected == "search":
            self.search()
        if selected == "following":
            self.following()

    def search(self):
        query = dmenu.show([], prompt="Search for:")
        if query:
            results = self.lbry.lbrynet_search_feed(text=query)
            self.play_from_results(results)

    def following(self):
        results = self.lbry.sub_feed
        self.play_from_results(results)

    def play_from_results(self, results):
        items = []
        for i in range(20):
            try:
                items.append(next(results))
            except StopIteration:
                break
        options = []
        for item in items:
            options.append(
                item.title + " - " + item.channel.title
                if hasattr(item, "channel")
                else "Anonymous"
            )
        selection = dmenu.show(options, lines=20, prompt="Claim to open:")
        if selection:
            selected_item = items[options.index(selection)]
            self.open_external(selected_item)

    def open_external(self, pub):
        file_type = pub.media_type.split("/")[0]
        if file_type == "video" or file_type == "audio":
            lyberry_api.settings.media_player(pub.streaming_url)
        elif file_type == "text":
            lyberry_api.settings.text_viewer(pub.streaming_url)


def main():
    LyBerry_Dmenu().repl()


if __name__ == "__main__":
    main()
