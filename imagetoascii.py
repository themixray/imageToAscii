from PIL import Image, ImageFont
import numpy as np

def asciiart(filename, letters=' .,:irs?@9B&#', size=()):
    SC = 0.2
    GCF = 2
    chars = np.asarray(list(letters))
    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]
    WCF = letter_height/letter_width
    img = Image.open(filename)
    if size == (): size = img.size
    widthByLetter=round(size[0]*SC*WCF)
    heightByLetter = round(size[1]*SC)
    S = (widthByLetter, heightByLetter)
    img = img.resize(S)
    img = np.sum(np.asarray(img), axis=2)
    img -= img.min()
    img = (1.0 - img/img.max())**GCF*(chars.size-1)
    lines = ("\n".join(("".join(r) for r in chars[img.astype(int)])))
    return lines

if __name__=='__main__':
    tk = tkinter.Tk()
    tk.withdraw()
    art = asciiart(tkinter.filedialog.askopenfilename(), ' _͇˖ʭʫȺ#', (100,100))
    tk.destroy()
    print(art)
