<h1 align="center">Holbertonbnb</h1>
<p align="center">An Airbnb clone.</p>

<p align="center">
  <img src="https://github.com/bdbaraban/holbertonbnb/blob/master/assets/hbnb-logo.png"
       alt="Holbertonbnb logo"
       width="500"
  >
</p>

## Description :house:

Holbertonbnb is a complete full-stack web application, integrating a MySQL database and Flask RESTful API with a dynamic
HTML5/CSS3/jQuery front-end.

<p align="center">
  <img src="https://github.com/bdbaraban/holbertonbnb/blob/master/assets/hbnb-stack.png"
       alt="Holbertonbnb logo"
       width="750"
  >
</p>

### Brennan, what is this, your fourth Airbnb repo?

Fifth, actually :sweat_smile:.

Holbertonbnb was the central web application of the Holberton School year one curriculum. The project spanned the course of two months and four versions, each of which you can view at the below links:

1. [AirBnB_clone](https://github.com/bdbaraban/AirBnB_clone)
2. [AirBnB_clone_v2](https://github.com/bdbaraban/AirBnB_clone_v2)
3. [AirBnB_clone_v3](https://github.com/bdbaraban/AirBnB_clone_v3)
4. [AirBnB_clone_v4](https://github.com/bdbaraban/AirBnB_clone_v4)

The above versions are separate, isolated codebases. While the first was started from scratch, each of versions 2, 3 and 4 involved inheriting and building on repositories started by previous cohorts at Holberton School. Additionally, the work completed for each version involved collaborating and pair programming with a cohort mate - I worked with a different cohort mate for each version.

This versioning process was a great experience in pair programming and working on unfamiliar, developed codebases. Yet, it was not so great from a portfolio perspective and the want of a central, organized repository where I could show off all the work I coded and learned over the course of this clone.

This repository is just the above - an organized, cleaned up version of Holbertonbnb. Call it a minified build, if you will.

I started this repository as a duplicate of [AirBnB_clone_v4](https://github.com/bdbaraban/AirBnB_clone_v4), the final version worked on within the scope of Holberton's curriculum. Since then, I have:

- Cut out all irrelevant code, organizing just that needed to deploy the application.
- Pieced together each of the front-end, back-end and API with strictly _my_ code, copying in the personal implementations of each that I worked on across all four versions.
- Spruced up the front-end and wrote new auto-deployment Puppet and Fabric scripts.
- Wrote thorough, organized documentation for all parts of repo.

### What this repository does include:

- Models class system built in Python.

  - [Source code](./models)
  - [Documentation](./documentation/MODELS.md)

- Python console to manage back-end models

  - [Source code](./console.py)
  - [Documentation](./documentation/CONSOLE.md)

- Flask web application server rendering HTML templates with Jinja2

  - [Source code](./web_flask)
  - [Documentation](./documentation/WEB_FLASK.md)

- RESTful Flask API

  - [Source code](./api)
  - [Documentation](./documentation/API.md)
  - Swagger documentation - [bdbnb.site/apidocs](https://bdbnb.site/apidocs)

- Automatic deployment scripts.
  - [fabfile.py](./fabfile.py)
  - [setup_server.pp](./setup_server.pp)
  - [Documentation](./documentation/DEPLOYMENT.md)

### What this repository does not include:

- Test suite

Unfortunately, the test suite did not hold up well over the course of four different codebases, and was a bit much to justifiably refactor for this minified repo. Which is too bad, because this project involved a significant amount of time spent developing an unittest test suite testing the entire back-end. If you're interested in looking at tests I was involved in writing, my most signficant test work occurred in [AirBnB_clone](https://github.com/bdbaraban/AirBnB_clone).

## Dependencies :couple:

Application:

| Tool/Library | Version |
| ------------ | ------- |
| Python       | ^3.6.4  |
| MySQL        | ^5.6.0  |
| Flask        | ^1.0.3  |
| flasgger     | ^0.9.2  |
| Flask-Cors   | ^3.0.8  |
| mysqlclient  | ^1.3.10 |
| SQLAlchemy   | ^1.3.5  |

View the complete list of app dependencies in the [requirements.txt](./requirements.txt).

Deployment:

| Tool/Library | Version |
| ------------ | ------- |
| Python       | ^3.7.3  |
| gunicorn     | ^19.9.0 |
| Fabric       | ^2.4.0  |
| Puppet       | ^5.4.0  |

## Documentation :book:

In case you missed it - I've documented this entire repository! [Please do check it out!](./documentation)

## Author :black_nib:

- **Brennan D Baraban** - <[bdbaraban](https://github.com/bdbaraban)>

## License :lock:

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
