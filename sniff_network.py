from who_is_on_my_wifi import *


WHO = who()
mac_addr = "my mac addr"
#print(WHO)
for i in range(0, len(WHO)):
    for j in WHO[i]:
        if mac_addr == j:
            print("Found your device with mac addr = "+ j +" device = " + WHO[i][5])
            break
    #print(WHO[i])
