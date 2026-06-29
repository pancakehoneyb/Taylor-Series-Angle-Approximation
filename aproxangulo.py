import math
import argparse

def calcular_x(H, g, V):
    """Calcula o valor de x baseado nos parâmetros H, g e V"""
    return math.sqrt(V**2 / (2*g*H + V**2))

def serie_taylor_arctan(x, n, tolerancia=None):
    """
    Calcula a série de Taylor para arctan(x) até o grau n.
    Série: x - x³/3 + x⁵/5 - x⁷/7 + ... + (-1)^n * x^(2n+1)/(2n+1)

    Se uma tolerância for fornecida, interrompe antecipadamente quando
    |termo_atual| < tolerância (critério de convergência).

    Retorna lista de (grau, aproximação_acumulada, termo, convergiu).
    """
    resultado = 0.0
    termos = []

    for i in range(n + 1):
        termo = ((-1)**i) * (x**(2*i + 1)) / (2*i + 1)
        resultado += termo
        convergiu = tolerancia is not None and abs(termo) < tolerancia
        termos.append((i, resultado, termo, convergiu))
        if convergiu:
            break

    return termos

def parse_args():
    parser = argparse.ArgumentParser(
        description="Aproximação do ângulo via série de Taylor para arctan(x).",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-H", type=float, default=0.26,
                        help="Altura em metros")
    parser.add_argument("-g", type=float, default=9.81,
                        help="Aceleração da gravidade em m/s²")
    parser.add_argument("-V", type=float, default=2.248,
                        help="Velocidade em m/s")
    parser.add_argument("-n", type=int, default=10,
                        help="Grau máximo da série de Taylor")
    parser.add_argument("--tol", type=float, default=None,
                        help="Tolerância para critério de convergência (ex: 1e-6). "
                             "Se omitido, calcula todos os n termos.")
    return parser.parse_args()

def main():
    args = parse_args()
    H, g, V, n, tolerancia = args.H, args.g, args.V, args.n, args.tol

    print("Cálculo da Série de Taylor para arctan(x)")
    print("=" * 60)
    print(f"Parâmetros: H = {H} m, g = {g} m/s², V = {V} m/s")
    print(f"Grau máximo: n = {n}", end="")
    if tolerancia is not None:
        print(f"  |  Tolerância: {tolerancia:.2e}")
    else:
        print()
    print("=" * 60)

    # Calcula x
    x = calcular_x(H, g, V)
    print(f"x = √(V²/(2gH + V²)) = {x:.6f}\n")

    # Calcula a série de Taylor
    resultados = serie_taylor_arctan(x, n, tolerancia)

    # Valor de referência
    valor_real = math.atan(x)
    valor_real_graus = math.degrees(valor_real)

    # Tabela de resultados
    print(f"{'Grau':>5} | {'Valor (rad)':>15} | {'Valor (graus)':>15} | {'Termo':>13} | {'Erro abs':>12}")
    print("-" * 72)

    grau_convergencia = None
    for grau, aproximacao, termo, convergiu in resultados:
        graus = math.degrees(aproximacao)
        erro = abs(aproximacao - valor_real)
        marcador = " ✓" if convergiu else ""
        print(f"{grau:>5} | {aproximacao:>15.8f} | {graus:>15.8f} | {termo:>13.2e} | {erro:>12.2e}{marcador}")
        if convergiu:
            grau_convergencia = grau

    ultima_aprox = resultados[-1][1]

    print()
    print("Resultados finais:")
    print(f"  Última aproximação (rad):  {ultima_aprox:.8f}")
    print(f"  Última aproximação (graus): {math.degrees(ultima_aprox):.8f}")
    print(f"  Valor real arctan({x:.6f}): {valor_real_graus:.8f}°")
    print(f"  Erro absoluto final:        {abs(ultima_aprox - valor_real):.2e} rad")

    if grau_convergencia is not None:
        print(f"\n  ✓ Convergência atingida no grau {grau_convergencia} (tolerância: {tolerancia:.2e})")
    elif tolerancia is not None:
        print(f"\n  ✗ Convergência não atingida em {n} termos (tolerância: {tolerancia:.2e})")

if __name__ == "__main__":
    main()
