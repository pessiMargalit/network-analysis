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

# password1234 - $2b$12$kpxxlFuaIn83u2jdHDUl4OsBdVd7p7f9kcB0Oo0eb8KvRFXHBbJn2
# leaPassword - $2b$12$e84ycBy5i85Q9UTXu.i1Y.e8rWU1bFau9SopT39iDcqk.0hZAPqFa
# sharonsPassword - $2b$12$emfMhOCHZQldK6CfIvDaauBmXkHb6g0pi0ClLYrsbIRTWlFB2.MP.
