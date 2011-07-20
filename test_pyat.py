import unittest

import pyat

SONGDATA = [
  dict(artist="Deadmau5", album="4x4", title="Raise Your Weapon"),
  dict(artist="Metallica", album="..and Justice for All", title="One"),
  dict(artist="Ratatat", album="Ratatat", title="Seventeen Years"),
  dict(artist="Phish", album="Festival 8", title="Backwards Down the Numberline")
]

SONGDATA_FORMATTED = """+---------------------+---------+-----------------------------+
|        album        |  artist |            title            |
+---------------------+---------+-----------------------------+
|         4x4         | Deadmau5|      Raise Your Weapon      |
|..and Justice for All|Metallica|             One             |
|       Ratatat       | Ratatat |       Seventeen Years       |
|      Festival 8     |  Phish  |Backwards Down the Numberline|
+---------------------+---------+-----------------------------+
"""

class TestPyat(unittest.TestCase):
  def test_simple(self):
    generated = pyat.format(SONGDATA, sorted(SONGDATA[0].keys()))
    self.assertEqual(SONGDATA_FORMATTED, generated)

  def test_skip_empty(self):
    data = SONGDATA[:] + [dict(artist="", album="", title="")]
    generated = pyat.format(data, sorted(SONGDATA[0].keys()))
    self.assertEqual(SONGDATA_FORMATTED, generated)
    

if __name__ == '__main__':
  unittest.main()
