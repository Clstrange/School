public class LowResFactory implements ResFactory {

    @Override
    public void PrintDocument() {
        LowResDocument document = new LowResDocument();
        document.PrintDocument();
    }

    @Override
    public void DrawWidget() {
        LowResWidget widget = new LowResWidget();
        widget.DrawWidget();
    }
    
}
