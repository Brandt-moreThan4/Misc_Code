from sympy import Symbol, sympify, solve
from sympy.plotting import plot


def main():
    formula = 'x - y'

    try:
        expression = sympify(formula)
    except:
        print('Invalid you dunce!')
    else:
        plot_expression(expression)


def plot_expression(expression):
    """Plots the expression in terms of y"""

    y = Symbol('y')
    solutions = solve(expression, y)
    expression_y = solutions[0]
    plot(expression_y)


if __name__ == '__main__':
    main()
