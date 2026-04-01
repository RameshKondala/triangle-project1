import java.util.InputMismatchException;
import java.util.Scanner;

public class TriangleApp {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Triangle Validator and Classifier");

        try {
            System.out.print("Enter side a: ");
            double a = scanner.nextDouble();

            System.out.print("Enter side b: ");
            double b = scanner.nextDouble();

            System.out.print("Enter side c: ");
            double c = scanner.nextDouble();

            Triangle triangle = new Triangle(a, b, c);

            if (!triangle.isValid()) {
                System.out.println("The given sides do NOT form a valid triangle.");
            } else {
                System.out.println("The triangle is valid.");
                System.out.println("Triangle type: " + triangle.getType());
            }
        } catch (InputMismatchException e) {
            System.out.println("Invalid input: please enter numeric values for sides.");
        } finally {
            scanner.close();
        }
    }
}
