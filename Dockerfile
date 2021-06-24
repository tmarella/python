FROM python:3

WORKDIR /usr/src/app
ARG github_TOKEN
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ENV GH_TOKEN=${github_TOKEN}
COPY . .

CMD ["python3", "main.py"]