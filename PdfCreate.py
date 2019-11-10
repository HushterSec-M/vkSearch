from fpdf import FPDF
def simple_table(spacing=1):
    data = [
        {'id': 16261643, 'first_name': 'Алексей', 'last_name': 'Харузин', 'domain': 'indeyets82', 'photo_100': 'https://sun9-48.userapi.com/c855236/v855236511/d8c97/oKyoVVEyn8g.jpg?ava=1', 'track_code': 'd107f272RfDVTvaBLexA0d528B6VqhegmFI-6mmhw7MpLDgnVPYimZJP_78r7hPR74NsvwrEc72HXyk'},
        {'id': 156360884, 'first_name': 'Алексей', 'last_name': 'Харузин', 'domain': 'id156360884', 'photo_100': 'https://pp.userapi.com/tbv8TVXyCxH0ycNOMuO42Ju58-6i1gOw1ctfLA/8Te3ALuH31E.jpg?ava=1', 'track_code': '44e58d8fyYYNFMpNd1aHge21MDXZreQf-w5sRSkzFCRcw8AIwrKu705ElCV2AdCL2kagn3SojBH9DWxF'},
        {'id': 9431998, 'first_name': 'Алексей', 'last_name': 'Харузин', 'domain': 'vodochnik', 'photo_100': 'https://sun9-50.userapi.com/c837633/v837633998/5109f/J-nrezQgRiY.jpg?ava=1', 'track_code': '9d3ac0cbJ_WhUNzR_h4HbzURsvC0EfT15uvKALZiMbl1ijb0biBAnLYFhLPwHgI9DusiZEBzg_H38Q'},
        {'id': 440477751, 'first_name': 'Алексей', 'last_name': 'Харузин', 'domain': 'kharuzin95', 'photo_100': 'https://sun1-16.userapi.com/c844216/v844216623/1fd80a/QMtIQKlCO2E.jpg?ava=1', 'track_code': '5e44664fbsrJ7fXuVZxyltlt3NMNI_6M9qpaBG9mcdXLFC4NpeQJo43rr95WnnCQ7ZlDdKUmloLwqVoE'},
        {'id': 435802527, 'first_name': 'Алексей', 'last_name': 'Харузин', 'domain': 'id435802527', 'photo_100': 'https://sun9-10.userapi.com/c852232/v852232496/ce10/b67phanNGMU.jpg?ava=1', 'track_code': 'a81ad9c7mGY7jichzylLWBtQsJy8XkNWxxXVK8yJZ-Vd0si1Qwj_Dy2Mfxyafh1TL6EtPBJbK1jBFtUr'},
        {'id': 513685226, 'first_name': 'Алексей', 'last_name': 'Харузин', 'domain': 'id513685226', 'photo_100': 'https://sun9-69.userapi.com/c851028/v851028170/198372/6JXzEPLS3RM.jpg?ava=1', 'track_code': 'ccf3d7a6-Ykyfp_q7XqQKksiTgVo_yidLOCpYRQ9raDAGGkljeue4HYuwNe-KcV6dtTUpcf6QJMq46lh'},
        {'id': 178562060, 'first_name': 'Алексей', 'last_name': 'Харузин', 'domain': 'id178562060', 'photo_100': 'https://vk.com/images/camera_100.png?ava=1', 'track_code': 'de2f4517KSyVaxFE0RbG4iH0RWfIq0nV6QsH6AUFehmpVK7-2mpORdBuGnXQRZ_nEQXdw2GuIdvvCAfo'}
    ]


    pdf=FPDF(format='letter', unit='in')
    pdf.set_font("Arial", size=12)
    pdf.add_page()

    col_width = pdf.w / 4
    row_height = pdf.font_size
    i = 1
    for row in data:
        print(f"{i}) ", end="")
        i+=1
        for item in row:
            if item == "track_code" or item == "photo_100" or item == "domain": continue
            text = str(row[item])
            text = text
            print(text, end=" ")
            pdf.cell(col_width, row_height * spacing,
                     txt="{}".format(text), border=1, ln=1)
        print()
        pdf.ln(row_height * spacing)
    print("Creating...")
    pdf.output('data.pdf')

if __name__ == '__main__':
    simple_table()
