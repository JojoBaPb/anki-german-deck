import genanki
from gtts import gTTS
import os

# Folder for generated audio files
AUDIO_DIR = 'german_audio'
os.makedirs(AUDIO_DIR, exist_ok=True)

# German number list: (number, German word)
german_numbers = [
    (0, 'null'), (1, 'eins'), (2, 'zwei'), (3, 'drei'), (4, 'vier'), (5, 'fünf'),
    (6, 'sechs'), (7, 'sieben'), (8, 'acht'), (9, 'neun'), (10, 'zehn'),
    (11, 'elf'), (12, 'zwölf'), (13, 'dreizehn'), (14, 'vierzehn'), (15, 'fünfzehn'),
    (16, 'sechzehn'), (17, 'siebzehn'), (18, 'achtzehn'), (19, 'neunzehn'),
    (20, 'zwanzig'), (21, 'einundzwanzig'), (22, 'zweiundzwanzig'),
    (23, 'dreiundzwanzig'), (24, 'vierundzwanzig'), (25, 'fünfundzwanzig'),
    (26, 'sechsundzwanzig'), (27, 'siebenundzwanzig'), (28, 'achtundzwanzig'),
    (29, 'neunundzwanzig'), (30, 'dreißig'), (31, 'einunddreißig'),
    (32, 'zweiunddreißig'), (33, 'dreiunddreißig'), (34, 'vierunddreißig'),
    (35, 'fünfunddreißig'), (36, 'sechsunddreißig'), (37, 'siebenunddreißig'),
    (38, 'achtunddreißig'), (39, 'neununddreißig'), (40, 'vierzig'),
    (41, 'einundvierzig'), (42, 'zweiundvierzig'), (43, 'dreiundvierzig'),
    (44, 'vierundvierzig'), (45, 'fünfundvierzig'), (46, 'sechsundvierzig'),
    (47, 'siebenundvierzig'), (48, 'achtundvierzig'), (49, 'neunundvierzig'),
    (50, 'fünfzig'), (51, 'einundfünfzig'), (52, 'zweiundfünfzig'),
    (53, 'dreiundfünfzig'), (54, 'vierundfünfzig'), (55, 'fünfundfünfzig'),
    (56, 'sechsundfünfzig'), (57, 'siebenundfünfzig'), (58, 'achtundfünfzig'),
    (59, 'neunundfünfzig'), (60, 'sechzig'), (61, 'einundsechzig'),
    (62, 'zweiundsechzig'), (63, 'dreiundsechzig'), (64, 'vierundsechzig'),
    (65, 'fünfundsechzig'), (66, 'sechsundsechzig'), (67, 'siebenundsechzig'),
    (68, 'achtundsechzig'), (69, 'neunundsechzig'), (70, 'siebzig'),
    (71, 'einundsiebzig'), (72, 'zweiundsiebzig'), (73, 'dreiundsiebzig'),
    (74, 'vierundsiebzig'), (75, 'fünfundsiebzig'), (76, 'sechsundsiebzig'),
    (77, 'siebenundsiebzig'), (78, 'achtundsiebzig'), (79, 'neunundsiebzig'),
    (80, 'achtzig'), (81, 'einundachtzig'), (82, 'zweiundachtzig'),
    (83, 'dreiundachtzig'), (84, 'vierundachtzig'), (85, 'fünfundachtzig'),
    (86, 'sechsundachtzig'), (87, 'siebenundachtzig'), (88, 'achtundachtzig'),
    (89, 'neunundachtzig'), (90, 'neunzig'), (91, 'einundneunzig'),
    (92, 'zweiundneunzig'), (93, 'dreiundneunzig'), (94, 'vierundneunzig'),
    (95, 'fünfundneunzig'), (96, 'sechsundneunzig'), (97, 'siebenundneunzig'),
    (98, 'achtundneunzig'), (99, 'neunundneunzig'), (100, 'hundert')
]

# Define the Anki card model
model = genanki.Model(
  1607392319,
  'German Number with TTS',
  fields=[
    {'name': 'Number'},
    {'name': 'German'},
    {'name': 'Audio'},
  ],
  templates=[
    {
      'name': 'Card with Audio',
      'qfmt': '{{Number}}<br>{{Audio}}',
      'afmt': '{{Number}}<br>{{Audio}}<hr id="answer">{{German}}',
    },
  ])

# Create the deck
deck = genanki.Deck(
  2059400110,
  'German Numbers 0–100 (with TTS)'
)

# Generate TTS and add notes
for number, word in german_numbers:
    filename = f'{word}.mp3'
    filepath = os.path.join(AUDIO_DIR, filename)

    if not os.path.exists(filepath):
        tts = gTTS(word, lang='de')
        tts.save(filepath)

    note = genanki.Note(
        model=model,
        fields=[
            str(number),
            word,
            f'[sound:{filename}]'
        ]
    )
    deck.add_note(note)

# Package deck with audio
package = genanki.Package(deck)
package.media_files = [os.path.join(AUDIO_DIR, f'{word}.mp3') for _, word in german_numbers]
package.write_to_file('german_numbers_tts.apkg')

print("✅ Anki deck generated: german_numbers_tts.apkg")

