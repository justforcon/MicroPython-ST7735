import wifi_connect
import json
from content_writer import write
from microWebSrv import MicroWebSrv
import _thread



@MicroWebSrv.route('/','GET')
def test(httpClient,httpResponse):
  t=httpClient.GetRequestMethod()
  print(dir(httpClient))
  print(httpClient.GetRequestQueryParams())
  params = httpClient.GetRequestQueryParams()
  try:
      _thread.start_new_thread(write, (json.dumps(params)))
  except Exception as e:
      print(e)
  content="""\

  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
  </head>
  <body>
    <h1>
        Hello world!
      </h1>
  </body>
  </html>
  """

  httpResponse.WriteResponseOk( headers         = None,
                                contentType     = "text/html",
                                contentCharset  = "UTF-8",
                                content         = content )

srv = MicroWebSrv(webPath="/")
srv.Start(threaded=True)