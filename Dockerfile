# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

# Install dependencies
RUN pip  install  pipenv fastapi fastapi-sqlalchemy pydantic alembic psycopg2 uvicorn

COPY ./app /app

EXPOSE 80

#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]