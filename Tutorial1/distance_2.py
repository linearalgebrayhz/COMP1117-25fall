import math

def distance(A, B):
    return math.sqrt((A[0]-B[0])**2 + (A[1] - B[1])**2)

city_A = [5, 5]
city_B = [8, 9]

print(distance(city_A, city_B))
