# import time

# animation = "|/-\\"
# idx = 0
# while True:
#     print(animation[idx % len(animation)], end="\r")
#     idx += 1
#     time.sleep(0.1)

import time

bar = [
    " [=     ]",
    " [ =    ]",
    " [  =   ]",
    " [   =  ]",
    " [    = ]",
    " [     =]",
    " [    = ]",
    " [   =  ]",
    " [  =   ]",
    " [ =    ]",
]
i = 0

while True:
    print(bar[i % len(bar)], end="\r")
    time.sleep(.2)
    i += 1
