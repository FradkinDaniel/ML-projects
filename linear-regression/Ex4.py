import random


def hillClimingSearch(h:list,d,y):
    fetuore = random.randint(0,2)
    change = random.randint(-5,5)
    temp = h.copy()
    temp[fetuore] += change
    newAvg = calc(d,y ,temp)
    return temp, newAvg
def calc(d,y,check):
    sum=0
    for i in range(d.__len__()):
        sum += ((check[0]+d[i][0]*check[1]+d[i][1]*check[2] )- y[i])**2
    sum /= y.__len__()
    print(sum)
    return sum


if __name__ == '__main__':
    theta = [90.0,-5.64,8.18]
    data = [[0.88,0], [0.79,1], [0.68,3], [0.65,4]]
    result = [95,88,72,66]
    avg =  calc(data,result,theta)
    for i in range(20):
        newH , newAvg =hillClimingSearch(theta,data,result)
        if avg>newAvg:
            print(newH)
            theta = newH
