total_aisles = 3
total_shelves = 4

# Outer loop handles each aisle
for aisle in range(1, total_aisles + 1):
    row_output = []
    
    # Inner loop handles shelves within the current aisle
    for shelf in range(1, total_shelves + 1):
        # Format the location code (e.g., A1-S1)
        location_code = f"A{aisle}-S{shelf}"
        row_output.append(location_code)
    
    # Print all shelves for the current aisle on a single row, separated by spaces
    print("  ".join(row_output))