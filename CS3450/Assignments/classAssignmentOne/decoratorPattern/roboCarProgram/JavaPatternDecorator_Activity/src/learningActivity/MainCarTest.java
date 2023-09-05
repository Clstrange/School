/**
 * Decorator demo
 * L. Thackeray
 */
package learningActivity;

public class MainCarTest
{
 
    public static void main(String[] args) 
    {
        try
        {
            final int SIZE = 3; // hard coded for now
            
            //array of CarClass Objects (polymorphic)
            CarClass[] myarray = new CarClass[SIZE];            
            
            myarray[0] = new OrdinaryCar();
            myarray[1] = new OrdinaryCompact();
            myarray[2] = new MuscleCar();
            
            for(int i =0; i < SIZE; i++)
            {
                System.out.println("Driver type: " + myarray[i].getDriverType() + 
                        " \nCar Notes: " + myarray[i].getCarNotes());      
                System.out.println("number of wheels: " + myarray[i].getWheels());                    
                System.out.println("number of cylinders: " + myarray[i].getCylinders() + 
                        " Engine size: " + myarray[i].getEngine());   
                                  
                System.out.println("\n******\n");      
            }
        }
        catch (Exception e)
        {
            System.out.print("\n error occured");
        }
    } //end Main
} // end class
