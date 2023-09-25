def main():
    email_input: str = input('Input the email: ')

    if '@' not in email_input or '.' not in email_input:
        print('The email is not valid 😶')
    else:
        (user_name, domain) = email_input.split('@')
        (domain, extension) = domain.split('.')
        print(f'''
User name: {user_name}
Domain: {domain}
Extension: {extension}
''')


main()
