public class Client {
    public static void main(String[] args) throws Exception {
        Reciever reciever = new Reciever();
        Buy buy = new Buy(reciever);
        Sell sell = new Sell(reciever);
        Invoker invoker = new Invoker();
        invoker.takeOrder(buy);
        invoker.takeOrder(sell);

    }
}
