# OOP Coffee Machine

Simple object-oriented coffee machine simulator used for learning.

## Description
This project implements a basic coffee machine using OOP principles in Python. It shows how `Menu`, `MoneyMachine`, and `CoffeeMaker` (inferred from filenames) interact to process orders, handle resources, and manage payments.

## Files
- `main.py`: Runner script that starts the coffee machine program.
- `menu.py`: Menu-related code (available drinks and options).
- `money_machine.py`: Payment handling and transaction logic.
- `coffee_maker.py`: Water, milk, coffee resource management and drink preparation.

## Requirements
- Python 3.8+

## Setup
1. (Optional) Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies if any (none required by default):

```bash
pip install -r requirements.txt
```

## Usage
Run the program from the project folder:

```bash
python main.py
```

Follow on-screen prompts to select drinks, insert coins, and watch resource updates.

## Extending the Project
- Add new drinks to `menu.py`.
- Improve `money_machine.py` to support different currencies or logging.
- Persist resource state to a file or database.

## Notes
This repository is intended as a learning exercise. Review the source files to understand class responsibilities and interactions.
