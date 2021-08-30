# Python Backend ML Assigment

## Запуск проекта

На `Python 3.8` и выше:
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python -m app.main [URL]
```

Или с помощью `Docker`:

```
docker build -t snailed_matrix .

docker run --rm snailed_matrix [URL]
```