FROM python

#Ambil File
ADD run.py .

#Instal lewat file txt
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD [ "python", "./run.py" ]


############## TUTORIAL MENJALANKAN ##############

#Building requirements.txt
# docker build -t python-dm-ig .

#Running
# docker run -t -i python-dm-ig