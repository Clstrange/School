public class Count implements Visitor{

    @Override
    public void visit(DirFile dirFile) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Command not supported for files");
    }

    @Override
    public void visit(Folder folder) {
        int temp = 0;
        for (Component component : folder.directory) {
            if (component.getName().charAt(component.getName().length()-1) == ':') {
            }  else {
                temp++;
            }
        }
        System.out.println(temp);
    }
    
}
