import unittest
from tiny_url import Codec

class TestCodec(unittest.TestCase):

    def test_basic_encode_decode(self):
        codec = Codec()
        url = "https://leetcode.com/problems/design-tinyurl"
        short = codec.encode(url)
        decoded = codec.decode(short)
        self.assertEqual(decoded, url)

    def test_multiple_urls(self):
        codec = Codec()
        urls = [
            "https://google.com",
            "https://github.com",
            "https://openai.com",
            "https://example.com/test",
        ]

        shorts = [codec.encode(u) for u in urls]

        # всі короткі URL мають бути різними
        self.assertEqual(len(shorts), len(set(shorts)))

        # декодуємо назад
        decoded = [codec.decode(s) for s in shorts]
        self.assertEqual(decoded, urls)

    def test_base62_format(self):
        codec = Codec()
        short = codec.encode("https://example.com")

        allowed = set(codec.chars)
        self.assertTrue(all(c in allowed for c in short))

    def test_incremental_ids_increase(self):
        codec = Codec()
        ids = [codec.encode(f"url{i}") for i in range(1, 6)]

        # Перевіряємо, що кожне наступне число у Base62 більше попереднього
        # (тобто код дійсно інкрементний)
        self.assertTrue(ids[0] < ids[1] < ids[2] < ids[3] < ids[4])

    def test_decode_nonexistent(self):
        codec = Codec()
        self.assertEqual(codec.decode("doesnotexist"), "")

    def test_id_length(self):
        codec = Codec()
        # перші кілька ID мають різну довжину в Base62:
        id1 = codec.encode("a")
        id2 = codec.encode("b")
        id3 = codec.encode("c")
        # Наприклад: 1 -> "1", 2 -> "2", 3 -> "3"
        self.assertGreaterEqual(len(id2), len(id1))
        self.assertGreaterEqual(len(id3), len(id2))


if __name__ == "__main__":
    unittest.main()
