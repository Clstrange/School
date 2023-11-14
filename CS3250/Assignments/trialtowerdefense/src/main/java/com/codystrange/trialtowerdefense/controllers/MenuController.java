package com.codystrange.trialtowerdefense.controllers;
import com.codystrange.trialtowerdefense.Main;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.control.Label;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;

public class MenuController {

    public MenuController() {

    }

    @FXML
    protected void onPlayButtonClick(javafx.event.ActionEvent event) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("/com/codystrange/trialtowerdefense/views/LevelOne.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 1055, 645);
        Stage stage = (Stage) ((Node) event.getSource()).getScene().getWindow();
        stage.setScene(scene);

    }


}