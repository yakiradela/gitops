FROM python:3.11-slim

RUN groupadd -g 1000 appgroup && \
    useradd -u 1000 -g appgroup -ms /bin/bash appuser

WORKDIR /app
COPY app.py /app/app.py

USER 1000:1000

EXPOSE 8080
CMD ["python", "app.py"]
