import java.io.File;  // Import the File class
import java.io.FileNotFoundException;  // Import this class to handle errors
import java.util.Scanner; // Import the Scanner class to read text files

public class Main {
    public static void main(String[] args) throws Exception {
        LocalStocks localStocks = new LocalStocks();
        Average average = new Average(localStocks);
        localStocks.registerObserver(average);

        Selections selections = new Selections(localStocks);
        localStocks.registerObserver(selections);

        ChangeTen changeTen = new ChangeTen(localStocks);
        localStocks.registerObserver(changeTen);
        // System.out.println("test");
        String screenShot = "";
        try {
            // System.out.println("test1");
            File myObj = new File("Ticker.dat");
            Scanner myReader = new Scanner(myObj);
            boolean counter = false;

            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                // System.out.println(data);
                if (data.isBlank()) {
                    if (counter == true){
                        continue;
                    }
                    // System.out.println("test3");
                    localStocks.newData(screenShot);
                    average.display();
                    changeTen.display();
                    selections.display();
                    screenShot = "";
                    counter = true;
                }
                else {
                    screenShot += (data + "\n");
                    counter = false;
                
                }

            }
            myReader.close();
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }

    }
}
