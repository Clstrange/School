package proxyassignment;

import java.util.HashMap;
import java.util.Map;

public class CacheDB implements IDatabase{
    Map<String, String> cache = new HashMap<String, String>();
    IDatabase database;
    public CacheDB(IDatabase database) {
        this.database = database;

    }
    @Override
    public String getId() {
        return this.database.getId();
    }

    @Override
    public Boolean exists(String key) {
        if (cache.containsKey(key)) {
            return (true);
        }
        else {
            return this.database.exists(key);
        }
    }

    @Override
    public String get(String key) {
        if (cache.containsKey(key)) {
            return (cache.get(key));
        }
        else {
            cache.put(key, this.database.get(key));
            return (cache.get(key));
        }
    }
    
}
