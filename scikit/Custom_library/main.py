import numpy as np
# from scikit.Custom_library.preprocessing import cust_std_scaler
# from scikit.Custom_library.preprocessing import cust_scaler

# data = np.array([[1],[2],[3],[4],[5]])

# print(cust_std_scaler(data),"\n")
# print(cust_scaler(data))
from scikit.Custom_library.preprocessing import MinMaxScaler
y = np.arange(100)
my_scaler = MinMaxScaler()
my_scaler.fit(y)
print()