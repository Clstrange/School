import java.util.Random;

public class ProblemThree
{
    public static void main(String[] args) {
        System.out.println(args[0] + " " + args[1]);
        int[] intArray = ReturnUnique(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
        for (int i: intArray) {
            System.out.println(i);
        }
        System.out.println("Average: " + CalculateAverage(intArray));
        System.out.println("Standard Deviation: " + CalculateStandardDeviation(intArray));
    }

    public static int[] ReturnUnique(int n, int r) {
        int [] intArray = new int[n];
        Random random = new Random();
        for (int i = 0; i < n; i++) {
            int randInt = random.nextInt(n+1);
            intArray[i] = randInt;
        }
        return intArray;
    }

    public static int CalculateAverage(int[] intArray) {
        int sum = 0;
        for (int i: intArray) {
            sum += i;
        }
        return sum / intArray.length;

    }

    public static int CalculateStandardDeviation(int[] intArray) {
        int average = CalculateAverage(intArray);

        int sumSquaredDiff = 0;

        for (int i : intArray) {
            int diff = i - average;
            sumSquaredDiff += diff * diff;
        }

        int variance = sumSquaredDiff / intArray.length;
        return (int) Math.sqrt(variance);
    }
}
