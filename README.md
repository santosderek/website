[![santosderek banner](website/static/images/santosderek.png)](https://santosderek.com)


![Build Passing](https://img.shields.io/github/workflow/status/santosderek/website/tests?style=for-the-badge) ![Languages Count](https://img.shields.io/github/languages/count/santosderek/website?style=for-the-badge) ![Total Lines](https://img.shields.io/tokei/lines/github/santosderek/website?style=for-the-badge)

The following repo is the source code to my [personal website](https://santosderek.com) intended to be the main area where people can get to know me and my past experiences, and is able to generate a DOCX of my resume for me.

Feel free to look around the source. 

--- 

> *NOTE: I will not be approving pull requests as everything is subject to change at any moment.*

--- 

## Technologies

The major key technologies and dependencies for the website are:

- Flask
- Docker
- DigitalOcean
- AWS Route53
- Requests
- Python-Dotenv
- Python-Docx
- Gunicorn
- PyTest

## Build

A series of GitHub actions are triggered upon pull request to the master branch and once more during the final merge into master.

The workflow consists of: 

1. Pulling and installing all dependencies.
2. Testing Python unit tests with the popular PyTest package.
3. Tests my Python resume generation.
4. Building the docker container.
5. Pushing the code to [DigitalOcean](https://www.digitalocean.com/). (Now handled by DigitalOcean's SaaS platform.)

## Deployment

The deployment of the website is hosted on [DigitalOcean](https://www.digitalocean.com/), as alluded to earlier.

After a successful merge to the master branch, the code gets pushed to DigitalOcean, built within a [Docker](https://www.docker.com/) image, and ran on top of [Gunicorn](https://gunicorn.org/) to handle requests.

## Resume Generation

Within my website application, I created a resume builder which will take JSON files written under the `../website/resources` directory and parse a list of respective objects to be placed within each sub-heading of my resume using the `python-docx` package.

This workflow allows me to only worry about updating each JSON file within the `resources` folder and have my website automatically generate the latest version of my resume without me having to deal with opening and editing a DOCX file.

It has already saved me hours of work, allows me to make quick changes to the content of the document on any device, (Laptop, Desktop, Phone, etc.), and share my updated resume by referencing [https://santosderek.com/resume](https://santosderek.com/resume).
