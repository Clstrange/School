import java.util.ArrayList;

public class Invoker {
    ArrayList<Command> instructionQueue = new ArrayList<Command>();
    Command undoCommand = null;

    public Invoker() {}
    
    public void loadInstruction(Command instruction) {
        this.instructionQueue.add(instruction);
        undoCommand = instruction;
    }

    public void runInstruction() {
        for (int i = 0; i < this.instructionQueue.size(); i++) {
            this.instructionQueue.get(i).execute();
        }
    }

    public void undoInstruction() {
        undoCommand.undo();
    }


}
