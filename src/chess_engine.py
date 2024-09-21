import chess

# Função para exibir o tabuleiro
def print_board(board):
    print(board)

# Função para permitir que o jogador humano faça um movimento
def player_move(board):
    move = input("Digite seu movimento (ex: e2e4): ")
    try:
        board.push_san(move)  # Converte o movimento no formato do xadrez para o tabuleiro
    except ValueError:
        print("Movimento inválido. Tente novamente.")
        player_move(board)  # Se inválido, peça outro movimento
import chess

# Função para exibir o tabuleiro
def print_board(board):
    print(board)

# Função para permitir que o jogador humano faça um movimento
def player_move(board):
    move = input("Digite seu movimento (ex: e2e4): ")
    try:
        board.push_san(move)  # Converte o movimento no formato do xadrez para o tabuleiro
    except ValueError:
        print("Movimento inválido. Tente novamente.")
        player_move(board)  # Se inválido, peça outro movimento
