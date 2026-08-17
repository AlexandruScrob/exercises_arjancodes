from decimal import Decimal

from nicegui import ui

orders: list[dict[str, str | float]] = []


def add_order() -> None:
    customer = customer_input.value.strip()
    amount_text = amount_input.value.strip()

    if not customer:
        ui.notify("Customer name is required.", type="negative")
        return

    try:
        amount = Decimal(amount_text)
    except Exception:
        ui.notify("Amount must be a valid number.", type="negative")
        return

    if amount <= 0:
        ui.notify("Amount must be greater than zero.", type="negative")
        return

    orders.append(
        {
            "customer": customer,
            "amount": float(amount),
        }
    )

    customer_input.value = ""
    amount_input.value = ""

    update_dashboard()
    ui.notify("Order added.", type="positive")


def update_dashboard() -> None:
    table.rows = orders
    total_label.text = f"Total revenue: €{sum(order['amount'] for order in orders):.2f}"

    chart.options["series"] = [
        {
            "name": "Revenue",
            "data": [order["amount"] for order in orders],
        }
    ]

    chart.options["xAxis"] = {
        "type": "category",
        "data": [order["customer"] for order in orders],
    }

    chart.update()


ui.label("Order Dashboard").classes("text-2xl font-bold")

with ui.card().classes("w-full max-w-xl"):
    ui.label("Add order").classes("text-lg font-semibold")

    customer_input = ui.input("Customer").classes("w-full")
    amount_input = ui.input("Amount").classes("w-full")

    ui.button("Add order", on_click=add_order)

total_label = ui.label("Total revenue: €0.00").classes("text-xl mt-4")

table = ui.table(
    columns=[
        {"name": "customer", "label": "Customer", "field": "customer"},
        {"name": "amount", "label": "Amount", "field": "amount"},
    ],
    rows=orders,
    row_key="customer",
).classes("w-full max-w-xl")

chart = ui.echart(
    {
        "tooltip": {},
        "xAxis": {
            "type": "category",
            "data": [],
        },
        "yAxis": {
            "type": "value",
        },
        "series": [
            {
                "name": "Revenue",
                "type": "bar",
                "data": [],
            }
        ],
    }
).classes("w-full max-w-xl h-64")

ui.run()
