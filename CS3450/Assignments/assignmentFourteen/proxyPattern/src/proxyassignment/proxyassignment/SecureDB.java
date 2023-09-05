package proxyassignment;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class SecureDB implements IDatabase{
    IDatabase database;
    public SecureDB(IDatabase database) {
        this.database = database;
    }
    @Override
    public String getId() {
        return database.getId();
    }

    @Override
    public Boolean exists(String Key) {
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Enter username");
        String userName = myObj.nextLine();  // Read user input
        System.out.println("Enter Password");  // Output user input
        String password = myObj.nextLine();

        try {
            File thisObj = new File("userdb.dat");
            Scanner myReader = new Scanner(thisObj);

            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] arrOfStr = data.split(" ", 2);
                if (arrOfStr[0].equals(userName)) {
                    if (arrOfStr[1].equals(password)) {
                        return(this.database.exists(data));
                    }

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
        Scanner myObj = new Scanner(System.in);  // Create a Scanner object
        System.out.println("Enter username");
        String userName = myObj.nextLine();  // Read user input
        System.out.println("Enter Password");  // Output user input
        String password = myObj.nextLine();

        try {
            File thisObj = new File("userdb.dat");
            Scanner myReader = new Scanner(thisObj);

            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String[] arrOfStr = data.split(" ", 2);
                if (arrOfStr[0].equals(userName)) {
                    if (arrOfStr[1].equals(password)) {
                        return(this.database.get(data));
                    }

                }

            }
            return ("Incorrect username or password");
          } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
          }
          return ("Incorrect username or password");
    }
    
}
