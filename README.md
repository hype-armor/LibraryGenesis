# LibraryGenesis

LibraryGenesis is a Newznab and NZBGet compatible indexer and downloader for ebooks that are found on the library genesis web sites.
This is to be used with readarr or similar software.

The indexer will craft a nzb file that works with the downloader in this repo.

## testing
run server.py

## running
### docker
docker run --name library_genesis -p 8003:8003 -v /path/to/downloads:/downloads library_genesis

### compose
version: "3"
services:
    library_genesis:
        container_name: library_genesis
        restart: always
        ports:
            - 8003:8003
        volumes:
            - /path/to/downloads:/downloads
        image: library_genesis

## readarr setup
setup readarr like you would an Newznab indexer and NZBGet downloader.
