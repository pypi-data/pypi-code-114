class History:
    def __init__(self) -> None:
        self._history = []
        self._labels = dict()

    def add(self, id: int, label: str) -> None:
        self._history.append(id)
        self._labels[id] = label

    def edit(self, id: int, label: str) -> None:
        assert id in self._history
        self._labels[id] = label

    def draw(self, st, edit_on_click):
        if len(self._history) > 0:
            st.header("History")
            for i, id in enumerate(self._history[::-1]):
                st.button(
                    f"✏️  {self._labels[id]}",
                    key=f"history_btn_{i}",
                    on_click=edit_on_click,
                    args=(id,),
                )
