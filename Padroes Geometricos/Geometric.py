def draw_triangle(rows):
    """Desenha um triângulo retângulo com estrelas."""
    print("Triângulo Retângulo:")
    for i in range(1, rows + 1):
        print("*" * i)
    print()


def draw_inverted_triangle(rows):
    """Desenha um triângulo retângulo invertido."""
    print("Triângulo Retângulo Invertido:")
    for i in range(rows, 0, -1):
        print("*" * i)
    print()


def draw_square(size):
    """Desenha um quadrado com estrelas."""
    print("Quadrado:")
    for _ in range(size):
        print("*" * size)
    print()


def draw_right_pyramid(rows):
    """Desenha uma pirâmide alinhada à direita."""
    print("Pirâmide Alinhada à Direita:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)
    print()


def draw_equilateral_pyramid(rows):
    """Desenha uma pirâmide equilátera."""
    print("Pirâmide Equilátera:")
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    print()


def draw_diamond(rows):
    """Desenha um losango (baseado na pirâmide equilátera)."""
    print("Losango:")
    # Parte superior
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    # Parte inferior
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "*" * (2 * i - 1))
    print()


def main():
    print("Escolha um padrão geométrico:")
    print("1. Triângulo Retângulo")
    print("2. Triângulo Retângulo Invertido")
    print("3. Quadrado")
    print("4. Pirâmide Alinhada à Direita")
    print("5. Pirâmide Equilátera")
    print("6. Losango")
    print("7. Sair")

    while True:
        choice = input("Digite o número da sua escolha: ")
        if choice == "1":
            rows = int(input("Digite o número de linhas: "))
            draw_triangle(rows)
        elif choice == "2":
            rows = int(input("Digite o número de linhas: "))
            draw_inverted_triangle(rows)
        elif choice == "3":
            size = int(input("Digite o tamanho do quadrado: "))
            draw_square(size)
        elif choice == "4":
            rows = int(input("Digite o número de linhas: "))
            draw_right_pyramid(rows)
        elif choice == "5":
            rows = int(input("Digite o número de linhas: "))
            draw_equilateral_pyramid(rows)
        elif choice == "6":
            rows = int(input("Digite o número de linhas (metade do losango): "))
            draw_diamond(rows)
        elif choice == "7":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()
