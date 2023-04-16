from operacoes.basicas import soma, subtracao, multiplicao, divisao

def test_soma():
    assert soma(2,2) == 4

def test_subtracao():
    assert subtracao(2,2) == 0
    
def test_multiplicacao():
    assert multiplicao(2,2) == 4
    
def test_divisao():
    assert divisao(2,2) == 1.0