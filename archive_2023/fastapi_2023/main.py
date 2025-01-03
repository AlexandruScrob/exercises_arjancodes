from enum import Enum

from fastapi import FastAPI, HTTPException, Path, Query, status

from pydantic import BaseModel, Field

# You can give your API a title and add additional metadata such as a description,
# version, title
# The description also supports markdown formatting.
app = FastAPI(
    title="Arjan's Handyman Emporium",
    description="Arjan does not only code but also helps you fix things. :O",
    version="0.1.0",
)


# Docstrings of classes will be reflected in the API documentation in the 'Schema'
class Category(Enum):
    """Category of an item."""

    TOOLS = "tools"
    CONSUMABLES = "consumables"


# You can add metadata to attributes using the Field class.
# This information will also be shown in the auto-generated documentation
class Item(BaseModel):
    """Representation of an item in the system."""

    name: str = Field(description="Name of the item.")
    price: float = Field(description="Price of the item in Euro.")
    count: int = Field(description="Amount of instances of this item in stock.")
    id: int = Field(description="Unique integer that specifies this item.")
    category: Category = Field(description="Category this item belongs to.")


items = {
    0: Item(name="Hammer", price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name="Nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}

# Function parameters that are not path parameters can be specified as query parameters
# Here we can query items like this /items?count=20
Selection = dict[
    str, str | int | float | Category | None
]  # dictionary containing the user's query arguments


# FastAPI handles JSON serialization and deserialization for us.
# We can simple use built-in python and Pydantic types, in this case dict[int, Item]
@app.get("/")
def index() -> dict[str, dict[int, Item]]:
    return {"items": items}


@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with {item_id=} does not exist.",
        )

    return items[item_id]


@app.get("/items")
def query_item_by_parameters(
    name: str | None = None,
    price: float | None = None,
    count: int | None = None,
    category: Category | None = None,
) -> dict[str, Selection | list[Item]]:
    def check_item(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count != count,
                category is None or item.category is category,
            )
        )

    selection = [item for item in items.values() if check_item(item)]
    return {
        "query": {"name": name, "price": price, "count": count, "category": category},
        "selection": selection,
    }


@app.post("/")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Item with {item.id=} already exists.",
        )

    items[item.id] = item
    return {"added": item}


@app.put(
    "/items/{item_id}",
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Item not found"},
        status.HTTP_400_BAD_REQUEST: {"description": "No arguments specified"},
    },
)
# The Query and Path classes also allow us to add documentation to query and path params
def update(
    item_id: int = Path(
        title="Item ID", description="Unique integer that specifies an item.", ge=0
    ),
    name: str
    | None = Query(
        title="Name",
        description="New name of the item.",
        default=None,
        min_length=1,
        max_length=8,
    ),
    price: float
    | None = Query(
        title="Price", description="Price of the item in Euro.", default=None, gt=0.0
    ),
    count: int
    | None = Query(
        title="Count",
        description="Amount of instances of this item in stock.",
        default=None,
        ge=0,
    ),
) -> dict[str, Item]:
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with {item_id=} does not exist.",
        )
    if all(info is None for info in (name, price, count)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            details="No parameters provided for update.",
        )

    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    return {"updated": item}


@app.delete("/items/{item_id}")
def delete_item(item_id: int) -> dict[str, Item]:
    if item_id not in items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with {item_id=} does not exist.",
        )

    item = items.pop(item_id)
    return {"deleted": item}
