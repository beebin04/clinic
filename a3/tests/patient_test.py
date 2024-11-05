from unittest import TestCase
from unittest import main
from clinic.patient import Patient
from clinic.notes import Note
class PatientTests(TestCase):

    def test_initialization(self):
        patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertIsNotNone(patient, "craeted patient cannot be null")
        actual_patient = Patient()
        self.assertIsNone(actual_patient.phn, "Created patient should be null")

    def test_equality(self):
        actual_patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        expected = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertEqual(actual_patient, expected, "Patient data correct")
        self.assertEqual(str(actual_patient), str(expected), "String representations must match")

    def test_create_note(self):
         expected_note = Note(1, "Patient comes with headache and high blood pressure.")
         self.assertIsNotNone(expected_note, "expected not cannot be null")
         patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
         note = patient.create_note("Patient comes with headache and high blood pressure.")
         self.assertIsNotNone(note, "created note cannot be null")
         self.assertEqual(note, expected_note, "Notes should contain same data")
         
    def test_search_note(self):
        patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertFalse(patient.search_note(1), "Cannot retrieve note from empty list")
        patient.create_note("Patient comes with headache and high blood pressure.")
        self.assertTrue(patient.search_note(1), "Note should exist and should be findable")
        self.assertFalse(patient.search_note(3), "No note should exist with this code")
        
    def test_update_note(self):
        patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertFalse(patient.update_note(3, "Arbitrary information"), "Patient record is empty, no note should be available to update")
        patient.create_note("Patient comes with headache and high blood pressure.")
        self.assertFalse(patient.update_note(2, "Patient diagnosed with migranes"), "Note code does not exist in record")
        self.assertTrue(patient.update_note(1, "Patient diagnosed with migranes"), "Note code exists in record, should be available to update")
        expected_note = Note(1, "Patient diagnosed with migranes")
        self.assertEqual(patient.search_note(1), expected_note, "Updated note should match expected")
        
    def test_delete_note(self):
        patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertFalse(patient.delete_note(1), "No notes to delete")
        patient.create_note("Patient has lost their arm")
        self.assertFalse(patient.delete_note(2), "Note code does not exist within record")
        self.assertTrue(patient.delete_note(1), "Deleted note should return true")
    def test_list_notes(self):
        patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        self.assertIsNone(patient.list_notes(), "Must be none, no notes in list")
        patient.create_note("Patient is missing big toe")
        patient.create_note("Patient suffering from hypothermia")
        patient.create_note("Patient has been plunged into a hot bath")
        self.assertIsNotNone(patient.list_notes(), "Notes exist, list must not be empty")
        
        n1 = Note(1, "Patient is missing big toe")
        n2 = Note(2, 'Patient suffering from hypothermia')
        n3 = Note(3, 'Patient has been plunged into a hot bath')
        expected_notelist = [n3, n2, n1]

        self.assertEqual(patient.list_notes(), expected_notelist)
    def test_retrieve_notes(self):
        patient = Patient(9790012000, "John Doe", "2000-10-10", "250 203 1010", "john.doe@gmail.com", "300 Moss St, Victoria")
        patient.create_note("Patient is missing big toe")
        patient.create_note("Patient suffering from hypothermia")
        patient.create_note("Patient has been plunged into a hot bath")
        expected_list = []
        expected_list.append(Note(2, "Patient suffering from hypothermia"))
        self.assertIsNone(patient.retrieve_notes("antibiotics"), "no notes exist in record with term antibiotics")
        self.assertIsNotNone(patient.retrieve_notes("hypothermia"), "Should retrieve note 2, which is not none")
        self.assertEqual(expected_list, patient.retrieve_notes("hypothermia"), "lists should contain one note, with same codes and text")
        
if __name__ == '__main__':
	main()
