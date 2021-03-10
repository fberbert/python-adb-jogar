import sys
import subprocess
import time

if len(sys.argv) != 2:
    print("""
-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
Use: {} <numero de vezes>

Exemplo:
    {} 10
-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
""".format(sys.argv[0], sys.argv[0]))
    sys.exit()

quantity = sys.argv[1]
adb = '/home/fabio/android/platform-tools/adb'
phone_id = 'ro7pcio7ypwk4toz'

coordinates = [
    '1700:750:5',
    '1300:500:1',
    '1300:500:1',

    '1000:970:2',
    '1425:700:2',
    '1300:500:2',
    '1300:500:2',

    '1000:970:2',
    '1425:700:2',
    '1300:500:2',
    '1300:500:2',

    '1000:970:2',
    '1425:700:2',
    '1300:500:2',
    '1300:500:2',

    '1000:970:2',
    '1425:700:2',
    '1300:500:2',
    '1300:500:2',

    '1000:970:2',
    '1425:700:2',
    '1300:500:2',
    '1300:500:2',
]

for job in range(int(quantity)):
    for click in coordinates:
        x, y, tempo = click.split(':')
        command = 'adb -s {} shell input tap {} {}'.format(phone_id, x, y).split(' ')
        subprocess.run(command)
        print(x, y, tempo)
        time.sleep(int(tempo))
