  /*
 * Validate Master card number
 */
package creditcard;

public class MasterCard extends Card{ 
  
  public MasterCard(Customer customer) {
    super(customer);
  }
  public boolean isNumOfDigitsValid() { 
    if (cardNum.length() == 16) { 
      return true; 
    } else { 
      return false; 
    } 
  } 
  public boolean isValidPrefix() { 
    String prefix = cardNum.substring(0, 1); 
    String nextChar = cardNum.substring(1, 2); 
    String validChars = "12345";
    //51-55 
    if ((prefix.equals("5")) &&
        (validChars.indexOf(nextChar) >= 0)) { 
      return true; 
    } else { 
      return false; 
    } 
  } 

}