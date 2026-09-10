# mpv-page

Tiny Flask page that takes a video URL and plays it fullscreen with `mpv` on the host, keeping a playlist of what was submitted. `piped.video` links are rewritten to YouTube.

## Run

```sh
pip install -r requirements.txt
python app.py
```

Open `http://<host>:5000`. `GET /skip` drops the first playlist entry. `app.spec` builds a single-file exe with PyInstaller.
