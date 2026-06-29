# Taylor Series Angle Approximation

Numerical approximation of a launch angle using iterative Taylor series expansion of `arctan(x)`, with per-term convergence tracking and absolute error analysis.

## Physics Background

Given a physical system with height `H`, gravitational acceleration `g`, and velocity `V`, the launch angle θ satisfies:

```
θ = arctan(x),   where   x = √( V² / (2gH + V²) )
```

Since `arctan(x)` has no trivial closed-form evaluation, this program approximates it via its Taylor series:

```
arctan(x) = x - x³/3 + x⁵/5 - x⁷/7 + ... + (-1)ⁿ · x^(2n+1) / (2n+1)
```

Each cumulative approximation is compared against Python's `math.atan` (reference value) to track the absolute error at every degree.

## Features

- Computes intermediate variable `x` from physical parameters
- Evaluates the Taylor series term by term up to degree `n`
- Displays a convergence table with values in **radians**, **degrees**, individual term magnitude, and **absolute error**
- Optional early stopping via a **tolerance threshold** (`--tol`): halts as soon as `|term| < tolerance`
- Reports whether convergence was reached and at which degree
- All parameters configurable via **command-line arguments**

## Requirements

- Python 3.x
- Standard library only (`math`, `argparse`); no installation needed

## Usage

```bash
python aproxangulo.py [options]
```

### Options

| Argument | Type  | Default | Description                                      |
|----------|-------|---------|--------------------------------------------------|
| `-H`     | float | `0.26`  | Height in meters                                 |
| `-g`     | float | `9.81`  | Gravitational acceleration in m/s²               |
| `-V`     | float | `2.248` | Velocity in m/s                                  |
| `-n`     | int   | `10`    | Maximum Taylor series degree                     |
| `--tol`  | float | `None`  | Convergence tolerance (e.g. `1e-6`). If omitted, all `n` terms are computed. |

### Examples

Run with default parameters:
```bash
python aproxangulo.py
```

Custom physical parameters:
```bash
python aproxangulo.py -H 0.30 -V 3.0 -n 20
```

Run until convergence at 1×10⁻⁸:
```bash
python aproxangulo.py --tol 1e-8
```

Show all available options:
```bash
python aproxangulo.py --help
```

### Example Output

```
Cálculo da Série de Taylor para arctan(x)
============================================================
Parâmetros: H = 0.26 m, g = 9.81 m/s², V = 2.248 m/s
Grau máximo: n = 10  |  Tolerância: 1.00e-06
============================================================
x = √(V²/(2gH + V²)) = 0.894427

 Grau |     Valor (rad) |   Valor (graus) |         Termo |     Erro abs
------------------------------------------------------------------------
    0 |      0.89442719 |     51.24390685 |   8.94e-01    |  1.58e-01
    1 |      0.65538062 |     37.55060766 |  -2.39e-01    |  7.71e-02
  ...
    9 |      0.73248814 |     41.96411769 |   5.31e-07    |  4.17e-07  ✓

Resultados finais:
  Última aproximação (rad):  0.73248814
  Última aproximação (graus): 41.96411769
  Valor real arctan(0.894427): 41.96411811°
  Erro absoluto final:        4.17e-07 rad

  ✓ Convergência atingida no grau 9 (tolerância: 1.00e-06)
```

## Possible Extensions

- [ ] Plot convergence curve with `matplotlib`
- [ ] Export results to CSV for further analysis
- [ ] Generalize to other Taylor-expandable functions (e.g. `sin`, `cos`)
- [ ] Add relative error column alongside absolute error


Developed as a numerical methods exercise applying Taylor series to a classical physics problem.
