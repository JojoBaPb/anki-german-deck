# 🧠 Anki German Numbers Deck Generator 🇩🇪

This project generates an Anki flashcard deck for German numbers **0–100**, complete with **text-to-speech (TTS)** audio using Python and `gTTS`.

Each card includes:
- The number (e.g., `42`)
- The German word (e.g., `zweiundvierzig`)
- Native-sounding pronunciation via TTS

## 🚀 Features

- Generates `.apkg` Anki deck file with audio
- Auto-downloads TTS audio for German words using `gTTS`
- Works on both **PC** and **Termux (Android)**
- GitHub-syncable — develop and generate on multiple devices

## 🧰 Requirements

- Python 3.x
- `gTTS` for text-to-speech
- `genanki` for Anki deck generation
- `tqdm` for progress bar

Install dependencies:

```bash
pip install -r requirements.txt

