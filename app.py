import os
import PyPDF2
import pytesseract
from PIL import Image
from mtranslate import translate


# 画像からテキストを抽出
def get_text_from_image(image_path):
    try:
        img = Image.open(image_path)
        # 画像からテキストを抽出
        text = pytesseract.image_to_string(img, lang='eng')
        return text
    except Exception as e:
        print(f"画像からテキストを抽出できませんでした: {e}")
        return None


# PDFファイルからテキストを抽出
def get_text_from_pdf(pdf_path):
    try:
        pdf_file = open(pdf_path, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
        return text
    except Exception as e:
        print(f"PDFファイルからテキストを抽出できませんでした: {e}")
        return None


# テキストを翻訳
def translate_text(text, target_lang='ja'):
    try:
        translated_text = translate(text, target_lang)
        return translated_text
    except Exception as e:
        print(f"テキストの翻訳に失敗しました: {e}")
        return None


# ファイルを取得
data_dir = 'image'
files = os.listdir(data_dir)

for file in files:
    file_path = os.path.join(data_dir, file)
    file_extension = os.path.splitext(file)[1].lower()  # ファイルの拡張子を取得し小文字に変換

    if file_extension in ('.jpeg', '.jpg', '.png'):
        # .jpegや.jpgや.pngファイルの場合の処理
        extracted_text = get_text_from_image(file_path)
        if extracted_text:
            translated_text = translate_text(extracted_text)
            if translated_text:
                print("抽出されたテキスト:")
                print(extracted_text)
                print("\n翻訳されたテキスト:")
                print(translated_text)

    elif file_extension == '.pdf':
        # .pdfファイルの場合の処理
        print(f"PDFファイルを処理: {file}")
        extracted_text = get_text_from_pdf(file_path)
        if extracted_text:
            translated_text = translate_text(extracted_text)
            if translated_text:
                print("抽出されたテキスト:")
                print(extracted_text)
                print("\n翻訳されたテキスト:")
                print(translated_text)

    else:
        # 上記以外のファイルの場合
        print(f"ファイルの形式が間違っています: {file}")
