git submodule update --init --recursive
git submodule update --recursive
cp ../twitter/twitter.json ./twitter
docker compose up --build --detach