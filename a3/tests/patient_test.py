from unittest import TestCase
from unittest import main
from clinic.patient import Patient
from clinic.notes import Note
class PatientTests(TestCase):

    def test_initialization(self):
        patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertIsNotNone(patient, "craeted patient cannot be null")

    def test_equality(self):
        actual_patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        expected = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertEqual(actual_patient, expected, "Patient data correct")
        actual_patient = Patient()
        self.assertIsNone(actual_patient.phn, "Created patient should be null")

    def test_create_note(self):
         expected_note = Note(1, "Patient comes with headache and high blood pressure.")
         self.assertIsNotNone(expected_note, "expected not cannot be null")
         patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
         note = patient.patient_record.add_note("Patient comes with headache and high blood pressure")
         self.assertIsNotNone(note, "created note cannot be null")
         self.assertEqual(note, expected_note, "Notes should contain same data")
if __name__ == '__main__':
	main()
