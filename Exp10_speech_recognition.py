try:
from gtts import gTTS
from IPython.display import Audio, display
AUDIO_MODE = True
except:
AUDIO_MODE = False
import re
print(" Educational AI Assistant Ready...")
 # Changed: Educational input instead of medical
text = "Student dharni studied 1 hours today for english exam."
print("Simulated Recognized Text:", text)
try:
# Extract educational information
student = re.search(r"Student ([A-Za-z]+)", text)
hours = re.search(r"(\d+)\s*hours?", text)
subject = re.search(r"for ([A-Za-z\s]+?)(?:exam|test)", text)
record = {
"Student": student.group(1) if student else "Not detected",
"Study_Hours": hours.group(1) if hours else "Not detected",
"Subject": subject.group(1).strip() if subject else "Not detected"
}
print("Structured Record:", record)
# Generate audio (if available)
if AUDIO_MODE:
tts = gTTS(text=confirmation, lang='en')
tts.save("confirmation.mp3")
display(Audio("confirmation.mp3", autoplay=True))
except Exception as e:
print("Error:", e)
confirmation = f"Great work! {record['Study_Hours']} hours of {record['Subject']} study logged for {record['Student']}."
print("Confirmation
