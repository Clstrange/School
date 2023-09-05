package stateassignment;

public class Remote {
    public void press(State command) {
        command.push();
    }
}
