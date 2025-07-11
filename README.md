# Journey of learning the Django framework

This is going to be a book where i track my learning experience.

As i learn more from the tutorial, the code will start to get more and more comments, so outside of what is already presented in [current-status](#current-status), i'm not going to comment what is not explained, with two exeptions:

1 - if i go out of the path of the tutorial to add something to this project, that was not presented. see: [differences](#some-differences-from-what-im-doing-in-the-documentation-tutorial)

In the future, i'm probably going to make a nother repo where i can categorize every new thing that i learn.

A structure Like: a Repo called `Learning` that references another repo of `Python` that references another repo of `Web Frameworks` where i would have other references for `Flask`, `FastAPI`, this Project, etc.

If this Happens, then this message is probably going to be a lot different than what it is right now.

#### django-version : 
[5.2.4](/pyproject.toml#L8)
#### documentation-version: 
[5.2](https://docs.djangoproject.com/en/5.2/) 
#### current-status: 
[tutorial02](https://docs.djangoproject.com/en/5.2/intro/tutorial02/)

#### Some differences of what i'm doing in contrast to the tutorial:
- Added this project to a repo so that i can track my progress.

- Added a [`.env`](./.env.example) file to manage the secret key from [`settings.py`](./src/mysite/settings.py#L12)

- Added a Shortcut script for [`manage.py`](./src/manage.py) so that i can run:
    ```sh
    manage <command>

    # The alternatives being:

    python manage.py <command>

    # or

    uv run manage.py <command>
    ```
