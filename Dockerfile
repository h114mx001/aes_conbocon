FROM python:3.12-bookworm
RUN apt update && apt install -y socat
RUN pip install pycryptodome
RUN useradd -m -U babycow
# USER babycow:babycow
USER babycow:babycow
WORKDIR /home/babycow
COPY . . 
# RUN chmod +s chal.py
# # RUN chmod 555 main.py   
EXPOSE 31339
CMD socat -T 30 TCP-LISTEN:31339,reuseaddr,fork EXEC:"python -u chal.py"