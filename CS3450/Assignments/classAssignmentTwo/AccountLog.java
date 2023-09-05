/*
 * Account transaction logging class
 * 
 */
package AccntLog;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

/**
 * Write financial transactions to log file
*/
public class AccountLog {
	
    
	private final String logFile = "financial_log.txt";
	private PrintWriter writer;
	
	private AccountLog() {
            try {
                    FileWriter fw = new FileWriter(logFile);
                    writer = new PrintWriter(fw, true);
		} catch (IOException e) {}
	}

	public void logWithdraw (String account, double amount) {
		writer.println("WITHDRAW (" + account + "): " + amount + "$");
	}
	
	public void logDeposit (String account, double amount) {
		writer.println("DEPOSIT (" + account + "): " + amount + "$");
	}
	
	public void logTransfer (String fromAccount, String toAccount, double amount) {
		writer.println("TRANSFER (" + fromAccount + "->" + toAccount + "): " + amount + "$");
	}

}
