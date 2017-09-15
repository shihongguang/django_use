# view opt

```python
from django.contrib.auth.decorators import login_required

from view import *

@instance(login_required)
class Test(view):
    pass

```