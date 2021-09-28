import uuid
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

# Enter service principal information
tenant_id = "3617ef9b-98b4-40d9-ba43-e1ed6709cf0d"
client_id = "fae08e3f-6d22-4dca-a666-a7064c1576ac"
client_secret = "qzc7Q~5hWxQYuP06wxPGR5zIb5CmVNbAZgpDZ"

# Enter Information for the Key Vault
keyVaultName = "mykeyvault270921"
keyVaultUri = f"https://{keyVaultName}.vault.azure.net"

# Getting the application credentials
app_credentials = ClientSecretCredential(tenant_id, client_id, client_secret) 

# Connecting to Key Vault using app credentials
client = SecretClient(vault_url=keyVaultUri, credential=app_credentials)

#User input for secret name to be read from the vault and then reading the secret from vault
existingSecretName = input("What is the name of the existing secret you want to retrieve:  ")
print(f"Now retrieving existing secret, '{existingSecretName.strip()}' from {keyVaultName}...", end=' '),
try:
  existingSecret = client.get_secret(existingSecretName.strip())
except Exception as readEx:
  print("\tERROR\n")
  print(f"{readEx}\n\nMoving on to next step ...\n")
else:
  print("\tOK!\n")
  print(f"The existing secret in {keyVaultName}, called '{existingSecretName}, has a value of '{existingSecret.value}'\n")


print ("\nAll done. Goodbye!")
