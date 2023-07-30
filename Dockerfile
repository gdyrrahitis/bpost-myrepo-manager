FROM python:3.10-alpine

ARG CALLER
ENV CALLER=${CALLER}

# Install required binaries
RUN apk update && apk add --no-cache git openssh-keygen openssh-client

# configure permissions for SSH directory
RUN mkdir -p -m 0700 ~/.ssh
RUN chown -R 0700 ~/.ssh

# configure python app
WORKDIR /app
COPY . .
RUN pip3 install .
RUN chmod +x ./bin/run.sh
CMD ["/bin/sh", "-c", "./bin/run.sh ${CALLER}"]
