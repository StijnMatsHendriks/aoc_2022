import numpy as np

def find_visible_tops(data, node):
    y, x = node
    height = data[x, y]
    top_visible = 0

    left, right = data[:x, y], data[x+1:, y]
    up, down = data[x, :y], data[x, y+1:]

    scenic_score = find_num_trees_visible(left, right, up, down, height)
    top_visible = find_trees_not_blocked(top_visible, left, right, up, down, height)
    return top_visible, scenic_score

def find_first(arr, height):
    for i in range(len(arr)):
        if arr[i] >= height:
            return i + 1
    return len(arr)

def find_num_trees_visible(left, right, up, down, height):
    right_vis = find_first(right, height)
    left_vis = find_first(left[::-1], height)
    up_vis = find_first(up[::-1], height)
    down_vis = find_first(down, height)
    return right_vis * left_vis * up_vis * down_vis

def find_trees_not_blocked(top_visible, left, right, up, down, height):
    for i in [left, right, up, down]:
        if np.all(i < height):
            top_visible += 1
            return top_visible
    return top_visible

def walk_through_forest(data):
    visible_tops = get_boundary_size(data)
    scenic_score = []

    for x in range(1, data.shape[0]-1):
        for y in range(1, data.shape[1]-1):
            visible_tops_xy, scenic_score_xy = find_visible_tops(data, (x,y))
            visible_tops += visible_tops_xy
            scenic_score.append((scenic_score_xy, (x, y)))
    return visible_tops, scenic_score

def get_boundary_size(data):
    top_visible = data.shape[0] * 2 - 2 + data.shape[1] * 2 -2
    return top_visible

if __name__ == "__main__":
    data = [list(line.strip('\n')) for line in open('input.txt').readlines()]
    data = np.array([[int(height) for height in line] for line in data])
    visible_tops, scenic_score = walk_through_forest(data)
    print(visible_tops, sorted(scenic_score)[-1][0])
