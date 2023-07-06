from unittest import TestCase, mock
from workflow import run_workflow
import pandas as pd


class RunWorkflowTest(TestCase):
    def setUp(self):
        self.dataframe = pd.DataFrame({
            "id": [1, 2, 3], 
            "smiles": ["xy", "CD", "FGH"]})

        self.patcher = mock.patch('workflow.numberHeavyAtoms')
        self.mock_numberHeavyAtoms = self.patcher.start()
        def fake_heavy_atoms(smiles):
            return {"xy": 6, "CD": 4, "FGH": 8}[smiles]
        self.mock_numberHeavyAtoms.side_effect = fake_heavy_atoms
    
    def tearDown(self) -> None:
        self.patcher.stop()

    def test_output_dataframe(self):
        df_out = run_workflow(self.dataframe)
        self.assertIsInstance(df_out, pd.DataFrame)

    def test_dataframe_consistancy(self):
        df_out = run_workflow(self.dataframe)
        number_of_rows = df_out.shape[0]
        self.assertEqual(df_out.merge(df_out, on=["id", "smiles"]).shape[0], number_of_rows)
        
    def test_has_heavy_atom_column(self):
        df_out = run_workflow(self.dataframe)
        self.assertIn("heavy_atoms", df_out.columns)
        
    def test_filter_heavy_atoms(self):
        self.assertTrue((df_out['heavy_atoms'] >=6).all())
