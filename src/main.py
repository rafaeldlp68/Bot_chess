from chess_engine import print_board, player_move
from ai import find_best_move
import chess

# Função principal para jogar
def play_game():
    board = chess.Board()  # Cria o tabuleiro inicial
    print("Tabuleiro inicial:")
    print_board(board)

    while not board.is_game_over():  # Enquanto o jogo não acabar
        # Movimento do jogador (brancas)
        print("\nMovimento do jogador:")
        player_move(board)
        print_board(board)

        if board.is_checkmate():
            print("Xeque-mate! Jogador vence!")
            break
        elif board.is_stalemate():
            print("Empate!")
            break

        # Movimento da IA (pretas)
        print("\nMovimento da IA...")
        best_move = find_best_move(board, 3)  # Profundidade de busca 3
        board.push(best_move)
        print_board(board)

        if board.is_checkmate():
            print("Xeque-mate! IA vence!")
            break
        elif board.is_stalemate():
            print("Empate!")
            break

# Inicia o jogo
if __name__ == "__main__":
    play_game()
