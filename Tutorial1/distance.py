import math

def distance(coord_A, coord_B):
    dist = math.sqrt((coord_A[0]-coord_B[0])**2 + (coord_A[1]-coord_B[1])**2)

    return dist

def main():
    city_A = [5, 5]
    city_B = [8, 9]
    distance_AB = distance(city_A, city_B)

    print(distance_AB)
    
main()
