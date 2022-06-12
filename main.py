# TODO:
# generate random white piece
# save position before exercise for infinite repeats

import chess
import random


def set_pieces_for_find_a_check_ex():
    board = chess.Board.empty()
    # board.set_piece_at(chess.H8, piece=chess.Piece(chess.KING, color=chess.BLACK))
    # board.set_piece_at(chess.A2, piece=chess.Piece(chess.QUEEN, color=chess.WHITE))
    set_piece_at_random_square(board, piece=chess.Piece(chess.KING, color=chess.BLACK))
    set_piece_at_random_square(board, piece=chess.Piece(chess.QUEEN, color=chess.WHITE))
    return board

def set_board_for_find_a_check_ex():
    while True:
        board = set_pieces_for_find_a_check_ex()
        if check_if_either_side_is_in_check(board):
            continue
        break
    board.turn = chess.WHITE
    return board


def set_piece_at_random_square(board, piece):
    while True:
        square = random.choice(chess.SQUARES)
        # if square not in board.piece_map():
            # break
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


def main():

    board = set_board_for_find_a_check_ex()

    while True:
        # board = generate_board()

        print('------------------------')
        print(board)

        # Show user a position in alg. form
        print('------------------------')
        for color in chess.COLORS:
            print(
                chess.COLOR_NAMES[color],
                ", ".join(piece.symbol().upper() + chess.square_name(sq) for sq, piece in board.piece_map().items() if piece.color == color)
            )

        print('------------------------')
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

if __name__ == '__main__':
    main()
