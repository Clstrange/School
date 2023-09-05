
public abstract class Component {
    String name;
    public Component(String name){
        this.name = name;
    }
    public void list() {
        System.out.println("ERROR list");
    };
    public void listall() {
        System.out.println("ERROR listall");
    };
    public Component chdir(String changeName) {
        return new DirFile("ERROR");
    };
    public Component up() {
        return new DirFile("ERROR up");
    }
    public void count() {
        System.out.println("ERROR count");
    }
    public int countall() {
        return -1;
    }

    public String getName(){
        return this.name;
    }
    public void load(Component data){
        System.out.println("ERROR load"); 

    }
    public Component getRecDir() {
        System.out.println("ERROR getRecDir");
        return new DirFile("ERROR");
    }


}
