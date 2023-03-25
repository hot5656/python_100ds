from flask import Flask, request, send_file, make_response
import qrcode
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/qrcode', methods=['GET'])
def generate_qr():
    # get the url parameter from the query string
    url = request.args.get('url')

    # generate the QR code image
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')

    # save the image to a file-like object
    img_file = BytesIO()
    img.save(img_file, 'PNG')
    img_file.seek(0)

    # create a response object with the image data
    response = make_response(img_file.getvalue())

    # set the headers for the response
    response.headers.set('Content-Type', 'image/png')
    response.headers.set('Content-Disposition', 'attachment', filename='qrcode.png')

    return response

# add run app
if __name__=="__main__":
	app.run()