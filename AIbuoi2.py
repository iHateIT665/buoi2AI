import numpy as np
#a
arr = np.random.randint(1, 101, (2, 7)) # mảng 2 hàng, 7 cột
print(arr)
max=0
maxIndex=0
for i in range(7):
    if arr[0,i]+ arr[1,i] > max:
        max = arr[0,i] + arr[1,i]
        maxIndex = i
print(f"Max: {max} at buổi thứ:{maxIndex+2}")
#b
max2=0
buoiSang = True
maxIndex2=0
for i in range(7):
    if arr[0,i] > max2:
        max2 = arr[0,i]
        maxIndex2 = i
        buoiSang = True
    if arr[1,i] > max2:
        max2 = arr[1,i]
        maxIndex2 = i
        buoiSang = False
if buoiSang:
    print(f"Max buổi sáng: {max2} at buổi thứ: {maxIndex2+2}")
else:
    print(f"Max buổi chiều: {max2} at buổi thứ: {maxIndex2+2}")
#c
sangHonChieu = 0
for i in range(7):
    if arr[0,i] > arr[1,i]:
        sangHonChieu += 1

if sangHonChieu > 3:
    print("Bán hàng buổi sáng tốt hơn buổi chiều")
elif sangHonChieu < 3:
    print("Bán hàng buổi chiều tốt hơn buổi sáng")
else:
    print("Bán hàng buổi sáng và chiều như nhau")
