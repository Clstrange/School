package proxyassignment;

public interface IDatabase {
    public String getId();
    public Boolean exists(String key);
    public String get(String key);
}
