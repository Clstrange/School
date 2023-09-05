
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.io.FileWriter;

public class Selections implements Observer, DisplayElement {
    LocalStocks localStocks;
    String currentData = "No Data";
    public Selections(LocalStocks localStocksField) {
        this.localStocks = localStocksField;
    }
    public void update() {
        currentData = localStocks.getCurrentData();
    }

    public void display() {
        String[] displayDataArray = currentData.split("\n");

        String[] updateDateArray = displayDataArray[0].split(" ");
        String updateDate = "";

        String[] selectionsArray;
        String selections = "";

        ArrayList<String> selectionsOption = new ArrayList<String>(
            Arrays.asList("ALL", "BA", "BC", "GBEL", "KFT", "MCD", "TR", "WAG"));
        for (int i = 2; i < updateDateArray.length; i++){
            updateDate += updateDateArray[i] + " ";
        }

        for (int i = 1; i < displayDataArray.length; i++) {
            selectionsArray = displayDataArray[i].split(" ");
            if (selectionsOption.contains(selectionsArray[(selectionsArray.length) - 9 ])) {
                selections += displayDataArray[i] + "\n";
            }

        }

        try {
            PrintWriter myWriter = new PrintWriter(new FileWriter("Selections.dat", true));
            myWriter.write(updateDate + "\n" + selections + "\n");
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
    
    }
}
