import unittest

from gorps.importers.grmt import parse_modifications


class TestGrmt(unittest.TestCase):
    def test_parse_modifications(self) -> None:
        mods = """&lt;decription&gt;
'''100% Beef Burgers'''
This is a very simple recipe for hamburgers best cooked on a grill or in an iron skillet.
&lt;/decription&gt;
&lt;tools&gt;
* 1 plate
* iron skillet or BBQ
* spatula
&lt;/tools&gt;
&lt;difficulty&gt;
	easy to medium
&lt;/difficulty&gt;
&lt;side-dish&gt;
	* Serve with Ketchup, Mustard, Mayo, tomatoe slices, lettuce, french fries, jalapeno slices, branston pickles, cheddar cheese, emmethaler cheese or whatever else you like!

Category:Hamburger

de:Hamburger
&lt;/side-dish&gt;"""
        self.assertEqual(
            parse_modifications(mods),
            (
                {
                    "difficulty": "easy to medium",
                    "tools": ["1 plate", "iron skillet or BBQ", "spatula"],
                },
                """&lt;side-dish&gt;
	* Serve with Ketchup, Mustard, Mayo, tomatoe slices, lettuce, french fries, jalapeno slices, branston pickles, cheddar cheese, emmethaler cheese or whatever else you like!

Category:Hamburger

de:Hamburger
&lt;/side-dish&gt;""",
                """'''100% Beef Burgers'''
This is a very simple recipe for hamburgers best cooked on a grill or in an iron skillet.""",
            ),
        )
