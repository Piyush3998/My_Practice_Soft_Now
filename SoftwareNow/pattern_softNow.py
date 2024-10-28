def create_pattern():
    for i in range(5):
        # Left section: @ and #
        left_section = "@ " * (i + 1) + "# " * (5 - i - 1)
        
        # Right section: * and %
        right_section = "* " * (5 - i) + "% " * i
        
        # Print both sections side by side
        print(left_section + "   " + right_section)

create_pattern()\
