from pydantic import BaseModel, ConfigDict, Field


class Ingredient(BaseModel):
    """Схема ингредиента"""
    name: str = Field(..., description="Название ингредиента")
    model_config = ConfigDict(from_attributes=True)


class RecipeBase(BaseModel):
    """Базовая схема рецепта"""
    name: str = Field(..., min_length=1, description="Название рецепта")
    cook_time: int | None = Field(None, ge=1, description="Время готовки в минутах")


class RecipeSchema(RecipeBase):
    """Схема для списка рецептов (GET /recipes)"""
    views: int = Field(default=0, ge=0, description="Количество просмотров")
    model_config = ConfigDict(from_attributes=True)


class RecipeDetailed(RecipeBase):
    """Схема подробной информации о рецепте (GET /recipes/{id})"""
    description: str | None = Field(None, description="Описание рецепта")
    ingredients: list[Ingredient] = Field(default_factory=list, description="Список ингредиентов")
    model_config = ConfigDict(from_attributes=True)


class RecipeIn(RecipeBase):
    """Схема для создания рецепта (POST /recipes)"""
    description: str | None = Field(None, description="Текстовое описание рецепта")
    ingredients: list[str] = Field(default_factory=list, description="Список ингредиентов")


class RecipeOut(RecipeDetailed):
    """Схема ответа после создания рецепта"""
    id: int = Field(..., description="Уникальный идентификатор рецепта")
    model_config = ConfigDict(from_attributes=True)
