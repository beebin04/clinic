from unittest import TestCase
from unittest import main
from clinic.notes import Note
class NoteTest(TestCase):
    def test_create_note(self):
        expected_note_1 = Note(1, "Patient comes with headache and high blood pressure.")
        expected_note_2 = Note(2, "Patient complains of a strong headache on the back of neck.")
        self.assertIsNotNone(expected_note_1, "note did not create successfully")
        self.assertNotEqual(expected_note_1, expected_note_2, "notes must not be equal, share different codes and details")
        comapred_note_1 = Note(1, "Patient comes with headache and high blood pressure.")
        self.assertEqual(expected_note_1, comapred_note_1, "notes must be equal")
        
    def test_update_note(self):
        note1 = Note(1, "Patient comes with headache and high blood pressure")
        updated_note = Note(1, "Patient comes with chronic migranes and high blood pressure")
        self.assertIsNotNone(note1)
        self.assertIsNotNone(updated_note)
        self.assertNotEqual(note1, updated_note)
        note1.update("Patient comes with chronic migranes and high blood pressure")
        self.assertEqual(note1, updated_note, "notes should have same details")
if __name__ == '__main__':
    main()