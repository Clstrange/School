/// assignment
/// L. Thackeray
/// template pattern demo
/// taken from head first into patterns
package Game;

public class GrameDriver {
    public static void main(String[] args) {
 

        
        //Baseball
        BaseBall baseball = new BaseBall();
        baseball.runGame();
        
        //Football
        Football football = new Football();
        football.runGame();
        
        //Lacrosse
        Lacrosse lacrosse = new Lacrosse();
        lacrosse.runGame();
        
        

    } //end main
} //end GameDriver
