import pandas as pd
import numpy as np

# .loc 매서드를 이용한 인덱싱
# DataFrame에서 index는 행, column은 열에 인덱스를 매겨줌줌.
sampleDataFrame = pd.DataFrame(
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
    index=["r0", "r1", "r2"],
    columns=["c0", "c1", "c2"],
)
print(sampleDataFrame)

print("-------------------------------------------------")

sampleByLoc = sampleDataFrame.loc["r1"]
print(sampleByLoc)
sampleByLoc2 = sampleDataFrame.loc["r1", "c1"]
print(sampleByLoc2)
# 아니 무슨 column만 인덱싱하는건 안된단다... 그지같은 매서드를 봤나 ㅎ
# 가 아니고 방법이 있네 이렇게 하면 됨
sampleByLoc3 = sampleDataFrame.loc["r0":, "c1"]
print(sampleByLoc3)
sampleByLoc4 = sampleDataFrame.loc[["r1", "r2"], ["c0", "c1"]]
print(sampleByLoc4)

print("-------------------------------------------------")

# .iloc 매서드를 이용한 인덱싱
# 이건 라벨을 이용한게 아니라 정수를 이용해 인덱싱하는 방법

sampleByIloc = sampleDataFrame.iloc[1]
print(sampleByIloc)
sampleByIloc2 = sampleDataFrame.iloc[1, 2]
print(sampleByIloc2)
sampleByIloc3 = sampleDataFrame.iloc[0:2, 1:3]
print(sampleByIloc3)

# 빠르게 하나의 스칼라 값만 뽑을 땐 at, iat을 사용한다는데 쓸일이 거의 없을 것 같으니 안함 ㅅㄱ
