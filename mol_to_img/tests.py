import os

from django.test import TestCase
from rdkit import Chem
from .utils import molecule_to_svg

class MoleculeToSvgTests(TestCase):

    TEST_MOL_SMILES = "CCO"  # Example SMILES string for ethanol
    TEST_FILE_NAME = "test_drug"
    TEST_PATH = "./"

    def test_molecule_to_svg_creates_svg_file(self):
        mol = Chem.MolFromSmiles(self.TEST_MOL_SMILES)
        molecule_to_svg(mol, file_name=self.TEST_FILE_NAME, path=self.TEST_PATH)
        file_svg = os.path.join(self.TEST_PATH, f"{self.TEST_FILE_NAME}.svg")

        self.assertTrue(os.path.exists(file_svg), "SVG file was created.")

        # Clean up the created file after the test
        os.remove(file_svg)
