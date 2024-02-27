from pydantic import BaseModel, Field


class Todo(BaseModel):
    user_id: int = Field(alias="userId")
    id: int
    title: str
    completed: bool
    estimate: str = Field(alias="estimat")

    def __str__(self) -> str:
        return f"Id: {self.id}, User Id: {self.user_id}, Title: {self.title}, Completed: {self.completed}, Estimate: {self.estimate}"
