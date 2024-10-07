FROM python 
WORKDIR C:/ipynb_checkpoints
COPY .C:/ipynb_checkpoints
CMD ["python3","dock.py"]



### docker build -t tag1
#### docker run tag1
### docker run --name dockerName tag1