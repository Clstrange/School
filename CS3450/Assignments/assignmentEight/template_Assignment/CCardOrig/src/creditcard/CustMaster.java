/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package creditcard;

/**
 *
 * @author lthac
 */
public class CustMaster extends Customer {
    String number = "5555555555554444";
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