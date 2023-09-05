public class Find implements Visitor{
    String name;
    public Find(String name) {
        this.name = name;
    }

    @Override
    public void visit(DirFile dirFile) {
        if (dirFile.getName().equals(this.name)) {
            System.out.println("Found leaf");
        }
    }

    @Override
    public void visit(Folder folder) {
        for (Component component : folder.directory){
            if (component.getName().equals(this.name)) {
                if (component.getName().charAt(component.getName().length()-1) == ':') {
                    System.out.println("Found directory");
                    component.accept(new ListAll());
                }
            }
            component.accept(this);
        }
    }
}
