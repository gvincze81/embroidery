def draw_rectangle(width, height, border_color=1, fill_color=1, border_width=1):
    matrix = []
    for i in range(height):
        submatrix = []
        for j in range(width):
            if border_width <= i < height - border_width and border_width <= j < width - border_width:
                submatrix.append(fill_color)
            else:
                submatrix.append(border_color)
        matrix.append(submatrix)
    return matrix


def draw_triangle(height, border_color=1, fill_color=1):
    width = (height - 1) * 2 + 1    # +1 is the top, -1 is the top row
    matrix = []
    for i in range(height):
        submatrix = []
        for j in range(width):
            if i == height - 1 or i + j == height - 1 or j - i == height - 1:
                submatrix.append(border_color)
            elif i + j < height - 1 or j - i > height - 1:
                submatrix.append(0)
            else:
                submatrix.append(fill_color)
        matrix.append(submatrix)
    return matrix


def draw_christmas_tree(blocks, border_color=1, fill_color=1):
    height = blocks * 3 # one block is 3 rows high
    width = 3 + blocks * 2 # last row of each block is 2 cells longer than the previous one
    
    matrix = []
    base = (width - 1) // 2
    for i in range(height):
        quotient = i // 3
        left_border = base + 2 * quotient
        right_border = base - 2 * quotient
        submatrix = []
        for j in range(width):
            if i + j == left_border or j - i == right_border or i == height - 1:
                submatrix.append(border_color)
            elif left_border < i + j and j - i < right_border:
                submatrix.append(fill_color)
            else:
                submatrix.append(0)
        matrix.append(submatrix)
    return matrix


def draw_circle(radius, border_color=1, fill_color=1, background_color=0):
    x = radius    # center of circle
    width = 2 * radius + 1
    matrix = []
    for i in range(width):
        submatrix = []
        for j in range(width):
            hypotenuse = math.floor( ((i - x) ** 2 + (j - x) ** 2) ** 0.5 )
            if hypotenuse == radius:
                submatrix.append(border_color)
            elif hypotenuse < radius:
                submatrix.append(fill_color)
            else:
                submatrix.append(background_color)
        matrix.append(submatrix)
    return matrix


def embroider(matrix, color_scheme):
    for row in matrix:
        for cell in row:
            print(color_scheme[cell], end='')
        print()
    print()


if __name__ == '__main__':
    color_scheme = {0: ' ', 1: '*', 2: '.'}
    embroider([[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 2, 1, 0, 0], [0, 1, 2, 2, 2, 1, 0], [1, 1, 1, 1, 1, 1, 1]], color_scheme)

    # This should have the same output:
    # embroider(draw_triangle(4, border_color=1, fill_color=2), color_scheme)
