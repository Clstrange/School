import java.io.File;
import java.io.FileWriter;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        FileWriter fileWriter = new FileWriter("output.txt");
        Output streamOutput = new StreamOutput(fileWriter);

        Scanner fileInput = new Scanner(System.in);
        System.out.print("Enter a file to read in: ");
        String file = fileInput.nextLine();

        File openFile = new File(file);
        Scanner sc = new Scanner(openFile);
        Scanner addOns;
        String userInput;
        addOns = new Scanner(System.in);
        System.out.print("select what decorators you would like: \nLineOutput \nNumberedOutput \nTeeOutput \nFilterOutput \nEnter 'done' when you have selected all of your decorators: ");
        userInput = addOns.nextLine();
        System.out.print("\n\n");
        while(!userInput.equals("done")) {
            switch(userInput) {
                case "LineOutput":
                    streamOutput = new LineOutput(streamOutput);
                    break;
                case "NumberedOutput":
                    streamOutput = new NumberedOutput(streamOutput);
                    break;
                case "TeeOutput":
                    Scanner secondFileInput = new Scanner(System.in);
                    System.out.print("Enter a file to read to");
                    String secondFile = secondFileInput.nextLine();
                    FileWriter secondFileWriter = new FileWriter(secondFile);
                    streamOutput = new TeeOutput(streamOutput, secondFileWriter);
                    break;
                case "FilterOutput":
                    streamOutput = new FilterOutput(streamOutput);
                    break;
                default:
                    System.out.println("Incorrect decorator name...");
                    break;
            }
            addOns = new Scanner(System.in);
            System.out.print("select what decorators you would like: \nLineOutput \nNumberedOutput \nTeeOutput \nFilterOutput \nEnter 'done' when you have selected all of your decorators: ");
            userInput = addOns.nextLine();
            System.out.println("\n\n");
        }
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            streamOutput.write(line);
        }
        addOns.close();
        sc.close();
        fileWriter.close();
        fileInput.close();
    }
}
