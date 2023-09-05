import java.util.ArrayList;
public class LocalStocks implements Subject{
    private ArrayList<Observer>  observerList = new ArrayList<Observer>();
    private String currentData;


    @Override
    public void registerObserver(Observer observer) {
        observerList.add(observer);
        
    }

    @Override
    public void removeObserver(Observer observer) {
        observerList.remove(observer);
        
    }

    @Override
    public void notifyObserver() {
        for(int i = 0; i < observerList.size(); i++) {
            observerList.get(i).update();
        }
        
    }

    public void newData(String newStocks) {
        currentData = newStocks;
        notifyObserver();
    }

    public String getCurrentData() {
        return currentData;
    }
    
    
}
