from unittest import TestCase
from workflow import run_workflow
import pandas as pd


class RunWorkflowTest(TestCase):
    
    def test_output_dataframe(self):
        dataframe = pd.DataFrame()
        df_out = run_workflow(dataframe)
        self.assertIsInstance(df_out, pd.DataFrame)
