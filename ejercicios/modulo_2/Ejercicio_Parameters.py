from fastapi import FastAPI

app = FastAPI()

# Escribe aquí tu endpoint

@app.get("/users/{user_id}")
def get_users(user_id:int,include_email:bool = False,format = "basic"):
    user_data = {
        "user id": user_id,
        "name ": f"Usuario : {user_id}",
        "format" : f"{format}"
    }
    
    if include_email:
        user_data["Email"] = f"user{user_id}@example.com"

    return user_data