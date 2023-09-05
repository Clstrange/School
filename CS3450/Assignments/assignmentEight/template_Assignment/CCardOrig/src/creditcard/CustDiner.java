/*
 * this is a class that simulated customer information
 */
package creditcard;

/**
 *
 * @author lthac
 */
public class CustDiner extends Customer {
    String number = "38520000023237";
    int month = 11;
    int year = 2023;
    @Override
    public String getNumber() {
        return number;
    }
    @Override
    public int getMonth() {
        return month;
    }
    @Override
    public int getYear() {
        return year;
    }
    
}
