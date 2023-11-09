package com.codystrange.trialtowerdefense.controllers;
import javafx.fxml.FXML;
import javafx.scene.control.Label;

public class MenuController {

    public MenuController() {

    }
    @FXML
    private Label welcomeText;

    @FXML
    protected void onPlayButtonClick() {
        System.out.println("test");
    }
}