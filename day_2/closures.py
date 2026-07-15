def network():
    packets = 1
    def ping():
        nonlocal packets
        print("Request no : ",packets)
        packets+=1
        #return packets 
    return ping

req = network()

req()
req()
req()