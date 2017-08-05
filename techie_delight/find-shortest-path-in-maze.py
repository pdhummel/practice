#!/usr/bin/python

import sys



def main():
    maze = [
        [ 1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
        [ 0, 1, 1, 1, 1, 1, 0, 1, 0, 1 ],
        [ 0, 0, 1, 0, 1, 1, 1, 0, 0, 1 ],
        [ 1, 0, 1, 1, 1, 0, 1, 1, 0, 1 ],
        [ 0, 0, 0, 1, 0, 0, 0, 1, 0, 1 ],
        [ 1, 0, 1, 1, 1, 0, 0, 1, 1, 0 ],
        [ 0, 0, 0, 0, 1, 0, 0, 1, 0, 1 ],
        [ 0, 1, 1, 1, 1, 9, 1, 1, 0, 0 ],
        [ 1, 1, 1, 1, 1, 0, 0, 1, 1, 1 ],
        [ 0, 0, 1, 0, 0, 1, 1, 0, 0, 1 ],
        ]
    source = "0,0"
    target = "5,7"
    
    #successful_paths = []
    shortest_path = []
    visited = []
    visited.append("0,0")
    current_x = 0
    current_y = 0
    shortest_path = find_paths(maze, current_x, current_y, visited, shortest_path, target)
    print shortest_path
    
    
def find_paths(maze, current_x, current_y, visited, shortest_path, target):
    moved = False
    # right
    new_visited = list(visited)
    if can_go(maze, current_x, current_y, current_x+1, current_y, new_visited):
        moved = True
        coord = str(current_x+1) + "," + str(current_y)
        new_visited.append(coord)
        if coord == target:
            if len(shortest_path) == 0 or len(new_visited) < len(shortest_path):
                shortest_path = new_visited
            return shortest_path
        else:
            shortest_path = find_paths(maze, current_x+1, current_y, new_visited, shortest_path, target)
    # left
    new_visited = list(visited)
    if can_go(maze, current_x, current_y, current_x-1, current_y, new_visited):
        moved = True
        coord = str(current_x-1) + "," + str(current_y)
        new_visited.append(coord)
        if coord == target:
            if len(shortest_path) == 0 or len(new_visited) < len(shortest_path):
                shortest_path = new_visited
            return shortest_path
        else:
            shortest_path = find_paths(maze, current_x-1, current_y, new_visited, shortest_path, target)        
    # down
    new_visited = list(visited)
    if can_go(maze, current_x, current_y, current_x, current_y+1, new_visited):
        moved = True
        coord = str(current_x) + "," + str(current_y+1)
        new_visited.append(coord)
        if coord == target:
            if len(shortest_path) == 0 or len(new_visited) < len(shortest_path):
                shortest_path = new_visited
            return shortest_path
        else:
            shortest_path = find_paths(maze, current_x, current_y+1, new_visited, shortest_path, target)
    # up
    new_visited = list(visited)
    if can_go(maze, current_x, current_y, current_x, current_y-1, new_visited):
        moved = True
        coord = str(current_x) + "," + str(current_y-1)
        new_visited.append(coord)
        if coord == target:
            if len(shortest_path) == 0 or len(new_visited) < len(shortest_path):
                shortest_path = new_visited
            return shortest_path
        else:
            shortest_path = find_paths(maze, current_x, current_y-1, new_visited, shortest_path, target)
    return shortest_path
        
    
def can_go(maze, current_x, current_y, new_x, new_y, visited):
    row = maze[current_y]
    if new_x < 0:
        return False
    if new_x >= len(row):
        return False
    if new_y < 0:
        return False
    if new_y >= len(maze):
        return False
    if maze[new_y][new_x] != 1 and maze[new_y][new_x] != 9:
        return False
    if str(new_x) + "," + str(new_y) in visited:
        return False
    return True
    
if __name__ == "__main__":
    main()
    
    