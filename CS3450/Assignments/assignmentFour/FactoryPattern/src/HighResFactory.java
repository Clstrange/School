public class HighResFactory implements ResFactory {

    @Override
    public void PrintDocument() {
        HighResDocument document = new HighResDocument();
        document.PrintDocument();
    }

    @Override
    public void DrawWidget() {
        HighResWidget widget = new HighResWidget();
        widget.DrawWidget();
    }
    
}
