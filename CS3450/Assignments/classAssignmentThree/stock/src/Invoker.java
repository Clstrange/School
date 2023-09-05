public class Invoker {
    public void takeOrder(Command command){
        command.execute();
    }
}
