FROM python:3.10.11
WORKDIR /calc_app
COPY . /calc_app
ADD calc_app.py .
RUN pip install numpy
CMD ["python", "calc_app.py"]