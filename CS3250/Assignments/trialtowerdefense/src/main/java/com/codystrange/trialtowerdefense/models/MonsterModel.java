package com.codystrange.trialtowerdefense.models;

public class MonsterModel {
    private double health;
    private double x, y; // position of monster
    private double speed;

    public MonsterModel(double health, double speed) {
        this.health = health;
        this.speed = speed;

    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }


}
