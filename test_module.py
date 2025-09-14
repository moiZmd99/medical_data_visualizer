import unittest
import pandas as pd
from medical_data_visualizer import df, draw_cat_plot, draw_heat_map

class TestMedicalDataVisualizer(unittest.TestCase):

    def test_dataframe_loaded(self):
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)
        required_columns = [
            'age', 'height', 'weight', 'gender', 'ap_hi', 'ap_lo',
            'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight'
        ]
        for col in required_columns:
            self.assertIn(col, df.columns)

    def test_overweight_column(self):
        self.assertIn('overweight', df.columns)
        self.assertTrue(df['overweight'].isin([0, 1]).all())

    def test_normalized_columns(self):
        self.assertTrue(df['cholesterol'].isin([0, 1]).all())
        self.assertTrue(df['gluc'].isin([0, 1]).all())

    def test_draw_cat_plot(self):
        fig = draw_cat_plot()
        self.assertTrue(hasattr(fig, "savefig"))

    def test_draw_heat_map(self):
        fig = draw_heat_map()
        self.assertTrue(hasattr(fig, "savefig"))

if __name__ == '__main__':
    unittest.main()
