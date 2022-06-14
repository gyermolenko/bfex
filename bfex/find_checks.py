# TODO:
# generate random white piece
# add "reveal board" to UI

import random

import chess


def set_pieces_for_find_a_check():
    board = chess.Board.empty()
    # board.set_piece_at(chess.H8, piece=chess.Piece(chess.KING, color=chess.BLACK))
    # board.set_piece_at(chess.A2, piece=chess.Piece(chess.QUEEN, color=chess.WHITE))
    set_piece_at_random_square(board, piece=chess.Piece(chess.KING, color=chess.BLACK))
    set_piece_at_random_square(board, piece=chess.Piece(chess.QUEEN, color=chess.WHITE))
    return board


def set_board_for_find_a_check() -> chess.Board:
    while True:
        board = set_pieces_for_find_a_check()
        if check_if_either_side_is_in_check(board):
            continue
        break
    board.turn = chess.WHITE
    return board


def set_piece_at_random_square(board, piece):
    while True:
        square = random.choice(chess.SQUARES)
        if square in board.piece_map():
            continue
        break
    board.set_piece_at(square, piece=piece)
    return square


def check_if_either_side_is_in_check(board):
    if board.is_check():
        return True
    board.turn = not board.turn
    if board.is_check():
        return True
    return False


def _convert_side_to_algebraic(board, color) -> str:
    return ", ".join(
        piece.symbol().upper() + chess.square_name(sq)
        for sq, piece in board.piece_map().items()
        if piece.color == color
    )


def convert_board_to_algebraic(board: chess.Board) -> dict:
    return {
        "white": _convert_side_to_algebraic(board, chess.WHITE),
        "black": _convert_side_to_algebraic(board, chess.BLACK),
    }


def convert_algebraic_to_piecetype_and_square(san: str):
    """
    Qa8 -> chess.QUEEN + chess.A8 (piece type + square)
    """
    match = chess.SAN_REGEX.match(san)
    if match.group(1):
        piece_type = chess.PIECE_SYMBOLS.index(match.group(1).lower())
    else:
        piece_type = chess.PAWN

    square = chess.SQUARE_NAMES.index(match.group(4))

    return piece_type, square


def convert_algebraic_to_board(alg: dict) -> chess.Board:
    """
    dict like {"white": "a2", "black": "Kh3"} -> chess.Board
    """
    board = chess.Board.empty()
    white = alg["white"]
    black = alg["black"]
    if white:
        for piece in white.split(","):
            piece_type, square = convert_algebraic_to_piecetype_and_square(piece.strip())
            board.set_piece_at(square, piece=chess.Piece(piece_type, color=chess.WHITE))
    if black:
        for piece in black.split(","):
            piece_type, square = convert_algebraic_to_piecetype_and_square(piece.strip())
            board.set_piece_at(square, piece=chess.Piece(piece_type, color=chess.BLACK))

    return board


def check_solution(board, move):
    in_check = False

    board.push_san(move)

    if board.is_check():
        in_check = True
    else:
        in_check = False

    board.pop()
    return in_check


def main():

    board = set_board_for_find_a_check()

    while True:

        print("------------------------")
        print(board)

        # Show user the position in alg. form
        print("------------------------")
        board_alg = convert_board_to_algebraic(board)
        for color in board_alg:
            print(f"{color}: {board_alg[color]}")

        print("------------------------")
        move = input("Make a move: ")
        if move == "q":
            exit()

        try:
            in_check = check_solution(board, move)
        except ValueError:
            print("Invalid move")
        else:
            if in_check:
                print("Check")
            else:
                print("Not a check")


if __name__ == "__main__":
    main()
