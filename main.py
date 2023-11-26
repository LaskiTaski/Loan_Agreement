from docxtpl import DocxTemplate

print('Общие данные')
Date_Contract = input('Введите Дату заключения договора: ')
print()
Loan_Amount_Num = input('Введите Сумму займа цифрами через .: ').replace('.', '')
Loan_Amount_Str = input('Введите Сумму займа буквами: ') + ' рублей ноль копеек'
print()
Date_Funds = input('Введите Дату предоставления средств: ')
Date_Return = input('Введите Дату полного возврата средств: ')
print()
Loan_Interest_Num = input('Введите % на займ числом: ')
Loan_Interest_Str = input('Введите % на займ текстом: ')
print()
Loan_in_Months_Num = input('Введите срок займа числом в месяцах: ')
Loan_in_Months_Str = input('Введите срок займа текстом в месяцах: ')
print()
Cost_of_Use_Num = input('Введите сумму за пользование средствами цифрами: ').replace('.', '')
Cost_of_Use_Str = input('Введите сумму за пользование средствами буквами: ') + ' рублей ноль копеек'
print()
Total_Amount_Num = input('Введите сумму которую должны вернуть цифрами: ').replace('.', '')
Total_Amount_Str = input('Введите сумму которую должны вернуть буквами: ') + ' рублей ноль копеек'


print('\n\nДанные ЗАЙМОДАТЕЛЯ')
LFP_Lender = 'ФАМИЛИЯ ИМЯ ОТЧЕСТВО'
LFP_Lender_a = (' '.join([i + 'а' for i in LFP_Lender.split()]))
LFP_Lender_y = (' '.join([i + 'у' for i in LFP_Lender.split()]))

Lender_Series, Lender_Number = 'СЕРИЯ НОМЕР'.split()
Lender_Issued = 'КЕМ ВЫДАН'
Lender_Issued_Date = 'ДАТА ВЫДАЧИ'
Lender_Adress = 'АДРЕС РЕГИСТРАЦИИ'
Lender_Email = 'EMAIL'
Lender_PhoneNumber = 'НОМЕРТ ТЕЛЕФОНА'
print(f'ФИО Займодателя: {LFP_Lender}\nСерия и Номер паспорта: {Lender_Series, Lender_Number}\nКем и кодга выдан: '
      f'{Lender_Issued} {Lender_Issued_Date}\nАдрес регистрации: {Lender_Adress}\n'
      f'Контактные данные: \nemail:{Lender_Email}\nНомер телефона:{Lender_PhoneNumber}')

print('\n\nДанные ЗАЁМЩИКА')
LFP_Borrower = input('Введите ФИО Заемщика: ')
LFP_Borrower_a = input('Введите ФИО Заемщика\nВ Родительном падеже: ')
LFP_Borrower_y = input('Введите ФИО Заемщика\nВ Дательном падеже: ')
Borrower_Series, Borrower_Number = input('Введите серию и номер паспорта через пробел: ').split()
Borrower_Issued = input('Кем выдан паспорт: ')
Borrower_Issued_Date = input('Когда выдан паспорт: ')
Borrower_Adress = input('Место регистрации: ')
Borrower_Email = input('Email: ')
Borrower_PhoneNumber = input('Ваш номер телефона: ')

context = {}
# Общие данные
context['Date_Contract'] = Date_Contract #Дата заключения договора

context['Loan_Amount_Num'] = Loan_Amount_Num #Сумма займа Цифрами
context['Loan_Amount_Str'] = Loan_Amount_Str #Сумма займа Буквами

context['Date_Funds'] = Date_Funds #Дата предоставления средств
context['Date_Return'] = Date_Return #Дата возврата средств

context['Loan_Interest_Num'] = Loan_Interest_Num #Годовой процент на займ Цифрами
context['Loan_Interest_Str'] = Loan_Interest_Str #Годовой процент на займ Буквами

context['Loan_in_Months_Num'] = Loan_in_Months_Num #Срок займа в месяцах Цифрами
context['Loan_in_Months_Str'] = Loan_in_Months_Str #Срок займа в месяцах Буквами

context['Cost_of_Use_Num'] = Cost_of_Use_Num # Выплачиваемый процент за пользование Цифрами
context['Cost_of_Use_Str'] = Cost_of_Use_Str # Выплачиваемый процент за пользование Буквами

context['Total_Amount_Num'] = Total_Amount_Num #Общая Сумма которую должны вернуть Цифрами
context['Total_Amount_Str'] = Total_Amount_Str #Общая Сумма которую должны вернуть Буквами

# Данные Займодателя
context['LFP_Lender'] = LFP_Lender #ФИО Займодателя
context['LFP_Lender_a'] = LFP_Lender_a #ФИО Займодателя в Родительном падеже
context['LFP_Lender_y'] = LFP_Lender_y #ФИО Займодателя в Дательном падеже
context['Lender_Series'] = Lender_Series #Серия паспорта
context['Lender_Number'] = Lender_Number #Номер паспорта
context['Lender_Issued'] = Lender_Issued #Кем выдан паспорт
context['Lender_Issued_Date'] = Lender_Issued_Date #Когда выдан паспорт
context['Lender_Adress'] = Lender_Adress #Адресс регистрации
context['Lender_Email'] = Lender_Email #Email
context['Lender_PhoneNumber'] = Lender_PhoneNumber #Номер телефона


# Данные Заёмщика
context['LFP_Borrower'] = LFP_Borrower #ФИО Заёмщика
context['LFP_Borrower_a'] = LFP_Borrower_a #ФИО Заёмщика в Родительном падеже
context['LFP_Borrower_y'] = LFP_Borrower_y #ФИО Заёмщика в Дательном падеже
context['Borrower_Series'] = Borrower_Series #Серия паспорта
context['Borrower_Number'] = Borrower_Number #Номер паспорта
context['Borrower_Issued'] = Borrower_Issued #Кем выдан паспорт
context['Borrower_Issued_Date'] = Borrower_Issued_Date #Когда выдан паспорт
context['Borrower_Adress'] = Borrower_Adress #Адресс регистрации
context['Borrower_Email'] = Borrower_Email #Email
context['Borrower_PhoneNumber'] = Borrower_PhoneNumber #Номер телефона

doc = DocxTemplate("Dogovor.docx")

doc.render(context)

doc.save("gen.docx")
