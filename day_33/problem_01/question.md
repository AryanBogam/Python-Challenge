Q1. PNR Status Tracker
Concept: Dictionary lookup + conditional messages
Problem:
Given a dictionary like:
pnr_db = {
  "1234567890": "Confirmed",
  "2345678901": "RAC",
  "3456789012": "Waiting List"
}
Write a function check_pnr_status(pnr_number) that returns the status or "Invalid PNR" if not found.