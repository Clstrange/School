public class Add implements Command {
    Database database = null;
    String key = null;
    String value = null;

    public Add(Database database, String key, String value){
        this.database = database;
        this.key = key;
        this.value = value;
    }

    @Override
    public void execute() {
        this.database.add(this.key, this.value);
    }

    @Override
    public void undo() {
        this.database.remove(this.key);
    }
    
}
