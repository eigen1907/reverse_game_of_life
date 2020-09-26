import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib as mpl
import tqdm as tqdm

train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")

print(train_df.head())

"""
colors = ["white", "black"]
bounds = [0, 1]
cmap = mpl.colors.ListedColormap(colors)
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
"""
print("wanted id: ")
wanted_id = int(input())
print(f"id = {wanted_id}")

delta = train_df.iloc[wanted_id, 1]
print(f"delta = {delta}")
print("===============================================================")

initial = np.array(train_df.iloc[wanted_id][2 : 2 + 625])
initial_mat = initial.reshape(25, 25)
print(f"initial_mat \n{initial_mat}")
print("===============================================================")

extended_mat = np.zeros((27, 27), int)
extended_mat[1:26, 1:26] = np.copy(initial_mat)
print(f"extended_mat \n{extended_mat}")
print("===============================================================")

extended_mat_tmp = np.copy(extended_mat)

for a in range(delta - 1):
    for i in tqdm.tqdm(range(1, 26)):
        for j in range(1, 26):
            nearCell = (
                extended_mat[i - 1][j - 1]
                + extended_mat[i - 1][j]
                + extended_mat[i - 1][j + 1]
                + extended_mat[i][j - 1]
                + extended_mat[i][j + 1]
                + extended_mat[i + 1][j - 1]
                + extended_mat[i + 1][j]
                + extended_mat[i + 1][j + 1]
            )
            if extended_mat[i][j] == 1:
                if (nearCell < 2) | (nearCell > 3):
                    extended_mat_tmp[i][j] = 0
            if extended_mat[i][j] == 0:
                if nearCell == 3:
                    extended_mat_tmp[i][j] = 1
    extended_mat = np.copy(extended_mat_tmp)
    print(f"extended_mat{a} \n{extended_mat}")
    print("===============================================================")


answer = np.copy(extended_mat[1:26, 1:26])
print(f"answer \n{answer}")
print("===============================================================")

final = np.array(train_df.iloc[wanted_id][2 + 625 : 2 + 1250])
final_mat = final.reshape(25, 25)
print(f"final_mat \n{final_mat}")
print("===============================================================")

print(np.equal(final_mat, answer))

"""
for i in range(3):
    start = np.asarray(train_df.iloc[i][2 : 2 + 625])
    start_mat = start.reshape(25, 25)

    stop = np.asarray(train_df.iloc[i][2 + 625 :])
    stop_mat = stop.reshape(25, 25)

    plt.rcParams["figure.figsize"] = (15.0, 7.0)
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.xlabel("start map")
    plt.imshow(start_mat, cmap=cmap)
    plt.colorbar()

    plt.subplot(1, 2, 2)
    plt.xlabel("stop map")
    plt.imshow(stop_mat, cmap=cmap)
    plt.colorbar()
    plt.show()
"""
