import java.util.Scanner;

public class GPSArea {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter Name of First City: ");
        String cityOneName = input.nextLine();

        System.out.print("Enter Name of Second City: ");
        String cityTwoName = input.nextLine();

        System.out.print("Enter Name of Third City: ");
        String cityThreeName = input.nextLine();

        System.out.print("Enter Longitude of the First City: ");
        double cityOneLongitude = Double.parseDouble(input.nextLine());

        System.out.print("Enter Latitude of the First City: ");
        double cityOneLatitude = Double.parseDouble(input.nextLine());

        System.out.print("Enter Longitude of the Second City: ");
        double cityTwoLongitude = Double.parseDouble(input.nextLine());

        System.out.print("Enter Latitude of the Second City: ");
        double cityTwoLatitude = Double.parseDouble(input.nextLine());

        System.out.print("Enter Longitude of the Third City: ");
        double cityThreeLongitude = Double.parseDouble(input.nextLine());

        System.out.print("Enter Latitude of the Third City: ");
        double cityThreeLatitude = Double.parseDouble(input.nextLine());

        double distanceBetweenOneTwo = CalculateDistance(cityOneLongitude,cityOneLatitude,cityTwoLongitude,cityTwoLatitude);
        double distanceBetweenTwoThree = CalculateDistance(cityTwoLongitude, cityTwoLatitude, cityThreeLongitude, cityThreeLatitude);
        double distanceBetweenOneThree = CalculateDistance(cityOneLongitude,cityOneLatitude,cityThreeLongitude,cityThreeLatitude);

        double areaBetweenCities = CalculateArea(distanceBetweenOneTwo,distanceBetweenTwoThree,distanceBetweenOneThree);

        System.out.println("Area between the three cities is: " + Math.round(areaBetweenCities * 10.0)/10.0);

    }

    public static double CalculateDistance(double LongitudeOne, double LatitudeOne, double LongitudeTwo, double LatitudeTwo) {
        double deltaLat = Math.toRadians(LatitudeTwo - LatitudeOne);
        double deltaLon = Math.toRadians(LongitudeTwo - LongitudeOne);

        double a = Math.sin(deltaLat / 2) * Math.sin(deltaLat / 2) +
                Math.cos(Math.toRadians(LatitudeOne)) * Math.cos(Math.toRadians(LatitudeTwo)) *
                        Math.sin(deltaLon / 2) * Math.sin(deltaLon / 2);

        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

        return 6371 * c;
    }

    public static double CalculateArea(double sideOne, double sideTwo, double sideThree) {
        double s = (sideOne + sideTwo + sideThree) / 2;
        return Math.sqrt(s * (s - sideOne) * (s - sideTwo) * (s - sideThree));
    }
}
