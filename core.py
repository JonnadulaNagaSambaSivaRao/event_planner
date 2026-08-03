#Step 1: Take Inputs

# Event Type
# Budget
# Number of Guests
# City
# Date

#Step 2: Search Services

# Search Venues
# Search Caterers
# Search Decorators
# Search Photographers

#Step 3: Finalize Plan

# Best Venue
# Best Food
# Decoration Theme
# Estimated Cost

#Step 4: Booking

# Venue Booked
# Catering Booked
# Photographer Booked
# Payment paid or not

#Step 5: Event Tracking

# Booking Status
# Remaining Payment
# Event Ready


planner_data = {}



# Step 1

def get_inputs():
    planner_data["event"] = input("Event Type: ")
    planner_data["budget"] = int(input("Budget: "))
    planner_data["guests"] = int(input("Guests: "))
    planner_data["city"] = input("City: ")
    planner_data["date"] = input("Date: ")

    print("\nInputs Saved\n")



# Step 2

def search_services():

    print("\nSearching Services...\n")

    planner_data["venue"] = "Royal Convention Hall"
    planner_data["catering"] = "Taste Catering"
    planner_data["decorator"] = "Dream Decorations"
    planner_data["photographer"] = "Pixel Studio"



# Step 3

def finalize_plan():

    print("\nFinalizing Plan...\n")

    planner_data["estimated_cost"] = planner_data["budget"] - 10000

    print("Venue :", planner_data["venue"])
    print("Food :", planner_data["catering"])
    print("Decoration :", planner_data["decorator"])
    print("Photographer :", planner_data["photographer"])
    print("Estimated Cost :", planner_data["estimated_cost"])





# Step 4

def booking():

    print("\nBooking Services...\n")

    planner_data["booking_id"] = "EVT2026001"

    payment = input("Payment Status (Paid/Not Paid): ").strip().lower()

    if payment == "paid":
        planner_data["payment_status"] = "Paid"
        planner_data["booking_status"] = "Confirmed"
    else:
        planner_data["payment_status"] = "Pending"
        planner_data["booking_status"] = "Waiting for Payment"

    print("\nBooking ID :", planner_data["booking_id"])
    print("Payment Status :", planner_data["payment_status"])
    print("Booking Status :", planner_data["booking_status"])

# Step 5

def tracking():

    print("\nTracking Event\n")

    print("Booking ID :", planner_data["booking_id"])
    print("Payment Status :", planner_data["payment_status"])
    print("Booking Status :", planner_data["booking_status"])

    if planner_data["payment_status"] == "Paid":
        print("Remaining Payment : ₹0")
        print("Event Status : Ready")
    else:
        print("Remaining Payment : ₹10000")
        print("Event Status : Waiting for Payment")
