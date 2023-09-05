/*
 * Origional Banking account logger
 * Driver (test) program:
 *     Simulates Automatic Bank Teller finincal 
 *     logging of Transactions
 * 
 */
package AccntLog;


public class BankTeller {

    /**
     * Simulates auto logging of banking functions
     * @param args the command line arguments
     */
    public static void main(String[] args) {
                AccountLog customer1 = new AccountLog();
		AccountLog customer2 = new AccountLog();
		AccountLog customer3 = new AccountLog();
		
                System.out.print("writing to log...");
		customer1.logDeposit("0001", 80.5);
		customer2.logWithdraw("0002", 100);
		customer1.logTransfer("0001", "0003", 40);
		customer3.logDeposit("0004", 56.74);
		customer2.logWithdraw("0005", 30);
                
                System.out.print("\nBanking session complete\n");
		
		
    }
    
}
