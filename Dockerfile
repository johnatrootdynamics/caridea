FROM python:3.10

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
run export FLASK_APP=run.py
COPY . .

#RUN flask db init # to be executed only once

RUN flask db migrate # Generate migration SQL
RUN flask db upgrade # Apply changes

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "run:app"]
