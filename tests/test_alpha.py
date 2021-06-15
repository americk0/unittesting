from unittesting.alpha import get_alpha

def test_alpha(mocker):
    mocker.patch('unittesting.alpha.get_bravo', return_value=2)

    assert get_alpha() == 2
