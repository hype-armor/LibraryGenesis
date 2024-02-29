FROM python:3

WORKDIR /usr/src/librarygenesis

# download LG repo
RUN wget -O librarygenesis.zip "https://github.com/hype-armor/LibraryGenesis/archive/refs/heads/main.zip";
COPY librarygenesis.zip /usr/src/librarygenesis/librarygenesis.zip
RUN unzip librarygenesis.zip;
RUN rm librarygenesis.zip;
RUN cd LibraryGenesis-main;
WORKDIR /usr/src/librarygenesis/LibraryGenesis-main
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir -p /downloads



EXPOSE 8003

CMD [ "python", "./server.py" ]
