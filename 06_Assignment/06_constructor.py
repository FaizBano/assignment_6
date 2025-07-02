# Constructor and deconstructor

class Logger:
    def __init__ (self): # self is a reference parameter jo hamen lazmi define krna parta he.
        print("Loggar object is created")
    
   
        # deinstructor ko banane k liye ham __del__ likhte hen yaani jab bhi hamara object reconstruct ya distroy hoga to ye reconsructor call hoga
    def __del__ (self):
        print ("Loggar object is distroyed")


log = Logger()
del log

