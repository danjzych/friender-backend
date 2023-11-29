<a name="readme-top"></a>

# Friender Frontend

<br />
<div align="center">
  <a href="https://github.com/danjzych/friender-backend">
    <h1>Friender</h1>
  </a>

  <h3 align="center">A geolocation-based social media application for finding friends near you.</h3>

  <p align="center">
    <a href="http://friender.danielzych.com/">View Demo</a>
    ·
    <a href="https://github.com/danjzych/friender-backend/issues">Report Bug</a>
    ·
    <a href="https://github.com/danjzych/friender-frontend">Frontend Repo</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Friender is a geolocation-based social media app for finding and chatting with friends near you. Each user sets their location, and a radius within which they can search for friends.

If two users indicate they'd like to be friends with each other, they _match_, and can began chatting with each other.

This API can be used in conjunction with the Friender frontend, or queried directly using tools such as Insomnia or Postman.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Flask][Flask.py]][Flask-url]
- [![postgresQL][postgresQL-db]][postgresQL-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local version of Friender up and running, do the following. Note that, to have an operational Friender frontend, you will need to set up the backend as well.

### Prequisites

1. Clone the repo
   ```sh
   git clone https://github.com/danjzych/friender-backend.git
   ```
2. Create and Start Virtual Environment

   ```sh
    python -m venv venv
    source venv/bin/activate
   ```

3. Install Requirements in Virtual Environment

   ```sh
   pip3 install -r reqquirements.txt
   ```

### Setup Images

1. Create postgresQL Database and Seed Data

   ```sh
   ipython
   [1] %run app.py
   [2] %run seed.py
   ```

2. Setup AWS S3 Bucket for user photos
   Friender uses S3 object storage to store and access user photos.
   Create an S3 bucket with CORS enabled.
3. Add AWS Credentials to .env
   You will need:

   - `'AWS_ACCESS_KEY_ID'`
   - `'AWS_SECRET_ACCESS_KEY'`
   - `'IMAGE_BUCKET'`

4. Upload user images from `/images` to your S3 bucket and ensure the file names match those used in `seed.py`.

### Run App

After doing the above, you are ready to launch the Friender backend. From your virtual environment, run

```sh
flask run -p 5001
```

   <p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [ ] Add Profile Photo Designation for user images
- [ ] Optimize searching for potential friends
- [ ] Add notifications system
  - [ ] Track whether new matches and messages have been seen by relevant users
- [ ] Refactor chatting using Flask websockets

See the [open issues](https://github.com/danjzych/friender-backend/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Daniel Zych - [LinkedIn](https://www.linkedin.com/in/danielzych/) - danjzych@gmail.com

Project Link: [https://github.com/danjzych/friender-backend](https://github.com/danjzych/friender-backend)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

This project was also built with:

- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/)
- [GeoPy](https://geopy.readthedocs.io/en/stable/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->

[Flask.py]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[postgresQL-db]: https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white
[postgresQL-url]: https://www.postgresql.org/
