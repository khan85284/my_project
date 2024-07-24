# My Project

A sample project for web scraping with logging.

## Setup

### Prerequisites

- [Poetry](https://python-poetry.org/)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your_username/my_project.git
    cd my_project
    ```

2. Install dependencies:
    ```bash
    poetry install
    ```

3. Create and configure the `.env` file:
    ```bash
    cp .env.example .env
    # Edit the .env file to set the required environment variables
    ```

4. Install pre-commit hooks:
    ```bash
    poetry run pre-commit install
    ```

### Usage

To start the project:
```bash
poetry run python -m my_project.main
