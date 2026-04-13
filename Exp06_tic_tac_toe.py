#6 typical AI problem (tic-tac-toe)
def check_winner(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != '_': return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != '_': return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != '_': return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != '_': return b[0][2]
    return None
def minimax(b, d, is_max):
    w = check_winner(b)
    if w: return (10 - d) if w == 'X' else (d - 10)
    if not any('_' in r for r in b): return 0
    best = -float('inf') if is_max else float('inf')
    for i in range(3):
       for j in range(3):
            if b[i][j] == '_':
                b[i][j] = 'X' if is_max else 'O'
                score = minimax(b, d + 1, not is_max)
                b[i][j] = '_'
                best = max(best, score) if is_max else min(best, score)
    return best
def best_move(b):
    best_score, move = -float('inf'), (-1, -1)
    for i in range(3):
        for j in range(3):
            if b[i][j] == '_':
                b[i][j] = 'X'
                score = minimax(b, 0, False)
                b[i][j] = '_'
                if score > best_score: best_score, move = score, (i, j)
    return move
board = [['X', 'O', 'X'], ['O', '_', '_'], ['_', '_', 'X']]
print(best_move(board))
