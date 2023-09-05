import java.util.ArrayList;

public class Macro implements Command {
    ArrayList<Command> instructionQueue = new ArrayList<Command>();

    @Override
    public void execute() {
        for (int i = 0; i < this.instructionQueue.size(); i++) {
            this.instructionQueue.get(i).execute();
            this.instructionQueue.remove(i);
        }
    }

    @Override
    public void undo() {
        for (int i = 0; i < this.instructionQueue.size(); i++) {
            this.instructionQueue.get(i).undo();
        }
    }

    public void add(Command instruction) {
        this.instructionQueue.add(instruction);
    }
    
}
