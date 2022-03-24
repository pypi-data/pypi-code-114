# from base import plot_3d, fit_surface
# import numpy as np
# from base import kriging
#
# #
# # with open(r'D:\Users\性能试验\2020\国华京燃\points.txt', 'r') as f:
# #     i = 0
# #     data = []
# #     for line in f:
# #         temp = line.strip().split(' ')
# #         data_line = [[i, c, float(d)] for c, d in enumerate(temp)]
# #         data.extend(data_line)
# #         i = i + 1
#
# with open(r'D:\Users\性能试验\2020\国华京燃\points3.txt', 'r') as f:
#     i = 0
#     data = []
#     for line in f:
#         line = line.strip()
#         if line:
#             temp = line.strip().split(' ')
#             x = float(temp[0])
#             y = float(temp[1])
#             z = float(temp[2])
#             data.append([x, y, z])
#             i = i + 1
#
# data = np.array(data)
# x = data[:, 0]
# y = data[:, 1]
# z = data[:, 2]
# plot_3d(x, y, z,
#         projection=True,
#         # surface=False,
#         x_range=np.arange(0, 21, 0.1), y_range=np.arange(0, 21, 0.1), method='kriging',
#         **{"epsilon": 1.5, "surface_rstride": 0.1, "surface_cstride": 0.1})

from yangke.common.mysql import *

res = connect_mysql(user='root', passwd='111111', db=None, return_type="engine")
create_db(res, "stocks")

print("over")

