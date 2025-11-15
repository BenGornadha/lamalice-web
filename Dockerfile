FROM zauberzeug/nicegui:latest

ENV MPLCONFIGDIR=/tmp/matplotlib
WORKDIR /app

RUN mkdir -p /tmp/matplotlib
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip freeze

COPY . .

EXPOSE 8080

CMD ["python3", "main.py"]