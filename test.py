from argon2 import PasswordHasher

ph = PasswordHasher()

password_hash = "$argon2id$v=19$m=65536,t=3,p=4$sVpexnvE3nOCEp83GS2kRQ$ciDqSvWOwAvJxBORNvFnI4kHbDIzIhvDZ1nOOsIEhwY"
password = "testing"

print(ph.verify(password_hash, password))