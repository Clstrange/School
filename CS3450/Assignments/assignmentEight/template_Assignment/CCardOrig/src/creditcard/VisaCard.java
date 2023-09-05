/*
 * validate visa card
 * 
 */
package creditcard;

public class VisaCard extends Card{ 
  public VisaCard(Customer customer) {
    super(customer);
  }
  public boolean isNumOfDigitsValid() { 
    if ((cardNum.length() == 13) || 
        (cardNum.length() == 16)) { 
      return true; 
    } else { 
      return false; 
    } 
  } 
  public boolean isValidPrefix() { 
    String prefix = cardNum.substring(0, 1); 
    if (prefix.equals("4")) { 
      return true; 
    } else { 
      return false; 
    } 
  } 

}