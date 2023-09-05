public class Buy implements Command {
    Reciever reciever = null;
    public Buy(Reciever reciever){
        this.reciever = reciever;
    }
    @Override
    public void execute() {
        this.reciever.buy();
    }
    
}
