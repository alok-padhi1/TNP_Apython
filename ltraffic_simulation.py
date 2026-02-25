import time

while True:
    print("\n===== TRAFFIC LIGHT =====")
    
    # RED Light
    print(" RED Light - STOP")
    for i in range(5, 0, -1):
        print("Time Left:", i)
        time.sleep(1)
    
    # GREEN Light
    print("\n🟢GREEN Light - GO")
    for i in range(5, 0, -1):
        print("Time Left:", i)
        time.sleep(1)
    
    # YELLOW Light
    print("\n YELLOW Light - WAIT")
    for i in range(3, 0, -1):
        print("Time Left:", i)
        time.sleep(1)