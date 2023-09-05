import java.util.HashMap;
import java.util.Map;
public class DatabaseReciever extends Database {
    Map<String, String> database = new HashMap<String, String>();
    final String id;

    public DatabaseReciever(String id) {
        super(id);
        this.id = id;
    }

    public String getId() {
        return this.id;
    }

    public void add(String key, String value) {
        this.database.put(key, value);
    }

    public String get(String key) {
        return this.database.get(key);
    }
  
    public void update(String key, String value) {
        this.database.put(key, value);
    }

    public void remove(String key) {
        this.database.remove(key);
    }
    
    public void display() {
        for (Map.Entry<String,String> entry : database.entrySet()) {
            System.out.println("Key = " + entry.getKey() +
            ", Value = " + entry.getValue());
        }
    }
}
