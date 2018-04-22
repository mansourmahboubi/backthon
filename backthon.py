from telethon import TelegramClient
from telethon import utils


def main():
    # get your api id from my.telegram.org
    api_id = "your_id_here"
    api_hash = 'your_hash_here'
    # archive.session is a sqlite database and where program store your account details
    session_name = 'archive.session'
    # client initiation
    client = TelegramClient(session_name,
                            api_id,
                            api_hash,
                            proxy=None,
                            update_workers=4,
                            spawn_read_thread=False)
    client.start()
    str = ""
    count = 0
    # descriptions about how many messages program is retrieving
    print("""Number of messages to be retrieved. Due to limitations with
the API retrieving more than 3000 messages will take longer
than half a minute (or even more based on previous calls).
The limit may also be ``None``, which would eventually return
the whole history.

working...
""")
    # program retrieves messages with 'me' contact which is your chat id
    for message in client.get_messages('me', limit=None):
        sender = utils.get_display_name(message.sender)
        message = message.message
        str += "<h1>{}</h1>{}<hr>".format(sender, message)
        count += 1
    mkhtml(str, count)
    print("history archived successfully :)")


# function store messages in a html template which is optimized with bootsrtap
def mkhtml(content, number):
    open('telegrambackup.html', 'a').close()
    file = open('telegrambackup.html', 'r+')
    file.write("""
    <!DOCTYPE html>
    <html dir="rtl" lang="fa">
    <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Telegram archive</title>
    <meta name="author" content="M Mansour Mahboubi">
    <!-- Bootstrap -->
    <link href="assets/bootstrap.min.css" rel="stylesheet">

    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
      <!--[if lt IE 9]>
    <script src="https://lib.arvancloud.com/ar/html5shiv/3.7.3/html5shiv.min.js"></script>
    <script src="https://lib.arvancloud.com/ar/respond.js/1.4.2/respond.min.js"></script>
      <![endif]-->
    </head>
    <body style="background:#d4d4d4;margin-top:50px;">

      <section>
          <div class="container">
            <div class="row">
              <div class="col-md-12">
                <div class="well">
                    <h1> %s پیغام استخراج شد </h1>
                  %s
                  <hr>
                </div>
              </div>
            </div>
          </div>
      </section>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="assets/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="assets/bootstrap.min.js"></script>
    <!-- Start JS Config (This is where you configure the Bootstrap JS options) -->

    <!-- End JS Config -->
    </body>
    </html>

    """ % (number, content))
    file.close()


if __name__ == '__main__':
    main()
