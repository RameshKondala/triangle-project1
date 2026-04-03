public class Triangle {

    private final double a;
    private final double b;
    private final double c;

    public Triangle(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public boolean isValid() {
        if (a <= 0 || b <= 0 || c <= 0) {
            return false;
        }
        return a + b > c && a + c > b && b + c > a;
    }

    public TriangleType getType() {
        if (!isValid()) {
            return TriangleType.INVALID;
        }
        if (a == b && b == c) {
            return TriangleType.EQUILATERAL;
        } else if (a == b || a == c || b == c) {
            return TriangleType.ISOSCELES;
        } else {
            return TriangleType.SCALENE;
        }
    }
}
