from moviepy.editor import *
from pydub import AudioSegment

# Cargar la canción
audio = AudioSegment.from_file("/Users/juanangelzapata/Dropbox/Juangelz Albums/demos/bocatoda.wav")

# Crear un clip de imagen
imagen_fondo = "/Users/juanangelzapata/Desktop/selfie.png"  # Nombre del archivo de imagen
clip = ImageClip(imagen_fondo).set_duration(audio.duration_seconds)

# Convertir la canción a un formato compatible con moviepy (mp3)
audio.export("temp_audio.mp3", format="mp3")
audio_clip = AudioFileClip("temp_audio.mp3")

# Asociar el audio al clip de imagen
video = clip.set_audio(audio_clip)

# Guardar el video en un archivo
video.write_videofile("video_final.mp4", fps=24)

# Eliminar el archivo de audio temporal
os.remove("temp_audio.mp3")
