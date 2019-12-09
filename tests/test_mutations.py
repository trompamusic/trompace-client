import unittest

from trompace.mutations import make_parameters, StringConstant


class TestMakeParameters(unittest.TestCase):
    """Test the encoding of trompace.mutations.make_parameters"""

    def test_make_parameters(self):
        """A regular set of parameters"""

        params = {"name": "My thing", "source": "The internet"}
        made_params = make_parameters(**params)
        expected = '''name: "My thing"\n        source: "The internet"'''
        self.assertEqual(expected, made_params)

    def test_string_constant(self):
        """String constants are represented without quotes around them"""
        params = {"name": "My thing", "language": StringConstant("en")}
        made_params = make_parameters(**params)
        expected = '''name: "My thing"\n        language: en'''
        self.assertEqual(expected, made_params)

    def test_boolean(self):
        """Boolean values should be represented as json bools (lowercase true/false)"""
        params = {"name": "My thing", "valueRequired": True}
        made_params = make_parameters(**params)
        expected = '''name: "My thing"\n        valueRequired: true'''
        self.assertEqual(expected, made_params)

    def test_list(self):
        """Lists of items should be represented properly"""
        params = {"name": "My thing", "items": [StringConstant("one"), StringConstant("two")]}
        made_params = make_parameters(**params)
        expected = '''name: "My thing"\n        items: [one, two]'''
        self.assertEqual(expected, made_params)

        params = {"name": "My thing", "items": ["val1", "val2"]}
        made_params = make_parameters(**params)
        expected = '''name: "My thing"\n        items: ["val1", "val2"]'''
        self.assertEqual(expected, made_params)
