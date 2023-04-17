import pytest
from seasons import chec_forf

def test_pos():
    assert chec_forf("2023-01-29") == None

def test_wrong():
    with pytest.raises(SystemExit):
         chec_forf("2023.10.29")
    with pytest.raises(SystemExit):
         chec_forf("2023-June-29")
