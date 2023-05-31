import numpy as np

numbers= np.array([0,5,10,15,20,25,50,75])

result=numbers[5]#25
result=numbers[-1]#75
result=numbers[0:3]#[ 0 5 10]
result=numbers[:3]#[ 0 5 10]
result=numbers[3:]#[15 20 25 50 75]
result=numbers[::]#[0 5 10 15 20 25 50 75]
result=numbers[::-1]#[75 50 25 20 15 10  5  0]
result=numbers[::-2]#[75 25 15  5]

numbers2= np.array([[0,5,10],[15,20,25],[50,75,85]])
result=numbers2[0]#[0 5 10]
result=numbers2[2]#[50 75 85]
result=numbers2[0,2]#10
result=numbers2[2,1]#75
result=numbers2[:,2]#[10 25 85]
result=numbers2[:,0]#[ 0 15 50]
result=numbers2[:,0:2]  # [[ 0  5]
                        #  [15 20]
                        #  [50 75]]
result=numbers2[-1,:]#[50 75 85]
result=numbers2[:3,:3]  # [[ 0  5 10]
                        #  [15 20 25]
                        #  [50 75 85]]
result=numbers2[:2,:2]  # [[ 0  5]
                        #  [15  20]]
# print(result)

arr1=np.arange(0,10)
# arr2=arr1 #reference
arr2=arr1.copy()

arr2[0]=20

print(arr1)
print(arr2)



