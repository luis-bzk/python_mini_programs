import qrcode


def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('qr_image.png')


text_value = input('Enter your URL or text to generate a new QRCode: ')
generate_qr_code(text_value)
