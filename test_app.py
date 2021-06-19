import pytest
from PrincipalHash import comandoShell, prin

def test_comandoShell():
    bande= False
    expre1= comandoShell()== "cls"
    expre2= comandoShell()== "clear"
    
    if expre1 or expre2:
        bande= True

    assert bande== True