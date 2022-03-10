#방법1
import test_package.module_a as a
import test_package.module_b as b

#방법2
from test_package.module_a import *
from test_package.module_b import *

print(variable_a)
print(variable_b)