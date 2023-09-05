package stateassignment;

public class Medium implements State {

    Fan fan;
    public Medium(Fan fan) {
        this.fan = fan;

    }

    @Override
    public void push() {
        System.out.println("medium speed");
        this.fan.setState(fan.getHighState());
    }
    
}
