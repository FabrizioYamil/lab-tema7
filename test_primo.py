from primo import es_primo


def test_numeros_primos():
    assert es_primo(2)
    assert es_primo(3)
    assert es_primo(13)
    assert es_primo(97)


def test_numeros_no_primos():
    assert not es_primo(4)
    assert not es_primo(9)
    assert not es_primo(100)


def test_casos_borde():
    assert not es_primo(0)
    assert not es_primo(1)
    assert not es_primo(-7)