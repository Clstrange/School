package learningActivity;
/*
Car master class
L. Thackeray
*/
public abstract class CarClass 
{
    protected double engineSize = 345;
    protected int wheels = 4;
    protected int cylinders = 8;    
    protected String driverType = "none";
    protected String carNotes = "none";
    
    public double getEngine()
    {
        return engineSize;        
    }
    
    public double getWheels()
    {
        return wheels;        
    }
    
    public double getCylinders()
    {
        return cylinders;        
    }    
    
    public String getDriverType()
    {    
        return driverType;
    }
    public  String getCarNotes()
     {
       return carNotes;

    }
}


