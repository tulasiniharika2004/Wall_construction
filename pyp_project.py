import sys
def wall_construction(width_of_wall, height_of_wall, type3_bricks_available, type2_bricks_available, type1_bricks_available):
    string= ''
    width = width_of_wall
    if width_of_wall > type3_bricks_available * 3 + type2_bricks_available * 2 + type1_bricks_available * 1 or height_of_wall <= 0:
        return 'case not possible'
    while height_of_wall >= 1:
        width_of_wall = width
        if width_of_wall > type3_bricks_available * 3 + type2_bricks_available * 2 + type1_bricks_available * 1:
            string += '\n Required case is not possible because we are left with '
            string += str(type3_bricks_available * 3 + type2_bricks_available * 2 + type1_bricks_available * 1)
            string += ' bricks only'
            break
        else:
            string += '\n'
            string,type3_bricks_available,type2_bricks_available,type1_bricks_available=print_wall(width_of_wall,type3_bricks_available,type2_bricks_available,type1_bricks_available)
            string+=string
            height_of_wall=height_of_wall-1
    return string

def print_wall(width_of_wall,type3_bricks_available,type2_bricks_available,type1_bricks_available):
    string=''
    for i in range(type3_bricks_available):
        if width_of_wall >= 3:
            string += ' ***'
            type3_bricks_available = type3_bricks_available - 1
            width_of_wall = width_of_wall - 3
    for i in range(type2_bricks_available):
        if width_of_wall >= 2:
            string += ' **'
            type2_bricks_available = type2_bricks_available - 1
            width_of_wall = width_of_wall - 2
    for i in range(type1_bricks_available):
        if width_of_wall >= 1:
            string += ' *'
            type1_bricks_available = type1_bricks_available - 1
            width_of_wall = width_of_wall - 1
    string+='\n'
    return string,type3_bricks_available,type2_bricks_available,type1_bricks_available
            
print(wall_construction(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))
