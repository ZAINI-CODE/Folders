from collections import deque

def get_moves(state):
    state_list = list(state)
    zero_index = state_list.index(0)
    moves = []
    x, y = zero_index // 3, zero_index % 3
    
    def swap_and_add(new_x, new_y):
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = state_list[:]
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            moves.append(tuple(new_state))
    
    swap_and_add(x - 1, y)
    swap_and_add(x + 1, y)
    swap_and_add(x, y - 1)
    swap_and_add(x, y + 1)
    
    return moves

def solve_8_puzzle_bfs(initial_state):
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    queue = deque([(initial_state, [])])
    visited = {initial_state}
    
    while queue:
        current_state, path = queue.popleft()
        if current_state == goal_state:
            return path + [current_state]
        
        for move in get_moves(current_state):
            if move not in visited:
                visited.add(move)
                queue.append((move, path + [current_state]))
    return None

def solve_8_puzzle_dfs(initial_state):
    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    stack = [(initial_state, [])]
    visited = {initial_state}
    
    while stack:
        current_state, path = stack.pop()
        if current_state == goal_state:
            return path + [current_state]
        
        for move in get_moves(current_state):
            if move not in visited:
                visited.add(move)
                stack.append((move, path + [current_state]))
    return None

initial = (1, 2, 3, 4, 0, 5, 7, 8, 6)
print("Solving with BFS...")
bfs_solution = solve_8_puzzle_bfs(initial)
print(f"BFS found a solution in {len(bfs_solution)-1} moves." if bfs_solution else "BFS: No solution")

print("\nSolving with DFS...")
dfs_solution = solve_8_puzzle_dfs(initial)
print(f"DFS found a solution in {len(dfs_solution)-1} moves." if dfs_solution else "DFS: No solution")
