FROM python:3
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python3 operate.py