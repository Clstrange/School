public class CountAll implements Visitor{

    int count = 0;

    @Override
    public void visit(DirFile dirFile) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unimplemented method 'visit'");
    }

    @Override
    public void visit(Folder folder) {
        int temp = 0;
        for (Component component : folder.directory) {
            if (component.getName().charAt(component.getName().length()-1) == ':') {
                component.accept(this);
            }  else {
                count++;
            }
        }
    }
    
}
