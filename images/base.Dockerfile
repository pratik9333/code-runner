FROM centos:7

RUN curl -fsSL https://rpm.nodesource.com/setup_17.x | bash -

RUN yum install -y \
    nodejs \
    gcc \
    python3 \
    pip3  

WORKDIR /src/app 

RUN mkdir /src/app/solutions/

COPY requirements.txt   . 

RUN pip3 install -r requirements.txt 

COPY .  . 

EXPOSE 4000 

CMD ["python3","main.py"] 


