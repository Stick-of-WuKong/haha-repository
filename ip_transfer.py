
"""
作者：马朴涵
时间：2022.10.17
简介：ip生成工具，可以根据合法的ip生成混淆ip
"""

if __name__ == '__main__':
    ip = input("input ip:")
    ipNum = ip.split(".")
    ipNumPoint = []
    for i in range(0,7):
        if i%2 == 0:
            ipNumPoint.append(ipNum[int(i/2)])
        else:
            ipNumPoint.append(".")
    print(ipNum)
    print(ipNumPoint)
    sum = 0
    j = 1
    for i in ipNum[::-1]:
        sum += int(i)*j
        j = j*256

    print(sum)
    print("0x%x"%sum)
    print("0%o"%sum)

    for k in range(0,127):
        for i in range(0,len(ipNumPoint)):
            if (k>>(6-i))&1 == 0:
                if ipNumPoint[i] == ".":
                    print(".",end="")
                else:
                    print("%d"%int(ipNumPoint[i]),end="")
            else:
                if ipNumPoint[i] == ".":
                    print("。",end="")
                else:
                    print("0x%x"%int(ipNumPoint[i]),end="")
        print()
