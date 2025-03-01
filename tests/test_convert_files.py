import unittest
from src.convert_files import generate_summary

class TestConvertFiles(unittest.TestCase):
    def test_generate_summary(self):
        text = "Satz eins. Satz zwei. Satz drei. Satz vier."
        summary = generate_summary(text)
        self.assertIn("Satz eins. Satz zwei. Satz drei.", summary)

if __name__ == "__main__":
    unittest.main()
