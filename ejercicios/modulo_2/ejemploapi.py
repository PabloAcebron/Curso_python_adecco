from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import Integer, String,create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped , mapped_column , sessionmaker


engine = create_engine("sqlite:///ecommerce.db")

SessionLocal = sessionmaker(bind=engine, autoflush=True)

# Crear clase

class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = "products"
    
    id : Mapped[int] = mapped_column(Integer, primary_key= True, autoincrement= True)
    nombre : Mapped[str] = mapped_column(String(100),nullable=False)

class ProductDTO(BaseModel):
    nombre: str | None = None
    


Base.metadata.create_all(engine)

app = FastAPI(title="Products App", version="1.0.0")

@app.get("/")
def home():
    return {"mensaje":"Products API"}



# API REST:
# GET all products JSON

@app.get("/api/products")
def find_all():
    session = SessionLocal()
    products = session.query(Product).all()
    session.close()
    return products

# GET one products
@app.get("/api/products/{id}")
def find_by_id(id: int):
    session = SessionLocal()
    product = session.query(Product).filter(Product.id == id).first()
    session.close()
    if not product:
        raise HTTPException(status_code = 404, detail= "Product Not found")
    return product

# POST create products

@app.post("/api/products")
def create(product_dto: ProductDTO):
    session = SessionLocal()
    product = Product(nombre=product_dto.nombre)
    session.add(product)
    session.commit()
    session.refresh(product)
    session.close
    return product
# PUT update products

@app.put("/api/products/{id}")
def update(id: int, product_dto : ProductDTO):
    session = SessionLocal()
    product = session.execute(
        select(Product).where(Product.id == id)
    ).scalar_one_or_none()
    
    if not product:
        raise HTTPException(status_code=404, detail="Not found")

    if product_dto.nombre is not None:
        product.nombre = product_dto.nombre

    session.commit()
    session.refresh(product)
    session.close()
    return product
# DELETE remove products

@app.delete("/api/products/{id}")
def delete_by_id(id: int):
    session = SessionLocal()
    product = session.execute(
        select(Product).where(Product.id == id)
    ).scalar_one_or_none()
    if not product:
        raise HTTPException(status_code=404, detail="Not found")
    
    session.delete(product)
    session.commit()
    session.close()
    
    session.delete()
    return product