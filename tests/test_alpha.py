import pytest
import unittesting.alpha

def test_alpha(mocker):
    mocker.patch('unittesting.alpha.bravo', return_value=2)

    assert get_alpha() == 2
