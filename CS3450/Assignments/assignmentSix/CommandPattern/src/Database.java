import java.util.HashMap;
import java.util.Map;
public abstract class Database {
    Map<String, String> database = new HashMap<String, String>();
    final String id;

    public Database(String id){
        this.id = id;    
    }

    public abstract String getId();

    public abstract void add(String key, String value);
    public abstract String get(String key);
  
    public abstract void update(String key, String value);
    public abstract void remove(String key);
    public abstract void display();
}
