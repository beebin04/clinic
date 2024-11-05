from unittest import TestCase
from unittest import main
from clinic.patient_record import PatientRecord
from clinic.notes import Note
class PatientRecordTest(TestCase):
    def test_create_find_record(self):
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
        
        expected_note = Note(3, "Patient admitted to ICU")
        p_record3 = PatientRecord()
        note = p_record3.find_note(1)
        self.assertIsNone(note, "Patient record is empty, should not return any notes")
        note = p_record.find_note(0)
        self.assertIsNone(note, "Cannot retrieve note with code 0")
        actual_note = p_record2.find_note(3)
        self.assertEqual(actual_note, expected_note, "Notes should be equal")
        actual_note = p_record2.find_note(1)
        self.assertNotEqual(actual_note, expected_note, "Notes should not be equal")