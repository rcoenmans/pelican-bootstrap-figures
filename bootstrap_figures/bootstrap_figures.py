# -----------------------------------------------------------------------------
# The MIT License (MIT)
# Copyright (c) 2020 Robbie Coenmans
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------

from bs4 import BeautifulSoup
from pelican import signals, contents

def run_plugin(data_passed_from_pelican):
    data_passed_from_pelican._content = bootstrap_figures(data_passed_from_pelican._content)

def bootstrap_figures(content):    
    soup = BeautifulSoup(content, 'html.parser')
    for img in soup.find_all('img'):
        # Figure
        fig = soup.new_tag('figure', attrs={'class': 'figure'})

        # Figure caption
        figcap = soup.new_tag('figcaption', attrs={'class': 'figure-caption text-right'} )
        figcap.string = img['alt']

        img['class'] = 'img-fluid'
        img.wrap(fig)
        img.insert_after(figcap)

    return soup.decode()


def register():
    signals.content_object_init.connect(run_plugin)