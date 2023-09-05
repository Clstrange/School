/*
 * Main fan class which manages the fan states
 */
package stateassignment;

/**
 *
 * @author Dr. Thackeray
 */
class Fan {

    State low;
    State medium;
    State high;
    State off;

    State state;

    public Fan() {
        this.low = new Low(this);
        this.medium = new Medium(this);
        this.high = new High(this);
        this.off = new Off(this);
        this.state = this.low;


    }

    public void setState(State state) {
        this.state = state;

    }

    public void push() {
        state.push();
    }

    public State getLowState() {
        return this.low;
    }

    public State getMediumState() {
        return this.medium;
    }

    public State getHighState() {
        return this.high;
    }

    public State getOffState() {
        return this.off;
    }
}