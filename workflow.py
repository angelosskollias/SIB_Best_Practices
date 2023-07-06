import pandas as pd


def numberHeavyAtoms(smiles: str, format="smi") -> int:
    import pybel
    mol = pybel.readstring(format, smiles)
    heavyatoms =  mol.OBMol.NumHvyAtoms()
    return heavyatoms


def run_workflow(smiles_df: pd.DataFrame) -> pd.DataFrame:
    smiles_df['heavy_atoms'] = smiles_df.smiles.apply(
        lambda x: numberHeavyAtoms(x))
    return smiles_df
