
import java.io.IOException;
import java.io.PrintWriter;
import java.io.FileWriter;

public class Average implements Observer, DisplayElement {
    LocalStocks localStocks;
    String currentData = "No Data";
    public Average(LocalStocks localStocksField) {
        this.localStocks = localStocksField;
    }
    public void update() {
        currentData = localStocks.getCurrentData();
    }

    public void display() {
        String[] displayDataArray = currentData.split("\n");

        String[] updateDateArray = displayDataArray[0].split(" ");
        String updateDate = "";

        String[] averageDataArray;
        float average = 0;

        for (int i = 2; i < updateDateArray.length; i++){
            updateDate += updateDateArray[i] + " ";
        }

        for (int i = 1; i < displayDataArray.length; i++) {
            averageDataArray = displayDataArray[i].split(" ");
            average += Float.parseFloat(averageDataArray[(averageDataArray.length) - 8]);
        }
        average = average/(displayDataArray.length - 1);
        
        try {
            PrintWriter myWriter = new PrintWriter(new FileWriter("Average.dat", true));
            myWriter.write(updateDate + ", Average price: " + average + "\n");
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
    
    }
}
