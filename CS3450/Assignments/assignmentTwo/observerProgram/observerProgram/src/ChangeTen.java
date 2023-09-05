
import java.io.IOException;
import java.io.PrintWriter;
import java.io.FileWriter;

public class ChangeTen implements Observer, DisplayElement {
    LocalStocks localStocks;
    String currentData = "No Data";
    public ChangeTen(LocalStocks localStocksField) {
        this.localStocks = localStocksField;
    }
    public void update() {
        currentData = localStocks.getCurrentData();
    }

    public void display() {
        String[] displayDataArray = currentData.split("\n");

        String[] updateDateArray = displayDataArray[0].split(" ");
        String updateDate = "";

        String[] changeTenArray;
        String changeTen = "";

        for (int i = 2; i < updateDateArray.length; i++){
            updateDate += updateDateArray[i] + " ";
        }

        for (int i = 1; i < displayDataArray.length; i++) {
            changeTenArray = displayDataArray[i].split(" ");
            if ((Float.parseFloat(changeTenArray[(changeTenArray.length) - 5 ]) >= 10) || (Float.parseFloat(changeTenArray[(changeTenArray.length) - 5 ]) <= -10)) {
                changeTen += changeTenArray[(changeTenArray.length) - 9] + " ";
                changeTen += changeTenArray[(changeTenArray.length) - 8] + " ";
                changeTen += changeTenArray[(changeTenArray.length) - 5 ] + " \n";
            }

        }

        try {
            PrintWriter myWriter = new PrintWriter(new FileWriter("ChangeTen.dat", true));
            myWriter.write(updateDate + "\n" + changeTen + "\n");
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
    
    }
}
