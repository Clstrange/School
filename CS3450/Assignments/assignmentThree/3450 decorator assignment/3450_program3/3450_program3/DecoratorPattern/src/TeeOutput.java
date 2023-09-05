import java.io.IOException;
import java.io.Writer;

public class TeeOutput extends OutputDecorator {
    Output output;
    private Writer sink;
    public TeeOutput(Output output, Writer file) {
        this.output = output;
        this.sink = file;
    }

    @Override
    public void write(Object o) {
        try {
            sink.write(o.toString());
            output.write(o);
        }
        catch (IOException ex) {
            throw new RuntimeException(ex);
        }
        
    }
    
}
