# DownloadAgent

DownloadAgent is a telegram bot to help you to download any links or files to your local storage in anywhere.

You can deploy it as a docker container or run it directly on your computer.

## Now support

- [x] Download telegra.ph photos
- [x] Download magnet links via [qbittorrent](https://www.qbittorrent.org/)
- [x] Download torrent links
- [x] Download youtube videos
- [x] Download x(formally twitter) videos

... in working

## Usage

You must have a telegram bot. If you don't have one, you can create one by talking to [@BotFather](https://t.me/BotFather).

### Deploy as a docker container

```bash
docker run -d \
    --name DownloadAgent \
    -e BOT_TOKEN=<your bot token> \
    -e USER_ID=<your tg user id> \
    -e PROXY=<your proxy> \
    -v <your download path>:/downloads \
    ghcr.io/estrellaxd/downloadagent
```

### Run directly on your computer

You must write a `.env` file in the root of the project.

```bash
git clone https://github.com/EstrellaXD/DownloadAgent.git

cd DownloadAgent

pip install -r requirements.txt

python main.py
```

## Environment variables

| Name        | Description               | Default | required |
|-------------|---------------------------|---------|----------|
| BOT_TOKEN   | Your telegram bot token   | None    | True     |
| USER_ID     | Your telegram user id     | None    | True     |
| PROXY       | Your proxy                | None    | False    |
| QB_HOST     | Your qbittorrent host     | None    | False    |
| QB_USERNAME | Your qbittorrent username | None    | False    |
| QB_PASSWORD | Your qbittorrent password | None    | False    |

