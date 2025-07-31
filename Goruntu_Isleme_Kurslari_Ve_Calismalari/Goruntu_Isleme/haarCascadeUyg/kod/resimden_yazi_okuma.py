from PIL import Image
import pytesseract ## path den dolayı çalışmadı


img =Image.open("C:\\vscode\\Python\\Teknofest\\haarCascadeUyg\\test_images\\text.png")

text = pytesseract.image_to_string(img,lang="eng")

print(text)









