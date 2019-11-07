

def checkFilas(sudoku):

    assert isinstance(sudoku, list), "Sudoku debe ser una lista"

    for fila in sudoku:

        for (posicion, numero) in enumerate(fila):

            if numero in fila[posicion + 1]:

                return False

    return True





##### CASOS TEST #####

if __name__ == '__main__':

    import casosTestSudoku

    for attr in sorted(casosTestSudoku.__dict__):

        if attr.startswith('__'):
            pass

        else:
            print(attr, " => ", checkFilas(casosTestSudoku.__dict__[attr]))

