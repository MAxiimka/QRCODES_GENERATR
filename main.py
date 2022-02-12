import qrcode

def get_qrcode(url="https://www.google.com", name="one"):
    qr= qrcode.make(data=url)
    qr.save(stream=f'{name}.png')

    return f'QR Создан! {name}.png'

def main():
    print(get_qrcode(url='https://github.com/MAxiimka', name='Portfolio'))
    print(get_qrcode(url='https://career.habr.com/maxim-koradel', name="Резюме"))

if __name__=='__main__':
    main()