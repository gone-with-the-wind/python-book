# -*- coding: utf-8 -*-
for i in range(5):
    for j in range(5):
        for k in range(5):
            if (i == j == k == 3):
                break
            else:    
                print (i, '----', j, '----', k)
        else:        # else1
            continue
        break        # break1
    else:            # else2
        continue
    break     
 
 