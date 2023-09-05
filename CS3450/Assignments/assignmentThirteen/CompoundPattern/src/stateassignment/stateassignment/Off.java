package stateassignment;

public class Off implements State {

    Fan fan;
    public Off(Fan fan) {
        this.fan = fan;

    }

    @Override
    public void push() {
        System.out.println("turning off");
        this.fan.setState(fan.getLowState());
    }
}
