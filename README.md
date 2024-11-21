# Days Since Calc

A very simple app that calculates days since specified date: can be used as a cli app, or to serve a json response.

### How to install:

- Clone
- cd into cloned directory
- Install dependencies:
  - With UV:
    `uv sync`
  - With pip:
    `pip install -r requirements.txt`
- Run:

  - As CLI app:

    - With UV:

      - `uv run daysSince.py --date=[DATE]`
      - (replace [DATE] with YYYY-MM-DD formatted date)

    - With python3:

      - `python3 daysSince.py --date=[DATE]`

      - (replace [DATE] with YYYY-MM-DD formatted date)

  - As server:

    - With UV:

      - `uv run daysSince.py --serve=[PORT]`

      - (replace [PORT] with desired port number, example: 8080)

    - With python3:

      - `python3 daysSince.py --serve=[PORT]`

      - (replace [PORT] with desired port number,
        example: 8080)

    - Json response can the be requested through:
      `localhost:[PORT]/days_since/[DATE]` in the browser, curl, etc.

    - Json response structure is as follows:

      ```json
      {
        "days": "3",
        "color": "black"
      }
      ```
