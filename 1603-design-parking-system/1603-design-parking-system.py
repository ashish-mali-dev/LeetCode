class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.Pbig=big
        self.Pmid=medium
        self.Psmall=small

    def addCar(self, carType: int) -> bool:
        if carType<1 or carType>3:
            return False
        
        match carType:
            case 1:
                if self.Pbig>=1:
                    self.Pbig-=1
                    return True
            case 2:
                if self.Pmid>=1:
                    self.Pmid-=1
                    return True
            case 3:
                if self.Psmall>=1:
                    self.Psmall-=1
                    return True
        return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)