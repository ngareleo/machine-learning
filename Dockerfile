FROM python
COPY  requirements.txt requirements.txt
COPY network.py network.py
RUN pip install -r requirements.txt
CMD python3 network.py