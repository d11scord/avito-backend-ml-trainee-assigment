FROM python:3.8

COPY requirements.txt /
RUN pip install -r requirements.txt

COPY matrix_traversal /matrix_traversal

ENTRYPOINT ["python", "-m", "matrix_traversal"]
