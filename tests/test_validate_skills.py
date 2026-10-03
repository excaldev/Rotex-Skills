import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_skills import validate_skill  # noqa: E402


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.folder = Path(self.temporary.name) / "example"
        self.folder.mkdir()
        self.entry = self.folder / "SKILL.md"
        self.entry.write_text("---\nname: example\ndescription: Helpful\n---\n# Use\n")

    def test_valid(self):
        self.assertEqual(validate_skill(self.folder), [])

    def test_missing_entry(self):
        self.entry.unlink()
        self.assertIn("missing SKILL.md", validate_skill(self.folder)[0])

    def test_missing_frontmatter(self):
        self.entry.write_text("# Use\n")
        self.assertIn("frontmatter", validate_skill(self.folder)[0])

    def test_wrong_name(self):
        self.entry.write_text(self.entry.read_text().replace("name: example", "name: other"))
        self.assertTrue(any("kebab-case" in e for e in validate_skill(self.folder)))

    def test_empty_description(self):
        self.entry.write_text(self.entry.read_text().replace("Helpful", ""))
        self.assertTrue(any("empty description" in e for e in validate_skill(self.folder)))

    def test_extra_field(self):
        self.entry.write_text(self.entry.read_text().replace("description:", "version: 1\ndescription:"))
        self.assertTrue(any("only name and description" in e for e in validate_skill(self.folder)))

    def test_duplicate_field(self):
        self.entry.write_text(self.entry.read_text().replace("description:", "name: example\ndescription:"))
        self.assertTrue(any("duplicate name" in e for e in validate_skill(self.folder)))

    def test_malformed_field(self):
        self.entry.write_text(self.entry.read_text().replace("description:", "oops\ndescription:"))
        self.assertTrue(any("malformed" in e for e in validate_skill(self.folder)))

    def test_empty_body(self):
        self.entry.write_text("---\nname: example\ndescription: Helpful\n---\n")
        self.assertTrue(any("empty body" in e for e in validate_skill(self.folder)))

    def test_missing_link(self):
        self.entry.write_text(self.entry.read_text() + "[ref](references/missing.md)\n")
        self.assertTrue(any("broken link" in e for e in validate_skill(self.folder)))

    def test_existing_link(self):
        (self.folder / "ref.md").write_text("# Ref\n")
        self.entry.write_text(self.entry.read_text() + "[ref](ref.md#anchor)\n")
        self.assertEqual(validate_skill(self.folder), [])

    def test_assets_forbidden(self):
        (self.folder / "assets").mkdir()
        self.assertTrue(any("fixed assets" in e for e in validate_skill(self.folder)))


if __name__ == "__main__":
    unittest.main()
