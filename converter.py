import pdfkit
from tools import namecreator, setlog


def runConvert(url: str):
    try:
        config = pdfkit.configuration(wkhtmltopdf="wkhtmltopdf.exe")
        file_name = namecreator(url)+'.pdf'
        try:
            pdfkit.from_url(url, file_name, configuration=config)
            setlog('SUCCESS ' + file_name, color='green')
        except OSError:
            print('nuraya')
            setlog('URL FAIL', color='red')
    except OSError:
        setlog('MISSING wkhtmltopdf.exe', color='red')
