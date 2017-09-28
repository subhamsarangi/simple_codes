from time import sleep
import PyPDF2

pdf_obj=open('file.pdf', 'rb')
pdf_reader=PyPDF2.PdfFileReader(pdf_obj)
pdf_len=pdf_reader.numPages
print('This PDF\'s got '+str(pdf_len)+' pages.')
def pdffilepy(): 
	print('HELP ::: Hit control+C to exit the program...\n')
	try:
		page_select=int(input('WHICH PAGE D\'YOU WANT? => '))
		page_select-=1
		if page_select in range(pdf_len):
			print('...\n')
			sleep(2)

			page_obj=pdf_reader.getPage(page_select)
			print('### Here you go, buddy...\n')
			page_obj.extractText()
			sleep(1)
			pdffilepy()
		else: 
			print('\nPlease, enter a valid value...\n')
			sleep(1)
			pdffilepy()
	except Exception as err:
		sleep(1)
		print('>>>PROBLEMM! You got: ***'+str(err)+'***\n')
		sleep(1)
		pdffilepy()

pdffilepy()