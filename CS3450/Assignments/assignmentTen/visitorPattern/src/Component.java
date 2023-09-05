
public interface Component {
    public void accept(Visitor visitor);
    public String getName();
    public void load(Component data);
    public Component getRecDir();
    public Component chdir(String changeName);
    public Component up();



}
