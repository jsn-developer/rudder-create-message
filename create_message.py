# %%
import openpyxl


# %%
book = openpyxl.load_workbook('target/エラーコード一覧.xlsx', data_only=True)
# %%
sheet = book.worksheets[0]

# %%
# Read Template
template = open('MessageCd.template.java', 'r').read()
template
# %%
write_target = open('target/messages.properties', 'w')

enums = []

for row in sheet.iter_rows(min_row=3):
    if row[4].value is None:
        continue
    ## Export to message.properties
    key = row[4].value.replace('-', '_')
    write_target.write(f'{row[4].value}={row[5].value}\n')

    ## Stacking for MessageCd.java
    enums.append(f'/** {row[4].value} {row[5].value} */\n  {key}("{row[4].value}")')

write_target.close()


# %%
enums
# %%
code = template.replace('%{enums}', ',\n  '.join(enums)+';')
# %%
java_code = open('target/MessageCd.java', 'w')
# %%
java_code.write(code)
# %%
java_code.close()