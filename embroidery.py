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


def draw_triangle(height):
    matrix = []
    return matrix


def draw_christmas_tree(blocks):
    matrix = []
    return matrix


def draw_circle(radius):
    matrix = []
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
