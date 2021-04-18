#%%
import base64

password = input('Input your password')
encoded = base64.b64encode(password.encode('utf-8'))

print(f'Encoded password: {encoded}')

encoded = base64.b64decode(encoded.decode('utf-8'))

# %%
