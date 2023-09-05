package proxyassignment;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class CDatabase implements IDatabase{
    String id;
    public CDatabase(String id) {
        this.id = id;

    }

    @Override
    public String getId() {
        return id;
    }

    @Override
    public Boolean exists(String key) {
        try {
            File myObj = new File(this.id);
            Scanner myReader = new Scanner(myObj);

            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] arrOfStr = data.split(" ", 2);
                if (arrOfStr[0].equals(key)) {
                    return (true);

                }

            }
            return false;

          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
            return false;
          }
    }

    @Override
    public String get(String key) {
        try {
            File myObj = new File(this.id);
            Scanner myReader = new Scanner(myObj);

            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] arrOfStr = data.split(" ", 2);
                if (arrOfStr[0].equals(key)) {
                    return (arrOfStr[1]);

                }

            }
            return ("key does not exist");

          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
            return ("Error");
          }
    }
    
}
