def area_of_triangle(side_a, side_b, side_c):
    semi_perimiter = 1 / 2 * (side_a + side_b + side_c)
    area = (semi_perimiter * (semi_perimiter - side_a) * (semi_perimiter - side_b) * (semi_perimiter - side_c)) ** (0.5) 
    return area

if __name__ == '__main__':
    print(area_of_triangle(3, 4, 5))