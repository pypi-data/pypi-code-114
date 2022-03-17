# Copyright (c) 2021, NVIDIA CORPORATION & AFFILIATES.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from nemo_text_processing.text_normalization.en.graph_utils import NEMO_NOT_QUOTE, GraphFst

try:
    import pynini
    from pynini.lib import pynutil

    PYNINI_AVAILABLE = True
except (ImportError, ModuleNotFoundError):
    PYNINI_AVAILABLE = False


class OrdinalFst(GraphFst):
    """
    Finite state transducer for classifying ordinal
        e.g. dreizehnter -> tokens { name: "13." }

    Args:
        itn_cardinal_tagger: ITN Cardinal Tagger
        tn_ordinal_verbalizer: TN Ordinal Verbalizer
    """

    def __init__(self, itn_cardinal_tagger: GraphFst, tn_ordinal_verbalizer: GraphFst, deterministic: bool = True):
        super().__init__(name="ordinal", kind="classify", deterministic=deterministic)

        tagger = tn_ordinal_verbalizer.graph.invert().optimize()

        graph = (
            pynutil.delete("integer: \"") + pynini.closure(NEMO_NOT_QUOTE, 1) + pynutil.delete("\"")
        ) @ itn_cardinal_tagger.graph

        final_graph = tagger @ graph + pynutil.insert(".")

        graph = pynutil.insert("name: \"") + final_graph + pynutil.insert("\"")
        self.fst = graph.optimize()
