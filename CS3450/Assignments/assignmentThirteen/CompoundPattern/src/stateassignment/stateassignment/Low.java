package stateassignment;

public class Low implements State {

    Fan fan;
    public Low(Fan fan) {
        this.fan = fan;
    }

    @Override
    public void push() {
        System.out.println("low speed");
        this.fan.setState(fan.getMediumState());
    }
    
}
