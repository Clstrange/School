import java.io.*;

class StreamOutput implements Output {
    private Writer sink;
    public StreamOutput(Writer stream) {
        sink = stream;
    }

    public void write(Object o) {
        try {
            sink.write(o.toString());
        }
        catch (IOException ex) {
            throw new RuntimeException(ex);
        }
    }
}