import random
from typing import List
import streamlit as st
import streamlit.components.v1 as components
import sys
import pandas as pd
from betag.history import History

ITEM_INDEX_KEY = "item_index"
EDIT_INDEX_KEY = "edit_index"
HISTORY_KEY = "history"

argv = sys.argv
input_path = argv[1]
text_column = argv[2]
label_column = argv[3]
options = argv[4].split(",")

st.set_page_config("Choice")


@st.cache(allow_output_mutation=True)
def load(path: str):
    df = pd.read_csv(path)
    if label_column not in df.columns:
        df[label_column] = None
    return df


def save(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)


def get_random_index(df) -> int:
    indices = list(df[df[label_column].isna()].index.values)
    if len(indices) > 0:
        return random.choice(indices)


def get_text(index: int) -> str:
    return df[text_column].iloc[index]


def label_example(index: int, option: str):
    df.loc[index, label_column] = option
    if st.session_state[EDIT_INDEX_KEY] is None:
        history.add(index, f"{get_text(index)} - {option}")
        st.session_state[ITEM_INDEX_KEY] = get_random_index(df)
    else:
        history.edit(index, f"{get_text(index)} - {option}")
        st.session_state[EDIT_INDEX_KEY] = None
    save(df, input_path)


def on_edit_history(index):
    st.session_state[EDIT_INDEX_KEY] = index


df = load(input_path)

if EDIT_INDEX_KEY not in st.session_state:
    st.session_state[EDIT_INDEX_KEY] = None
if ITEM_INDEX_KEY not in st.session_state:
    st.session_state[ITEM_INDEX_KEY] = get_random_index(df)
if HISTORY_KEY not in st.session_state:
    st.session_state[HISTORY_KEY] = History()

history: History = st.session_state[HISTORY_KEY]


def get_index():
    if st.session_state[EDIT_INDEX_KEY] is None:
        return st.session_state[ITEM_INDEX_KEY]
    return st.session_state[EDIT_INDEX_KEY]


def make_cb(option: str):
    def f():
        label_example(get_index(), option)

    return f


index = get_index()

if index is None:
    st.header("Nothing left to label!")
else:
    st.header(df[text_column].iloc[index])
    cols = st.columns([1] * len(options))

    for i, option in enumerate(options):
        with cols[i]:
            st.button(f"{option} ({i+1})", on_click=make_cb(option))


def gen_html_key_map(options: List[str]):
    buttons = []
    for i, option in enumerate(options):
        option_text = f"{option} ({i+1})"
        buttons.append(f"'{i+1}': buttons.find(el => el.innerText === '{option_text}')")
    return "{" + ",".join(buttons) + "};"


components.html(
    """
<script>
const doc = window.parent.document;
buttons = Array.from(doc.querySelectorAll('button[kind=primary]'));
key_map = %s
doc.addEventListener('keydown', function(e) {
    console.log(event.key)
    if (key_map[event.key]) {
        key_map[event.key].click();
    }
});
</script>
"""
    % gen_html_key_map(options),
    height=0,
    width=0,
)


def progress(df: pd.DataFrame) -> float:
    return df[label_column].notna().sum() / len(df)


st.sidebar.title("betag")
st.sidebar.header("Progress")
columns = st.sidebar.columns([1, 4])
with columns[0]:
    st.text(f"{progress(df)*100:.0f}%")
with columns[1]:
    st.progress(progress(df))


def draw_label_counts(counts, options, context):
    context.header("Options")
    total = df[label_column].count()
    values = [counts[option] / total if option in counts else 0 for option in options]
    for option, value in zip(options, values):
        columns = context.columns([1, 4])
        with columns[0]:
            st.text(option)
        with columns[1]:
            st.progress(value)


draw_label_counts(dict(df[label_column].value_counts()), options, st.sidebar)

history.draw(st.sidebar, on_edit_history)
