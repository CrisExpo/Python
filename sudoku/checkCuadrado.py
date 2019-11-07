

def checkCuadrado(sudoku):

    assert isinstance(sudoku, list), "Sudoku debe ser una lista"

    sudokuSano = True
    numeroFilas = len(sudoku)

    for fila in sudoku:

        if len(fila != numeroFilas):
            sudokuSano = False
            break

    assert isinstance(sudoku, bool), "Se exige devolver un valo lógico"

    return sudokuSano


if __name__ == '__main':

    from sudoku import casosTestSudoku

    for attr in sorted(casosTestSudoku.__dict__):

        if attr.startswith('__'):
            pass

        else:
            print(attr, " => ", checkCuadrado(casosTestSudoku.__dict__[attr]))
