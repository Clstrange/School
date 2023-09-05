public class List implements Visitor{
    @Override
    public void visit(DirFile dirFile) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Command not supported for files");
    }

    @Override
    public void visit(Folder folder) {
        for (Component component : folder.directory) {
            System.out.print(component.getName());
        }
        System.out.println();
    }

    
}
