public class ParkingSystem {

    int Big {get; set;}
    int Medium {get; set;}
    int Small {get; set;}

    public ParkingSystem(int big, int medium, int small) {
        Big= big;
        Medium=medium;
        Small=small;
    }
    
    public bool AddCar(int carType) {
        if (carType<1 || carType >3){
            return false;
        }

        switch(carType){
            case 1:
            if (Big<=0)
            return false;
            Big-=1;
            break;
            case 2:
            if (Medium<=0)
            return false;
            Medium-=1;
            break;
            case 3:
            if (Small<=0)
            return false;
            Small-=1;
            break;
        }
        return true;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj.AddCar(carType);
 */