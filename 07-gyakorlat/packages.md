# Packages

Unit teszteléshez: https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
## Nose
`pip install nose`
Teszt-keretrendszer Bővebben [itt](http://nose.readthedocs.io/)


## PyCodeStyle (PEP8)

`pip install pycodestlye`
pep8 --first 
pep8 --show-source --show-pep8

Style guide
http://pycodestyle.pycqa.org/en/latest/
https://www.python.org/dev/peps/pep-0008/

## Flake8 
Gyakorlatilag különböző eszközöket csomagol egybe:
- Lint checker, PyFlakes projekt
- PEP8 checker, PyCodeStyle projekt
- MCCC checker, McCabe projekt

http://flake8.pycqa.org/en/latest/

## Coverage
Lefedettség mérésre
`pip install coverage`

Program futtatása, közben lefedettség mérés:
`coverage run 01tests.py`

Az eredmények exportálása
`coverage report -m`
`coverage html`

## Tox
Egész tesztelési folyamat automatizáló keretrendszer
https://tox.readthedocs.io


## Mock 
Mock keretrendszer. 
https://docs.python.org/3/library/unittest.mock.html

