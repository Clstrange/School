

public class Update implements Command {
    Database database = null;
    String key = null;
    String value = null;
    String previousValue = null;
    public Update(Database database, String key, String value){
        this.database = database;
        this.key = key;
        this.value = value;
    }

    @Override
    public void execute() {
        this.previousValue = this.database.get(this.key);
        this.database.update(this.key, this.value);
    }

    @Override
    public void undo() {
        this.database.update(this.key, this.previousValue);
    }
    
}