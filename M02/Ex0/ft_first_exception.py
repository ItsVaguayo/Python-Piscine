def check_temperature(temp_str: str):
    print("Testing temperature:", temp_str)
    try:
        num = int(temp_str)
    except:
        print(f"Error: '{temp_str}' is not a valid number")
    if num > 40:
        print(f"Error: {num}°C is too hot for plants (max 40°C)")
def ft_first_exception() -> None:
    
if __name__ == "__main__":
    ft_first_exception()
   