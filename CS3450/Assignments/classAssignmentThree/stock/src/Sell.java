public class Sell implements Command{
    Reciever reciever = null;
    public Sell(Reciever reciever){
        this.reciever = reciever;
    }
    @Override
    public void execute() {
        this.reciever.sell();
    }
    
}
