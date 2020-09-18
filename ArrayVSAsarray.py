import numpy as np

arr = np.arange(8).reshape(2, 4)

print(arr)
print(type(arr))

arr2 = arr
arr3 = np.copy(arr)

arr[0] = 10
print(arr)
print(arr2)
print(arr3)

print("----------------------------------------")

asarr = np.asarray([[0, 1, 2, 3], [4, 5, 6, 7]])
print(asarr)
print(type(asarr))

asarr2 = asarr
asarr3 = np.copy(asarr)

asarr[0] = 10
print(asarr)
print(asarr2)
print(asarr3)

print("----------------------------------------")

arrA = np.zeros([4, 2], int)
arrB = np.array(arrA)
arrC = np.asarray(arrA)

arrA[0] = 10

print(arrA)
print(arrB)
print(arrC)

print(
    "결론은 array자체는 값형으로 취급한다(계산이 훨씬 빠르기 때문)"
    "그러나 array를 슬라이싱 하게 되면 참조형으로 슬라이싱이 됨(즉 원본에 의해 본인도 변함)"
    "슬라이싱 한 array를 값형으로 쓰고 싶다면? np.copy를 사용하면 값형, 즉 복사본이 생성됨(원본이 변해도 변하지 않음)"
    "만약 array자체를 참조형으로 쓰고 싶다면 asarray를 사용하도록 하자(asarray는 참조형)"
    "참고로 array는 그냥 ndarray라는 클래스를 만드는 함수일 뿐임 array자체가 객체는 아님"
)
