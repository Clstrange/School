import java.util.ArrayList;

public class Folder implements Component {
    String name;
    ArrayList<Component> directory;
    Component parentDirectory;
    public Folder(String name, Component parent) {
        this.directory = new ArrayList<Component>();
        this.parentDirectory = parent;
        this.name = name;

    }

    public String getName(){
        return this.name;
    }

    public void load(Component data){
        directory.add(data);
    }

    public Component chdir(String changeName) {

        for (Component component : this.directory) {
            String temp = component.getName();
            temp = temp.trim();
            if (changeName.equals(temp)) {
                return component;
            }
        }

        System.out.println("ERROR-2 chdir");
        return new DirFile("ERROR-2");
    }

    public Component up() {
        return this.parentDirectory;

    }

    public Component getRecDir() {
        return directory.get(directory.size()-1);
    }

    @Override
    public void accept(Visitor visitor){
        visitor.visit(this);
    }
}
