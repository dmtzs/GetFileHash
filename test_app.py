import pytest
from PrincipalHash import comandoShell, prin

def test_comandoShell():
    assert comandoShell()== "cls" or "clear"