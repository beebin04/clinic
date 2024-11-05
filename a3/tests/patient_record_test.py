from unittest import TestCase
from unittest import main
from clinic.patient_record import PatientRecord
from clinic.notes import Note
class PatientRecordTest(TestCase):
    def test_create_record(self):
        p_record = PatientRecord()
        #Test that empty records are equal
        p_record2 = PatientRecord()
        self.assertEqual(p_record, p_record2, "Empty records should be equal as they contain no data")
        p_record.add_note("Patient comes with headaches and elevated blood pressure")
        p_record.add_note("Patient perscribed with antibiotics")
        p_record.add_note("Patient reports disapearance of headaches")
        self.assertNotEqual(p_record, p_record2, "Non empty list should not equal empty list")
        p_record2.add_note("Patient comes with headaches and elevated blood pressure")
        p_record2.add_note("Patient headaches worsening, describes a progression towards migranes")
        p_record2.add_note("Patient admitted to ICU")
        self.assertNotEqual(p_record, p_record2, "Lists with different notes should not be equal")
        
    def test_find_note_from_record(self):
        expected_note = Note(3, "Patient admitted to ICU")
        p_record = PatientRecord()
        p_record2 = PatientRecord()
        note = p_record.find_note(1)
        self.assertIsNone(note, "Patient record is empty, should not return any notes")
        p_record.add_note("Patient comes with headaches and elevated blood pressure")
        p_record.add_note("Patient perscribed with antibiotics")
        p_record.add_note("Patient reports disapearance of headaches")
        
        p_record2.add_note("Patient comes with headaches and elevated blood pressure")
        p_record2.add_note("Patient headaches worsening, describes a progression towards migranes")
        p_record2.add_note("Patient admitted to ICU")
        
        note = p_record.find_note(0)
        self.assertIsNone(note, "Cannot retrieve note with code 0")
        actual_note = p_record2.find_note(3)
        self.assertEqual(actual_note, expected_note, "Notes should be equal")
        actual_note = p_record2.find_note(1)
        self.assertNotEqual(actual_note, expected_note, "Notes should not be equal")
        
    def test_update_note(self):
        p_record = PatientRecord()
        self.assertFalse(p_record.update_note(1, "Patient diagnosed with jaundice"), "Cannnot update a note in an empty record")
        p_record.add_note("Patient enters with high blood pressure")
        self.assertFalse(p_record.update_note(0, "Patient enters with BP of 120x80"), "Cannot update note with code of 0; notes do not have codes less than 1")
        expected_note = Note(1, "Patient enters with blood pressure of 120x80")
        self.assertNotEqual(p_record.find_note(1), expected_note, "Notes should not be equal")
        p_record.update_note(1, "Patient enters with blood pressure of 120x80")
        self.assertEqual(p_record.find_note(1), expected_note, "Notes should be equal after update")
        
    def test_delete_note(self):
        p_record = PatientRecord()
        self.assertFalse(p_record.delete_note(1), "Cannot delete from empty list")
        p_record.add_note("Patient enters with elevated BP")
        self.assertFalse(p_record.delete_note(0), "Cannot delete notes with code less than 1, Notes should hold a code equal to or greater than 1")
        self.assertTrue(p_record.delete_note(1), "Should return true as note exists, and correct code is passed as parameter")
        p_record.add_note("Patient comes with headaches and elevated blood pressure")
        p_record.add_note("Patient headaches worsening, describes a progression towards migranes")
        p_record.add_note("Patient admitted to ICU")
        self.assertFalse(p_record.delete_note(6), "Cannot delete note that is greater than length of record")
        self.assertTrue(p_record.delete_note(3), "Note at code 3 should be deleted and the function return true")
        self.assertIsNone(p_record.find_note(3), "Note should not be retrievable after deletion")
    
    def test_list_notes(self):
        p_record = PatientRecord()
        n1 = Note(1, "Patient comes with headaches and elevated blood pressure")
        n2 = Note(2, 'Patient headaches worsening, describes a progression towards migranes')
        n3 = Note(3, 'Patient admitted to ICU')
        expected_notelist = [n1, n2, n3]
        p_record.add_note("Patient comes with headaches and elevated blood pressure")
        p_record.add_note("Patient headaches worsening, describes a progression towards migranes")
        p_record.add_note("Patient admitted to ICU")
        notelist = p_record.list_notes()
        self.assertEqual(notelist, expected_notelist)