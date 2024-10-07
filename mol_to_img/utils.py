import os
import cairosvg
from rdkit.Chem.Draw import rdMolDraw2D
from rdkit import Chem


# Create Default Structure
default_structure = "CC(=O)OC1=CC=CC=C1C(=C)C=C1C=CC(=O)O1"
class Drug:
    
    def __init__(self, drug_id, smol):
          self.smol = smol
          self.pk = drug_id

defaultVal = Drug('test_001', Chem.MolFromSmiles(default_structure))
 

def molecule_to_svg(drug_object=defaultVal, width=450, height=450):
    """Save substance structure as SVG"""
    mol = drug_object.smol
    drawer = rdMolDraw2D.MolDraw2DSVG(width, height)
    drawer.DrawMolecule(mol)
    drawer.FinishDrawing()
    try:
        svg=cairosvg.svg2svg(bytestring=drawer.GetDrawingText().encode())
        return svg

    except Exception as err:
         print(err)
  