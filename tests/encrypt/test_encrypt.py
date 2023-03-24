from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 5)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('olá', 'olá')

    assert encrypt_message('olá', 5) == 'álo'
    assert encrypt_message('testando123testando', 3) == 'set_odnatset321odnat'
