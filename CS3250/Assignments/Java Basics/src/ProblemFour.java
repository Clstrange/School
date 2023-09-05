import java.util.Random;

public class ProblemFour {
    public static void main(String[] args) {
        char[][] unicodeArray = new char[10][10];

        //noinspection DataFlowIssue
        unicodeArray = GenerateRandomUnicode(unicodeArray);

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10;j++) {
                System.out.print(unicodeArray[i][j] + " ");
            }
            System.out.print("\n");
        }
        System.out.println("\n" + unicodeArray[4][5]);

    }
    public static char[][] GenerateRandomUnicode(char[][] unicodeArray) {

        int seed = 1776;
        Random random = new Random(seed);

        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                unicodeArray[i][j] = generateRandomUnicodeCharacter(random);
            }
        }
        return unicodeArray;
    }

    public static char generateRandomUnicodeCharacter(Random random) {
        int range1 = 0x0020;
        int range2 = 0x007E;
        int range3 = 0x00A0;
        int range4 = 0x00FF;

        int codePoint;
        do {
            int rangeChoice = random.nextInt(2);
            if (rangeChoice == 0) {
                codePoint = random.nextInt(range2 - range1 + 1) + range1;
            } else {
                codePoint = random.nextInt(range4 - range3 + 1) + range3;
            }
        } while (Character.isISOControl(codePoint));

        return (char) codePoint;
    }
}
