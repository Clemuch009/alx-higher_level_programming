from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    id: int
    name: str = 'jane Doe'

    model_config = ConfigDict(str_max_length=10)

user = User(id='123')
assert user.model_dump() == {'id': 123, 'name': 'jane Doe'}
print(user.model_dump())
print(b"hello")
