FROM Tepthone/sbb_b1:slim-buster

#clonning repo 
RUN git clone https://github.com/Tepthone/sbb_b1 /root/sbb_b1
#working directory 
WORKDIR /root/sbb_b1

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/sbb_b1/bin:$PATH"

CMD ["python3","-m","sbb_b1"]
