import chess
from bfex import find_checks


def test_display():
    board = chess.Board.empty()
    assert find_checks._display_board_for_one_side(board, chess.WHITE) == ""
    assert find_checks._display_board_for_one_side(board, chess.BLACK) == ""
    
    board.set_piece_at(chess.H8, piece=chess.Piece(chess.KING, color=chess.BLACK))
    assert find_checks._display_board_for_one_side(board, chess.BLACK) == "Kh8"
    assert find_checks._display_board_for_one_side(board, chess.WHITE) == ""
