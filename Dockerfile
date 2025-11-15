FROM zauberzeug/nicegui:latest

ENV MPLCONFIGDIR=/tmp/matplotlib
WORKDIR /app

RUN mkdir -p /tmp/matplotlib
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8080

CMD ["python3", "main.py"]