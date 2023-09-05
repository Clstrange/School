import java.io.BufferedReader;
import java.io.FileReader;

public class Client {
    public static void main(String[] args) throws Exception {
        // // Setting up databases
        Invoker invoker = new Invoker();
        Database databaseOne = new DatabaseReciever("one");
        Database databaseTwo = new DatabaseReciever("two");
        
        // // Creating commands
        // Command addTwo = new Add(databaseOne, "key2", "value2");
        // Command addThree = new Add(databaseOne, "key3", "value3");
        // /// Loading and running commands
        // invoker.loadInstruction(addOne);
        // invoker.loadInstruction(addTwo);
        // invoker.loadInstruction(addThree);



        try (BufferedReader br = new BufferedReader(new FileReader("SampleFile.txt"))) {
            Boolean macroRunning = false;
            Macro macro = null;
            String line = br.readLine();
            String[] commands;
            while (line != null) {
                commands = line.split(" ");
                switch (commands[0]) {
                    case "A":
                        if (commands[1] == "one") {
                            if (macroRunning) {
                                macro.add(new Add(databaseOne,commands[2],commands[3]));
                            }
                            else {
                                invoker.loadInstruction(new Add(databaseOne,commands[2],commands[3]));
                            }
                        }
                        else if (commands[1] == "two") {
                            if (macroRunning) {
                                macro.add(new Add(databaseTwo,commands[2],commands[3]));
                            }
                            else {

                                invoker.loadInstruction(new Add(databaseTwo,commands[2],commands[3]));                            }
                            }
                        break;
                    case "B":
                        macroRunning = true;
                        macro = new Macro();
                        break;
                    case "E":
                        macroRunning = false;
                        invoker.loadInstruction(macro);
                        break;
                    case "R":
                        if (commands[1] == "one") {
                            if (macroRunning) {
                                macro.add(new Remove(databaseOne,commands[2]));
                            }
                            else {
                                invoker.loadInstruction(new Remove(databaseOne,commands[2]));
                            }
                        }
                        else if (commands[1] == "two") {
                            if (macroRunning) {
                                macro.add(new Remove(databaseTwo,commands[2]));
                            }
                            else {

                                invoker.loadInstruction(new Remove(databaseTwo,commands[2]));                            }
                            }
                            break;
                    case "U":
                        invoker.undoInstruction();
                        break;

                }
                line = br.readLine();

            }
        }

        invoker.runInstruction();
        databaseOne.display();
        
    }
}
