files = ['font', '1.png', '10.jpg', '11.gif',
         '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda file: file[-4:] ==
      '.jpg' or file[-4:] == '.png', files)))
