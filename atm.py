class Atm(object):
    def __init__(self,withdrawel,enquiry,pin,cardNumber):
        self.withdrawel = withdrawel
        self.enquiry=enquiry
        self.pin = pin
        self.cardNumber = cardNumber

HDFC = Atm("1000","Change Pin","1567","11045 6457 63452")
print(HDFC.withdrawel)
print(HDFC.enquiry)
print(HDFC.pin)
print(HDFC.cardNumber)