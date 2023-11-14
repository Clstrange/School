package com.codystrange.trialtowerdefense.controllers;
import javafx.animation.PathTransition;
import javafx.fxml.FXML;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.AnchorPane;
import javafx.scene.shape.Path;
import javafx.util.Duration;

public class LevelOneController {
    @FXML
    private Path path;

    @FXML
    private AnchorPane level;

    ImageView monsterView = new ImageView(new Image("com/codystrange/trialtowerdefense/assests/2d-monster-sprites/PNG/1/1_enemies_1_idle_000.png"));

    public LevelOneController() {

    }

    @FXML
    private void initialize() {
        System.out.println("test");
        if(level == null) {
            System.out.println("level is null");
        } else {
            level.getChildren().add(monsterView);
        }
        if (path == null) {
            System.out.println("path is null");
        }

        PathTransition transition = new PathTransition();
        transition.setNode(monsterView);
        transition.setPath(path);
        transition.setDuration(Duration.seconds(10));
        transition.setOrientation((PathTransition.OrientationType.NONE));
        transition.setCycleCount(1);
        transition.setAutoReverse(false);
        transition.play();


    }

}
