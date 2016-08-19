#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi
import codecs

#<textarea type="text" name="rot13" value="%(rot13)s" cols="40" rows="5"></textarea>
#<input type="text" name ="rot13" value="%(rot13)s" style="font-size:18pt;height:100px;width:300px;">

page_header = """
<!DOCTYPE html>
<html lang="en"> <!-- lang="en" is for bootstrap-->
<head>


    <!-- bootstrap links-->
    <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <style type="text/css">
        .error {
            color: red;
        }
        #inner {
            width: 50%;
            margin: 0 auto;
            text-align: center;
        }
    </style>

    <title>Caesar</title>
    <meta charset="utf-8"> <!-- for bootstrap-->
    <meta name="viewport" content="width=device-width, initial-scale=1">  <!-- for bootstrap mobile responsiveness-->

</head>
<body>
    <div class="container">
        <h1 id="inner">
            <a href="/">Caesar</a>
        </h1>
        <br>
    </div>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""

form = """
<div class="container"> <!-- for bootstrap, body must be in this class -->
<form method = "post" id = "inner">
    <div class="form-group">
    <h2 id="inner">Enter Some Text to ROT13</h2><div></div>
    <br>
    <label><strong>ROT13</strong><div></div>
        <textarea type="text" name ="rot13"  cols="40" rows="5"">%(rot13)s</textarea>
    </label>
    <div></div>
    <br>
    <br>
    <label><strong>Cypher Value<strong>
        <input type="text" name ="cypher" value="%(cypher)s">
    </label>
    <br>
    <br>
    <input class="btn btn-success btn-block" type="submit">
    <div style = "color:red">%(error)s</div>
    </div>
</form>
</div>
"""

def is_digit(n):
    if n and n.isdigit():
        num = int(n)
        return num

def escape_html(s):
    return cgi.escape(s, quote = True)

def escape_html_practice(s):
    s = s.replace("&", "&amp;")
    s = s.replace(">", "&gt;")
    s = s.replace("<", "&lt;")
    s = s.replace('"', "&quot;")

    return s

def sub1(s):
    return given_string % s

def sub2(s1, s2):
    return given_string2 % (s1, s2)

def sub_m(name, nickname):
    return given_string2 % {"nickname" : nickname, "name": name}

def caesar(string, shift):
    #return codecs.encode(string, 'rot_13')
    #def caesar(plainText, shift):
    #shift = int(13)
    cipherText = ""
    for ch in string:
        if ch.isalpha():
            stayInAlphabet = ord(ch) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
        else:
            cipherText += ch
    return cipherText


class MainHandler(webapp2.RequestHandler):
    def write_form(self, error="", rot13="", cypher=""):
        self.response.write(page_header + form % {"error" : error, "rot13" : rot13, "cypher" : cypher} + page_footer)

    def get(self):
        self.write_form()

    def post(self):
        user_input = self.request.get(escape_html('rot13'))
        cypher = self.request.get('cypher')

        if is_digit(cypher):
            userinput = caesar(user_input, int(cypher))
            self.write_form("", userinput, cypher)
        else:
            self.write_form("Must Input A Number", user_input, cypher)


        ##self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Thanks for the Bday")


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/thanks', ThanksHandler)
], debug=True)
