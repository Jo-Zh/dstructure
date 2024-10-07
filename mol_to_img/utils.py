import os
import cairosvg
from django.conf import settings
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit import Chem


# Create Default Structure
default_structure = "CC(=O)OC1=CC=CC=C1C(=C)C=C1C=CC(=O)O1"
class Drug:
    
    def __init__(self, drug_id, smol):
          self.smol = smol
          self.pk = drug_id

defaultVal = Drug('test_001', Chem.MolFromSmiles(default_structure))


def convert_mol_img(drug_object=defaultVal):
    # create the structur image folder if not existed
    if not os.path.exists(settings.MOL_IMG_DIR):
        os.makedirs(settings.MOL_IMG_DIR)
    try:
        molecule_to_svg(drug_object.smol, drug_object.pk, path = settings.MOL_IMG_DIR)
    except Exception as err:
        pass
    


def molecule_to_svg(mol, file_name="drug_pk", width=450, height=450, path=settings.MOL_IMG_DIR):
    """Save substance structure as SVG"""
# ----------------------------------------------------------------------------------------------------

    file_svg=os.path.join(path, f"{file_name}.svg")  
    # Render high resolution molecule
    drawer = rdMolDraw2D.MolDraw2DSVG(width, height)
    drawer.DrawMolecule(mol)
    drawer.FinishDrawing()
    try:
        cairosvg.svg2svg(bytestring=drawer.GetDrawingText().encode(), write_to=file_svg)

    except Exception as err:
         print(err)
  