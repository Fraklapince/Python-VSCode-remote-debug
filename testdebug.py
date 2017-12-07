import sys
import ptvsd

if ((len(sys.argv) > 0) and ('debug' in map(lambda x:x.lower(), sys.argv))) :
    ptvsd.settrace = True
    ptvsd.enable_attach(secret='testDebug', address=('0.0.0.0', 3000))

    """
    pip3 ptvsd == 3.0.0

    VSCode
    launch.json
    ...
    {
        "name": "Python: Attach",
        "type": "python",
        "request": "attach",
        "localRoot": "${workspaceRoot}",
        "remoteRoot": "/home/frak/FreeboxAPI",
        "port": 3000,
        "secret": "testDebug",
        "host": "localhost"
    },
    """
    print('Wait for debugger connexion')
    ptvsd.wait_for_attach()
    ptvsd.break_into_debugger()
    print('debug On')

print('Start')
pom = 0
pim = 0
#ptvsd.break_into_debugger()
while(ptvsd.is_attached()):
    print('.')
    pom+=1
    if((pom % 255) == 0):
        print('Pim')
        pim+=1
    
