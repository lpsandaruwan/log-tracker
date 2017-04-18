FROM python:3.5
RUN pip3 install -r requirements.txt
CMD ["python", "ltrk.py"]
