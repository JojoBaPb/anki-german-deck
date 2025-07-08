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

🛠️ How to Use

    Clone the repository:

git clone git@github.com:yourusername/anki-german-deck.git
cd anki-german-deck

    Generate the deck:

python create_anki_german_numbers.py

    The output file german_numbers_tts.apkg will be created.

        Transfer it to your PC or Android device

        Import it into Anki or AnkiDroid

📦 File Structure

anki-german-deck/
├── create_anki_german_numbers.py   # Main deck generator
├── german_audio/                   # Auto-generated TTS audio files (ignored in Git)
├── german_numbers_tts.apkg         # Anki deck file (auto-generated)
├── requirements.txt                # Python dependencies
└── README.md

📄 License

This project is MIT-licensed. You're free to modify and distribute it.

Built with ❤️ by JojoBaPb — inspired by the Fluent Forever method.
