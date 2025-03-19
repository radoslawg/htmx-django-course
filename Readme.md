# Htmx + Django course

Following course at [NetNinja.dev](https://www.youtube.com/watch?v=ig3syqGT1Fg)

## Other Links

- [DaisyUI](https://daisyui.com/)
- [Htmx](https://htmx.org/docs/)

## Setting up

```sh
python -m venv venv
venv\scripts\activate
pip install -r requirements.txt
python .\manage.py migrate
python .\manage.py runserver
```

### Creating superuser

```sh
python manage.py createsuperuser
```

## Notes

After changing model run: `python .\manage.py makemigrations`
To create superuser run: `python .\manage.py createsuperuser`
[Admin page](http://127.0.0.1:8000/admin/)
