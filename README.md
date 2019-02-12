# py-pps
##### Python PseudoPHPServer library

The module connecting Python with PPS
## Examples
### PyPPSPS
```python3
from PyPPSPS import *
p = PyPPSPS('http://pps.rf.gd', 'test')
p.connect(auto=True, force=True)
print(p.version())
p.log('test')
```
### PyPPSPC
```python3
from PyPPSPC import *
p = PyPPSPC('http://pps.rf.gd')
p.connect(auto=True, force=True)
print(p.version())
p.login('root', 'toor')
print(p.refresh())
```
