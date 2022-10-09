package org.example;

public class Customer {
    public void order(String menuname, Menu menu, Cooking cooking){
        MenuItem menuItem = menu.choose(menuname);
        Cook cook = cooking.makeCook(menuItem);
    }
}
