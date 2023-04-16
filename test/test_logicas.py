from operacoes.logicas import operador_and, operador_not, operador_or

def test_logico_and_true():
    assert operador_and(True, True) == True
    
def test_logico_and_false():
    assert operador_and(False, True) == False

def test_logico_or_true():
    assert operador_or(True, False) == True
    
def test_logico_or_false():
    assert operador_or(False, False) == False
    
def test_logico_not_false():
    assert operador_not(False) == True

def test_logico_not_true():
    assert operador_not(True) == False

