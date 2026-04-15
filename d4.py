num = input('Digite algo: ')

print(f"""informações sobre a entrada:
        {type(num)} 
        {num.isnumeric()} 
        {num.isalpha()}
        {num.isalnum()}
        {num.isupper()}
        {num.islower()}
    """)
