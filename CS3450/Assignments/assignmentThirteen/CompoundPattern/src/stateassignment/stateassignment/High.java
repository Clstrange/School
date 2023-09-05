package stateassignment;

public class High implements State {

    Fan fan;
    public High(Fan fan) {
        this.fan = fan;

    }

    @Override
    public void push() {
        System.out.println("high speed");
        this.fan.setState(fan.getOffState());
    }
    
}
