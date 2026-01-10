from flask import Flask, render_template, request, jsonify
import random, copy

app = Flask(__name__)


EASY_PUZZLES = [
    [
        [5,3,0,0,7,0,0,0,2],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,4,0,5,6,0],
        [8,0,9,7,6,1,0,0,3],
        [4,2,0,8,0,3,0,9,1],
        [7,0,3,0,2,4,8,0,0],
        [0,6,1,0,3,7,0,8,0],
        [0,0,7,4,1,9,0,3,5],
        [3,0,0,0,8,0,0,7,9]
    ]
]

MEDIUM_PUZZLES = [
    [
        [5,0,0,0,7,0,0,0,2],
        [6,0,0,1,0,5,0,0,0],
        [0,9,8,0,0,0,5,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,6,8,0,3,7,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,0,9,0,0,5],
        [3,0,0,0,8,0,0,0,9]
    ]
]

HARD_PUZZLES = [
    [
        [0,0,0,0,0,0,0,1,2],
        [0,0,0,1,0,0,0,0,0],
        [0,9,0,0,0,0,5,0,0],
        [0,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [0,0,0,0,2,0,0,0,0],
        [0,6,0,0,0,0,2,0,0],
        [0,0,0,4,0,9,0,0,0],
        [0,0,0,0,8,0,0,0,0]
    ]
]

PUZZLES = {"easy": EASY_PUZZLES, "medium": MEDIUM_PUZZLES, "hard": HARD_PUZZLES}


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_puzzle", methods=["POST"])
def get_puzzle():
    level = request.json["level"]
    return jsonify(copy.deepcopy(random.choice(PUZZLES[level])))

@app.route("/solve", methods=["POST"])
def solve():
    board = request.json["board"]

    def valid(r, c, n):
        for i in range(9):
            if board[r][i] == n or board[i][c] == n:
                return False
        sr, sc = 3 * (r // 3), 3 * (c // 3)
        for i in range(sr, sr + 3):
            for j in range(sc, sc + 3):
                if board[i][j] == n:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for n in range(1, 10):
                        if valid(r, c, n):
                            board[r][c] = n
                            if backtrack():
                                return True
                            board[r][c] = 0
                    return False
        return True

    backtrack()
    return jsonify(board)

if __name__ == "__main__":
    app.run(debug=True)