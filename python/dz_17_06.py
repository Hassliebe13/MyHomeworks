small_rus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и',
'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф',
'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
['оafбasdf%^о^FFжа$#af243ю'],['afпFsfайFтFsfо13н'],
['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
['и$##sfF'], ['вSFSDам'],['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]

final_decrypted_text = []

for list_decrypted_text in secret_letter:
    for list_letter in list_decrypted_text:
        decrypted_text = []
        final_decrypted_text.append(decrypted_text)
        for letter in list_letter:
            if letter in small_rus:
                decrypted_text.append(letter)

final_decrypted_text_list = [''.join([str(c) for c in lst]) for lst in final_decrypted_text]
final_decrypted_text_string = ' '.join(final_decrypted_text_list)

print(final_decrypted_text_string)

input('Для выхода из программы нажмите Enter')
