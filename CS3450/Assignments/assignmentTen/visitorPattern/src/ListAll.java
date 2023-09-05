public class ListAll implements Visitor{

    @Override
    public void visit(DirFile dirFile) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Command not supported for files");
    }

    @Override
    public void visit(Folder folder) {
        for (Component component : folder.directory){
            System.out.println(component.getName());
            if (component.getName().charAt(component.getName().length()-1) == ':') {
                component.accept(this);
            }
        }
    }
}
