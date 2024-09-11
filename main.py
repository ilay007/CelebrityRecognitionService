

from fastapi import FastAPI

from models import Person

app = FastAPI()
persons=[]
nperson=Person(name="Ivan",person_id=1)
print(f"{nperson.name} {nperson.person_id}")




@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/get_person/{person_id}")
def get_person(person_id: int):
    selected_person = [person for person in persons if person.person_id == person_id]
    if selected_person:
        return (selected_person)
    else:
        return ("Person not found")


@app.get("/delete_person/{person_id}")
def delete_person(person_id: int):
    selected_person = [person for person in persons if person.person_id == person_id]
    if selected_person:
        return {"Person is deleted": selected_person}
    else:
        return ("Person not deleted")


@app.post("/add_person")
async def add_person(name:str,person_id:int):
    print(f"{name} {person_id}")
    persons.append(Person(name=name,person_id=person_id))
    return {"person": "Person has been added"}


