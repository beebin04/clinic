from unittest import TestCase
from unittest import main
from clinic.patient_record import PatientRecord
from clinic.notes import Note
class PatientRecordTests(TestCase): 
    def test_create_note(self):
         expected_note = Note(1, "Patient comes with headache and high blood pressure.")
         self.assertIsNotNone(expected_note, "expected not cannot be null")
         patientrecord = PatientRecord()
         note = patientrecord.add_note("Patient comes with headache and high blood pressure")
         self.assertIsNotNone(note, "created note cannot be null")
         self.assertEqual(note, expected_note, "Notes should contain same data")

