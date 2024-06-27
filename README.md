
![](https://img.shields.io/badge/GitHub-181717.svg?style=for-the-badge&logo=GitHub&logoColor=white)![GitHub top language](https://img.shields.io/github/languages/top/AsHfIEXE/Spotify-Music-Downloader?style=for-the-badge)
 ![GitHub Downloads )](https://img.shields.io/github/downloads/AsHfIEXE/Spotify-Music-Downloader/total) ![](https://img.shields.io/github/last-commit/AsHfIEXE/Spotify-Music-Downloader/main?display_timestamp=author&style=for-the-badge) ![GitHub Repo stars](https://img.shields.io/github/stars/AsHfIEXE/Spotify-Music-Downloader?style=for-the-badge)![GitHub Discussions](https://img.shields.io/github/discussions/AsHfIEXE/Spotify-Music-Downloader?style=for-the-badge)





# Spotify Music Downloader🎵


Welcome to the Spotify Music Downloader project! Dive into the world of offline music with this handy tool, making it easy to download your favorite tracks and playlists from Spotify. Whether you're prepping for a long flight or building your ultimate music collection, this downloader has got your back.
## Features ✨

- Download songs in AAC 128kbps or in AAC 256kbps with a premium account
- Download music videos with a premium account
- Download synced lyrics with a premium account
- Highly configurable


## Prerequisites 📋

- Python 3.8 or higher
- The cookies file of your Spotify account (free or premium)
- You can get your cookies by using one of the following extensions on your browser of choice at the Spotify website with your account signed in:
- Firefox: https://addons.mozilla.org/addon/export-cookies-txt
- Chromium based browsers: https://chrome.google.com/webstore/detail/gdocmgbfkjnnpapoeobnolbbkoibbcif
- FFmpeg on your system PATH.Older versions of FFmpeg may not work.
- Up to date binaries can be obtained from the links below:
- Windows: https://github.com/AnimMouse/ffmpeg-stable-autobuild/releases
- Linux: https://johnvansickle.com/ffmpeg/

## Installation 🛠️

1. Install the package `spotify-web-downloader`using pip


```bash
  pip install spotify-web-downloader
```
2. Place your cookies file in the directory from which you will be running spotify-web-downloader and name it `cookies.txt`.



    
## Usage/Examples 🚀

You can use 
bash
``` bash
spotify-web-downloader [OPTIONS] URLS...
```



## Demo

- Download song/Track/Playlist
```bash
spotify-web-downloader "spotify-link"
```
Replace The `spotify-link` with your desired song/Track/Playlist

## Configuration ⚙️

`spotify-web-downloader` can be configured using command line arguments or a config file. The config file is created automatically on the first run:

- Linux: ~/.spotify-web-downloader/config.json
- Windows: %USERPROFILE%\.spotify-web-downloader\config.json
- Command Line Arguments / Config File Keys

| Command line argument / Config file key                         | Description                                                                  | Default value                                |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------- |
| `--download-music-video` / `download_music_video`               | Attempt to download music videos from songs (can lead to incorrect results). | `false`                                      |
| `--save-cover`, `-s` / `save_cover`                             | Save cover as a separate file.                                               | `false`                                      |
| `--overwrite` / `overwrite`                                     | Overwrite existing files.                                                    | `false`                                      |
| `--read-urls-as-txt`, `-r` / -                                  | Interpret URLs as paths to text files containing URLs.                       | `false`                                      |
| `--lrc-only`, `-l` / `lrc_only`                                 | Download only the synced lyrics.                                             | `false`                                      |
| `--no-lrc` / `no_lrc`                                           | Don't download the synced lyrics.                                            | `false`                                      |
| `--config-path` / -                                             | Path to config file.                                                         | `<home>/.spotify-web-downloader/config.json` |
| `--log-level` / `log_level`                                     | Log level.                                                                   | `INFO`                                       |
| `--print-exceptions` / `print_exceptions`                       | Print exceptions.                                                            | `false`                                      |
| `--cookies-path`, `-c` / `cookies_path`                         | Path to .txt cookies file.                                                   | `./cookies.txt`                              |
| `--output-path`, `-o` / `output_path`                           | Path to output directory.                                                    | `./Spotify`                                  |
| `--temp-path` / `temp_path`                                     | Path to temporary directory.                                                 | `./temp`                                     |
| `--wvd-path` / `wvd_path`                                       | Path to .wvd file.                                                           | `null`                                       |
| `--ffmpeg-path` / `ffmpeg_path`                                 | Path to FFmpeg binary.                                                       | `ffmpeg`                                     |
| `--mp4box-path` / `mp4box_path`                                 | Path to MP4Box binary.                                                       | `MP4Box`                                     |
| `--mp4decrypt-path` / `mp4decrypt_path`                         | Path to mp4decrypt binary.                                                   | `mp4decrypt`                                 |
| `--aria2c-path` / `aria2c_path`                                 | Path to aria2c binary.                                                       | `aria2c`                                     |
| `--nm3u8dlre-path` / `nm3u8dlre_path`                           | Path to N_m3u8DL-RE binary.                                                  | `N_m3u8DL-RE`                                |
| `--remux-mode` / `remux_mode`                                   | Remux mode.                                                                  | `ffmpeg`                                     |
| `--date-tag-template` / `date_tag_template`                     | Date tag template.                                                           | `%Y-%m-%dT%H:%M:%SZ`                         |
| `--exclude-tags` / `exclude_tags`                               | Comma-separated tags to exclude.                                             | `null`                                       |
| `--truncate` / `truncate`                                       | Maximum length of the file/folder names.                                     | `40`                                         |
| `--template-folder-album` / `template_folder_album`             | Template of the album folders as a format string.                            | `{album_artist}/{album}`                     |
| `--template-folder-compilation` / `template_folder_compilation` | Template of the compilation album folders as a format string.                | `Compilations/{album}`                       |
| `--template-file-single-disc` / `template_file_single_disc`     | Template of the song files for single-disc albums as a format string.        | `{track:02d} {title}`                        |
| `--template-file-multi-disc` / `template_file_multi_disc`       | Template of the song files for multi-disc albums as a format string.         | `{disc}-{track:02d} {title}`                 |
| `--download-mode-song` / `download_mode_song`                   | Download mode for songs.                                                     | `ytdlp`                                      |
| `--premium-quality`, `-p` / `premium_quality`                   | Download songs in premium quality.                                           | `false`                                      |
| `--template-folder-music-video` / `template_folder_music_video` | Template of the music video folders as a format string.                      | `{artist}/Unknown Album`                     |
| `--template-file-music-video` / `template_file_music_video`     | Template of the music video files as a format string.                        | `{title}`                                    |
| `--download-mode-video` / `download_mode_video`                 | Download mode for videos.                                                    | `ytdlp`                                      |
| `--no-config-file`, `-n` / -                                    | Do not use a config file.                                                    | `false`                                      |


## Tag Variables 🏷️

There are some variables can be used in the template folder/file and/or in the `exclude_tags` list:
- `album`
- `album_artist`
- `artist`
- `compilation`
- `composer`
- `copyright`
- `cover`
- `disc`
- `disc_total`
- `isrc`
- `label`
- `lyrics`
- `media_type`
- `producer`
- `rating`
- `release_date`
- `release_year`
- `title`
- `track`
- `track_total`
- `url`
  
## Remux Modes 🔄

### Remux modes
The following remux modes are available:
* `ffmpeg`
* `mp4box`
    * Requires mp4decrypt
    * Can be obtained from here: https://gpac.wp.imt.fr/downloads

## Music Videos Quality 📺
Music videos will be downloaded in the highest quality available in H.264/AAC, up to 1080p.

## Download Modes ⬇️

Songs

* `ytdlp`
* `aria2c`
    * Faster than `ytdlp`
    * Can be obtained from here: https://github.com/aria2/aria2/releases

    Videos
     - `ytdlp`

    - `nm3u8dlre`
    - Faster than `ytdlp`
    - Download N_m3u8DL-RE:https://github.com/nilaoda/N_m3u8DL-RE/releases

  

## Contributing

Contributing 🤝
We love collaboration! If you'd like to contribute to the Spotify Music Downloader:

  1. Fork the repository.
  2. Create a new branch (git checkout -b feature-branch).
  3. Make your changes and commit them (git commit -m 'Add new feature').
  4. Push to the branch (git push origin feature-branch).
  5. Create a Pull Request.


## Issues and Feedback 🐛
Encountered a bug or have some feedback? Open an issue on [GitHub Issues](https://github.com/AsHfIEXE/Spotify-Music-Downloader/issues). We'd love to hear from you!
## Acknowledgements 

Made with ![](https://img.shields.io/badge/Spotify-1DB954.svg?style=for-the-badge&logo=Spotify&logoColor=white)              ![](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)

## Support

For support, email me on this address `salahin0ashfi@gmail.com` or join our Discord Server.


## License

MADE WITH [MIT License](https://choosealicense.com/licenses/mit/)


## Authors

- [AsHfIEXE](https://www.github.com/AsHfIEXE)

