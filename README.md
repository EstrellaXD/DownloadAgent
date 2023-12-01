# DownloadAgent

DownloadAgent is a telegram bot to help you to download any links or files to your local storage in anywhere.

You can deploy it as a docker container or run it directly on your computer.

## Now support

- [x] Download telegra.ph photos
- [x] Download magnet links
- [x] Download torrent links
- [ ] Download youtube videos
- [ ] Download x(formally twitter) videos

... in working

## Usage

You must have a telegram bot. If you don't have one, you can create one by talking to [@BotFather](https://t.me/BotFather).

### Deploy as a docker container

```bash
docker run -d 
```

### Run directly on your computer

You must write a `.env` file in the root of the project.

```bash
git clone https://github.com/EstrellaXD/DownloadAgent.git

cd DownloadAgent

pip install -r requirements.txt

python main.py
```


