package com.codystrange.trialtowerdefense.controllers;
import com.codystrange.trialtowerdefense.Main;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.Label;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.layout.AnchorPane;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;

import java.io.IOException;

public class MenuController {

    public MenuController() {

    }
    @FXML
    private Label welcomeText;

    @FXML
    protected void onPlayButtonClick(javafx.event.ActionEvent event) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("/com/codystrange/trialtowerdefense/views/LevelOne.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 1055, 645);
        Stage stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
        stage.setScene(scene);

    }


}