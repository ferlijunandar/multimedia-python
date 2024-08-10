from PIL import Image
from PIL import ImageFilter
from pydub import AudioSegment

# Memuat gambar
image = Image.open('gambar1.jpg')

# Menyimpan gambar
image.save('gambar1.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('gambar1.jpg')

resized_image = cropped_image.resize((100, 100))
resized_image.save('gambar1.jpg')

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('gambar1.jpg')

# Memuat file audio
audio = AudioSegment.from_file('audio1.mp3')

# Menyimpan file audio
audio.export('audio1.mp3', format='mp3')

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')

combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')

audio.export('result.wav', format='wav')

louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')