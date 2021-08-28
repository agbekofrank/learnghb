# from .base import *
# try:
#     from .production import * 
# except:
#     pass

# try:
#     from .local import * 
# except:
#     pass

from .base import *

try:
    from .local import *
    live = False

except:
    live = True

if live:
    from .production import *
