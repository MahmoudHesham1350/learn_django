# learn_django

This is my first project learning the Django framework. This project consists of 3 apps:

## 1. Hello

- **URL:** `http://127.0.0.1:8000/hello/`
  - **Description:** Prints out "Hello, World!"

- **URL:** `http://127.0.0.1:8000/hello/mahmoud`
  - **Description:** Prints out "Hello, Mahmoud!"

- **URL:** `http://127.0.0.1:8000/hello/hazem`
  - **Description:** Prints out "Hello, Hazem!"

- **URL:** `http://127.0.0.1:8000/hello/<name>`
  - **Description:** Prints out "Hello, Name!"

## 2. NewYear

- **URL:** `http://127.0.0.1:8000/newyear/`
  - **Description:** Checks if it is New Year's Day and prints "YES" or "NO".

## 3. Tasks

- **URL:** `http://127.0.0.1:8000/tasks/`
  - **Description:** Default page that shows the tasks you have added and provides a link to add tasks.

- **URL:** `http://127.0.0.1:8000/tasks/add`
  - **Description:** You can add tasks to the default page and get a link back to the default page.
