
public class Remove implements Command {
    Database database = null;
    String key = null;
    String value = null;

    public Remove(Database database, String key){
        this.database = database;
        this.key = key;
    }

    @Override
    public void execute() {
        this.value = this.database.get(this.key); // Needed for the undo button
        this.database.remove(this.key);
    }

    @Override
    public void undo() {
        this.database.add(this.key, this.value);
    }
    
}