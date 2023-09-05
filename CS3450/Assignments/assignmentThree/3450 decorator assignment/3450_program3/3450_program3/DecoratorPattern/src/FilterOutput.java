public class FilterOutput extends OutputDecorator implements Predicate {
    Output output;

    public FilterOutput(Output output) {
        this.output = output;

    }
    @Override
    public void write(Object o) {
        if (execute(o) == true) {
            output.write(o);
        }
        
    }

    @Override
    public boolean execute(Object o) {
        if (((String) o).matches(".*\\d+.*")) {
            return true;
        }
        return false;
    }
    
}
