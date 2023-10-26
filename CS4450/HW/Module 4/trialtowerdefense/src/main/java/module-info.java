module com.codystrange.trialtowerdefense {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;

    opens com.codystrange.trialtowerdefense to javafx.fxml;
    exports com.codystrange.trialtowerdefense;
}