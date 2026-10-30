FROM python:3-alpine3.24
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

# Install tshark and libcap (for the setcap utility)
RUN apk add --no-cache tshark libcap

# Grant dumpcap the capabilities needed to capture network traffic
RUN setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap

EXPOSE 5000
CMD ["python","-m", "flask", "run", "--host=0.0.0.0"]


