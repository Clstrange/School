public class NumberedOutput extends OutputDecorator {
    Output output;
    static int count = 0;
    public NumberedOutput(Output output) {
        this.output = output;
    }
    @Override
    public void write(Object o) {
        count++;
        output.write(count);
        output.write(":     ");
        output.write(o);
        output.write('\n');
        
    }
    
}
