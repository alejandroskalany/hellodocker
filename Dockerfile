FROM fedora
WORKDIR /project

RUN dnf install -y pip
RUN dnf install -y python3
RUN pip install wheel

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . ./
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

