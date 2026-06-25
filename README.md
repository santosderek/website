[![santosderek banner](frontend/public/static/images/santosderek.png)](https://santosderek.com)


![Build Passing](https://img.shields.io/github/actions/workflow/status/santosderek/website/tests.yml?branch=master&style=for-the-badge) ![Languages Count](https://img.shields.io/github/languages/count/santosderek/website?style=for-the-badge)
![Total Lines](https://img.shields.io/tokei/lines/github/santosderek/website?style=for-the-badge)

The following repo is the source code to my [personal website](https://santosderek.com) intended to be the main area where people can get to know me and my past experiences, and is able to generate a DOCX of my resume for me.

Feel free to look around the source.

---

> *NOTE: I will not be approving pull requests as everything is subject to change at any moment.*

---

## Technologies

The major key technologies and dependencies for the website are:

- Flask
- React
- React Router
- Vite
- Docker
- DigitalOcean
- AWS Route53
- Requests
- Python-Dotenv
- Python-Docx
- Gunicorn
- PyTest

## Local Development

This project targets Python 3.10, matching the Docker runtime.

```bash
python3.10 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest -v
npm ci --prefix frontend
npm run build --prefix frontend
npm test --prefix frontend
```

The React Router frontend is a standalone Vite app in `frontend/`. Flask is now API/download only. During local development, run Flask for `/api/v1/*` and `/resume`, and run Vite for the website UI with API proxies:

```bash
# terminal 1
. .venv/bin/activate
export FLASK_APP=website
export FLASK_ENV=flask
flask run --host 127.0.0.1 --port 8000

# terminal 2
npm run dev --prefix frontend
```

To run the standalone frontend production preview:

```bash
npm run build --prefix frontend
npm run preview --prefix frontend
```

## Dependency Workflow

Top-level dependency intent is recorded in `requirements.in`. Runtime and test installs use the pinned `requirements.txt` so CI, Docker, and local development resolve the same package versions.

When dependencies need to change, update `requirements.in`, regenerate `requirements.txt` with a Python 3.10-compatible resolver, then run:

```bash
python -m pip install -r requirements.txt
python -m pip check
python -m pytest -v
```

## Configuration

Configuration can be supplied through environment variables or explicit app-factory overrides in tests.

| Variable | Default | Purpose |
| --- | --- | --- |
| `API_KEY` | empty | Reserved API key setting. |
| `SECRET_KEY` | empty | Flask secret key. |
| `RESOURCE_DIRECTORY` | `website/resources` | Directory containing JSON resources used by routes, APIs, and resume generation. |
| `RESUME_DIRECTORY_LOCATION` | `/tmp` on Linux, home directory otherwise | Directory where the generated resume is written. |
| `RESUME_FILENAME` | `Derek Santos - Resume.docx` | Public download filename for `/resume`. |
| `GENERATE_RESUME_ON_STARTUP` | `true` | Generates the DOCX resume when the app starts. Tests can disable this. |
| `GITHUB_TIMEOUT_SECONDS` | `5` | Timeout for GitHub API requests used by the GitHub API endpoint. |

## Build

A series of GitHub actions are triggered upon pull request to the master branch and once more during the final merge into master.

The workflow consists of:

1. Pulling and installing pinned dependencies.
2. Running `python -m pip check`.
3. Testing Python unit tests with PyTest.
4. Installing and building the React Router frontend.
5. Testing Dockerfile build of the API image.
6. Pushing the code to [DigitalOcean](https://www.digitalocean.com/). (Now handled by DigitalOcean's SaaS platform.)

## Docker

Build and run the container locally with:

```bash
docker build -t santosderek-website .
docker run --rm -p 8000:8000 santosderek-website
```

The Docker image is now for the Flask API/download backend only and defaults to `FLASK_ENV=gunicorn`, which starts Gunicorn through `docker-entrypoint.sh`. The React Router frontend is built and served separately with npm/Vite. Set `FLASK_ENV=flask` to run the Flask development server in the backend container.

## Deployment

The deployment of the website is hosted on [DigitalOcean](https://www.digitalocean.com/), as alluded to earlier.

After a successful merge to the master branch, the code gets pushed to DigitalOcean, built within a [Docker](https://www.docker.com/) image, and ran on top of [Gunicorn](https://gunicorn.org/) to handle requests.

## Resume Generation

Within my website application, I created a resume builder which will take JSON files written under the `../website/resources` directory and parse a list of respective objects to be placed within each sub-heading of my resume using the `python-docx` package.

This workflow allows me to only worry about updating each JSON file within the `resources` folder and have my website automatically generate the latest version of my resume without me having to deal with opening and editing a DOCX file.

By default, the Flask app generates `Derek Santos - Resume.docx` from the JSON resources during startup and serves that generated file from [https://santosderek.com/resume](https://santosderek.com/resume).

It has already saved me hours of work, allows me to make quick changes to the content of the document on any device, (Laptop, Desktop, Phone, etc.), and share my updated resume by referencing [https://santosderek.com/resume](https://santosderek.com/resume).
