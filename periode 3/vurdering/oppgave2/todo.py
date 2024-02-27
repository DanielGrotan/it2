from pydantic import BaseModel, Field, field_validator


class Todo(BaseModel):
    user_id: int = Field(alias="userId")
    id: int
    title: str = Field()
    completed: bool
    estimate: int = Field(alias="estimat", default=1)

    @field_validator("title", mode="before")
    @classmethod
    def remove_extra_spaces(cls, raw_title: str) -> str:
        all_words = raw_title.split(" ")
        all_words = [word for word in all_words if word != ""]

        return " ".join(all_words)

    @field_validator("estimate", mode="before")
    @classmethod
    def set_default_value(cls, raw_estimate: str) -> int:
        return int(raw_estimate.split("d")[0]) if raw_estimate != "" else 1

    def __str__(self) -> str:
        return f"Id: {self.id}, User Id: {self.user_id}, Title: {self.title}, Completed: {self.completed}, Estimate: {self.estimate}"
