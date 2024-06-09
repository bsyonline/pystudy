from foo import foo

foo()

from bar import foo

foo()

import foo as f1
import bar as f2

f1.foo()
f2.foo()
