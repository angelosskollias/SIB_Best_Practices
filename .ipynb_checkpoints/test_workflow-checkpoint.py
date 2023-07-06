from unittest import TestCase
from workflow import run_workflow
import pandas as pd


class RunWorkflowTest(TestCase):
    def setUp(self):
        self.dataframe = pd.DataFrame({"id": [1, 2, 3], "smiles": ["xy", "CD", "FGH"]})
    
    def test_output_dataframe(self):
        df_out = run_workflow(self.dataframe)
        self.assertIsInstance(df_out, pd.DataFrame)

    def test_dataframe_consistancy(self):
        df_out = run_workflow(self.dataframe)
        number_of_rows = df_out.shape[0]
        self.assertEqual(dataframe.merge(df_out, on=["id", "smiles"]).shape[0], number_of_rows)
        
    def test_has_heavy_atom_column(self):
        df_out = run_workflow(self.dataframe)
        self.assertIn("heavy_atoms", df_out.columns)
        