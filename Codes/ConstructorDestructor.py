import gc

class Demo:
    def __init__(self):
        print("Inside Constructor")
        
    def __del__(self):
        print("Inside Destructor")

obj = Demo()

del obj

gc.collect()

print("End of Application")