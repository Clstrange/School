import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Stack;
import java.io.File;

public class App {
    public static void main(String[] args) throws Exception {
      Stack<Component> stack = new Stack<Component>();
      int spaceCount = 0;
      int tempSpaceCount = 0;
      try {
          File myObj = new File("directory.dat");
          Scanner myReader = new Scanner(myObj);

          String data = myReader.nextLine();
          stack.push(new Folder(data, null));
          while (myReader.hasNextLine()) {
            data = myReader.nextLine();




            for (int i = 0; i < data.length(); i++) {
              if (data.charAt(i) == ' ') {
                tempSpaceCount++;
              }
            }

            if (tempSpaceCount < spaceCount) {
              stack.pop();
            }
            spaceCount = tempSpaceCount;
            tempSpaceCount = 0;

            if (data.charAt(data.length()-1) == ':') {

              stack.peek().load(new Folder(data, stack.peek()));
              stack.push(stack.peek().getRecDir());
            } else {
              stack.peek().load(new DirFile(data));
            }




          }
          myReader.close();
        } catch (FileNotFoundException e) {
          System.out.println("An error occurred.");
          e.printStackTrace();
        }



        Component currentDirectory = stack.firstElement();

        String command = "";

        while (command.equals("q") == false) {
          Scanner scan = new Scanner(System.in); // Create Reader 
          System.out.print(currentDirectory.getName() + ">"); // Ask the user for something
          command = scan.nextLine();
          String[] cmd = command.split(" ");


          if (cmd[0].equals("chdir")) {
            currentDirectory = currentDirectory.chdir(cmd[1]);
          }
          else if (cmd[0].equals("up")) {
            currentDirectory = currentDirectory.up();
          }
          else if (cmd[0].equals("countall")) {
            System.out.println(currentDirectory.countall());
          }
          else if (cmd[0].equals("list")) {
            currentDirectory.list();
          }
          else if (cmd[0].equals("listall")) {
            currentDirectory.listall();
          }
          else if (cmd[0].equals("count")) {
            currentDirectory.count();
          }
        }
    }
}
