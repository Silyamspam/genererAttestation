from who_is_on_my_wifi import *
import config

def sniff(mac_addr):
    WHO = who()
    #print(WHO)
    for i in range(0, len(WHO)):
        for j in WHO[i]:
            if mac_addr == j:
                print("Found your device with mac addr = "+ j +" device = " + WHO[i][5])
                return True
            else:
                print("Nothing found, you are out !")
                return False

# # sniff(config.MAC_ADR)
#
# WHO = who()
# #print(WHO)
# for i in range(0, len(WHO)):
#     print(WHO[i])
