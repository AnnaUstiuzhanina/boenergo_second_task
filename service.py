from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def start():
    return {"message": "Введите номер предмета (от 1 до 100 включительно) после знака / в адресной строке."}

@app.get("/{item}")
def color(item: int):
    if item in range(1, 101):
        return {"message": "Вероятно, этот предмет синий."}
    else:
        return {"message": "Несуществующий номер предмета. Попробуйте еще раз."}