from __future__ import print_function
import yaml

def header_to_phidget_num(n,m):
    return 2*(n-1) + m

header_list = [
        (3,  1),   # region 0
        (2,  0),   # region 1
        (2,  1),   # etc
        (1,  0),
        (1,  1),
        (5,  0),
        (4,  1),
        (3,  0),
        (17, 0), 
        (18, 0),
        (6,  1),
        (5,  1),
        (4,  0),
        (16, 0),
        (17, 1),
        (6,  0),
        (7,  1),
        (7,  0), 
        (15, 0),
        (16, 1),
        (8,  0), 
        (8,  1),
        (13, 0), 
        (14, 0),
        (15, 1),
        (9,  1),
        (12, 1),
        (12, 0),
        (13, 1),
        (14, 1),
        (9,  0),
        (10, 1),
        (10, 0),
        (11, 1),
        (11, 0),
        ]

phidget_num_list = [header_to_phidget_num(*h) for h in header_list]

with open('ledmap.yaml','w') as f:
    yaml.dump(phidget_num_list,f)




