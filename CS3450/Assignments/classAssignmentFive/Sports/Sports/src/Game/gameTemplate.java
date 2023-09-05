package Game;

public abstract class gameTemplate {

    protected boolean hasEntertainment;
    public void runGame() {
        initalize();
        startGame();
        intermission();
        
        if (hasEntertainment) {
            addEntertainment();
        }
        else {
            System.out.println("...No entertainment during intermission...");
        }
        endgame();
    }
    
    protected abstract void initalize();

    protected final void startGame() {
            System.out.println("Game is starting.....");
    }
        

    protected abstract void intermission();

    
    protected final void endgame() {
            System.out.println("game is now over - thanks for playing\n");
    }
        
    protected abstract void addEntertainment();

}
