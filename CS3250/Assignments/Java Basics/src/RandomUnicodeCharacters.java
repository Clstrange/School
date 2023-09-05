import java.util.Random;

public class RandomUnicodeCharacters {
    public static void main(String[] args) {
        int seed = 1776;
        Random random = new Random(seed);

        // Generate and print random Unicode characters from the specified ranges
        for (int i = 0; i < 10; i++) {
            char randomChar = generateRandomUnicodeCharacter(random);
            System.out.print(randomChar);
        }
    }

    public static char generateRandomUnicodeCharacter(Random random) {
        // Ranges: U+0020 to U+007E and U+00A0 to U+00FF
        int range1 = 0x0020;
        int range2 = 0x007E;
        int range3 = 0x00A0;
        int range4 = 0x00FF;

        int codePoint;
        do {
            // Choose one of the specified ranges randomly
            int rangeChoice = random.nextInt(2);
            if (rangeChoice == 0) {
                codePoint = random.nextInt(range2 - range1 + 1) + range1;
            } else {
                codePoint = random.nextInt(range4 - range3 + 1) + range3;
            }
        } while (Character.isISOControl(codePoint)); // Exclude control characters

        return (char) codePoint;
    }
}
