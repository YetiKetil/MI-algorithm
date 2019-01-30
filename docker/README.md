### Build container
`docker build . --tag=text-similarity-image`

### Create image
`docker run -itd --rm -p5000:5000 --name text-similarity --hostname text-similarity -v C:\marko\GitHub\text-similarity-web:/local-git text-similarity-image`

### Run container
`docker exec -it text-similarity bash`

### Stop container
In case of recreating the image
`docker stop text-similarity`
