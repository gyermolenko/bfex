import chess

from bfex import find_checks


def test__display_board_for_one_side():
    board = chess.Board.empty()

    assert find_checks._convert_side_to_algebraic(board, chess.WHITE) == ""
    assert find_checks._convert_side_to_algebraic(board, chess.BLACK) == ""

    board.set_piece_at(chess.H8, piece=chess.Piece(chess.KING, color=chess.BLACK))

    assert find_checks._convert_side_to_algebraic(board, chess.BLACK) == "Kh8"
    assert find_checks._convert_side_to_algebraic(board, chess.WHITE) == ""


def test_convert_board_to_algebraic():
    board = chess.Board.empty()

    assert find_checks.convert_board_to_algebraic(board) == {"white": "", "black": ""}

    board.set_piece_at(chess.H8, piece=chess.Piece(chess.KING, color=chess.BLACK))
    board.set_piece_at(chess.A1, piece=chess.Piece(chess.QUEEN, color=chess.WHITE))

    assert find_checks.convert_board_to_algebraic(board) == {"white": "Qa1", "black": "Kh8"}


def test_convert_algebraic_to_board():
    board = chess.Board.empty()
    board.set_piece_at(chess.A1, piece=chess.Piece(chess.QUEEN, color=chess.WHITE))
    board.set_piece_at(chess.H8, piece=chess.Piece(chess.KING, color=chess.BLACK))

    assert find_checks.convert_algebraic_to_board({"white": "Qa1", "black": "Kh8"}) == board

    board = chess.Board.empty()
    board.set_piece_at(chess.A2, piece=chess.Piece(chess.PAWN, color=chess.BLACK))
    board.set_piece_at(chess.B2, piece=chess.Piece(chess.PAWN, color=chess.BLACK))

    assert find_checks.convert_algebraic_to_board({"white": "", "black": "a2, b2"}) == board
