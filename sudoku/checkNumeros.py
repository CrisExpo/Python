

def checkNumeros(sudoku):

    assert isinstance(sudoku, list), "Sudoku debe ser una lista"

    numerosValidos = range(1, len(sudoku) + 1)

    for fila in sudoku:

        for numero in fila:

            if not isinstance(numero, int) or numero not in numerosValidos:
                return False

    return True

if __name__ == '__main__':

    from sudoku import casosTestSudoku

    for attr in sorted(casosTestSudoku.__dict__):

        if attr.startswith('__'):
            pass

        else:
            print(attr, " => ", checkNumeros(casosTestSudoku.__dict__[attr]))
