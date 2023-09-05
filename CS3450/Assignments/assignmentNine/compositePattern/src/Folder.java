import java.util.ArrayList;

public class Folder extends Component {
    ArrayList<Component> directoryTree;
    Component parentDirectory;

    public Folder(String name, Component parent) {
        super(name);
        this.directoryTree = new ArrayList<Component>();
        this.parentDirectory = parent;

    }

    public void list(){
        for (int i = 0; i < this.directoryTree.size(); i++) {
            System.out.print(this.directoryTree.get(i).getName());
        }
        System.out.println();
    }

    public void listall() {
        for (int i = 0; i < this.directoryTree.size(); i++){
            System.out.println(this.directoryTree.get(i).getName());
            if (this.directoryTree.get(i).getName().charAt(this.directoryTree.get(i).getName().length()-1) == ':') {
                this.directoryTree.get(i).listall();
            }
        }
    }

    public Component chdir(String changeName) {

        for (int i = 0; i < directoryTree.size(); i++) {
            String temp = this.directoryTree.get(i).getName();
            temp = temp.trim();
            if (changeName.equals(temp)) {
                return this.directoryTree.get(i);
            }
        }

        System.out.println("ERROR-2 chdir");
        return new DirFile("ERROR-2");
    }

    public Component up() {
        return this.parentDirectory;

    }
    
    public void count() {
        int temp = 0;
        for (int i = 0; i < this.directoryTree.size(); i++) {
            if (this.directoryTree.get(i).getName().charAt(this.directoryTree.get(i).getName().length()-1) == ':') {
            }  else {
                temp++;
            }
        }
        System.out.println(temp);
    }
    
    public int countall() {
        int temp = 0;
        for (int i = 0; i < this.directoryTree.size(); i++) {
            if (this.directoryTree.get(i).getName().charAt(this.directoryTree.get(i).getName().length()-1) == ':') {
                temp += this.directoryTree.get(i).countall();
            }  else {
                temp++;
            }
        }
        return temp;
    }

    public void load(Component data){
        directoryTree.add(data); 
    }
    
    public Component getRecDir() {
        return directoryTree.get(directoryTree.size()-1);
    }
    
}
