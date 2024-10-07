from django.test import TestCase
from rdkit import Chem
from .utils import molecule_to_svg, Drug

class MoleculeToSvgTests(TestCase):

    TEST_Obj = Drug('test_001', Chem.MolFromSmiles("CCO")) 

    def test_molecule_to_svg_creates_svg_file(self):     
        svg = molecule_to_svg(self.TEST_Obj)
        svg_output_decoded = svg.decode('utf-8')

        self.assertIsInstance(svg_output_decoded, str, "Output should be a string.")
        self.assertIn('<svg', svg_output_decoded, "Output should contain the SVG element.")
