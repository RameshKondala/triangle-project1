from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Triangle API")

class TriangleInput(BaseModel):
    a: float = Field(..., gt=0)
    b: float = Field(..., gt=0)
    c: float = Field(..., gt=0)

class Triangle(BaseModel):
    id: int
    a: float
    b: float
    c: float
    valid: bool
    type: str

triangles_db: list[Triangle] = []
next_id = 1

def classify_triangle(a: float, b: float, c: float) -> tuple[bool, str]:
    
    if a <= 0 or b <= 0 or c <= 0:
        return False, "INVALID"
    if not (a + b > c and a + c > b and b + c > a):
        return False, "INVALID"
    if a == b == c:
        return True, "EQUILATERAL"
    if a == b or a == c or b == c:
        return True, "ISOSCELES"
    return True, "SCALENE"

@app.get("/triangles", response_model=list[Triangle])
def list_triangles():
    return triangles_db

@app.post("/triangles", response_model=Triangle, status_code=201)
def create_triangle(data: TriangleInput):
    global next_id
    valid, ttype = classify_triangle(data.a, data.b, data.c)
    triangle = Triangle(
        id=next_id,
        a=data.a,
        b=data.b,
        c=data.c,
        valid=valid,
        type=ttype
    )
    triangles_db.append(triangle)
    next_id += 1
    return triangle

@app.get("/triangles/{triangle_id}", response_model=Triangle)
def get_triangle(triangle_id: int):
    for t in triangles_db:
        if t.id == triangle_id:
            return t
    raise HTTPException(status_code=404, detail="Triangle not found")

@app.delete("/triangles/{triangle_id}", status_code=204)
def delete_triangle(triangle_id: int):
    for i, t in enumerate(triangles_db):
        if t.id == triangle_id:
            del triangles_db[i]
            return
    raise HTTPException(status_code=404, detail="Triangle not found")
