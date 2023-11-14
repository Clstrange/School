package com.codystrange.trialtowerdefense;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;
import java.io.IOException;

public class Main extends Application {
    @Override
    public void start(Stage stage) {
        try {
            FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("/com/codystrange/trialtowerdefense/views/Game.fxml"));

            Scene scene = new Scene(fxmlLoader.load(), 1055, 645);
            stage.setScene(scene);
            stage.setResizable(false);
            stage.show();
        } catch (IOException e) {
            System.out.println("File not found");
            e.printStackTrace();
        }



    }

    public static void main(String[] args) {
        launch(args);
    }
}
