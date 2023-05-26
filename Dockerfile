FROM fedora
WORKDIR /project

RUN dnf update -y
RUN dnf install -y python3
RUN dnf install -y pip
RUN pip install wheel

COPY . ./
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 3000
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
#CMD python ./app.py