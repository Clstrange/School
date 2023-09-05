public class LineOutput extends OutputDecorator {
    Output output;
    public LineOutput(Output output) {
        this.output = output;
    }

    @Override
    public void write(Object o) {
        output.write(o);
        output.write('\n');
        
    }
    
}
