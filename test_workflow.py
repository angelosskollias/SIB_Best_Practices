from unittest import TestCase
from workflow import run_workflow
import pandas as pd


class RunWorkflowTest(TestCase):

    def test_output_dataframe(self):
        dataframe = pd.DataFrame()
        df_out = run_workflow(dataframe)
        self.assertIsInstance(df_out, pd.DataFrame)

    def test_dataframe_consistancy(self):
        dataframe = pd.DataFrame({"id": [1, 2, 3], "smiles": ["xy", "CD", "FGH"]})
        df_out = run_workflow(dataframe)
        number_of_rows = df_out.shape[0]
        self.assertEqual(dataframe.merge(df_out, on=["id", "smiles"]).shape[0], number_of_rows)