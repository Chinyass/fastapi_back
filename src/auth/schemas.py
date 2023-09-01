from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    username: str
    role_id: int
    '''
    id: models.ID
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    if PYDANTIC_V2:  # pragma: no cover
        model_config = ConfigDict(from_attributes=True)  # type: ignore
    else:  # pragma: no cover

        class Config:
            orm_mode = True
    '''


class UserCreate(schemas.BaseUserCreate):
    username: str
    role_id: int
    '''
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    '''


class UserUpdate(schemas.BaseUserUpdate):
    pass
    '''
    password: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None
    '''