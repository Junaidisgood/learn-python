class Mobile:
    old_phone = "Keypad"
    new_phone = "Touchscreen"

    def old(self):
        print("1. " + self.old_phone)
        pass
    
    def new(self):
        print("2. " + self.new_phone)
        pass
    pass

def Main():
    myMobile = Mobile()
    myMobile.old()
    myMobile.new()
    pass

Main()