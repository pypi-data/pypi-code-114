import os
import numpy as np
import pandas as pd
from scipy import interpolate


class DataHandler:
    def __init__(self, data_name):
        self.df = pd.read_csv(data_name)

    def get_column(
        self,
        column_name,
        column_index_name=None,
        elements=None,
        extend_row=False,
        inter_value=False,
    ):
        if inter_value:
            column_index, column = self.interp_two_column(
                column_index_name, column_name
            )
            indices = self.get_index_nearest_element_in_array(column_index, elements)
            result = np.array([])
            for i in indices:
                try:
                    value = np.take(column, i)
                except IndexError:
                    value = np.take(column, i - 1)
                result = np.append(result, value)
            return result

        if column_index_name and elements.size > 0:
            indices = self._get_row_indices_where_element(column_index_name, elements)
            column = self.df.loc[indices, column_name].to_numpy()
        else:
            column = self.df[column_name].to_numpy()
            column = self._remove_nan_in_array(column)

        if extend_row:
            column = self._add_zero_mach_row(column)
            return column
        else:
            return column

    @staticmethod
    def save_data(data, data_name, file_name, save_path):
        try:
            columns_name = data_name[1]
            data = pd.DataFrame(data, index=data_name[0], columns=columns_name)
        except (IndexError, TypeError):
            try:
                data = pd.DataFrame(data, index=data_name[0])
            except TypeError:
                data = pd.DataFrame(data, index=data_name)

        DataHandler.change_dir(save_path)
        transpose_data = data.T
        transpose_data.to_csv(file_name)
        DataHandler.change_dir(go_back=True)
        print(f'Saved data: {file_name!r}')

    def _get_row_indices_where_element(self, column_name, elements):
        column = self.df[column_name].isin(elements)
        return column.index[column == True].to_numpy()

    def _add_zero_mach_row(self, elements):
        return np.insert(elements, 0, elements[0])

    def _remove_nan_in_array(self, array):
        return np.array([x for x in array if str(x) != "nan"])

    def interp_two_column(self, column_left, column_right):
        column_one = self.get_column(column_left)
        column_two = self.get_column(column_right)
        try:
            column_one_interp, column_two_interp = DataHandler.interp_arrays(
                column_one, column_two
            )
        except ValueError:
            column_one_interp, column_two_interp = DataHandler.interp_arrays(
                np.flip(column_one), np.flip(column_two)
            )

        return column_one_interp, column_two_interp

    @staticmethod
    def change_dir(path=None, go_back=False):
        if go_back:
            os.chdir("..")
            return
        try:
            os.chdir(str(path))
        except FileNotFoundError:
            os.mkdir(str(path))
            os.chdir(str(path))

    @staticmethod
    def remove_first_element_in_array(*args):
        if len(args) == 1:
            array = np.array(args)
            return np.delete(array, [0])
        else:
            return [np.delete(i, [0]) for i in args]

    @staticmethod
    def interp_arrays(x, *arrays):
        did_xnew = False
        for array in arrays:
            f = interpolate.PchipInterpolator(x, array, extrapolate="bool")
            xnew = np.arange(
                x[0],
                DataHandler.get_array_last_element(x),
                DataHandler.get_step_for_interp(x),
            )
            ynew = f(xnew)
            if not did_xnew:
                result = np.concatenate(([xnew], [ynew]), axis=0)
                did_xnew = True
            else:
                result = np.concatenate((result, [ynew]), axis=0)
        return tuple([result[i] for i in range(0, len(result))])

    @staticmethod
    def get_array_last_element(array):
        return array[-1]

    @staticmethod
    def get_step_for_interp(array):
        return (array[1] - array[0]) / 1000

    @staticmethod
    def get_index_element(np_array, element):
        return np.where(np_array == element)

    @staticmethod
    def get_index_nearest_element_in_array(array, elements):
        return np.searchsorted(array, elements)

    @staticmethod
    def get_crossing_point(array_1, array_2):
        return np.argwhere(np.diff(np.sign(array_1 - array_2))).flatten()

    @staticmethod
    def get_min_or_max(array, min_or_max="min"):
        if min_or_max == "min":
            min_pos = np.argmin(array).item()
            return min_pos
        else:
            max_pos = np.argmax(array).item()
            return max_pos

    @staticmethod
    def find_min_max_from_arrays(array1, *args, find_min=True):
        did_firtst_array = False
        for array in args:
            if not did_firtst_array:
                result = DataHandler.__min_max_in_two_arrays(
                    array1, array, find_min=find_min
                )
                did_firtst_array = True
            else:
                result = DataHandler.__min_max_in_two_arrays(
                    result, array, find_min=find_min
                )
        return result

    def __min_max_in_two_arrays(array1, array2, find_min=True):
        if find_min:
            return np.minimum(array1, array2)
        else:
            return np.maximum(array1, array2)

    @staticmethod
    def prepare_data_for_plot(*args, remove_first_element=False):
        if remove_first_element:
            array = np.array(
                [DataHandler.remove_first_element_in_array(i) for i in args],
                dtype=object,
            )
        else:
            array = np.array([i for i in args], dtype=object)

        did_first = False
        for arr in array[1:]:
            array_x_int, array_y_int = DataHandler.interp_arrays(array[0], arr)
            if not did_first:
                result = np.concatenate(([array_x_int], [array_y_int]), axis=0)
                did_first = True
            else:
                result = np.concatenate((result, [array_y_int]), axis=0)
        return tuple([result[i] for i in range(0, len(result))])

    @staticmethod
    def sum_array(t):
        axes_t = np.array([0])
        sum_time = 0
        for i, _ in enumerate(t[:-1]):
            sum_time = sum_time + t[i]
            axes_t = np.append(axes_t, sum_time)
        return axes_t

    @staticmethod
    def find_diff_in_two_plot_by_target(up_plot, down_plot, x, target):
        """
        _____________________________________________________________________
        up_plot - linear function.
        down_plot - linear function divergent from first one.
        x - x values
        target - desirable different value between plot.
        _____________________________________________________________________

        This function takes two divergent linear function defined using two
        points on axis corresponded to x.

        taget is different between two function.

        Function result is x value where difference between function
        equal to target value.
        _____________________________________________________________________
        EXAMPLE:
        we have two functions:

        y1 = x + 1
        y2 = -0.1x + 1

        these function can be define using two point:

        y1 = [1, 7]
        y2 = [1, 0.4]
        x = [0, 6]

        We need to find x point where difference between them will be
        2.0 it's out target value.

        target = 2.0
        >>> find_diff_in_two_plot_by_target(y1, y2, x, target)
        1.818145751953125

        so output be approximetly 1.818 it's our desire result :)
        _____________________________________________________________________
        """

        fun1 = DataHandler.find_linear_func(x, up_plot)
        fun2 = DataHandler.find_linear_func(x, down_plot)

        while (target - (fun1(x[0]) - fun2(x[0]))) > 0.0001:
            middle_point = (x[-1] + x[0]) / 2
            if abs(fun1(middle_point) - fun2(middle_point)) > target:
                x = [x[0], middle_point]
            else:
                x = [middle_point, x[-1]]

        return middle_point

    def find_linear_func(x, y):
        left_s = y[-1] - y[0]
        right_s = x[-1] - x[0]
        if x[0] == x[-1]:
            raise ValueError
        a = left_s / right_s
        b = y[1] - a * x[1]
        return lambda x: a * x + b

    @staticmethod
    def proper_array(x0, xk, s, abs_error=0.00001):
        """
        _____________________________________________________________________
        x0 - array start value.
        xk - array end value. 
        s - step size between two value in array.
        abs_error - just be equal 0.00001
        _____________________________________________________________________

        Create array with start and stop value in it.
        """
        array = np.arange(start=x0, stop=xk, step=s, dtype='f')
        if abs(array[-1]-xk) < abs_error:
            pass
        else:
            array = np.append(array, xk)
        return array

