import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TriangleTest {

    @Test
    void validScaleneTriangle345() {
        Triangle t = new Triangle(3, 4, 5);
        assertTrue(t.isValid());
        assertEquals(TriangleType.SCALENE, t.getType());
    }

    @Test
    void equilateralTriangle555() {
        Triangle t = new Triangle(5, 5, 5);
        assertTrue(t.isValid());
        assertEquals(TriangleType.EQUILATERAL, t.getType());
    }

    @Test
    void isoscelesTriangleDifferentOrders() {
        Triangle t1 = new Triangle(5, 5, 3);
        Triangle t2 = new Triangle(5, 3, 5);
        Triangle t3 = new Triangle(3, 5, 5);

        assertEquals(TriangleType.ISOSCELES, t1.getType());
        assertEquals(TriangleType.ISOSCELES, t2.getType());
        assertEquals(TriangleType.ISOSCELES, t3.getType());
    }

    @Test
    void zeroLengthSideIsInvalid() {
        Triangle t = new Triangle(0, 4, 5);
        assertFalse(t.isValid());
        assertEquals(TriangleType.INVALID, t.getType());
    }

    @Test
    void triangleInequalityViolationIsInvalid() {
        Triangle t = new Triangle(1, 2, 10);
        assertFalse(t.isValid());
        assertEquals(TriangleType.INVALID, t.getType());
    }
}
