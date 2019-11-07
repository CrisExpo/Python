

def checkFilas(sudoku):

    assert isinstance(sudoku, list), "Sudoku debe ser una lista"

    pass

    return True





##### CASOS TEST #####

if __name__ == '__main__':

    import casosTestSudoku

    for attr in sorted(casosTestSudoku.__dict__):

        if attr.startswith('__'):
            pass

        else:
            print(attr, " => ", checkFilas(casosTestSudoku.__dict__[attr]))

