# TODO:
# generate random white piece
# save position before exercise for infinite repeats

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


def _display_board_for_one_side(board, color) -> str:
    return ", ".join(
        piece.symbol().upper() + chess.square_name(sq)
        for sq, piece in board.piece_map().items()
        if piece.color == color
    )


def display_board_in_algebraic_form(board) -> None:
    for color in chess.COLORS:
        print(chess.COLOR_NAMES[color], _display_board_for_one_side(board, color))


def main():

    board = set_board_for_find_a_check()

    while True:
        # board = generate_board()

        print("------------------------")
        print(board)

        # Show user a position in alg. form
        print("------------------------")
        display_board_in_algebraic_form(board)

        print("------------------------")
        move = input("Make a move: ")
        if move == "q":
            exit()

        # make a move
        try:
            board.push_san(move)
        except ValueError:
            print("Invalid move")
        else:
            # check results
            if board.is_check():
                print("Check")
            else:
                print("Not a check")
            board.pop()


if __name__ == "__main__":
    main()
