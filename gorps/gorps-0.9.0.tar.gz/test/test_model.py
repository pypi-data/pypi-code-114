import unittest
from fractions import Fraction

from gorps.model import Ingredient, AmountRange, Image


class TestIngredient(unittest.TestCase):
    def test_from_dict_amount_range(self) -> None:
        ingredient = Ingredient.from_dict(
            {
                "name": "I",
                "amount": {"min": 1.0, "max": 2},
                "unit": None,
            }
        )
        self.assertEqual(
            ingredient,
            Ingredient(
                name="I",
                amount=AmountRange(Fraction(1), Fraction(2)),
                unit=None,
                optional=False,
            ),
        )

    def test_from_dict_scalar_amount(self) -> None:
        ingredient = Ingredient.from_dict({"name": "I", "amount": 1.0, "unit": None})
        self.assertEqual(
            ingredient,
            Ingredient(name="I", amount=Fraction(1), unit=None, optional=False),
        )


class TestImage(unittest.TestCase):
    def test_as_b64(self) -> None:
        self.assertEqual(
            Image(
                fmt="image/png",
                data=b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDAT\x08\xd7c\xf8\xff\xff?\x00\x05\xfe\x02\xfe\xdc\xccY\xe7\x00\x00\x00\x00IEND\xaeB`\x82",
            ).as_b64(),
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAIAAACQd1PeAAAADElEQVQI12P4//8/AAX+Av7czFnn"
            "AAAAAElFTkSuQmCC",
        )
