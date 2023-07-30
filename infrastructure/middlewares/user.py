from pydantic import BaseModel, field_validator, constr, EmailStr

from infrastructure.middlewares.auth import pwd_context


class RegistrationUser(BaseModel):
    email: EmailStr
    password: constr(min_length=8)
    confirm_password: constr(min_length=8)

    @classmethod
    @field_validator("confirm_password")
    def compare_passwords(cls, confirm_password):
        if confirm_password == cls.password:
            return confirm_password
        raise ValueError("confirm password must be the equals to password")


def get_password_hash(password):
    return pwd_context.hash(password)


print(get_password_hash("password1234"))

