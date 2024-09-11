from pydantic import BaseModel

class Person(BaseModel):
    person_id: int
    name: str

    def __repr__(self):
        return f"Person(name='{self.name}', id={self.person_id})"