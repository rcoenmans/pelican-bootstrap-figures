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

import unittest
import pelican_bootstrap_figures.pelican_bootstrap_figures

class BootstrapFiguresTest(unittest.TestCase):
    def test_wrap_figure_around_img(self):
        # Arrange
        html = '<img alt="Example" src="example.jpg" />'
        
        # Act
        html = pelican_bootstrap_figures.bootstrap_figures(html)

        # Assert
        self.assertIsNotNone(html)
        self.assertEqual(html, '<figure class="figure"><img alt="Example" class="figure-img img-fluid" src="example.jpg"/><figcaption class="figure-caption text-right">Example</figcaption></figure>')

    def test_wrap_figure_around_multiple_imgs(self):
        # Arrange
        html = '<p><img alt="Example" src="example.jpg" /></p><p><img alt="Example" src="example.jpg" /></p>'
        
        # Act
        html = pelican_bootstrap_figures.bootstrap_figures(html)

        # Assert
        self.assertIsNotNone(html)
        self.assertEqual(html, '<p><figure class="figure"><img alt="Example" class="figure-img img-fluid" src="example.jpg"/><figcaption class="figure-caption text-right">Example</figcaption></figure></p><p><figure class="figure"><img alt="Example" class="figure-img img-fluid" src="example.jpg"/><figcaption class="figure-caption text-right">Example</figcaption></figure></p>')

    def test_wrap_figure_around_no_imgs(self):
        # Arrange
        html = '<p></p>'
        
        # Act
        html = pelican_bootstrap_figures.bootstrap_figures(html)

        # Assert
        self.assertIsNotNone(html)
        self.assertEqual(html, '<p></p>')

if __name__ == '__main__':
    unittest.main()