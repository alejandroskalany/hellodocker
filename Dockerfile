FROM fedora
WORKDIR /project

RUN dnf update -y
RUN dnf install python3 -y
RUN dnf install python3-pip -y
RUN pip install wheel

COPY . ./
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "./app.py"]