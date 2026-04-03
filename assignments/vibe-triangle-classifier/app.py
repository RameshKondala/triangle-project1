import streamlit as st

def classify_triangle(a, b, c):
    """Classify triangle based on side lengths."""
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle (sides must be positive)"
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle (triangle inequality violated)"
    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"

# Streamlit app
st.title("🔺 Triangle Classifier")
st.markdown("Enter three side lengths to classify the triangle")

col1, col2, col3 = st.columns(3)
with col1:
    a = st.number_input("Side A", min_value=0.0, value=3.0, step=0.1)
with col2:
    b = st.number_input("Side B", min_value=0.0, value=4.0, step=0.1)
with col3:
    c = st.number_input("Side C", min_value=0.0, value=5.0, step=0.1)

if st.button("Classify Triangle"):
    result = classify_triangle(a, b, c)
    st.success(f"**Result:** {result}")
    
    # Show equivalence class info
    st.markdown("### Test Case Analysis")
    if a <= 0 or b <= 0 or c <= 0:
        st.info("🟡 **Equivalence Class:** Invalid - Zero/Negative values")
    elif a + b <= c or a + c <= b or b + c <= a:
        st.info("🟡 **Equivalence Class:** Invalid - Triangle inequality")
    elif a == b == c:
        st.success("🟢 **Equivalence Class:** Valid - Equilateral")
    elif a == b or a == c or b == c:
        st.success("🟢 **Equivalence Class:** Valid - Isosceles")
    else:
        st.success("🟢 **Equivalence Class:** Valid - Scalene")
    
    # Boundary analysis
    st.markdown("### Boundary Analysis")
    if a == 0 or b == 0 or c == 0:
        st.warning("🔴 **Boundary:** Zero value (invalid)")
    elif abs(a - b) < 0.1 or abs(a - c) < 0.1 or abs(b - c) < 0.1:
        st.info("🔵 **Boundary:** Sides nearly equal")

# Test case examples
st.markdown("### Sample Test Cases")
st.markdown("""
| Case | A | B | C | Expected | Type |
|------|---|---|---|----------|------|
| Sunny Day | 3 | 4 | 5 | Scalene | Valid |
| Sunny Day | 5 | 5 | 5 | Equilateral | Valid |
| Rainy Day | 1 | 2 | 10 | Invalid | Invalid |
| Rainy Day | 0 | 4 | 5 | Invalid | Invalid |
| Boundary | 1 | 1 | 1 | Equilateral | Valid |
| Boundary | 2 | 2 | 4 | Invalid | Invalid |
""")
