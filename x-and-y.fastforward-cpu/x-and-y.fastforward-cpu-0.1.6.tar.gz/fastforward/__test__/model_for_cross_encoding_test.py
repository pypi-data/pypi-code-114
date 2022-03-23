import unittest

from fastforward.model_for_sequence_classification import ModelForSequenceClassification
from fastforward.model_for_cross_encoding import ModelForCrossEncoding
from fastforward.tokenizer.abstract_tokenizer import EncodingConfig


class ModelForCrossEncodingTest(unittest.TestCase):

    def test_encode(self):
        text1 = 'How many people live in Berlin?'
        text2 = 'Berlin has a population of 3,520,031 registered inhabitants in an area of 891.82 square kilometers.'

        config = EncodingConfig()
        encoder = ModelForCrossEncoding("/home/christian/IdeaProjects/x-and-y/onnx-fabric/onnx_fabric/__tests__/msmarco-MiniLM-L6-en-de-v1/cpu-int8", use_sigmoid=False)
        print(encoder((text1, text2), config=config))
        # self.assertTrue(encoder(("A", "B")) is not None)

    def test_encode_batch(self):
        encoder = ModelForCrossEncoding("./dummy", use_sigmoid=True)
        self.assertEqual(len(encoder([("A", "B"), ("A", "B")])), 2)
        self.assertEqual(len(encoder([("A", "B"), ("A", "B")])), 2)

    def test_encode_batch_with_different_sequence_lengths(self):
        encoder = ModelForCrossEncoding("./dummy", use_sigmoid=True)
        self.assertEqual(len(encoder([("A", "B"), ("A", "B")])), 2)
        self.assertEqual(len(encoder([("A", "B C"), ("A", "B C D E")])), 2)