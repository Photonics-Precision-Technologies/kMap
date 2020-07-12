import unittest
import numpy as np
from map.model.plotdata import PlotData


class TestPlotData(unittest.TestCase):

    def setUp(self):
        self.data = [[1, 2, 3], [4, 5, 6]]
        self.range_ = [[1, 2], [-1, 1]]

    def test_correct_initialization(self):

        plot_data = PlotData(self.data, self.range_)

        np.testing.assert_equal(plot_data.data, self.data)
        np.testing.assert_equal(plot_data.range, self.range_)
        np.testing.assert_equal(plot_data.data.shape, (2, 3))
        np.testing.assert_equal(plot_data.x_axis, [1, 2])
        np.testing.assert_equal(plot_data.y_axis, [-1, 0, 1])
        np.testing.assert_equal(plot_data.step_size, [1, 1])

        self.data = [[1, 2, np.nan], [4, np.inf, 6]]
        plot_data = PlotData(self.data, self.range_)

        np.testing.assert_equal(
            plot_data.data, [[1, 2, np.nan], [4, np.nan, 6]])

    def test_incorrect_data_shape(self):

        self.data = [1, 2, 3, 4, 5, 6]
        self.assertRaises(TypeError, PlotData, self.data, self.range_)

    def test_too_small_data(self):

        self.data = [[1], [2]]
        self.assertRaises(TypeError, PlotData, self.data, self.range_)

    def test_incorrect_range_shape(self):

        self.range_ = [[1, 2]]
        self.assertRaises(TypeError, PlotData, self.data, self.range_)

    def test_incorrect_range_values(self):

        self.range_ = [[1, 2], [np.nan, 1]]
        self.assertRaises(ValueError, PlotData, self.data, self.range_)

        self.range_ = [[1, 2], [np.inf, 1]]
        self.assertRaises(ValueError, PlotData, self.data, self.range_)

    def test_basic_interpolation(self):

        plot_data = PlotData(self.data, self.range_)

        new_x_axis = [1.5, 2]
        new_y_axis = [-0.5, 0, 0.5]
        new_data = plot_data.interpolate(new_x_axis, new_y_axis)
        np.testing.assert_equal(new_data, [[3, 3.5, 4], [4.5, 5, 5.5]])
        np.testing.assert_equal(plot_data.data, self.data)

        new_x_axis = [-2, 1]
        new_y_axis = [0, -0.5, -10]
        new_data = plot_data.interpolate(new_x_axis, new_y_axis)
        np.testing.assert_equal(
            new_data, [[np.nan, np.nan, np.nan], [2., 1.5, np.nan]])

        new_x_axis = [1, 1.25, 1.5, 2]
        new_y_axis = [-1, -0.25, 0.5, 1]
        new_data = plot_data.interpolate(new_x_axis, new_y_axis)
        np.testing.assert_equal(
            new_data, [[1, 1.75, 2.5, 3],
                       [1.75, 2.5, 3.25, 3.75],
                       [2.5, 3.25, 4, 4.5],
                       [4, 4.75, 5.5, 6]])

    def test_update_interpolation(self):

        plot_data = PlotData(self.data, self.range_)

        new_x_axis = [1.5, 2]
        new_y_axis = [-0.5, 0, 0.5]
        new_data = plot_data.interpolate(new_x_axis, new_y_axis, update=True)
        np.testing.assert_equal(new_data, [[3, 3.5, 4], [4.5, 5, 5.5]])
        np.testing.assert_equal(plot_data.data, [[3, 3.5, 4], [4.5, 5, 5.5]])


if __name__ == '__main__':
    unittest.main()