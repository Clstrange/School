public class DirFile implements Component{
    String name;
    public DirFile(String name) {
        this.name = name;
    }
    @Override
    public void accept(Visitor visitor){
        visitor.visit(this);
    }
    @Override
    public String getName() {
        return name;
    }
    @Override
    public void load(Component data) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unsupported method for files");
    }
    @Override
    public Component getRecDir() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unsupported method for files");
    }
    @Override
    public Component chdir(String changeName) {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unsupported method for files");
    }
    @Override
    public Component up() {
        // TODO Auto-generated method stub
        throw new UnsupportedOperationException("Unsupported method for files");
    }
}
